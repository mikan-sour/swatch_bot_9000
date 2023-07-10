from PIL import Image

def overlay_silhouette_on_floral_print(silhouette_path, floral_print_path, output_path):
    # Open the silhouette image
    silhouette = Image.open(silhouette_path).convert("RGBA")

    # Open the floral print image
    floral_print = Image.open(floral_print_path).convert("RGBA")

    # Resize the floral print image to match the silhouette size
    resized_floral_print = floral_print.resize(silhouette.size)

    # Create a new image for the overlay
    overlay = Image.alpha_composite(resized_floral_print, silhouette)

    # Save the overlay image
    overlay.save(output_path)
