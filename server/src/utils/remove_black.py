from PIL import Image

def remove_black_pixels(image):
    # Open the image using Pillow
    # image = Image.open(image)

    # Get the pixel data from the image
    pixels = image.load()

    # Get the image dimensions
    width, height = image.size

    # Iterate over each pixel in the image
    for y in range(height):
        for x in range(width):
            # Get the pixel value as a tuple
            pixel = pixels[x, y]

            # Check if the pixel is white (255, 255, 255) in any channel
            if all(channel == 255 for channel in pixel[:3]):
                # Set the pixel to transparent (0, 0, 0, 0) for RGBA images
                if len(pixel) == 4:
                    pixels[x, y] = (0, 0, 0, 0)
                # Set the pixel to black (0, 0, 0) for RGB images
                else:
                    pixels[x, y] = (0, 0, 0)

    return image

def overlay_images(background_image, overlay_image):


    # Resize the overlay image to match the background size
    overlay = overlay_image.resize(background_image.size)

    # Create a new image with transparency
    result = Image.new('RGBA', background_image.size)

    # Paste the background image onto the result image
    result.paste(background_image, (0, 0))

    # Paste the overlay image onto the result image with alpha blending
    result.paste(overlay, (0, 0), mask=overlay)

    # Save the resulting image
    return result