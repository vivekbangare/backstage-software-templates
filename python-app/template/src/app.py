from flask import Flask, jsonify
import socket 
import datetime

app = Flask(__name__)

@app.route('/api/v1/healthz')
def health_check():
    return 'OK', 200    

@app.route('/api/v1/details')
def get_details():
    return jsonify(
        {
            'app_name': '{{ values.app_name }}',
            'env': '{{ values.app_env }}',
            'description': 'This is a sample Flask application.!!',
            'author': 'Vivek Bangare',
            'license': 'MIT',
            'hostname': socket.gethostname(),
            'timestamp': datetime.datetime.now().isoformat(),
            'message': 'you are doing great, keep going!!'
        }
    ), 200

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=8080, debug=False)
           