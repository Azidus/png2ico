from sys import argv
from os import path
from PIL import Image

def convert_png_to_ico(png_path, sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]):
    """
    Converts a PNG file to a Windows ICO file with transparency.

    Args:
        png_path (str): Path to the input .png file.
        sizes (list): Icon sizes to include in the output .ico file.
    """
    if not path.exists(png_path):
        print(f"❌ File not found: {png_path}")
        return

    if not png_path.lower().endswith(".png"):
        print("❌ Please provide a .png file.")
        return

    # Set output path
    ico_path = path.splitext(png_path)[0] + ".ico"

    try:
        # Load image and convert to RGBA (for transparency)
        img = Image.open(png_path).convert("RGBA")
        img.save(ico_path, format="ICO", sizes=sizes)
        print(f"✅ Converted '{png_path}' → '{ico_path}'")
    except Exception as e:
        print(f"❌ Conversion failed: {e}")

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python png_to_ico.py <path_to_image.png>")
    else:
        png_path = argv[1]
        convert_png_to_ico(png_path)
