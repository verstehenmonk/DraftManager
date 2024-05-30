from flask import Flask, jsonify, request, send_file
import random
import csv
from io import StringIO
from threading import Timer

app = Flask(__name__)

# Store the current state of the draft
draft_state = {
    'players': [],
    'pods': [],
    'players_per_pod': 0,
    'round_time': 0,
    'timer': None
}

# Function to create pods
def create_pods(players, players_per_pod):
    random.shuffle(players)
    return [players[i:i + players_per_pod] for i in range(0, len(players), players_per_pod)]

# Endpoint to start a new draft
@app.route('/start_draft', methods=['POST'])
def start_draft():
    content = request.json
    draft_state['players'] = content['players']
    draft_state['players_per_pod'] = content['players_per_pod']
    draft_state['pods'] = create_pods(draft_state['players'], draft_state['players_per_pod'])
    return jsonify(draft_state)

# Endpoint to update the draft
@app.route('/update_draft', methods=['POST'])
def update_draft():
    content = request.json
    draft_state['players'] = content['players']
    draft_state['pods'] = create_pods(draft_state['players'], draft_state['players_per_pod'])
    return jsonify(draft_state)

# Endpoint to export draft to CSV
@app.route('/export_draft', methods=['GET'])
def export_draft():
    output = StringIO()
    writer = csv.writer(output)
    for pod_number, pod in enumerate(draft_state['pods'], start=1):
        writer.writerow([f'Pod {pod_number}'] + pod)
    output.seek(0)
    return send_file(output, mimetype='text/csv', as_attachment=True, attachment_filename='draft.csv', cache_timeout=0)

# Function to update the timer
def update_timer():
    draft_state['round_time'] -= 1
    if draft_state['round_time'] <= 0:
        draft_state['timer'] = None
    else:
        draft_state['timer'] = Timer(1, update_timer)
        draft_state['timer'].start()

# Endpoint to set the timer
@app.route('/set_timer', methods=['POST'])
def set_timer():
    content = request.json
    draft_state['round_time'] = content['round_time']
    update_timer()
    return jsonify({'message': 'Timer started'})

# Endpoint to get the current timer
@app.route('/get_timer', methods=['GET'])
def get_timer():
    return jsonify({'round_time': draft_state['round_time']})

if __name__ == '__main__':
    app.run(debug=True)
