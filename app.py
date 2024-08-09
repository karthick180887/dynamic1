from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data for dynamic dropdown and checkbox
events = {
    "concert": ["Rock", "Jazz", "Classical"],
    "sports": ["Football", "Basketball", "Tennis"]
}

tickets = {
    "Rock": ["Front Row", "Middle Row", "Back Row"],
    "Jazz": ["VIP", "Regular", "Balcony"],
    "Classical": ["Orchestra", "Mezzanine", "Balcony"],
    "Football": ["Premium", "Standard", "Economy"],
    "Basketball": ["Courtside", "Standard", "Upper Level"],
    "Tennis": ["VIP Box", "Standard", "Ground"]
}

@app.route('/')
def index():
    return render_template('index.html', events=events)

@app.route('/get_tickets', methods=['POST'])
def get_tickets():
    event_type = request.form.get('event_type')
    print("Received Event Type:", event_type)  # Debugging statement
    if event_type in events:
        ticket_types = events[event_type]
        response = [tickets[ticket_type] for ticket_type in ticket_types]
        print("Sending Tickets:", response)  # Debugging statement
        return jsonify(response)
    return jsonify([])

@app.route('/submit', methods=['POST'])
def submit():
    event_type = request.form.get('event_type')
    selected_tickets = request.form.getlist('tickets')
    return f"Selected Event Type: {event_type}, Selected Tickets: {selected_tickets}"

if __name__ == '__main__':
    app.run(debug=True)
