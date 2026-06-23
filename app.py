import os
import tempfile
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from pdf2image import convert_from_path
import pytesseract
import pdfplumber
load_dotenv(".env.txt")

api_key = st.secrets.get("GOOGLE_API_KEY", os.getenv("GOOGLE_API_KEY"))

genai.configure(api_key=api_key)


if not api_key:
    st.error("Google API Key not found. Please add it to your .env file.")
    st.stop()

genai.configure(api_key=api_key)


# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""

    try:
        # Direct text extraction
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        if text.strip():
            return text.strip()

    except Exception as e:
        print(f"Direct text extraction failed: {e}")

    # OCR fallback
    try:
        images = convert_from_path(pdf_path)

        for image in images:
            page_text = pytesseract.image_to_string(image)
            text += page_text + "\n"

    except Exception as e:
        print(f"OCR failed: {e}")

    return text.strip()


# Function to analyze resume using Gemini
def analyze_resume(resume_text, job_description=None):

    if not resume_text:
        return "No resume text found."

    prompt = f"""
You are an experienced HR professional and technical recruiter.

Analyze the following resume and provide:

1. Overall Profile Evaluation
2. Suitable Job Roles
3. Existing Technical Skills
4. Missing Skills / Skill Gaps
5. Resume Strengths
6. Resume Weaknesses
7. Recommended Courses or Certifications
8. Suggestions to Improve ATS Score
9. Final Verdict

Resume:
{resume_text}
"""

    if job_description and job_description.strip():
        prompt += f"""

Additionally compare the resume against the following Job Description.

Job Description:
{job_description}

Provide:
1. Match Percentage
2. Matching Skills
3. Missing Skills
4. ATS Compatibility
5. Recommendations to improve fit for this role.
"""

    try:
        model = genai.GenerativeModel("gemini-2.5-flash")

        response = model.generate_content(prompt)

        if hasattr(response, "text") and response.text:
            return response.text.strip()

        return "No response generated."

    except Exception as e:
        return f"Analysis failed: {str(e)}"


# Streamlit UI
st.set_page_config(
    page_title="AI Resume Analyzer",
    layout="wide"
)

st.title("AI Resume Analyzer")
st.write(
    "Analyze your resume and compare it with job descriptions using Google Gemini AI."
)

col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"]
    )

with col2:
    job_description = st.text_area(
        "Enter Job Description",
        placeholder="Paste the job description here..."
    )

if uploaded_file:
    st.success("Resume uploaded successfully!")
else:
    st.warning("Please upload a PDF resume.")

st.markdown("<br>", unsafe_allow_html=True)

if uploaded_file:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.getbuffer())
        pdf_path = tmp_file.name

    resume_text = extract_text_from_pdf(pdf_path)

    if not resume_text:
        st.error("Unable to extract text from the uploaded resume.")
    else:
        if st.button("Analyze Resume"):

            with st.spinner("Analyzing Resume..."):

                analysis = analyze_resume(
                    resume_text,
                    job_description
                )

                st.success("Analysis Complete!")

                st.markdown("## Analysis Report")
                st.write(analysis)

    # Cleanup temporary file
    try:
        os.remove(pdf_path)
    except:
        pass


# Footer
st.markdown("---")

st.markdown(
    """
    <p style='text-align:center;'>
        Powered by <b>Streamlit</b> and <b>Google Gemini AI</b><br>
        Developed by <b>Athinti Navyasri</b>
    </p>
    """,
    unsafe_allow_html=True
)
