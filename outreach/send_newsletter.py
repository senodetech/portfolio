"""
Interactive Outreach & Newsletter Dispatcher for ApexTasks
Features:
- Preview list of owners
- Send test verification email to avsentech@gmail.com
- Safe interactive confirmation before dispatching
"""

import os
import sys
import csv
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email_templates import get_email_subject, get_html_email, get_text_email

def load_leads(csv_file="leads.csv"):
    if not os.path.exists(csv_file):
        print(f"Error: {csv_file} not found.")
        return []
    with open(csv_file, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def send_single_email(smtp_server, sender_email, recipient_email, subject, html_body, text_body):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = f"Senapathy <{sender_email}>"
    msg["To"] = recipient_email
    msg["Reply-To"] = sender_email

    msg.attach(MIMEText(text_body, "plain"))
    msg.attach(MIMEText(html_body, "html"))

    smtp_server.sendmail(sender_email, recipient_email, msg.as_string())

def main():
    print("=" * 65)
    print("📧 ApexTasks Small Business Outreach & Newsletter Tool")
    print("=" * 65)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(script_dir, "leads.csv")
    leads = load_leads(csv_file)

    if not leads:
        print("No leads found in leads.csv.")
        return

    print(f"\n📋 Loaded {len(leads)} target business owners/leads from leads.csv:\n")
    for i, lead in enumerate(leads, 1):
        print(f"  {i}. {lead['Owner / Lead Name']} ({lead['Role']}) - {lead['Business Name']}")
        print(f"     Email: {lead['Email']} | Industry: {lead['Industry']}")

    print("\n" + "-" * 65)
    print("OPTIONS:")
    print("  [1] Send TEST preview email to avsentech@gmail.com")
    print("  [2] Send outreach campaign to ALL leads (Requires confirmation)")
    print("  [3] Exit")
    print("-" * 65)

    choice = input("Enter option (1/2/3): ").strip()

    if choice == "3":
        print("Exiting.")
        return

    # SMTP Configuration
    print("\n🔑 SMTP Server Configuration (e.g. Gmail / Outlook / Custom SMTP):")
    smtp_host = os.environ.get("SMTP_HOST", "smtp.gmail.com")
    smtp_port = int(os.environ.get("SMTP_PORT", "587"))
    sender_email = os.environ.get("SMTP_USER", "avsentech@gmail.com")
    
    print(f"Sender Email: {sender_email}")
    smtp_pass = os.environ.get("SMTP_PASSWORD")
    if not smtp_pass:
        smtp_pass = input("Enter Gmail App Password (or SMTP password): ").strip()

    if not smtp_pass:
        print("❌ Password required to connect to SMTP. Aborting.")
        return

    try:
        print(f"\nConnecting to {smtp_host}:{smtp_port}...")
        server = smtplib.SMTP(smtp_host, smtp_port)
        server.starttls()
        server.login(sender_email, smtp_pass)
        print("✅ SMTP Authentication successful!")
    except Exception as e:
        print(f"❌ Failed to connect to SMTP server: {e}")
        print("Tip: For Gmail, create an App Password at: https://myaccount.google.com/apppasswords")
        return

    if choice == "1":
        # Send Test Email
        test_recipient = "avsentech@gmail.com"
        print(f"\n🚀 Sending TEST email to {test_recipient}...")
        subject = get_email_subject("Sena", "Apex Studio")
        html_content = get_html_email("Sena", "Apex Studio", "This is a test preview of your newsletter campaign.", "Testing agile task workflows")
        text_content = get_text_email("Sena", "Apex Studio", "This is a test preview of your newsletter campaign.", "Testing agile task workflows")

        try:
            send_single_email(server, sender_email, test_recipient, subject, html_content, text_content)
            print(f"🎉 Test email delivered successfully to {test_recipient}!")
        except Exception as e:
            print(f"❌ Failed to send test email: {e}")

    elif choice == "2":
        # Bulk Dispatch with Confirmation
        print(f"\n⚠️ YOU ARE ABOUT TO SEND EMAILS TO {len(leads)} RECIPIENTS.")
        confirm = input("Type 'CONFIRM' to proceed with dispatch: ").strip()

        if confirm != "CONFIRM":
            print("Dispatch cancelled by user.")
            server.quit()
            return

        print("\n🚀 Starting email dispatch...")
        sent_count = 0
        for i, lead in enumerate(leads, 1):
            recipient = lead["Email"]
            name = lead["Owner / Lead Name"]
            company = lead["Business Name"]
            custom_note = lead.get("Custom Note", "")
            pain_point = lead.get("Current Pain Point", "")

            subject = get_email_subject(name, company)
            html_content = get_html_email(name, company, custom_note, pain_point)
            text_content = get_text_email(name, company, custom_note, pain_point)

            try:
                print(f"  [{i}/{len(leads)}] Sending to {name} <{recipient}> at {company}...")
                send_single_email(server, sender_email, recipient, subject, html_content, text_content)
                sent_count += 1
                time.sleep(2) # Friendly 2-second rate limit to prevent spam triggers
            except Exception as e:
                print(f"  ✗ Error sending to {recipient}: {e}")

        print(f"\n🎉 Campaign completed! Successfully sent {sent_count}/{len(leads)} emails.")

    server.quit()

if __name__ == "__main__":
    main()