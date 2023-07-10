from PIL import Image

def make_outside_white(image_path, output_path):
    # Open the image
    image = Image.open(image_path).convert("RGBA")

    # Get the image data
    pixels = image.load()

    # Process pixels from top to bottom
    for y in range(image.height):
        for x in range(image.width):
            # Get the pixel value
            pixel = pixels[x, y]

            # Check if the pixel is black
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                # Move to the next row if pixel is black
                break

            # Make the pixel transparent
            pixels[x, y] = (pixel[0], pixel[1], pixel[2], 0)

        else:
            continue  # Continue to the next column in the same row
        # break  # Break if pixel is black and move to the next row

    # Process pixels from right to left
    for x in reversed(range(image.width)):
        for y in range(image.height):
            # Get the pixel value
            pixel = pixels[x, y]

            # Check if the pixel is black
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                # Move to the next column if pixel is black
                break

            # Make the pixel transparent
            pixels[x, y] = (pixel[0], pixel[1], pixel[2], 0)

        else:
            continue  # Continue to the next row in the same column
        # break  # Break if pixel is black and move to the next column

    # Process pixels from bottom to top
    for y in reversed(range(image.height)):
        for x in reversed(range(image.width)):
            # Get the pixel value
            pixel = pixels[x, y]

            # Check if the pixel is black
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                # Move to the next row if pixel is black
                break

            # Make the pixel transparent
            pixels[x, y] = (pixel[0], pixel[1], pixel[2], 0)

        else:
            continue  # Continue to the next column in the same row
        # break  # Break if pixel is black and move to the next row

    # Process pixels from left to right
    for x in range(image.width):
        for y in reversed(range(image.height)):
            # Get the pixel value
            pixel = pixels[x, y]

            # Check if the pixel is black
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                # Move to the next column if pixel is black
                break

            # Make the pixel transparent
            pixels[x, y] = (pixel[0], pixel[1], pixel[2], 0)

        else:
            continue  # Continue to the next row in the same column
        # break  # Break if pixel is black and move to the next column

    # Save the modified image
    image.save(output_path)