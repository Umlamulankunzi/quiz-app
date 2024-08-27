document.addEventListener('DOMContentLoaded', function() {
    // Getting the timer element and the form element
    const timerElement = document.getElementById('timer');
    const formElement = document.querySelector('form');

    if (timerElement && formElement) {
        // Getting time limit from a data attribute of p tag in template
        const timeLimit = parseInt(timerElement.dataset.timeLimit);
        let timeRemaining = timeLimit;

        // If there's no time limit, show "No Timer"
        if (timeLimit == 0) {
            timerElement.textContent = 'No Timer';
        } else {
            // Update the timer display
            function updateTimer() {
                const minutes = Math.floor(timeRemaining / 60);
                const seconds = timeRemaining % 60;
                timerElement.textContent = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
                timeRemaining--;

                if (timeRemaining < 0) {
                    // Time is up, submitting the form
                    formElement.submit();
                }
            }

            // Update the timer every second
            setInterval(updateTimer, 1000);
        }
    }
});
