import os
import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# ======== LOAD ENVIRONMENT VARIABLES ========
load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

# ======== DATE CHECKING ========
today = datetime.date.today()

# Calculate the last day of this month
if today.month == 12:
    last_day = datetime.date(today.year, 12, 31)
else:
    next_month = datetime.date(today.year, today.month + 1, 1)
    last_day = next_month - datetime.timedelta(days=1)

# Reminder day: 7 days before end of month
reminder_day = last_day - datetime.timedelta(days=7)

# ======== TEST MODE FLAG ========
test_mode = True  # Change to False in production

# ======== SEND REMINDER IF TODAY MATCHES OR IN TEST MODE ========
if today == reminder_day or test_mode:
    subject = "🏠 Rent Reminder"
    body = f"""Hello,

This is a friendly reminder that your rent is due in 7 days — on {last_day.strftime('%B %d')}.

Please make sure to pay your rent on time.

Thanks!
- Your Python Script 🤖
"""

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, TO_EMAIL.split(","), msg.as_string())
        server.quit()
        print("✅ Rent reminder sent successfully.")
    except Exception as e:
        print(f"❌ Error sending email: {e}")
else:
    print(f"📅 Today is {today}. Rent reminder will be sent on {reminder_day}.")
