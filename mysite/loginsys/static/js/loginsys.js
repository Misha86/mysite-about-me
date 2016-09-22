$(function() {
    //$.datepicker.setDefaults( $.datepicker.regional[ "ru" ])
    $("#id_date_of_birth").datepicker(
        {changeMonth: true,
            changeYear: true,
            dateFormat: "yy-mm-dd",
            //showOn: "both",
            showWeek: true,
            yearRange: "1920:"

        });
});