from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

# Create a new image (background color and size)
img = Image.new('RGB', (1584, 396), color=(255, 255, 255))

# Create a drawing object to add text and elements
draw = ImageDraw.Draw(img)

# Load a font
font = ImageFont.truetype("arial_narrow_7.ttf", 80)  # Change path to a font available on your system

# Add your name 'Nakeeran' at the top
draw.text((150, 50), "Nakeeran", font=font, fill=(255, 255, 255))

# Add 'Python' text
draw.text((150, 200), "Python", font=font, fill=(255, 255, 255))

# Load Python logo and paste it
python_logo = Image.open("/home/ns/projects_files/Linkedin_banner_creating_with_python/Python-logo-removebg-preview.png")
python_logo = python_logo.resize((100, 100))
img.paste(python_logo, (50, 200), python_logo)

# Add 'Algorithm' text and icon
draw.text((150, 350), "Algorithm", font=font, fill=(255, 255, 255))

# Add HTML, CSS, JavaScript text and icons
tech_stack = ["HTML", "CSS", "JavaScript"]
x, y = 150, 500
for tech in tech_stack:
    draw.text((x, y), tech, font=font, fill=(255, 255, 255))
    y += 100  # Move each text down

# Add 'React JS' text
draw.text((150, 800), "React JS", font=font, fill=(255, 255, 255))

# Add 'Computer Vision' text
draw.text((150, 900), "Computer Vision", font=font, fill=(255, 255, 255))

# Add contact email at the bottom
draw.text((50, 950), "Contact: nakeeranthavasiappn@gmail.com", font=font, fill=(255, 255, 255))

# Save the image
img.save('/home/ns/projects_files/Linkedin_banner_creating_with_python/linkedin_background.png')

# Show the image
img.show()
