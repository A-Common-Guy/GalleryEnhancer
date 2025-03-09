import sys
import shutil
import os
from image_utils import resize_images
from lightly_utils import (
    create_or_reuse_dataset,
    schedule_run,
    monitor_run,
    export_selected_filenames,
)

def main(gallery_folder, input_folder, output_folder):
    print("Resizing images...")
    resize_images(gallery_folder, input_folder)
    print("Images resized!")
    client = create_or_reuse_dataset()

    print("Scheduling Lightly run...")
    run_id = schedule_run(client)
    if not monitor_run(client, run_id):
        raise RuntimeError("Lightly processing failed!")

    print("Exporting filenames...")
    filenames = export_selected_filenames(client)

    print("Copying selected images to output folder...")
    os.makedirs(output_folder, exist_ok=True)
    for filename in filenames:
        shutil.copy2(os.path.join(gallery_folder, filename), output_folder)

    print("Pipeline completed successfully!")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python -m lightly_pipeline.pipeline <gallery_folder> <input_folder> <output_folder>")
        sys.exit(1)

    _, gallery, input_folder, output_folder = sys.argv
    main(gallery, input_folder, output_folder)
