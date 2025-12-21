import easyocr
import cv2

# Image read
img = cv2.imread("captcha.png")

# Resize incresing 2x Size
img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# EasyOCR reader (English only)
reader = easyocr.Reader(['en'], gpu=True)

# OCR
result = reader.readtext(
    img,
    detail=0,
    allowlist='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
)

print("CAPTCHA TEXT:", result)
