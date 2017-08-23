$(".button-collapse").sideNav();


$('.dropdown-button').dropdown({
    inDuration: 300,
    outDuration: 225,
    constrainWidth: false, // Does not change width of dropdown to that of the activator
    hover: false, // Activate on hover
    gutter: 0, // Spacing from edge
    belowOrigin: false, // Displays dropdown below the button
    alignment: 'right', // Displays dropdown with edge aligned to the left of button
    stopPropagation: false // Stops event propagation
});


$(document).ready(function () {
    $('select').material_select();
});


$("#fuck").click(function () {
    console.log('bdfbd');
    $.ajax({
        url: /ajax_test/,
        dataType: 'json',
        success: function (data) {
            $("#fuck").html(data.qqq)
        }

    });

});

// функция для правильной работы лукасов
$("#lukas").click(function () {
    var pk = $('#lukas').attr('name');
    console.log(pk);
    $.ajax({
            url: /like/,
            data: {'pk': pk, 'csrfmiddlewaretoken': '{{ csrf_token }}'},
            dataType: "json",
            success: function (data) {
                $("#count").html(data.likes_count)
                console.log('huy')
            },
            error: function (rs, e) {
                alert('pizda');
            }
        }
    );
    if ($('#lukas').hasClass("red-text")) {
        $('#lukas').removeClass("red-text");
        $('#lukas').addClass("grey-text");
    }
    else {
        $('#lukas').removeClass("grey-text");
        $('#lukas').addClass("red-text");
    }
})