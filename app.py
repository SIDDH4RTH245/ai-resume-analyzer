import streamlit as st
from pypdf import PdfReader
import re

st.set_page_config(
    page_title="AI Resume Analyzer",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")

skills = [
    # Programming Languages
    "python",
    "java",
    "c++",
    "javascript",
    "typescript",
    "sql",
    "r",
    "go",

    # Data Science & Analytics
    "data analysis",
    "data visualization",
    "data cleaning",
    "exploratory data analysis",
    "statistical analysis",
    "business intelligence",
    "power bi",
    "tableau",
    "excel",
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",

    # Machine Learning
    "machine learning",
    "deep learning",
    "supervised learning",
    "unsupervised learning",
    "reinforcement learning",
    "feature engineering",
    "model deployment",
    "scikit-learn",
    "xgboost",
    "lightgbm",

    # AI & NLP
    "natural language processing",
    "nlp",
    "transformers",
    "hugging face",
    "bert",
    "llms",
    "generative ai",
    "prompt engineering",
    "langchain",
    "openai api",
    "chatbot development",

    # Deep Learning Frameworks
    "tensorflow",
    "keras",
    "pytorch",

    # Computer Vision
    "computer vision",
    "opencv",
    "image processing",
    "object detection",

    # Backend & APIs
    "flask",
    "fastapi",
    "django",
    "rest api",
    "graphql",

    # Frontend & App Development
    "streamlit",
    "react",
    "html",
    "css",
    "bootstrap",

    # Databases
    "mysql",
    "postgresql",
    "mongodb",
    "sqlite",
    "firebase",

    # Cloud & DevOps
    "aws",
    "azure",
    "google cloud",
    "docker",
    "kubernetes",
    "jenkins",
    "ci/cd",

    # Tools & Platforms
    "git",
    "github",
    "linux",
    "jupyter notebook",
    "postman",

    # Big Data
    "apache spark",
    "hadoop",
    "kafka",

    # Soft Skills
    "problem solving",
    "communication",
    "teamwork",
    "leadership",
    "critical thinking",
    "project management",
    "time management",
    "adaptability",
]

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=250
)

def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + " "

    return text.lower()

def extract_skills(text):
    found = []

    for skill in skills:
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"
        if re.search(pattern, text):
            found.append(skill)

    return found

if st.button("Analyze Resume"):

    if uploaded_file is None:
        st.error("Please upload a resume PDF.")

    elif not job_description.strip():
        st.error("Please enter job description.")

    else:
        resume_text = extract_text_from_pdf(uploaded_file)

        resume_skills = extract_skills(resume_text)
        required_skills = extract_skills(job_description.lower())

        matched = list(set(resume_skills).intersection(required_skills))
        missing = list(set(required_skills) - set(resume_skills))

        if len(required_skills) > 0:
            score = round((len(matched) / len(required_skills)) * 100, 2)
        else:
            score = 0

        st.subheader("Analysis Result")

        st.metric("Match Score", f"{score}%")

        st.subheader("Skills Found")
        st.write(resume_skills)

        st.subheader("Matched Skills")
        st.success(", ".join(matched) if matched else "No matched skills")

        st.subheader("Missing Skills")
        st.error(", ".join(missing) if missing else "No missing skills")

        st.subheader("Suggestions")

        if missing:
            st.info(
                "Consider adding missing skills if you have experience with them."
            )
        else:
            st.success("Excellent resume-job match.")