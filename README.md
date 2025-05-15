# AI IAM Access Manager

**Automated AI-powered system to detect suspicious IAM-related logs, simulate access revocation, and send real-time alerts to Slack.**

---

## Features

- Log analysis with risk scoring based on keywords (e.g., unauthorized access).
- Simulation of IAM actions like revoking access for suspicious users.
- Real-time Slack alerts for high-risk security events.
- Simple REST API built with FastAPI for log ingestion and analysis.
- Easily extensible for future AI-powered enhancements and AWS integration.

---

## Tech Stack

- Python 3.9+
- FastAPI
- Requests
- dotenv (for environment variables)
- Slack Incoming Webhooks
- Uvicorn (ASGI server)

---

## Setup & Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/ai-iam-access-manager.git
   cd ai-iam-access-manager
````

2. Create and activate a Python virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your Slack webhook URL:

   ```env
   SLACK_WEBHOOK_URL=https://hooks.slack.com/services/your/webhook/url
   ```

5. Run the FastAPI server:

   ```bash
   uvicorn api.main:app --reload
   ```

---

## Usage

* Send POST requests to `/logs/analyze` endpoint with JSON body:

  ```json
  {
    "log": "unauthorized access to admin panel"
  }
  ```

* The system will analyze the log, score risk, simulate IAM actions, and send a Slack alert if necessary.

---

## Future Work

* Integrate AWS IAM via Boto3 to enforce actual policy changes.
* Add AI/ML models for intelligent log analysis and anomaly detection.
* Expand support for other AWS security logs (CloudTrail, VPC Flow Logs).
* Implement a web dashboard for monitoring alerts and actions.

---

## License

MIT License

---

## Contact

For questions or collaboration, reach out at loganathansuresh01@gmail.com.


