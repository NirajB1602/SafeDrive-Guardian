from flask import Flask, request
import cv2 
import numpy as np
import base64
from keras.models import load_model
from flask_cors import CORS
from flask import jsonify


model = load_model('models/cnnCat2.h5')

app = Flask(__name__)
CORS(app)

model = load_model('models/cnncat2.h5')

score = 0

face = cv2.CascadeClassifier('D:\\Projects\\BEproject\\Repo\\SafeGuardian-model\\model\\essentials\\haarcascade_frontalface_alt.xml')
leye = cv2.CascadeClassifier('D:\\Projects\\BEproject\\Repo\\SafeGuardian-model\\model\\essentials\\haarcascade_lefteye_2splits.xml')
reye = cv2.CascadeClassifier('D:\\Projects\\BEproject\\Repo\\SafeGuardian-model\\model\\essentials\\haarcascade_righteye_2splits.xml')


font = cv2.FONT_HERSHEY_COMPLEX_SMALL
rpred = [99]
lpred = [99]

def detect_drowsiness(frame):
    global score
    global rpred, lpred

    # height, width = frame.shape[:2]

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if face.empty() or leye.empty() or reye.empty():
        print("Error: One or more cascade classifiers failed to load.")
    else:
        print("Cascade classifiers loaded successfully.")

    faces = face.detectMultiScale(gray, minNeighbors=5, scaleFactor=1.1, minSize=(25, 25))
    left_eye = leye.detectMultiScale(gray)
    right_eye = reye.detectMultiScale(gray)

    # cv2.rectangle(frame, (0, height - 50), (200, height), (0, 0, 0), thickness=cv2.FILLED)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (100, 100, 100), 1)

    for (x, y, w, h) in right_eye:
        r_eye = frame[y:y + h, x:x + w]
        r_eye = cv2.cvtColor(r_eye, cv2.COLOR_BGR2GRAY)
        r_eye = cv2.resize(r_eye, (24, 24))
        r_eye = r_eye / 255
        r_eye = r_eye.reshape(24, 24, -1)
        r_eye = np.expand_dims(r_eye, axis=0)
        rpred = np.argmax(model.predict(r_eye), axis=1)

    for (x, y, w, h) in left_eye:
        l_eye = frame[y:y + h, x:x + w]
        l_eye = cv2.cvtColor(l_eye, cv2.COLOR_BGR2GRAY)
        l_eye = cv2.resize(l_eye, (24, 24))
        l_eye = l_eye / 255
        l_eye = l_eye.reshape(24, 24, -1)
        l_eye = np.expand_dims(l_eye, axis=0)
        lpred = np.argmax(model.predict(l_eye), axis=1)

    if rpred[0] == 0 and lpred[0] == 0:
        score += 1
        # cv2.putText(frame, "Closed", (10, height - 20), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
    else:
        score -= 1
        # cv2.putText(frame, "Open", (10, height - 20), font, 1, (255, 255, 255), 1, cv2.LINE_AA)

    # Ensure score doesn't go below 0
    score = max(0, score)

    return score


# def decode_image_string(image_string):
#     # Convert base64 string to byte array
#     image_bytes = base64.b64decode(image_string)
#     # Convert byte array to numpy array
#     nparr = np.frombuffer(image_bytes, np.uint8)
#     # Decode the image
#     frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
#     return frame


@app.route('/predict', methods=['POST'])
def predict():
    request_data = request.json
    # print("request body: ", request_data, " this data")
    
    image_data = request_data.get('image')
    image_data_object = image_data.get('data')
    if image_data:
        binary_data = image_data_object['data']
        # print("binaryData: ", binary_data)
        binary_data_bytes = bytes(binary_data)
        # print(binary_data_bytes)
        image_array = np.frombuffer(binary_data_bytes, dtype=np.uint8)
        frame = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        final_score = detect_drowsiness(frame)

        # Return the result as a JSON response
        return jsonify({'score': final_score})

    # Check if the score exceeds the threshol

    else:
        return jsonify({'error': 'No image data found in the request'}), 400

@app.route('/', methods=['GET'])
def start():
    print("Server Working")
    return {"name": "rushiraj"}


if __name__ == '__main__':
    print("Server Started!!!")
    app.run(host='0.0.0.0', port=3000)
