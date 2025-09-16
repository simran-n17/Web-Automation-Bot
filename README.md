# Web Automation Bot

This project is a **Python Selenium bot** that automates interactions with a web browser. It uses **Google Chrome** and a matching **ChromeDriver** to perform tasks like opening websites, filling forms, and clicking buttons.

---

## 📌 Prerequisites

1. **Python 3.8+** installed
   [Download Python](https://www.python.org/downloads/)

2. **Google Chrome (Stable version)** installed
   [Download Chrome](https://www.google.com/chrome/)

3. **Selenium** (installed via `requirements.txt`)

4. **ChromeDriver** that matches your Chrome version.
   For Chrome `140.0.7339.128`, download:
   👉 [chromedriver-win64.zip](https://storage.googleapis.com/chrome-for-testing-public/140.0.7339.82/win64/chromedriver-win64.zip)

---

## ⚙️ Setup Instructions

1. **Clone or download** this project folder:

   ```bash
   git clone <your-repo-url>
   cd web_automation_bot
   ```

2. **Create a virtual environment** (recommended):

   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   source venv/bin/activate  # On Mac/Linux
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Download and set up ChromeDriver**:

   * Download the zip file from the link above.
   * Extract it → you’ll get `chromedriver.exe`.
   * Place `chromedriver.exe` inside your project folder:

     ```
     web_automation_bot/
     ├── bot.py
     ├── requirements.txt
     ├── chromedriver.exe
     ```

---

## 🚀 Running the Bot

Run the script using:

```bash
python bot.py
```

This will:

* Open Google Chrome
* Execute the steps defined inside `bot.py`

---

## 🛠 Troubleshooting

* **Chrome opens and closes instantly**
  → Add `time.sleep(5)` after opening to keep the window open.

* **Version mismatch error**
  → Ensure your Chrome version matches the ChromeDriver version.
  Check Chrome version:

  * Open Chrome → Settings → Help → About Google Chrome.

* **Want to skip downloading ChromeDriver manually?**
  Use `webdriver-manager`.
  Replace your driver setup in `bot.py` with:

  ```python
  from selenium import webdriver
  from webdriver_manager.chrome import ChromeDriverManager

  driver = webdriver.Chrome(ChromeDriverManager().install())
  ```

  And install:

  ```bash
  pip install webdriver-manager
  ```

---

## 📂 Project Structure

```
web_automation_bot/
├── bot.py              # Main automation script
├── requirements.txt    # Python dependencies
├── chromedriver.exe    # ChromeDriver (manual setup)
└── README.md           # Documentation
```

---

✨ You’re now ready to run your automation bot!