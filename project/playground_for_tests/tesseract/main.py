import cv2
import pytesseract

# Path to Tesseract executable (for Windows, adjust the path accordingly)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load Haar Cascade for license plate detection
plate_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')

# Function to detect license plates and extract text
def detect_license_plate(image_path):
    # Read the image
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect license plates
    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

    for (x, y, w, h) in plates:
        # Draw rectangle around the detected plate
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Crop the license plate
        plate_img = gray[y:y+h, x:x+w]

        # Apply OCR to read text
        text = pytesseract.image_to_string(plate_img, config='--psm 8')
        print(f"Detected License Plate Number: {text.strip()}")

        # Display the cropped plate
        cv2.imshow('Plate', plate_img)

    # Display the result
    cv

