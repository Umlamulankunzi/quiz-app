document.addEventListener('DOMContentLoaded', function() {
    // Get the timer element and the form element
    const timerElement = document.getElementById('timer');
    const formElement = document.querySelector('form');

    if (timerElement && formElement) {
        // Get the time limit from a hidden input field or data attribute
        const timeLimit = parseInt(timerElement.dataset.timeLimit, 10) || 60;
        let timeRemaining = timeLimit;

        // Update the timer display
        function updateTimer() {
            const minutes = Math.floor(timeRemaining / 60);
            const seconds = timeRemaining % 60;
            timerElement.textContent = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
            timeRemaining--;

            if (timeRemaining < 0) {
                // Time is up, submit the form
                formElement.submit();
            }
        }

        // Update the timer every second
        setInterval(updateTimer, 1000);
    }
});
