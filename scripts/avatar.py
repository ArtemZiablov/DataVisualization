from PIL import Image, ImageDraw, ImageFont
import random
import string

# Define resolution and list of letters
width, height = 35, 35
letters = string.ascii_uppercase

# Function to generate a random color
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Loop through each letter to create an avatar
for letter in letters:
    # Create a new image with a random background color
    img = Image.new('RGB', (width, height), random_color())
    draw = ImageDraw.Draw(img)

    # Set font and font size
    font_size = 18
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    # Calculate the text position using textbbox
    bbox = draw.textbbox((0, 0), letter, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    text_x = (width - text_width) / 2
    text_y = (height - text_height) / 2 - 2  # Slight upward adjustment

    # Draw the letter in the center
    draw.text((text_x, text_y), letter, font=font, fill="white")

    # Save the image
    img.save(f"{letter}.png")

print("Avatar images generated successfully.")
