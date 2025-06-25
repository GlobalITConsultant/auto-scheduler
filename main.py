from flask import Flask, request, Response, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

HOUSECALL_API_KEY = os.getenv("HOUSECALL_API_KEY")
HEADERS = {
    "Authorization": f"Bearer {HOUSECALL_API_KEY}",
    "Content-Type": "application/json"
}

@app.route("/", methods=["GET"])
def home():
    return "Auto Scheduler is running."

@app.route("/webhook", methods=["POST"])
def process_call():
    speech_text = request.form.get('SpeechResult', '').lower()
    print(f"Received speech input: {speech_text}")

    if "appointment" in speech_text:
        email = "caller@example.com"
        service = "HVAC Diagnostic"
        datetime_str = "2025-06-25T10:00:00-04:00"
        response_msg = schedule_housecall_appointment(email, service, datetime_str)
    else:
        response_msg = "Sorry, I couldn't understand your request. Please try again."

    return Response(f"<Response><Say>{response_msg}</Say></Response>", mimetype='text/xml')

def schedule_housecall_appointment(email, service, datetime_str):
    customer = {
        "first_name": "Caller",
        "last_name": "Auto",
        "email": email,
        "phone": "+15551234567"
    }
    cust_res = requests.post("https://api.housecallpro.com/v1/customers", json=customer, headers=HEADERS)
    if cust_res.status_code not in [200, 201]:
        return "Failed to create customer."

    cust_id = cust_res.json().get("id")
    job = {
        "customer_id": cust_id,
        "scheduled_start": datetime_str,
        "scheduled_end": datetime_str,
        "line_items": [{"name": service, "quantity": 1, "unit_cost": 89.99}]
    }
    job_res = requests.post("https://api.housecallpro.com/v1/jobs", json=job, headers=HEADERS)
    if job_res.status_code in [200, 201]:
        return "Your appointment has been scheduled. Thank you!"
    else:
        return "Failed to schedule the appointment."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
