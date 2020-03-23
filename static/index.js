onload = function(){
    var button = document.querySelector("button");
    var show_output = function() { 
        var active_output_parent_id = document.querySelector("#output_tab_list").querySelector(".active").querySelector("a").getAttribute("href");
        var active_output = document.querySelector(active_output_parent_id).querySelector("textarea");
        active_output.value = this.responseText;
    }
    button.onclick = function() {
        //Grab the values of which tabs the generator will pull input from       
        var input_tab_numbers = $("input[id^=include_input]:checked").map(function() { return this.value; }).get();
        var text_to_process = "";
        for (index in input_tab_numbers) {
            tab_id = "#inputtab" + input_tab_numbers[parseInt(index,10)];
            console.log(tab_id);
            text_to_process += document.querySelector(tab_id).querySelector("textarea").value + " ";
        }

        if (input_tab_numbers.length && text_to_process.length > 2) {
            if (document.querySelector("#cutup").checked) {
                var post_parameters = "./cutup?wordcount=" + document.querySelector("#wordcount").value;
                var block_sizes = $(".cutup_block_size").map(function(){return parseInt($(this).attr("value"),10);}).get();
                post_parameters += "&cutupmin=" + Math.min.apply(Math, block_sizes) + "&cutupmax=" + Math.max.apply(Math, block_sizes)
            } else {
                var post_parameters = "./markov";
            }
            var req = new XMLHttpRequest()
            req.addEventListener("load", show_output)
            req.open("post", post_parameters, true)
            req.send(text_to_process)
        }
    }
    $(".cutup_block_size").change(function() {
       if ($(this).val() > 99) {
           $(this).val(99)
       } else if ($(this).val() < 1) {
           $(this).val(1)
       }       
    });
    $('input[name=mode_selector]').change(function() {
        if ($(this).attr('id') == "cutup") {
            $("#cutup_block_size_container").removeClass("hidden")
        } else {
            $("#cutup_block_size_container").addClass("hidden")
        }
    });
}