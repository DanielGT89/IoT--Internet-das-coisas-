from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

capture_running = True  

@app.route('/status_capture', methods=['GET'])
def status_capture():
    global capture_running
    return jsonify({'capture_running': capture_running})

@app.route('/stop_capture', methods=['POST'])
def stop_capture():
    global capture_running
    data = request.get_json()
    command = data.get('command')

    print(f"Comando recebido: {command}")  

    if command == 'stop':
        capture_running = False
        print("Captura parada pelo comando.")  
        return jsonify({'status': 'Captura parada'}), 200
    elif command == 'start':
        capture_running = True
        print("Captura reiniciada pelo comando.")  
        return jsonify({'status': 'Captura reiniciada'}), 200
    else:
        print("Comando inválido recebido.")  
        return jsonify({'error': 'Comando inválido'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
