# 🛡️ Factify: Advanced AI-Driven Misinformation & Fake News Intelligence Portal

> **"Verify before you share."** A real-time cyber-intelligence desk designed to instantly detect fake news, malicious scams, and deceptive social media forwards using advanced LLM reasoning.

---

## 🚀 Overview
In an era where digital misinformation and hyper-personalized scams propagate instantly across messaging and social platforms, **Factify** serves as an automated frontline defense. Built with a sleek, professional cyber-security aesthetic, Factify ingests unstructured text or viral forwards, evaluates risk levels, flags manipulation patterns (such as artificial urgency and forward-baiting), and delivers structured forensic verdicts instantly.

---

## ✨ Key Features
* **Live AI Intelligence Engine:** Powered via secure OpenRouter API integration (`nex-agi/nex-n2.5-mini:free`), ensuring high-speed semantic verification.
* **Granular Risk Diagnostics:** Computes explicit risk levels (`Low`, `Medium`, `High`), confidence percentages, credibility scores, and detected language indicators.
* **Forensic Warning Signs:** Automatically isolates deceptive tactics such as artificial urgency, forward-baiting, and unverified reward promises.
* **Resilient Fallback Architecture:** Features an intelligent heuristic fallback protocol to guarantee 100% uptime even during network disruptions.
* **Cyber-Security UI:** Custom dark-themed layout crafted via Streamlit for seamless investigative workflows.

---

## 🛠️ Tech Stack
* **Frontend / UI:** Streamlit (Custom cyber-desk layout)
* **Backend & Core Logic:** Python, OpenAI SDK / Requests wrapper
* **AI Provider:** OpenRouter API (`nex-agi/nex-n2.5-mini:free`)
* **Security & Config:** Local environment variable isolation via `.env`

---

## ☁️ Cloud & AWS Architecture
Factify has been engineered with a **cloud-native mindset** designed for scalable deployment:
* **Compute & Hosting (Amazon EC2):** Optimized for running on AWS EC2 Ubuntu server instances inside virtualized environments for high availability.
* **Security & Secrets Management:** Built with strict environment variable boundaries aligned with AWS IAM and parameter store best practices.
* **Robust Networking:** Configured for secure inbound traffic management over custom TCP security group ports (Port 8501) to support enterprise verification workloads.

---

## ⚙️ Installation & Local Setup

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/your-username/Factify.git](https://github.com/your-username/Factify.git)
   cd Factify
