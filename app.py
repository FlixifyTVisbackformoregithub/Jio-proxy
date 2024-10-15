from flask import Flask, request, Response
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow CORS

@app.route('/proxy', methods=['GET', 'POST'])
def proxy():
    url = request.args.get('url')
    if not url:
        return "No URL provided", 400

    try:
        # Handle GET and POST
        if request.method == 'POST':
            resp = requests.post(url, data=request.form, headers=request.headers)
        else:
            resp = requests.get(url, headers=request.headers)

        return Response(resp.content, resp.status_code, resp.headers.items())
    except requests.RequestException as e:
        return str(e), 400

if __name__ == '__main__':
    app.run(debug=True)
