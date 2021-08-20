from flask import Flask, request, jsonify, render_template, redirect, url_for
import os
from flask_cors import CORS, cross_origin
import shutil
from com_in_ineuron_ai_utils.utils import decodeImage
from research.obj import MultiClassObj
from werkzeug.utils import secure_filename

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = 'research/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#@cross_origin()
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        modelPath = 'research/ssd_mobilenet_v1_coco_2017_11_17'
        self.objectDetection = MultiClassObj(self.filename, modelPath)



@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

    

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    f = request.files['file']
    filename = secure_filename(f.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    f.save(filepath)
    os.rename("research/" + filename, "research/inputImage.jpg")
    print(os.getcwd())
    shutil.copy("research/inputImage.jpg", "static/uploads")
    result = clApp.objectDetection.getPrediction()
    return render_template("uploaded.html")


port = int(os.getenv("PORT"))
if __name__ == "__main__":
    clApp = ClientApp()
    # app.run(host='0.0.0.0', port=port)
    app.run(host='0.0.0.0', port=port, debug=True)
