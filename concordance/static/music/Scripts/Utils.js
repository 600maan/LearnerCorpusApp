

var corpus = {
    getConcordance : function() {
        $.ajax({
            method  : "GET",
            url     :"http://localhost:8000/concordance/",
            done    : function(data) {
                        console.log(data)
                    }
        });
    }
}

