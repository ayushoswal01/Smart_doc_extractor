# 🧠 Smart Document Extractor (AI-Based)

A Python Flask web application that intelligently detects and extracts only **QR Codes**, **Barcodes**, and **Signatures** from uploaded documents (PDF or images). Cropped outputs are saved and displayed visually.

---

## 🚀 Features

- 📄 Upload PDF or image documents
- 🔍 Automatically detect:
  - ✅ QR Codes
  - ✅ Barcodes
  - ✅ Signatures (using image processing)
- ✂️ Crops and displays only important components
- 🧠 Powered by:
  - OpenCV
  - Tesseract OCR
  - PDF2Image

---

## 📁 Project Structure

smart_doc_extractor/
│
├── app.py
├── requirements.txt
├── templates/
│ └── index.html
├── static/
│ └── crops/ # Auto-generated cropped outputs
├── uploads/ # Uploaded files
├── utils/
│ ├── pdf_handler.py # Convert PDF to images
│ └── crop.py # Core logic to detect QR, barcode, signature
└── README.md





---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/smart_doc_extractor.git
cd smart_doc_extractor
2. Set Up Virtual Environment
bash
Copy code
python -m venv venv
venv\Scripts\activate      # On Windows
# source venv/bin/activate  # On macOS/Linux
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Install Tesseract & Poppler
Tesseract: https://github.com/tesseract-ocr/tesseract

Poppler (for Windows): https://github.com/oschwartz10612/poppler-windows/releases/

➡️ Make sure to add Poppler's bin/ path to your environment variables:

makefile
Copy code
C:\poppler\Library\bin
🧪 Run the App
bash
Copy code
python app.py
Visit: http://127.0.0.1:5000

### 🛠 Tech Stack
Python 3.8+

Flask

OpenCV

Tesseract OCR

PDF2Image

