import cv2
import numpy as np
from pyzbar.pyzbar import decode

def extract_qr_codes(image):
    qr_codes = decode(image)
    cropped = []
    for qr in qr_codes:
        x, y, w, h = qr.rect
        cropped.append(("qr", image[y:y+h, x:x+w]))
    return cropped

def extract_barcodes(image):
    barcodes = decode(image)
    cropped = []
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        cropped.append(("barcode", image[y:y+h, x:x+w]))
    return cropped

def extract_signatures(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cropped = []

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        aspect_ratio = w / float(h)
        area = cv2.contourArea(cnt)

        if 300 < area < 4000 and 1.5 < aspect_ratio < 6:
            sig_crop = image[y:y+h, x:x+w]
            cropped.append(("signature", sig_crop))

    return cropped

def extract_all_features(image):
    features = []
    features += extract_qr_codes(image)
    features += extract_barcodes(image)
    features += extract_signatures(image)
    return features
