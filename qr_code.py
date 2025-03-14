"""
This script generates a QR code that links to a resume PDF hosted online.
It adds a text label below the QR code, prompting users to scan the code to view the resume.
The QR code and text are combined into a new image, which is displayed and saved as "qrcode.png".
"""

# Import libraries
import qrcode
from PIL import Image, ImageDraw, ImageFont

# Create QR code with specified parameters
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4,
)
qr.add_data('https://mdislam1.github.io/resume-host/Md_Islam_Resume.pdf')
qr.make(fit = True)

# Generate the QR code image
img = qr.make_image(fill_color = "black", back_color = "white")
img = img.convert("RGB")

# Define the text to be added below the QR code
text = "Scan to view my resume"
font = ImageFont.load_default(size = 20)
draw = ImageDraw.Draw(img)
text_bbox = draw.textbbox((0, 0), text, font = font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

# Create a new image with space for the QR code and text
new_img = Image.new("RGB", (img.width, img.height + text_height + 20), "white")
new_img.paste(img, (0, 0))

# Draw the text on the new image below the QR code
draw = ImageDraw.Draw(new_img)
text_x = (img.width - text_width) // 2
text_y = img.height + 10
draw.text((text_x, text_y), text, fill = "black", font = font)

# Display and save the final image
new_img.show()
new_img.save("qrcode.png")