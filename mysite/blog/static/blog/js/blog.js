$(function () {
    $("#pages").on('click', ".pagination li a", function(event){
        event.preventDefault();
        var page = $(this);
        console.log(page.text())
        console.log(page.attr("href"))
        $.ajax({
            async: true,
            url: '/3d-max/galereya-robit/list-ajax/' + page.attr("href"),
            type: 'get',
            //data: {
            //    page : page.text()
            //},
            dataType: 'json',

            success: function (data) {
                $("#content").html(data.html_articles)
                $("#pages").html(data.html_page)

            },

            error : function(xhr, errmsg, err) {
                $('#result').html("<div class='container' data-alert><h1>Oops! We have encountered an error: " + xhr.status + errmsg +
                "</h1><a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                alert("Oops! We have encountered an error: " + err + " " + xhr.status + " " + errmsg )
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    });

    $("#search").on('submit', function(event){
        event.preventDefault();
        var form = $(this);
        $.ajax({
            async: true,
            url: form.attr("action"),
            type: form.attr("method"),
            data: {
                q : $("#search .form-control").val()
            },
            dataType: 'json',

            success: function (data) {
                 console.log("success")
                $("#content").html(data.html_articles)
                $("#pages").html(data.html_page)
            },

            error : function(xhr, errmsg, err) {
                $('#result').html("<div class='container' data-alert><h1>Oops! We have encountered an error: " + xhr.status + errmsg +
                "</h1><a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                alert("Oops! We have encountered an error: " + err + " " + xhr.status + " " + errmsg )
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    });
});
