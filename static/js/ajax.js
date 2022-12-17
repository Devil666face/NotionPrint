function deactivate(obj) {
    var id = obj.id.split('deactivate_')[1];
    $.ajax({
        method: "GET",
        url: "{% url 'deactivate' %}",
        data: {
            "pk": id,
        },
        success: function (data) {
            console.log(data);
        },
        error: function (er) {
            console.log(er);
        }
    });
    var card = $(obj).parent();
    card.remove();
}