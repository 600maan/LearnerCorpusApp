

var corpus = {
    getConcordance : function() {
                            // retrieve the search query
                            var search_word = document.getElementById('search_word').value
                            $.ajax({
                                method  : "GET",
                                url     :"http://localhost:8000/concordance/",
                                data    : { param : search_word },
                                success : function(data) {
                                            $("#concordance_display").text(data);
                                        }
                            });
    }
}

