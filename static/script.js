$(document).ready(function() {
    $('#event_type').change(function() {
        var eventType = $(this).val();
        console.log("Selected Event Type:", eventType);  // Debugging statement
        $.ajax({
            type: 'POST',
            url: '/get_tickets',
            data: { event_type: eventType },
            success: function(data) {
                console.log("Received Data:", data);  // Debugging statement
                var checkboxes = '';
                $.each(data, function(index, ticketArray) {
                    $.each(ticketArray, function(idx, value) {
                        checkboxes += '<div><input type="checkbox" name="tickets" value="' + value + '">' + value + '</div>';
                    });
                });
                $('#ticket_options').html(checkboxes);
            },
            error: function(error) {
                console.log("Error:", error);
            }
        });
    });
});
