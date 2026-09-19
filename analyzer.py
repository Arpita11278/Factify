import os
import json
import requests

# OpenRouter Default Model (Aap apne hisaab se change bhi kar sakti hain)
DEFAULT_MODEL = "google/gemini-2.5-flash"

class FactifyAnalyzer:
    def __init__(self, api_key: str = None):
        # Yahan aap apni OpenRouter API key daal sakti hain ya .env se le sakte hain
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY", "your_openRouter_api_key_here")

    def analyze(self, text: str, model_name: str = DEFAULT_MODEL) -> dict:
        if self.api_key and self.api_key != "your_openRouter_api_key_here":
            try:
                url = "https://openrouter.ai/api/v1/chat/completions"
                headers = {
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                    "HTTP-Referer": "https://github.com/Arpita11278/Factify", # Optional, for OpenRouter rankings
                    "X-Title": "Factify AI" # Optional
                }
                
                prompt = f"""
                You are an expert fact-checker and misinformation analyst specializing in regional social media and WhatsApp forwards (English, Hindi, Hinglish).
                Analyze the following text for fake news, rumors, manipulation tactics, or misinformation.

                Text to analyze:
                \"\"\"{text}\"\"\"

                Return a valid JSON object ONLY, with the following exact keys:
                - "verdict": Must be one of ["Likely True", "Needs Verification", "Likely Misleading"]
                - "risk_level": Must be one of ["Low", "Medium", "High"]
                - "confidence": Integer percentage between 0 and 100
                - "credibility_score": Integer score between 0 and 100 (100 being completely credible)
                - "detected_language": Language of the text (e.g. "English", "Hindi", "Hinglish")
                - "claim_summary": A concise one-sentence summary of the core claim
                - "warning_signs": List of strings describing warning signs found (e.g., ["Artificial Urgency", "Forward-Baiting"]) or ["None explicitly detected"]
                - "explanation": Detailed reasoning behind the assessment (2-3 sentences)
                - "key_findings": List of 2 to 3 bullet points detailing specific observations
                - "recommended_action": Actionable advice for the user before they share
                """

                payload = {
                    "model": model_name,
                    "messages": [{"role": "user", "content": prompt}],
                    "response_format": {"type": "json_object"}
                }

                response = requests.post(url, headers=headers, json=payload)
                if response.status_code == 200:
                    res_data = response.json()
                    content = res_data["choices"][0]["message"]["content"]
                    data = json.loads(content.strip())
                    data["engine"] = f"OpenRouter ({model_name})"
                    return data
            except Exception as e:
                pass

        # Fallback Heuristic Engine (Agar API key na ho ya error aaye)
        return self._heuristic_analysis(text)

    def _heuristic_analysis(self, text: str) -> dict:
        text_lower = text.lower()
        urgency_words = ["urgent", "sabko forward", "share karo", "turant", "breaking", "warning", "note band", "jaldi"]
        has_urgency = any(word in text_lower for word in urgency_words)

        if has_urgency or "₹2000" in text_lower or "free" in text_lower or "lottery" in text_lower:
            return {
                "verdict": "Likely Misleading",
                "risk_level": "High",
                "confidence": 88,
                "credibility_score": 25,
                "detected_language": "Hinglish / Regional",
                "claim_summary": "Sensational forward containing urgent calls to action or unverified benefits.",
                "warning_signs": ["Artificial Urgency", "Forward-Baiting", "Unverified Offer"],
                "explanation": "The text triggers panic or excitement using urgent phrasing and lacks official attribution or verifiable institutional references.",
                "key_findings": [
                    "Contains strong emotional trigger words.",
                    "Prompts mass forwarding without a concrete official source."
                ],
                "recommended_action": "Do not forward this message. Cross-check official portals or news outlets.",
                "engine": "Factify Heuristic Engine (Offline Mode)"
            }
        else:
            return {
                "verdict": "Needs Verification",
                "risk_level": "Medium",
                "confidence": 65,
                "credibility_score": 60,
                "detected_language": "English / General",
                "claim_summary": "General statement or news snippet requiring standard baseline verification.",
                "warning_signs": ["None explicitly detected"],
                "explanation": "No aggressive deceptive patterns or extreme urgency markers were found, but independent source verification is advised.",
                "key_findings": [
                    "Tone appears relatively balanced.",
                    "Lacks explicit external verification links."
                ],
                "recommended_action": "Verify core facts via reputable news organizations before publishing or sharing widely.",
                "engine": "Factify Heuristic Engine (Offline Mode)"
            }