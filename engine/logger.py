
import os

AUDIT_LOG = os.path.join("logs", "iam_audit.log")

def log_audit_entry(entry: str):
    with open(AUDIT_LOG, "a") as f:
        f.write(entry + "\n")
