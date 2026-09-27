import requests
import streamlit as st
from document_utils import format_docx, format_pdf

st.set_page_config(page_title="LegalEase", page_icon="⚖️", layout="wide")
st.title("⚖️ LegalEase")
st.caption("AI-Powered Legal Document Generator")

API_URL = st.sidebar.text_input("Backend URL", "http://127.0.0.1:8000")

document_type = st.text_input("Document Type", "Freelance Work Contract")
parties = st.text_area("Parties Involved", "Jane Doe (Service Provider), TechNova Inc. (Client)")
terms = st.text_area(
    "Terms & Conditions",
    "Payment to be made within 30 days of invoice; Provider agrees to deliver work by the agreed deadline; Confidentiality must be maintained at all times"
)
dates = st.text_input("Effective Date", "September 25, 2026")

if "document" not in st.session_state:
    st.session_state.document = ""

if st.button("Generate Document", type="primary"):
    try:
        response = requests.post(
            f"{API_URL}/generate",
            json={"document_type": document_type, "parties": parties, "terms": terms, "dates": dates},
            timeout=120
        )
        response.raise_for_status()
        st.session_state.document = response.json()["document"]
    except Exception as exc:
        st.error(f"Generation failed: {exc}")

if st.session_state.document:
    st.subheader("Document Preview")
    st.session_state.document = st.text_area(
        "Click to edit", st.session_state.document, height=500
    )

    st.download_button(
        "Download TXT", st.session_state.document.encode("utf-8"),
        "legalease_document.txt", "text/plain"
    )

    docx = format_docx(st.session_state.document, document_type)
    st.download_button(
        "Download DOCX", docx.getvalue(), "legalease_document.docx",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

    pdf = format_pdf(st.session_state.document, document_type)
    st.download_button(
        "Download PDF", pdf.getvalue(), "legalease_document.pdf", "application/pdf"
    )

st.info("AI-generated drafts should be reviewed by a qualified legal professional before legal use.")
