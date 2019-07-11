from flask import Flask, request
from flask_cors import CORS
import run
app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST'])
def upload_train():
    data = request.get_json()
    print(data['text'])
    result = run.predict(str(data['text']))
    poornag = ''
    if result == 0:
        poornag = '부정적'
    else:
        poornag = '긍정적'

    response = Response()
    response.headers[
        'Access-Control-Allow-Headers'] = 'Access-Control-Allow-Headers, Origin, X-Requested-With, Content-Type, Accept, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS, HEAD'

    return poornag, 200

app.run(port=5000, debug=True, threaded=True)

