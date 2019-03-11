$(document).ready(function () {
    // timer function


    function startTimer(duration, display) {
        let timer = duration, minutes, seconds;
        let refresh = setInterval(function () {
            minutes = parseInt(timer / 60, 10);
            seconds = parseInt(timer % 60, 10);

            minutes = minutes < 10 ? "0" + minutes : minutes;
            seconds = seconds < 10 ? "0" + seconds : seconds;

            let output = minutes + " : " + seconds;
            localStorage.setItem('timer', output);
            display.text(output);
            $("title").html(output + " - MSc Quiz");

            if (--timer < 0) {
                display.text("Time's Up!");
                if (localStorage.getItem('timer')) {
                    localStorage.removeItem("timer");
                }
                clearInterval(refresh);  // exit refresh loop
                // alert("Time's Up!");
                window.location = window.location.protocol + "//" + window.location.host + "/time_up";
            }
        }, 1000);

    }

    function cleartimer(buttonId) {
        document.getElementById(buttonId).onclick = function (e) {
            e.preventDefault();
            e.valueOf();
            let link = $("#" + buttonId).get([0]);
            console.log(link);
            let linkFromButton = link.href;
            let splitedLink = linkFromButton.split("/");
            let protocol = splitedLink[0];
            let hostPortion = splitedLink[2];
            let pathname = splitedLink[3];
            if (localStorage.getItem('timer')) {
                console.log(localStorage.getItem("timer"));
                localStorage.removeItem("timer");
                window.location = protocol + "//" + hostPortion + "/" + pathname;
            } else {
                window.location = protocol + "//" + hostPortion + pathname;
            }
        };
    }

    // start timer
    $(function ($) {
        let localTIme = localStorage.getItem("timer");

        if (localStorage.getItem('timer')) {
            let split_time = localTIme.split(":");
            let a = (parseInt(split_time[0]) * 60);
            let b = parseInt(split_time[1]);
            let c = a + b;
            if (c === 0) {
                localStorage.clear();
                $('#time').text("Time's Up!")
            } else {
                let display = $('#time');
                startTimer(c, display);
            }
            // console.log(localTIme)
        } else {
            let display = $('#time');
            startTimer(Minutes, display);
        }
    });

    // disable login button
    $("#loginForm").submit(function () {
        //disable the submit button
        $("#loginSubmit").attr("disabled", true);
    });

    // disable signup button
    $("#signupForm").submit(function () {
        //disable the submit button
        $("#signupSubmit").attr("disabled", true);
    });

    // disable signup button
    $("#updateForm").submit(function () {
        //disable the submit button
        $("#updateSubmit").attr("disabled", true);
    });

    $("#forwardValidator").click(function () {
        $("#forwardValidator").attr("disabled", true);
        setTimeout(function () {
            localStorage.removeItem("timer");
        });
        $("#answerform_python").submit();
    });
    // disable submit question button
    $("#answerform_python").submit(function () {
        //disable the submit button
        $("#backwardValidator").attr("disabled", true);
        $("#r8").attr("disabled", true);
        $("#r9").attr("disabled", true);
    });

    // onclick event is assigned to the #button element.
    $(function (e) {
        cleartimer("logoutUser");
        cleartimer("updateLogout");
        cleartimer("resultLogout");
    });
});
