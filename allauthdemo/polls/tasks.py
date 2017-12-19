from __future__ import absolute_import
import csv
from os import urandom
import base64
from io import StringIO
from celery import task
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.core.mail import send_mail
from allauthdemo.polls.models import Ballot, Event, EmailUser, AccessKey
from .cpp_calls import param, combpk, addec, tally

def is_valid_email(email):
    try:
        valid_email = EmailValidator()
        valid_email(email)
        return True
    except ValidationError:
        return False

@task()
def create_ballots(poll):
    for voter in poll.event.voters.all():
        ballot = poll.ballots.create(voter=voter, poll=poll)

@task()
def create_voters(csvfile, event):
    reader = csv.reader(csvfile, delimiter=',')
    string = ""
    for row in reader:
        email = string.join(row)
        if (is_valid_email(email)):
            voter = EmailUser.objects.get_or_create(email=email)[0]
            event.voters.add(voter)
            key = base64.urlsafe_b64encode(urandom(16)).decode('utf-8')
            AccessKey.objects.create(user=voter, event=event, key=key)
            send_mail(
                'Your Voting Key',
                'Key: ' + key,
                'from@example.com',
                [string.join(row)],
                fail_silently=False,
            )

@task()
def generate_event_param(event, num):
    event.EID = param(str(num))
    event.save()

@task()
def tally_results(event):
    for poll in event.polls.all():
        result = tally(event.EID, poll.enc, " ".join(str(dec.text) for dec in poll.decryptions.all()), str(poll.options.count()))
        send_mail(
            'Your Results:',
            poll.question_text + ": " + result,
            'from@example.com',
            ["fake@fake.com"],
            fail_silently=False,
        )

@task()
def generate_combpk(event):
    event.public_key = combpk(event.EID, " ".join(str(tkey.key) for tkey in event.trustee_keys.all()))
    event.prepared = True
    event.save()

@task
def generate_enc(poll):
    encs = []
    for ballot in poll.ballots.all():
        if (ballot.cast):
            encs.append(ballot.cipher_text)
    poll.enc = addec(" ".join(encs), str(poll.options.count())) # poll.choices
    poll.save()

@task()
def add(x, y):
    return x + y

@task()
def mul(x, y):
    return x * y

@task()
def xsum(numbers):
    return sum(numbers)
