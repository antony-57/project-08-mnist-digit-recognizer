import joblib
import numpy as np
from PIL import Image, ImageOps

model = joblib.load("models/digit_recognizer_model.pkl")

image = Image.open("sample_digit.png").convert("L")
image = ImageOps.invert(image)

image_array = np.array(image)
coords = np.argwhere(image_array > 30)

if coords.size == 0:
    print("No digit detected.")
    exit()

y_min, x_min = coords.min(axis=0)
y_max, x_max = coords.max(axis=0)

cropped = image.crop(
    (x_min, y_min, x_max + 1, y_max + 1)
)

cropped.thumbnail(
    (20, 20),
    Image.Resampling.LANCZOS
)

canvas = Image.new("L", (28, 28), 0)

x = (28 - cropped.width) // 2
y = (28 - cropped.height) // 2

canvas.paste(cropped, (x, y))

processed = np.array(canvas)
processed = processed / 255.0
processed = processed.reshape(1, 784)

prediction = model.predict(processed, verbose=0)
predicted_digit = np.argmax(prediction)

print("Predicted digit:", predicted_digit)