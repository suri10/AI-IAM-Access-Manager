import os
import requests
from dotenv import load_dotenv

load_dotenv()

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def send_alert_to_slack(log_text: str, score: float):
    if not SLACK_WEBHOOK_URL:
        print("❌ Slack webhook not set.")
        return

    payload = {
        "text": f"🚨 *Threat Detected!*\n*Log:* `{log_text}`\n*Score:* {score}"
    }

    try:
        response = requests.post(SLACK_WEBHOOK_URL, json=payload)
        response.raise_for_status()
        print("✅ Slack alert sent")
    except Exception as e:
        print(f"❌ Failed to send Slack alert: {e}")
