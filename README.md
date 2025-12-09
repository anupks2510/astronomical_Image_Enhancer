
# 🌌 AstroEnhance — Astronomical Image Enhancement System

AstroEnhance is a web-based image enhancement platform designed specifically for **astronomical images**. It uses a **two-stage AI processing pipeline**:

1️⃣ **Denoising Model** — Removes noise caused by atmospheric interference and low-light capture
2️⃣ **Real-ESRGAN Super-Resolution Model** — Improves detail and resolution of stars, galaxies, and deep-space objects

Built with **Django**, AstroEnhance allows users to upload noisy astronomical photos and instantly obtain high-clarity enhanced results.

---

## ✨ Key Features

✔ **AI-based denoising** for astronomical noise reduction
✔ **Super-resolution enhancement** using Real-ESRGAN (general model for astronomy)
✔ **Upload → Process → Download** clean UI workflow
✔ Supports **PNG / JPG / JPEG** formats
✔ Before vs. After image display
✔ CPU and GPU compatibility
✔ Modular structure for future upgrades

---

## 🧠 Tech Stack

| Component         | Technology           |
| ----------------- | -------------------- |
| Backend Framework | Django (Python)      |
| Super-Resolution  | Real-ESRGAN          |
| Denoising Model   | Custom-trained model |
| Frontend          | HTML, CSS, Bootstrap |
| Storage           | Local File Storage   |

---

## 📂 Project Structure

```
astro_enhance/
│
├── image_processor/
│   ├── models/               # Denoising & Real-ESRGAN models
│   ├── utils/                # Image processing scripts
│   ├── views.py              # Processing logic + model inference
│   ├── urls.py
│   └── templates/            # UI pages
│
├── static/                   # CSS, JS, icons
├── media/                    # Uploaded and output images
├── requirements.txt
└── manage.py
```

> Real-ESRGAN dependency folder placed at:
> `REAL_ESRGAN/` (local model directory integrated into Django)

---

## 🔧 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/astro_enhance.git
cd astro_enhance

# Create virtual environment
python -m venv env
source env/bin/activate         # Linux/Mac
env\Scripts\activate            # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
```

---

## 🚀 How It Works

1️⃣ User uploads an astronomical image
2️⃣ Backend performs:

* Denoising → noise removal
* Real-ESRGAN → resolution enhancement

3️⃣ Enhanced output shown on final results page
4️⃣ Image can be downloaded and compared with original

---

## 📌 Future Upgrades

* GPU inference via CUDA support
* Batch image enhancement
* API endpoint for remote applications
* Additional astronomy-specific SR models
* Result quality metrics visualization
* User authentication + image history

---

## 🧑‍💻 Developer

**Anup Kumar Singh**
AI | ML | Python | Computer Vision
Email: *your-email*
LinkedIn: *(optional)*

---

