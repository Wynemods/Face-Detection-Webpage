from flask import Flask, render_template, request, redirect, url_for
import cv2
import numpy as np
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['DETECTED_FOLDER'] = 'static/detected'

# Create folders if they don't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['DETECTED_FOLDER'], exist_ok=True)

# Load OpenCV pre-trained face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' not in request.files:
            return redirect(request.url)
        file = request.files['image']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Read image and detect faces
            img = cv2.imread(filepath)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

            # Draw rectangles around faces
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

            detected_path = os.path.join(app.config['DETECTED_FOLDER'], filename)
            cv2.imwrite(detected_path, img)

            # Return the detected image URL and face count
            return render_template('index.html', detected_image=url_for('detected_file', filename=filename), faces=len(faces))

    return render_template('index.html', detected_image=None, faces=0)

@app.route('/detected/<filename>')
def detected_file(filename):
    return redirect(url_for('static', filename='detected/' + filename))

if __name__ == '__main__':
    # Run the Flask app on localhost port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
