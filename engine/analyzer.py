from engine.iam_simulator import revoke_iam_access
from engine.logger import log_audit_entry
from engine.slack import send_alert_to_slack  # ✅ Import Slack integration

def score_log(log_text: str) -> float:
    if "unauthorized" in log_text.lower():
        return 0.9
    return 0.2

def extract_user_from_log(log_text: str) -> str:
    words = log_text.split()
    for i, word in enumerate(words):
        if word.lower() == "user" and i + 1 < len(words):
            return words[i + 1]
    return None

def analyze_log(log_text: str):
    score = score_log(log_text)
    response = {
        "log": log_text,
        "score": score,
        "action": "✅ Safe - no action taken"
    }

    if score > 0.5:
        # 🧠 Optional Slack alert here
        send_alert_to_slack(log_text, score)

        user = extract_user_from_log(log_text)
        if user:
            action_msg = revoke_iam_access(user)
            log_audit_entry(action_msg)
            response["action"] = f"🚨 IAM access revoked for {user}"
        else:
            response["action"] = "⚠️ High risk, but user unknown"

    return response
