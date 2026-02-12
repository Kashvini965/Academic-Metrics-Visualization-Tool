import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Student Development Dashboard",
                   page_icon="🎓",
                   layout="wide")

st.title("🎓 Academic Metrics Visualization Tool")

# -------------------------------
# SIDEBAR - STUDENT PROFILE
# -------------------------------
st.sidebar.header("Student Profile")

name = st.sidebar.text_input("Student Name", "John Doe")
age = st.sidebar.number_input("Age", 18, 30, 20)
course = st.sidebar.selectbox("Course", ["CSE", "ECE", "EEE", "IT", "MECH"])
year = st.sidebar.selectbox("Year", ["1st", "2nd", "3rd", "4th"])

st.sidebar.markdown("---")

# -------------------------------
# SAMPLE DATA (Can be replaced with real data)
# -------------------------------

subjects = ["Maths", "Physics", "Chemistry", "Programming", "English"]
marks = [78, 65, 70, 85, 90]

attendance = [85, 75, 80, 92, 88]

skills = ["Python", "Java", "Data Structures", "ML", "Communication"]
skill_levels = [70, 60, 65, 50, 80]

goals = {
    "Learn Python": "In Progress",
    "Build ML Project": "Not Started",
    "Improve Communication": "Completed",
    "Internship Preparation": "In Progress"
}

# -------------------------------
# MAIN DASHBOARD TABS
# -------------------------------

tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Academics",
    "📅 Attendance",
    "🛠 Skills",
    "🎯 Goals"
])

# -------------------------------
# TAB 1: ACADEMICS
# -------------------------------

with tab1:
    st.subheader("Subject-wise Marks")

    df_marks = pd.DataFrame({
        "Subject": subjects,
        "Marks": marks
    })

    st.dataframe(df_marks)

    fig, ax = plt.subplots()
    ax.bar(subjects, marks)
    ax.set_xlabel("Subjects")
    ax.set_ylabel("Marks")
    ax.set_title("Academic Performance")
    plt.xticks(rotation=30)
    st.pyplot(fig)

    avg_marks = np.mean(marks)
    st.metric("Average Marks", round(avg_marks, 2))

# -------------------------------
# TAB 2: ATTENDANCE
# -------------------------------

with tab2:
    st.subheader("Attendance Percentage")

    df_att = pd.DataFrame({
        "Subject": subjects,
        "Attendance %": attendance
    })

    st.dataframe(df_att)

    fig2, ax2 = plt.subplots()
    ax2.plot(subjects, attendance, marker='o')
    ax2.set_ylim(0, 100)
    ax2.set_xlabel("Subjects")
    ax2.set_ylabel("Attendance %")
    ax2.set_title("Attendance Overview")
    plt.xticks(rotation=30)
    st.pyplot(fig2)

    avg_att = np.mean(attendance)
    st.metric("Average Attendance", f"{avg_att:.2f}%")

# -------------------------------
# TAB 3: SKILLS
# -------------------------------

with tab3:
    st.subheader("Skill Levels")

    df_skills = pd.DataFrame({
        "Skill": skills,
        "Level (%)": skill_levels
    })

    st.dataframe(df_skills)

    fig3, ax3 = plt.subplots()
    ax3.barh(skills, skill_levels)
    ax3.set_xlabel("Proficiency Level")
    ax3.set_title("Skills Progress")
    st.pyplot(fig3)

# -------------------------------
# TAB 4: GOALS
# -------------------------------

with tab4:
    st.subheader("Personal Goals")

    for g, status in goals.items():
        if status == "Completed":
            st.success(f"{g} - {status}")
        elif status == "In Progress":
            st.warning(f"{g} - {status}")
        else:
            st.error(f"{g} - {status}")

    st.markdown("---")

    new_goal = st.text_input("Add New Goal")
    if st.button("Add Goal"):
        st.success(f"Goal '{new_goal}' added!")

# -------------------------------
# FOOTER SUMMARY
# -------------------------------

st.markdown("---")
st.subheader("Student Summary")

st.write(f"**Name:** {name}")
st.write(f"**Age:** {age}")
st.write(f"**Course:** {course}")
st.write(f"**Year:** {year}")
st.write(f"**Average Marks:** {round(avg_marks,2)}")
st.write(f"**Average Attendance:** {round(avg_att,2)}%")

st.success("Dashboard Loaded Successfully ✔️")
