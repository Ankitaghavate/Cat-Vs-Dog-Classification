# 🐶🐱 Cat vs Dog Classifier

A deep learning project to classify cat vs dog images using a custom CNN and deployed with Flask.

## 📊 Dataset
- Kaggle: [Dogs vs Cats Dataset](https://www.kaggle.com/competitions/dogs-vs-cats/data)
- Used 3,000 images (due to RAM limits)
- Resized to `200x200`, RGB format
- Train/Test split

## ⚙️ Setup
1. Create a `kaggle.json` API key from your Kaggle account.
2. Upload it to your Colab or working directory.
3. Run this setup to download the dataset:
```python
!pip install -q kaggle
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json
!kaggle competitions download -c dogs-vs-cats
!unzip dogs-vs-cats.zip
```
4. Resize images to `200x200` and split into train/test.

## 🧠 Model
- CNN built from scratch (Conv → Pool → Dense)
- Activation: ReLU + Softmax
- Loss: `sparse_categorical_crossentropy`
- Optimizer: `adam`
- Epochs: 15  
- Accuracy: 82% (Train), 69% (Test)

## 🚀 Deployment
- Built with Flask
- Upload image → Predict Cat 🐱 or Dog 🐶
- Files:
  - `app.py`: Flask backend
  - `index.html`: UI
  - `model.h5`: Trained model
  - `static/uploads`: Uploaded images

## 🛠️ Run Locally
```bash
pip install -r requirements.txt
python app.py
```
Go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## ✨ By Ankita Ghavate
