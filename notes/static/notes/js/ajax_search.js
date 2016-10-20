$(function(){
    $('#search').keyup(function(){
        $.ajax({
            type: 'POST',
            url: "/search/",
            data: {
                'query': $('#search').val(),
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
            success: searchSuccess,
            dataType: 'html'
        });
    });
});

function searchSuccess(data, textStatus, jqXHR){
    $('#sresults').html(data);
}