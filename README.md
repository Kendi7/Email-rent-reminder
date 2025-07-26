
## 📧 Python Email Automation – Monthly Rent Reminder

This project is a simple Python script that sends **automatic rent reminder emails** 7 days before the end of every month. It uses the Gmail SMTP server to send emails securely using environment variables for your credentials.

---

### ✅ Features

* Sends an automated rent reminder to your inbox.
* Uses `.env` file to protect sensitive credentials.
* Built-in test mode for debugging and confirmation.
* Scheduled based on the current date logic.
* Easily customizable.

---

### 🧰 Requirements

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

### 📁 File Structure

```
rent_reminder/
│
├── rent_reminder.py         # Main script
├── .env                     # Environment variables file (not shared)
├── requirements.txt         # Python dependencies
└── README.md                # This guide
```

---

### 🔐 .env File Setup

Create a `.env` file in the root directory and add the following:

```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password_without_spaces
TO_EMAIL=receiver_email@example.com
```

**Example with arbitrary values (for learning only):**

```env
EMAIL_ADDRESS=janedoe@gmail.com
EMAIL_PASSWORD=abcnftcuhwqynkxcn(generic_for testing-replace with your own)
TO_EMAIL=janedoe@gmail.com
```

> ❗️ Make sure to use a [Gmail App Password](https://support.google.com/accounts/answer/185833?hl=en) instead of your actual email password. This requires 2FA to be enabled on your Gmail account.

---

### ⚙️ Setting Up & Running

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/rent_reminder.git
cd rent_reminder
```

2. **Install required libraries**:

```bash
pip install -r requirements.txt
```

3. **Create and configure your `.env` file** as shown above.

4. **Run the script manually**:

```bash
python rent_reminder.py
```

---

### 🔄 Automated Scheduling (Optional)

You can set this script to run automatically using:

#### 🪟 On Windows (Task Scheduler):

* Open Task Scheduler
* Create a basic task
* Trigger: Daily
* Action: Start a Program → `python` and path to `rent_reminder.py`

#### 🐧 On Linux/macOS (Crontab):

```bash
crontab -e
```

Add this line to run daily at 9 AM:

```bash
0 9 * * * /usr/bin/python3 /path/to/rent_reminder.py
```

---

### 🧪 Testing

To force the email to send even when it's not 7 days before month-end, enable test mode in the script:

```python
test_mode = True
```

Once confirmed, set it back to `False` for production.

---

### 📦 Sample `requirements.txt`

```txt
python-dotenv
```

You can generate your own by running:

```bash
pip freeze > requirements.txt
```

---

### 🤝 Contribution

Pull requests are welcome! If you'd like to add more features (e.g. attachments, HTML email, logging), feel free to fork and improve.

---

### 🛡️ Disclaimer

This is a basic demo project. Use it responsibly. Make sure you secure your credentials and do not expose the `.env` file.

---

### 💬 Support

For questions, feel free to raise an issue or email the maintainer.

---

