document.addEventListener("DOMContentLoaded", function() {
    console.log("H");
    var d1 = document.getElementsByClassName("div1")[0];
    console.log(d1.hidden);
    document.getElementById("hideCode").addEventListener("click", function() {
        console.log("h");
        d1.hidden = !d1.hidden;
    });

    var state = 1; // paused

    const graph = document.getElementById("graph");
    const forwardButton = document.getElementById("forwardButton");
    const backwardButton = document.getElementById("backwordButton");

    document.body.onkeyup = function(e) {
        if (e.key == " " || e.code == "Space") {
            state = state == 1 ? 0 : 1;
        }
    }

    forwardButton.addEventListener("onclick", function() {
        if (state == 0){ // unpaused
            graph.goForward(true); // true means play animations
        }
        else {// paused
            graph.goForward(false); // false means skip to end
        }
    })

    backwardButton.addEventListener("click", function() {
        if (state == 0) {
            graph.goBackward(true);
        }
        else {
            graph.goBackward(false);
        }
    })


});