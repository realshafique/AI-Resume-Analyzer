import json
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types


# Load environment variables from .env
load_dotenv()


# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set")


# Create Gemini client
client = genai.Client(
    api_key=api_key
)


def generate_json(prompt: str) -> dict:
    """
    Send a prompt to Gemini and return the response as Python dictionary.
    """

    try:

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json"
            )
        )

        # Check if Gemini returned anything
        if not response.text:
            raise ValueError(
                "Gemini returned an empty response"
            )

        # Convert JSON string → Python dictionary
        return json.loads(response.text)

    except json.JSONDecodeError as e:

        raise ValueError(
            f"Gemini returned invalid JSON: {str(e)}"
        )

    except Exception as e:

        raise RuntimeError(
            f"Gemini API error: {str(e)}"
        )


def analyze_resume(resume_text: str) -> dict:
    """
    Analyze a resume using Gemini.
    """

    prompt = f"""
You are an expert technical recruiter.

Analyze the following resume.

Return ONLY valid JSON.

Use exactly this structure:

{{
    "candidate_name": "",
    "resume_score": 0,
    "skills": [],
    "experience_summary": "",
    "education": [],
    "strengths": [],
    "weaknesses": [],
    "missing_skills": [],
    "suggestions": []
}}

Rules:

1. resume_score must be between 0 and 100.
2. Never invent information.
3. Only use information present in the resume.
4. If information is unavailable, use an empty string or empty list.
5. Keep suggestions practical.
6. skills should contain technical and relevant professional skills.
7. weaknesses should identify genuine weaknesses in the resume.
8. missing_skills should contain skills that would normally strengthen the candidate's profile.
9. Return JSON only.
10. Do not use Markdown.

RESUME:

{resume_text}
"""

    return generate_json(prompt)


def match_resume_to_job(
    resume_text: str,
    job_description: str
) -> dict:
    """
    Compare a resume against a job description.
    """

    prompt = f"""
You are an expert technical recruiter.

Compare the resume against the job description.

Return ONLY valid JSON.

Use exactly this structure:

{{
    "match_score": 0,
    "matched_skills": [],
    "missing_skills": [],
    "experience_match": "",
    "education_match": "",
    "strengths_for_role": [],
    "recommendations": []
}}

Rules:

1. match_score must be between 0 and 100.
2. Never invent candidate experience.
3. Only mark a skill as matched if the resume clearly supports it.
4. missing_skills should contain important job requirements that are not supported by the resume.
5. Compare the candidate's actual experience with the job requirements.
6. Compare education only using information present in the resume.
7. Keep recommendations practical.
8. Return JSON only.
9. Do not use Markdown.

RESUME:

{resume_text}


JOB DESCRIPTION:

{job_description}
"""

    return generate_json(prompt)