

var corpus = {
    getConcordance : function() {
        $.ajax({
            method  : "GET",
            url     :"http://localhost:8000/concordance/",
            success    : function(data) {
                        $("#concordance_display").text(data);
                    }
        });
    }
}

