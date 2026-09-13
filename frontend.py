import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


st.title("📄 AI Resume Analyzer")

st.write(
    "Analyze your resume and compare it with a job description using Gemini."
)


resume = st.file_uploader(
    "Upload your resume",
    type=["pdf"]
)


job_description = st.text_area(
    "Paste the Job Description",
    height=250,
    placeholder="Paste the job description here..."
)


analyze_button = st.button(
    "🚀 Analyze Resume",
    type="primary"
)


if analyze_button:

    if resume is None:
        st.error("Please upload a PDF resume.")

    elif not job_description.strip():
        st.error("Please enter a job description.")

    else:

        with st.spinner("Analyzing your resume..."):

            files = {
                "file": (
                    resume.name,
                    resume.getvalue(),
                    "application/pdf"
                )
            }

            data = {
                "job_description": job_description
            }

            response = requests.post(
                f"{API_URL}/match",
                files=files,
                data=data
            )

        if response.status_code == 200:

            result = response.json()
            analysis = result["job_match"]

            st.success("Analysis complete!")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Job Match Score",
                    f"{analysis['match_score']}%"
                )

            with col2:
                st.metric(
                    "Resume",
                    resume.name
                )

            st.divider()

            st.subheader("✅ Matched Skills")

            for skill in analysis["matched_skills"]:
                st.write(f"✓ {skill}")

            st.subheader("❌ Missing Skills")

            for skill in analysis["missing_skills"]:
                st.write(f"• {skill}")

            st.subheader("💪 Strengths")

            for strength in analysis["strengths_for_role"]:
                st.write(f"• {strength}")

            st.subheader("💡 Recommendations")

            for recommendation in analysis["recommendations"]:
                st.write(f"• {recommendation}")

            st.subheader("Experience Match")

            st.write(
                analysis["experience_match"]
            )

            st.subheader("Education Match")

            st.write(
                analysis["education_match"]
            )

        else:

            st.error(
                f"API Error: {response.status_code}"
            )
# Footer
st.markdown(
    """
    <div style="
        text-align: center;
        color: #888888;
        padding: 30px 0 10px 0;
        font-size: 14px;
    ">
        Made with ❤️ by <b>shafique2606</b>
    </div>
    """,
    unsafe_allow_html=True
)