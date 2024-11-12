pip install streamlit reportlab
import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from io import BytesIO

def generate_european_cv(data):
    # Create a BytesIO buffer to store the PDF
    buffer = BytesIO()
    pdf = SimpleDocTemplate(buffer, pagesize=A4)

    # Define styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(name="Title", fontSize=14, leading=16, spaceAfter=12, bold=True)
    header_style = ParagraphStyle(name="Header", fontSize=12, spaceAfter=8, bold=True)
    normal_style = ParagraphStyle(name="Normal", fontSize=10, spaceAfter=4)

    elements = []

    # Title
    elements.append(Paragraph("Curriculum Vitae", title_style))
    elements.append(Spacer(1, 12))

    # Personal Information Section
    elements.append(Paragraph("Personal Information", header_style))
    personal_info_data = [
        ["Name:", data.get("name", "")],
        ["Address:", data.get("address", "")],
        ["Phone:", data.get("phone", "")],
        ["Email:", data.get("email", "")],
        ["Nationality:", data.get("nationality", "")],
        ["Date of Birth:", data.get("dob", "")]
    ]
    table = Table(personal_info_data, colWidths=[4*cm, 12*cm])
    table.setStyle(TableStyle([("BACKGROUND", (0, 0), (1, 0), colors.lightgrey),
                               ("GRID", (0, 0), (-1, -1), 0.25, colors.black)]))
    elements.append(table)
    elements.append(Spacer(1, 12))

    # Work Experience Section
    elements.append(Paragraph("Work Experience", header_style))
    work_experience = data.get("work_experience", [])
    for job in work_experience:
        elements.append(Paragraph(f"{job.get('position', '')} at {job.get('company', '')}", normal_style))
        elements.append(Paragraph(f"{job.get('start_date', '')} - {job.get('end_date', '')}", normal_style))
        elements.append(Paragraph(job.get("description", ""), normal_style))
        elements.append(Spacer(1, 8))

    # Education Section
    elements.append(Paragraph("Education", header_style))
    education = data.get("education", [])
    for edu in education:
        elements.append(Paragraph(f"{edu.get('degree', '')}, {edu.get('institution', '')}", normal_style))
        elements.append(Paragraph(f"{edu.get('start_date', '')} - {edu.get('end_date', '')}", normal_style))
        elements.append(Paragraph(edu.get("description", ""), normal_style))
        elements.append(Spacer(1, 8))

    # Skills Section
    elements.append(Paragraph("Skills", header_style))
    skills = data.get("skills", [])
    for skill in skills:
        elements.append(Paragraph(f"- {skill}", normal_style))
    elements.append(Spacer(1, 12))

    # Languages Section
    elements.append(Paragraph("Languages", header_style))
    languages = data.get("languages", [])
    for lang in languages:
        elements.append(Paragraph(f"{lang.get('language', '')}: {lang.get('proficiency', '')}", normal_style))
    elements.append(Spacer(1, 12))

    # Additional Information Section
    elements.append(Paragraph("Additional Information", header_style))
    additional_info = data.get("additional_info", "")
    elements.append(Paragraph(additional_info, normal_style))

    # Build the PDF
    pdf.build(elements)

    # Move to the start of the BytesIO buffer
    buffer.seek(0)
    return buffer

# Streamlit UI
st.title("European CV Generator")

# Collecting user data with Streamlit's form
with st.form("cv_form"):
   
