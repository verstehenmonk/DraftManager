$(document).ready(function() {
    // Function to start the draft
    $('#startDraftBtn').click(function() {
        const players = $('#playersInput').val().split(',');
        const playersPerPod = parseInt($('#playersPerPodInput').val());
        $.ajax({
            url: '/start_draft',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ players: players, players_per_pod: playersPerPod }),
            success: function(response) {
                alert('Draft started successfully!');
                console.log(response);
            }
        });
    });

    // Function to update the draft
    $('#updateDraftBtn').click(function() {
        const players = $('#playersInput').val().split(',');
        $.ajax({
            url: '/update_draft',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ players: players }),
            success: function(response) {
                alert('Draft updated successfully!');
                console.log(response);
            }
        });
    });

    // Function to export the draft
    $('#exportDraftBtn').click(function() {
        window.location.href = '/export_draft';
    });

    // Function to set the timer
    $('#setTimerBtn').click(function() {
        const roundTime = parseInt($('#roundTimeInput').val());
        $.ajax({
            url: '/set_timer',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ round_time: roundTime }),
            success: function(response) {
                alert('Timer set successfully!');
                console.log(response);
            }
        });
    });

    // Function to get the current timer
    function getTimer() {
        $.ajax({
            url: '/get_timer',
            type: 'GET',
            success: function(response) {
                $('#timerDisplay').text('Time remaining: ' + response.round_time + ' seconds');
            }
        });
    }

    // Call getTimer every second to update the timer display
    setInterval(getTimer, 1000);
});
