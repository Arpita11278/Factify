import streamlit as st
from analyzer import FactifyAnalyzer

# --- APP CONFIGURATION ---
st.set_page_config(
    page_title="Factify | Intelligence & Verification Desk",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CLEAN & ORIGINAL STYLING ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

    html, body, [class*="st-emotion-cache"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    .stApp {
        background-color: #0c0f1d;
        color: #f1f5f9;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #121829;
        border-right: 1px solid #1e293b;
    }

    /* Headers */
    h1, h2, h3 {
        color: #f8fafc;
        font-weight: 700;
    }

    /* Input Box */
    .stTextArea textarea {
        background-color: #121829 !important;
        color: #e2e8f0 !important;
        border: 1px solid #334155 !important;
        border-radius: 12px !important;
        padding: 16px !important;
        font-size: 1rem;
    }
    .stTextArea textarea:focus {
        border: 1px solid #06b6d4 !important;
        box-shadow: 0 0 0 2px rgba(6, 182, 212, 0.2) !important;
    }

    /* Custom Action Button */
    .stButton > button {
        background: linear-gradient(135deg, #06b6d4 0%, #3b82f6 100%);
        color: #ffffff;
        border: none;
        border-radius: 10px;
        padding: 12px 32px;
        font-weight: 600;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        opacity: 0.9;
        box-shadow: 0 4px 12px rgba(6, 182, 212, 0.3);
    }

    /* Metric Cards Styling */
    [data-testid="stMetricValue"] {
        color: #06b6d4 !important;
        font-size: 2.2rem !important;
        font-weight: 700 !important;
    }
    [data-testid="stMetricLabel"] {
        color: #94a3b8 !important;
        font-size: 0.9rem !important;
    }

    /* Containers */
    .stAlert {
        background-color: #121829;
        border: 1px solid #1e293b;
        color: #e2e8f0;
        border-radius: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown("""
    <div style="padding: 10px 0;">
        <h1 style="margin-bottom: 0px; font-size: 2.5rem;">🛡️ Factify</h1>
        <p style="color: #94a3b8; font-size: 1.05rem; margin-top: 5px;">Advanced AI-Driven Misinformation & Fake News Intelligence Portal</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<div style='margin-bottom: 10px;'></div>", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### 🧭 Control Center")
    st.write("Verify text snippets, news excerpts, or viral forwards securely using multi-engine AI protocols.")
    
    st.markdown("---")
    st.markdown("#### 💡 Quick Guidelines")
    st.markdown("- Look out for sensational headlines.")
    st.markdown("- Check for unverified source citations.")
    st.markdown("- Beware of artificial urgency calls.")
    
    st.markdown("---")
    if st.button("Clear Session"):
        st.rerun()
        
    st.markdown("<div style='position: fixed; bottom: 20px; color: #475569; font-size: 0.75rem;'>System Status: Secure & Active</div>", unsafe_allow_html=True)

# --- MAIN INPUT SECTION (CLEAN & FULL WIDTH) ---
st.markdown("### 📝 Input Verification Text")
user_text = st.text_area(
    label="Enter claim",
    placeholder="Paste WhatsApp forward, news snippet, or social media claim here to verify authenticity...",
    height=160,
    label_visibility="collapsed"
)

col_btn, col_space = st.columns([1, 4])
with col_btn:
    analyze_btn = st.button("Execute Verification")

# --- ANALYSIS RESULTS ---
if analyze_btn:
    if user_text.strip():
        with st.spinner("Running deep linguistic parsing and authenticity checks..."):
            analyzer = FactifyAnalyzer()
            result = analyzer.analyze(user_text)
        
        st.markdown("---")
        st.markdown(f"### 📊 Verification Intelligence Report &nbsp;|&nbsp; <span style='color: #06b6d4; font-size: 1.1rem;'>Detected Language: {result.get('detected_language')}</span>", unsafe_allow_html=True)
        st.write("")
        
        # Metrics Row
        m1, m2, m3 = st.columns(3)
        
        verdict = result.get('verdict')
        v_indicator = "#06b6d4"
        if verdict == "Needs Verification": v_indicator = "#f59e0b"
        if verdict == "Likely Misleading": v_indicator = "#ef4444"

        with m1:
            st.metric(label="Final Verdict", value=verdict)
            st.markdown(f"<div style='height:4px; background-color:{v_indicator}; width:100%; border-radius:2px; margin-top:-10px;'></div>", unsafe_allow_html=True)
        with m2:
            st.metric(label="Risk Assessment", value=result.get('risk_level'))
        with m3:
            conf = result.get('confidence', 0)
            st.metric(label="Confidence Level", value=f"{conf}%")
            st.progress(conf / 100)
        
        st.write("")
        
        # Core Summary Container
        st.markdown("#### 📌 Claim Summary")
        st.info(result.get('claim_summary'))
        
        st.markdown("#### 🔍 Deep Analysis & Reasoning")
        st.write(result.get('explanation'))
        
        # Findings & Warning Grid
        findings = result.get('key_findings', [])
        warnings = result.get('warning_signs', [])
        
        col_f, col_w = st.columns(2)
        with col_f:
            st.markdown("#### 💡 Key Observations")
            for f in findings:
                st.markdown(f"• {f}")
        with col_w:
            st.markdown("#### ⚠️ Identified Warning Signs")
            for w in warnings:
                st.markdown(f"<span style='color:#ef4444;'>• {w}</span>", unsafe_allow_html=True)
                
        st.write("")
        st.markdown("#### ✅ Recommended Action")
        st.success(result.get('recommended_action'))
        
        st.caption(f"Engine Protocol: {result.get('engine')}")
        
    else:
        st.warning("⚠️ Please provide text content inside the input box to initiate verification.")