from flask import Flask, render_template, request
import os
import cv2
from utils.pdf_handler import convert_pdf_to_images

UPLOAD_FOLDER = "uploads"
CROP_FOLDER = "static/crops"

# Ensure upload and crop folders exist
os.makedirs(CROP_FOLDER, exist_ok=True)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    crops = []

    if request.method == "POST":
        file = request.files["doc"]
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)

        images = convert_pdf_to_images(path) if path.endswith(".pdf") else [path]

        for img_path in images:
            image = cv2.imread(img_path)
            features = extract_all_features(image)

            for label, crop_img in features:
                filename = f"{label}_{len(crops)}.png"
                crop_path = os.path.join(CROP_FOLDER, filename)
                cv2.imwrite(crop_path, crop_img)
                crops.append(crop_path)

    return render_template("index.html", crops=crops)

if __name__ == "__main__":
    app.run(debug=True)
