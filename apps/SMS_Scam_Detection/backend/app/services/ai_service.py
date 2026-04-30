import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

HF_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
HF_MODEL = os.getenv("HF_MODEL", "meta-llama/Llama-3.1-8B-Instruct")


def analyze_sms_with_ai(message: str, sender_known: str):
    if not HF_API_KEY:
        return {
            "decision": "Error",
            "confidence": "Low",
            "key_evidence": ["Hugging Face API key is missing."],
            "recommended_actions": ["Check backend/.env file."],
            "disclaimer": "This is not professional or legal advice."
        }

    prompt = f"""
You are a cybersecurity assistant analysing SMS messages.

Your task is to classify the message as:
- Likely Scam
- Likely Legitimate
- Uncertain

Use these indicators:
- urgency or pressure language
- suspicious links
- request for money, OTP, or personal information
- impersonation of trusted organisations (bank, ATO, delivery services)

SMS Message:
"{message}"

Sender Known:
"{sender_known}"

Respond STRICTLY in this format:

Decision:
Confidence: (Low/Medium/High)
Reason:
"""

    try:
        client = InferenceClient(api_key=HF_API_KEY)

        completion = client.chat.completions.create(
            model=HF_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=200,
            temperature=0.2
        )

        ai_output = completion.choices[0].message.content

        def parse_ai_output(text: str):
            try:
                lines = text.split("\n")

                decision = ""
                confidence = ""
                reason = ""

                for line in lines:
                    if "Decision:" in line:
                        decision = line.replace("Decision:", "").strip()
                    elif "Confidence:" in line:
                        confidence = line.replace("Confidence:", "").strip()
                    elif "Reason:" in line:
                        reason = line.replace("Reason:", "").strip()

                return decision, confidence, reason

            except:
                return "Uncertain", "Low", "Could not parse AI response"
        
        decision, confidence, reason = parse_ai_output(ai_output)


        return {
        "decision": decision,
        "confidence": confidence,
        "key_evidence": [reason],
        "recommended_actions": [
            "Do not click suspicious links",
            "Verify sender before taking action"
        ],
        "disclaimer": "This is not professional or legal advice."
    }

    except Exception as error:
        return {
            "decision": "Error",
            "confidence": "Low",
            "key_evidence": [str(error)],
            "recommended_actions": ["Check token, model availability, or internet."],
            "disclaimer": "This is not professional or legal advice."
        }