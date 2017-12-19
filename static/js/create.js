var datetime_now = window.moment().seconds(0);
var datetime_format = "YYYY-MM-DD H:mm";
$(".date").each(function(index, element) {

    // Set datetimepickers' current, default and minimum date/time

    var datetime_picker = $(element);
    var datetime_iso8601 = datetime_picker.siblings(".datetime-iso8601-input").val();
    var datetime_local = moment(datetime_iso8601);

    datetime_picker.datetimepicker({
        sideBySide: false,
        minDate: datetime_now.clone().startOf("day"),
        format: datetime_format,
        widgetParent: $(datetime_picker)
    });

    var minutes = (Math.ceil(datetime_now.minute() / 5) * 5) + 5 * index;
    var datetime_default = datetime_now.clone().minutes(minutes);

    datetime_picker.data("DateTimePicker").defaultDate(datetime_default);

    datetime_local = datetime_local.isValid() ? datetime_local.format(datetime_format) : "";
    datetime_picker.children("input").val(datetime_local);
});
