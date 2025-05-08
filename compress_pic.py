from PIL import Image
import os

def resize_to_target(input_path, output_path, target_kb):
    img = Image.open(input_path)
    width, height = img.size
    quality = 95

    while True:
        # reduce the size (10% each time)
        width = int(width * 0.9)
        height = int(height * 0.9)
        resized = img.resize((width, height), Image.Resampling.LANCZOS)

        resized.save(output_path, format="JPEG", quality=quality, optimize=True)
        if os.path.getsize(output_path) <= target_kb * 1024:
            break

if __name__ == '__main__':
    resize_to_target("src_path/my_pic.jpg", "output_path/resized.jpg", 240)  # target：240KB
