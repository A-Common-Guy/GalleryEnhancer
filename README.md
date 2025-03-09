# Lightly Image Selection Pipeline

This repository provides an automated, efficient, and easy-to-use image-selection pipeline using [Lightly](https://docs.lightly.ai/docs).

---

## 📁 Project Structure

```
project-root/
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── image_utils.py
│   ├── lightly_utils.py
│   └── pipeline.py
├── run_pipeline.sh              # Runs Docker container and Python pipeline
├── reports/                     # Stores pipeline reports and filenames
├── .env                         # Securely stores Lightly API token
├── requirements.txt             # Python dependencies
└── README.md                    # Documentation
```

---

## 🚀 Quickstart

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd project-root
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API Token
Create a `.env` file and insert your Lightly API token:
```bash
LIGHTLY_KEY=your_api_token_here
```

### 4. Make the pipeline executable
```bash
chmod +x run.sh
```


### 5. Run the Pipeline
```bash
bash run.sh <gallery_folder> <input_folder> <output_folder>
```

---

## 🛠️ Customization

- **Number of samples**: Adjust directly in `scripts/run_pipeline.sh` or pass via environment variables.
- **Resize dimensions**: Modify `image_utils.py`.
- **Selection strategy**: Edit `lightly_utils.py`.

---

## 📌 Dependencies

- Python 3.10+
- Docker


---

## 🐳 Docker Integration

The pipeline runs a Docker container (`lightly/worker:latest`) to execute Lightly operations. Container lifecycle (start, stop, remove) is managed automatically in `scripts/run_pipeline.sh`.

---

## ⚠️ Troubleshooting

- **Permission errors (401/403)**: Verify your `LIGHTLY_KEY` in `.env`.
- **Docker issues**: Check container logs:
```bash
docker logs lightly_worker_container
```

---

## 📖 References

- [Lightly Documentation](https://docs.lightly.ai/docs)

---

## ✅ License

Distributed under the MIT License.

---


# 🌟 Automatic Gallery Picture Selector 

Welcome to your smart gallery curator! This simple yet powerful pipeline is designed to automatically choose the most diverse and representative images from your vast collection, making it perfect for reducing redundancy and resource usage.

Imagine you've returned from a long photography session or event with hundreds or even thousands of images. Going through all of them manually would take hours, maybe even days. This is where your Automatic Gallery Picture Selector comes in—helping you effortlessly select the most diverse set of photos.

## 📸 How it Works

1. **Feeding the Gallery:**

   - You place your raw, high-resolution images into the 'gallery' folder.

2. **Automatic Image Optimization**

   - The pipeline first resizes your images to a manageable size (max 800x800 pixels), maintaining their original aspect ratios, ensuring the selection process remains efficient and fast.

3. **Smart Selection with AI**:

   - The resized images are analyzed by a powerful AI from Lightly.ai. It carefully picks out the images that maximize visual diversity, reducing redundancy.

4. **Instantly Accessible Results**:

   - After processing, the selected images are neatly collected into a dedicated output folder. You're left with a carefully curated selection that’s diverse, compact, and ready for sharing or further editing.

## 🌟 Imagine the Possibilities

- Quickly select the best images to showcase in a portfolio.
- Reduce storage by selecting and keeping only unique and meaningful images.
- Speed up your workflow dramatically, freeing your time for creativity and innovation.

No more scrolling endlessly or guessing which photos best capture the uniqueness of your gallery—let your Automatic Gallery Picture Selector bring clarity and simplicity to your photo selection process!

---

Ready to give it a try? Just follow the Quickstart guide and see the magic for yourself!



