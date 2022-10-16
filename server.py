from flask import Flask, send_file, request, send_from_directory
from scaler import runScaler
import pickle
import os
# fix mime type guessing on windows
import mimetypes
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('text/css', '.css')

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def index():
    return send_file('static/index.html')


@app.route('/assets/<path:path>')
def assets(path):
    return send_from_directory('static/assets', path)


@app.route('/api/prediction', methods=['POST'])
def callModel():
    prediction = model.predict(runScaler(request.args.get('texture_mean'), request.args.get('area_mean'), request.args.get('concavity_mean'), request.args.get('area_se'), request.args.get(
        'concavity_se'), request.args.get('fractal_dimension_se'), request.args.get('smoothness_worst'), request.args.get('concavity_worst'), request.args.get('symmetry_worst'), request.args.get('fractal_dimension_worst')))
    return ' '.join(str(x) for x in prediction)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
