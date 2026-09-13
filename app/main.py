from fastapi import FastAPI, UploadFile, File, HTTPException, Form

from app.parser import extract_text_from_pdf
from app.analyzer import analyze_resume, match_resume_to_job


app = FastAPI(
    title="AI Resume Analyzer",
    description="AI-powered resume analysis and job matching API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "AI Resume Analyzer API is running!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/analyze")
async def analyze_resume_endpoint(
    file: UploadFile = File(...)
):
    try:

        # Check filename
        if not file.filename:
            raise HTTPException(
                status_code=400,
                detail="No file selected."
            )

        if not file.filename.lower().endswith(".pdf"):
            raise HTTPException(
                status_code=400,
                detail="Only PDF files are supported."
            )

        # Read uploaded file
        pdf_bytes = await file.read()

        print("Filename:", file.filename)
        print("Content type:", file.content_type)
        print("PDF size:", len(pdf_bytes), "bytes")

        # Check empty file
        if len(pdf_bytes) == 0:
            raise HTTPException(
                status_code=400,
                detail="Uploaded PDF is empty. Please select a valid PDF file."
            )

        # Extract text
        resume_text = extract_text_from_pdf(pdf_bytes)

        print("Extracted text:", len(resume_text), "characters")

        if not resume_text.strip():
            raise HTTPException(
                status_code=400,
                detail="PDF was uploaded, but no readable text was found."
            )

        # Gemini analysis
        analysis = analyze_resume(resume_text)

        return {
            "filename": file.filename,
            "analysis": analysis
        }

    except HTTPException:
        raise

    except Exception as e:

        print("\n========== ERROR ==========")
        print("Error type:", type(e).__name__)
        print("Error:", str(e))
        print("============================\n")

        raise HTTPException(
            status_code=500,
            detail=f"{type(e).__name__}: {str(e)}"
        )


@app.post("/match")
async def match_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    try:

       
        if not file.filename:
            raise HTTPException(
                status_code=400,
                detail="No file selected."
            )

        if not file.filename.lower().endswith(".pdf"):
            raise HTTPException(
                status_code=400,
                detail="Only PDF files are supported."
            )

       
        if not job_description.strip():
            raise HTTPException(
                status_code=400,
                detail="Job description cannot be empty."
            )

       
        pdf_bytes = await file.read()

        print("\n========== UPLOAD ==========")
        print("Filename:", file.filename)
        print("Content type:", file.content_type)
        print("PDF size:", len(pdf_bytes), "bytes")
        print("============================")

       
        if len(pdf_bytes) == 0:
            raise HTTPException(
                status_code=400,
                detail="Uploaded PDF is empty. Please select a valid PDF file."
            )

       
        resume_text = extract_text_from_pdf(pdf_bytes)

        print("Extracted text:", len(resume_text), "characters")

        if not resume_text.strip():
            raise HTTPException(
                status_code=400,
                detail="PDF was uploaded, but no readable text was found."
            )

      
        result = match_resume_to_job(
            resume_text,
            job_description
        )

        return {
            "filename": file.filename,
            "job_match": result
        }

    except HTTPException:
        raise

    except Exception as e:

        print("\n========== ERROR ==========")
        print("Error type:", type(e).__name__)
        print("Error:", str(e))
        print("============================\n")

        raise HTTPException(
            status_code=500,
            detail=f"{type(e).__name__}: {str(e)}"
        )