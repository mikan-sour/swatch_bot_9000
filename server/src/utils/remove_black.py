from PIL import Image

def remove_black_pixels(image_path):
    # Open the image using Pillow
    image = Image.open(image_path)

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

    image.save(image_path)

def overlay_images(background_path, overlay_path, output_path):
    # Open the background image
    background = Image.open(background_path)

    # Open the overlay image
    overlay = Image.open(overlay_path)

    # Resize the overlay image to match the background size
    overlay = overlay.resize(background.size)

    # Create a new image with transparency
    result = Image.new('RGBA', background.size)

    # Paste the background image onto the result image
    result.paste(background, (0, 0))

    # Paste the overlay image onto the result image with alpha blending
    result.paste(overlay, (0, 0), mask=overlay)

    # Save the resulting image
    result.save(output_path)
    print(f"Overlay image saved to: {output_path}")