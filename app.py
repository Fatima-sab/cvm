import streamlit as st

class CVBuilder:
    def __init__(self):
        self.name = ""
        self.email = ""
        self.address = ""
        self.education = {}
        self.work_experience = []
        self.skills = []
        self.languages = []

    def display_form(self):
        # Personal Details
        st.header("Personal Details")
        self.name = st.text_input("Full Name")
        self.email = st.text_input("Email Address")
        self.address = st.text_area("Address")

        # Education Details
        st.header("Educational Details")
        self.education["High School"] = {
            "Institution": st.text_input("High School Institution"),
            "Year": st.text_input("High School Completion Year"),
        }
        self.education["Secondary School"] = {
            "Institution": st.text_input("Secondary School Institution"),
            "Year": st.text_input("Secondary School Completion Year"),
        }
        self.education["Bachelors"] = {
            "Institution": st.text_input("Bachelors Institution"),
            "Year": st.text_input("Bachelors Completion Year"),
        }
        self.education["Masters"] = {
            "Institution": st.text_input("Masters Institution"),
            "Year": st.text_input("Masters Completion Year"),
        }

        # Work Experience
        st.header("Work Experience")
        num_experiences = st.number_input("Number of Work Experiences", min_value=1, step=1)
        for i in range(num_experiences):
            with st.expander(f"Work Experience {i + 1}"):
                company = st.text_input(f"Company Name {i + 1}")
                role = st.text_input(f"Role/Position {i + 1}")
                duration = st.text_input(f"Duration {i + 1} (e.g., Jan 2020 - Dec 2021)")
                self.work_experience.append({"Company": company, "Role": role, "Duration": duration})

        # Soft Skills
        st.header("Soft Skills")
        self.skills = st.text_area("Enter your skills, separated by commas").split(',')

        # Languages
        st.header("Languages")
        self.languages = st.text_area("Enter languages you know, separated by commas").split(',')

    def display_cv(self):
        st.title("Generated CV")
        st.write("### Personal Details")
        st.write(f"**Name**: {self.name}")
        st.write(f"**Email**: {self.email}")
        st.write(f"**Address**: {self.address}")

        st.write("### Education")
        for level, details in self.education.items():
            st.write(f"**{level}**: {details['Institution']} ({details['Year']})")

        st.write("### Work Experience")
        for exp in self.work_experience:
            st.write(f"**{exp['Role']}** at {exp['Company']} ({exp['Duration']})")

        st.write("### Soft Skills")
        for skill in self.skills:
            st.write(f"- {skill.strip()}")

        st.write("### Languages")
        for language in self.languages:
            st.write(f"- {language.strip()}")

# Main App
st.title("CV Builder App")

cv_builder = CVBuilder()
cv_builder.display_form()

if st.button("Generate CV"):
    cv_builder.display_cv()
