from PIL import Image

def make_below_threshold_black(image, threshold=128):
    # Open the image
    image.convert("RGBA")

    # Get the image data
    data = image.getdata()

    # Create a new image with black pixels
    new_data = []
    for item in data:
        # If the pixel is below the threshold, make it black
        if item[0] < threshold:
            new_data.append((0, 0, 0, item[3]))  # Set RGB to black, preserve alpha
        else:
            new_data.append(item)

    # Update the image data
    image.putdata(new_data)

    return image

def make_white_pixels_transparent(file, threshold=200):
    # Open the image
    image = Image.open(file)
    image.convert("RGBA")

    # Get the image data
    data = image.getdata()

    # Create a new image with transparent pixels
    new_data = []
    for item in data:
        # If the pixel is white or above the threshold, make it transparent
        if all(channel >= threshold for channel in item[:3]):
            new_data.append((255, 255, 255, 0))  # Set alpha to 0 (transparent)
        else:
            new_data.append(item)

    # Update the image data
    image.putdata(new_data)

    return image



def overlay_images(background_file, overlay_file):
    # Open the background image

    background = Image.open(background_file)

    # Open the overlay image
    overlay = Image.open(overlay_file)

    # Resize the overlay image to match the background size
    overlay = overlay.resize(background.size)

    # Create a new image with transparency
    result = Image.new('RGBA', background.size)

    # Paste the background image onto the result image
    result.paste(background, (0, 0))

    # Paste the overlay image onto the result image with alpha blending
    result.paste(overlay, (0, 0), mask=overlay)

    # Save the resulting image
    return result