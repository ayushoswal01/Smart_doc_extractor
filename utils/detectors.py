import cv2
import pytesseract
from pyzbar.pyzbar import decode
import os
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Change if different


def detect_signature(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, threshed = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(threshed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    signature_regions = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        aspect_ratio = w / h
        area = cv2.contourArea(cnt)

        if 1200 < area < 20000 and 2.0 < aspect_ratio < 8.0 and h < 200:
            signature_regions.append((x, y, w, h))

    return signature_regions

def detect_and_crop(img_path, output_dir):
    img = cv2.imread(img_path)
    results = {"images": [], "texts": {}}
    h, w, _ = img.shape

    barcodes = decode(img)
    for i, bc in enumerate(barcodes):
        x, y, bw, bh = bc.rect
        crop = img[y:y+bh, x:x+bw]
        fname = os.path.join(output_dir, f"barcode_{i}.png")
        cv2.imwrite(fname, crop)
        results["images"].append(fname)
        results["texts"][f"Barcode {i}"] = bc.data.decode()

    data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
    for i, text in enumerate(data['text']):
        if int(data['conf'][i]) > 60 and len(text.strip()) > 3:
            x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
            crop = img[y:y+h, x:x+w]
            fname = os.path.join(output_dir, f"text_{i}.png")
            cv2.imwrite(fname, crop)
            results["images"].append(fname)
            results["texts"][f"Text Block {i}"] = text.strip()

    sig_boxes = detect_signature(img)
    for i, (x, y, w, h) in enumerate(sig_boxes):
        crop = img[y:y+h, x:x+w]
        fname = os.path.join(output_dir, f"signature_{i}.png")
        cv2.imwrite(fname, crop)
        results["images"].append(fname)
        results["texts"][f"Signature {i}"] = "Signature area detected"

    return results
