from flask import Flask, render_template, request
import numpy as np
import cv2
import os
from tensorflow.keras.models import load_model
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Load your trained model (fix path for Windows)
model = load_model(r'C:\Users\ghava\Downloads\Cats_Dog_Classification\cat_dog_classifier_model_new.h5')

# Prediction function
def predict_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (200, 200))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    prediction = model.predict(img)[0][0]
    print(f"Prediction score: {prediction}")
    return "Cat 🐱" if prediction > 0.5 else "Dog 🐶 "

# Home route
@app.route('/', methods=['GET', 'POST'])
def index():
    label = None
    image_url = None

    if request.method == 'POST' and request.files.get('image'):
        image = request.files['image']
        filename = secure_filename(image.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(file_path)

        label = predict_image(file_path)
        image_url = f"/static/uploads/{filename}"

    return render_template("index.html", label=label, image_url=image_url)

if __name__ == '__main__':
    print("🔥 Starting Flask server...")
    app.run(debug=True, host='127.0.0.1', port=5000)

