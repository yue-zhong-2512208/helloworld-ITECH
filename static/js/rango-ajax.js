// like a movie
$(document).ready(function() {
    $('#like_btn').click(function() {
        var catecategoryIdVar;
        catecategoryIdVar = $(this).attr('data-movieid');
        $.get('/rango/like_movie/',
            {'movie_id': catecategoryIdVar},
            function(data) {
                $('#like_count').html(data);
                $('#like_btn').hide();
            })
    });
});



