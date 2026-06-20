import streamlit as st
import sys
import os

# Fix import path
project_root = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(project_root)

try:
    from main import run_cybershield
except Exception as e:
    st.error(f"Import Error: {e}")
    st.stop()

# Page Configuration
st.set_page_config(
    page_title="CyberShield AI Agent",
    page_icon="🛡️",
    layout="wide"
)

# Header
st.title("🛡️ CyberShield AI Agent")
st.markdown(
    """
    AI-Powered Security Operations Center (SOC) Assistant

    Upload a security log file and CyberShield will:
    - Detect Threats
    - Assess Vulnerabilities
    - Generate Recommendations
    - Create Security Reports
    """
)

st.divider()

# File Upload
uploaded_file = st.file_uploader(
    "Upload Security Log File",
    type=["txt", "log"]
)

# Sample Logs Option
st.subheader("Or Use Sample Logs")

use_sample = st.button("Analyze Sample Logs")

log_content = None

# Uploaded File
if uploaded_file is not None:
    try:
        log_content = uploaded_file.read().decode("utf-8")
    except Exception as e:
        st.error(f"File Read Error: {e}")

# Sample Logs
if use_sample:
    try:
        sample_path = os.path.join(
            project_root,
            "data",
            "sample_logs.txt"
        )

        with open(sample_path, "r", encoding="utf-8") as f:
            log_content = f.read()

    except Exception as e:
        st.error(f"Sample Log Error: {e}")

# Run Analysis
if log_content:

    st.success("Logs Loaded Successfully")

    with st.expander("View Logs"):
        st.text(log_content)

    if st.button("Run CyberShield Analysis"):

        try:

            with st.spinner("Analyzing Threats..."):

                results = run_cybershield(log_content)

            st.success("Analysis Completed")

            # Threats
            st.subheader("🚨 Threat Detection")
            st.write(results["threats"])

            # Vulnerabilities
            st.subheader("🔍 Vulnerability Assessment")
            st.write(results["vulnerabilities"])

            # Recommendations
            st.subheader("✅ Security Recommendations")
            st.write(results["recommendations"])

            # PDF Download
            if os.path.exists(results["pdf"]):

                with open(results["pdf"], "rb") as pdf_file:

                    st.download_button(
                        label="📄 Download Security Report",
                        data=pdf_file,
                        file_name="CyberShield_Report.pdf",
                        mime="application/pdf"
                    )

        except Exception as e:

            st.error("CyberShield Analysis Failed")
            st.exception(e)

# Footer
st.divider()

st.caption(
    "CyberShield AI Agent | Kaggle AI Agents Capstone Project"
)