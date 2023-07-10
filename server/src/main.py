from src.clients.db import DBClient
from src.utils.transparify import make_white_pixels_transparent, make_below_threshold_black
from src.utils.overlay import overlay_silhouette_on_floral_print
from src.utils.cleanup import make_outside_white
from src.utils.remove_black import remove_black_pixels, overlay_images

from src.api import api

def make_an_image():
    make_white_pixels_transparent("../IN/in_3.png", "../OUT/out.png", 220)
    make_below_threshold_black("../OUT/out.png", "../OUT/out.png", 219)
    overlay_silhouette_on_floral_print("../OUT/out.png", "../IN/in_swatch.png", "../out_overlay.png")
    make_outside_white("../out_overlay.png", "../out_overlay.png")
    make_white_pixels_transparent("../IN/in_3.png", "../OUT/out.png", 220)
    remove_black_pixels("../out_overlay.png")
    overlay_images("../out_overlay.png", "../OUT/out.png", "../out_overlay.png")

def main():
    db = DBClient().connect()
    api.run()

if __name__ == '__main__':
    main()