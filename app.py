from io import BytesIO
import streamlit as st

from resume_lens.parser import extract_pdf_text
from resume_lens.scoring import compare_texts, build_report
from resume_lens.skills import find_skills

st.set_page_config(page_title="ResumeLens AI", page_icon="🔎", layout="wide")

st.title("🔎 ResumeLens AI")
st.caption("A practical resume-to-job-description checker with explainable, keyword-based feedback.")
st.info("This is an educational heuristic, not an official ATS score or a guarantee of interview selection.")

with st.sidebar:
    st.header("How it works")
    st.markdown("1. Upload a text-based PDF resume.\n2. Paste a job description.\n3. Review overlap, skill gaps, and suggestions.")
    st.caption("Your resume is processed in this app session and is not intentionally saved by this project.")

uploaded = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste the job description", height=220, placeholder="Include responsibilities, required skills, and qualifications…")

if st.button("Analyze resume", type="primary", use_container_width=True):
    if uploaded is None:
        st.error("Please upload a PDF resume first.")
    elif not job_description.strip():
        st.error("Please paste the job description first.")
    else:
        try:
            resume_text = extract_pdf_text(BytesIO(uploaded.getvalue()))
            if len(resume_text.strip()) < 40:
                st.error("Very little text was extracted. Try a text-based PDF rather than a scanned image PDF.")
            else:
                result = compare_texts(resume_text, job_description)
                resume_skills = find_skills(resume_text)
                job_skills = find_skills(job_description)
                matched = sorted(resume_skills & job_skills)
                missing = sorted(job_skills - resume_skills)
                report = build_report(result, matched, missing)

                left, right = st.columns(2)
                left.metric("Text similarity", f"{result['similarity']:.0%}")
                right.metric("Shared skills", f"{len(matched)} / {len(job_skills)}" if job_skills else "No known skills detected")

                st.progress(result["similarity"])
                st.subheader("Skills already reflected")
                st.write(", ".join(matched) if matched else "No direct matches from the built-in skill dictionary were detected.")
                st.subheader("Potential skill gaps")
                st.write(", ".join(missing) if missing else "No missing skills from the built-in dictionary were detected.")
                st.subheader("Suggestions")
                suggestions = []
                if missing:
                    suggestions.append("If you genuinely have these skills, add relevant evidence in your skills or project sections: " + ", ".join(missing[:12]) + ".")
                if result["resume_words"] < 250:
                    suggestions.append("Your resume text looks brief. Consider adding measurable project outcomes and relevant experience where accurate.")
                if not suggestions:
                    suggestions.append("Tailor the summary and project bullets to the role, using specific evidence rather than keyword stuffing.")
                for item in suggestions:
                    st.markdown(f"- {item}")

                st.subheader("Text checks")
                c1, c2, c3 = st.columns(3)
                c1.metric("Resume words", result["resume_words"])
                c2.metric("Job description words", result["job_words"])
                c3.metric("Shared terms", result["shared_terms"])
                st.download_button("Download analysis report", data=report, file_name="resume_lens_report.txt", mime="text/plain")
        except Exception as exc:
            st.error(f"Could not analyze this PDF: {exc}")

st.divider()
st.caption("Tip: Use the feedback as a checklist. Never add a skill, qualification, or achievement you cannot substantiate.")
