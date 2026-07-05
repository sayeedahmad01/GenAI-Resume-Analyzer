import streamlit as st
from pdf_reader import extract_text_from_pdf
from analyzer import analyze_resume

st.set_page_config(
    page_title="SAYEED AHMAD RESUME ANALYZER",
    page_icon="📄",
    layout="wide"
)

st.title("SAYEED AHMAD RESUME ANALYZER APP")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file is not None:

    with st.spinner("Reading resume..."):
        resume = extract_text_from_pdf(uploaded_file)

    st.success("Resume read successfully!")

    if st.button("Show Analysis Result"):

        with st.spinner("Analyzing resume..."):
            result = analyze_resume(resume)

        st.markdown("## Analysis Result")
        st.write(result)

        st.download_button(
            label="Download Analysis Result",
            data=result,
            file_name="analysis_result.txt",
            mime="text/plain"
        )