from PIL import Image

def overlay_silhouette_on_floral_print(silhouette_file, swatch_file):
    # Open the asset image
    # silhouette = Image.open(silhouette_file).convert("RGBA")
    silhouette_file.convert("RGBA")

    # Open the floral print image
    floral_print = Image.open(swatch_file).convert("RGBA")

    # Resize the floral print image to match the asset size
    resized_floral_print = floral_print.resize(silhouette_file.size)

    # Create a new image for the overlay
    overlay = Image.alpha_composite(resized_floral_print, silhouette_file)

    return overlay
