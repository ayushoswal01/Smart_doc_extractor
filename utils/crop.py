from flask import Flask, render_template, request
import os
from utils.pdf_handler import convert_pdf_to_images
from utils.detectors import detect_and_crop

UPLOAD_FOLDER = "uploads"
CROP_FOLDER = "static/crops"

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CROP_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    extracted_text = {}
    crops = []

    if request.method == "POST":
        file = request.files["doc"]
        path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(path)

        # Convert to image(s)
        images = convert_pdf_to_images(path) if path.lower().endswith(".pdf") else [path]

        # Process each image
        for img_path in images:
            results = extract_all_features(img_path, CROP_FOLDER)
            crops.extend(results["images"])
            extracted_text.update(results["texts"])

    return render_template("index.html", crops=crops, extracted=extracted_text)

if __name__ == "__main__":
    # For local debugging — not used on Render
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
