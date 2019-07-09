from flask import Flask, request
from AI.run import predict
app = Flask(__name__)


@app.route('/', methods=['POST'])
def upload_train():
    data = request.get_json()
    print(data['text'])
    result = predict(str(data['text']))
    poornag = ''
    if result == 0:
        poornag = '부정적'
    else:
        poornag = '긍정적'
    return poornag, 200

app.run(port=5000, debug=True, threaded=True)

