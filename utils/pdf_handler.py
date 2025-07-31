from pdf2image import convert_from_path
import os

def convert_pdf_to_images(pdf_path):
    # Update this path to your actual Poppler binary directory
    poppler_path = r"C:\poppler\Library\bin"

    # Convert PDF to images using the specified Poppler path
    images = convert_from_path(pdf_path)

    # Save images to disk
    img_paths = []
    os.makedirs("uploads", exist_ok=True)  # Make sure uploads directory exists

    for i, img in enumerate(images):
        path = f"uploads/page_{i}.png"
        img.save(path, "PNG")
        img_paths.append(path)

    return img_paths
