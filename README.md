# 🎬 Modex Video Downloader Bot

A Telegram bot that downloads public videos from multiple social media platforms and sends them directly back to users.

## 🚀 Features

- Download TikTok videos
- Download Instagram Reels & Posts
- Download X (Twitter) videos
- Download Snapchat videos
- Automatic file cleanup
- Download logging
- User cooldown protection
- Modular architecture
- Easy deployment on Render

---

## 📂 Project Structure

```text
telegram-video-bot/
│
├── bot.py
├── config.py
├── logger.py
├── requirements.txt
├── Procfile
├── runtime.txt
│
├── handlers/
├── downloaders/
├── database/
├── keyboards/
├── services/
├── utils/
├── downloads/
└── logs/
```

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/modex-video-downloader-bot.git

cd modex-video-downloader-bot
```

Create a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
```

---

## ▶ Running

```bash
python bot.py
```

---

## ☁ Deploy

This project is ready for deployment on Render.

---

## 📋 Supported Platforms

- TikTok
- Instagram
- X (Twitter)
- Snapchat

---

## 🛠 Tech Stack

- Python
- python-telegram-bot
- yt-dlp
- SQLite
- Render

---

## 📄 License

MIT License

---

## 👨‍💻 Developer

Built by **Modex**