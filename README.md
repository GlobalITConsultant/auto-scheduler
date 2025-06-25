# Auto Scheduler with Twilio and Housecall Pro

This is a Python-based backend service that:
- Answers phone calls using Twilio
- Schedules appointments using the Housecall Pro API
- Deployed on AWS or Google Cloud via Flask

## Requirements

- Python 3.10+
- Twilio account with a phone number and webhook
- Housecall Pro API access (MAX Plan)
- Ngrok or public URL for Twilio webhook testing

## Quick Start

1. Clone the repo
2. Create a `.env` file based on `.env.example`
3. Run locally:
   ```
   pip install -r requirements.txt
   python app/main.py
   ```

## Deployment

### AWS (via Zappa)
```bash
pip install zappa
zappa init
zappa deploy
```

### GCP (via Cloud Run)
```bash
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/auto-scheduler
gcloud run deploy --image gcr.io/YOUR_PROJECT_ID/auto-scheduler --platform managed
```

## License

MIT License
