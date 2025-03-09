from PIL import Image
import os

def resize_images(input_dir, output_dir, max_size=(800, 800)):
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            img_path = os.path.join(input_dir, filename)
            img = Image.open(img_path)
            img.thumbnail(max_size)
            img.save(os.path.join(output_dir, filename))
