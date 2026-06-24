import streamlit as st

st.set_page_config(
    page_title="Sulman Tariq | Portfolio",
    page_icon="💻",
    layout="wide",
)

# ---------- THEME / CSS ----------
st.markdown("""
<style>
:root {
    --accent: #38bdf8;
}
body, .stApp {
    background-color: #0f172a;
    color: #f8fafc;
}
h1, h2, h3 {
    color: #f8fafc !important;
}
.muted {
    color: #94a3b8;
}
.card {
    background-color: #1e293b;
    border: 1px solid #334155;
    border-radius: 8px;
    padding: 1.2rem 1.5rem;
    margin-bottom: 1rem;
}
.badge {
    display: inline-block;
    background-color: #334155;
    color: #f8fafc;
    font-size: 0.8rem;
    padding: 0.15rem 0.6rem;
    border-radius: 4px;
    margin-right: 0.4rem;
}
.skill-pill {
    display: inline-block;
    background-color: #1e293b;
    border: 1px solid #334155;
    padding: 0.4rem 0.8rem;
    border-radius: 6px;
    font-size: 0.9rem;
    margin: 0.2rem;
}
a {
    color: var(--accent);
}
.accent {
    color: var(--accent);
}
</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown("## Hi, I'm <span class='accent'>Sulman Tariq</span>", unsafe_allow_html=True)
st.markdown("<p class='muted'>Lahore, Punjab 54000</p>", unsafe_allow_html=True)
st.write(
    "Motivated Computer Science undergraduate at COMSATS University Lahore with "
    "hands-on programming experience in C++ and Java, and a foundation in database "
    "management (MySQL). Combines technical coursework with practical customer "
    "service and cash-handling experience, demonstrating strong communication "
    "skills and reliability in fast-paced environments."
)

col1, col2, col3 = st.columns(3)
with col1:
    st.link_button("📧 Get in Touch", "mailto:salmangujjar100303@gmail.com")
with col2:
    st.link_button("🔗 View GitHub", "https://github.com/M-Sulman-Tariq")
with col3:
    try:
        with open("resume.pdf", "rb") as f:
            st.download_button(
                label="📄 Download Resume (PDF)",
                data=f,
                file_name="Sulman_Tariq_Resume.pdf",
                mime="application/pdf",
            )
    except FileNotFoundError:
        st.warning("resume.pdf not found in this folder.")

st.divider()

# ---------- NAV (sidebar) ----------
section = st.sidebar.radio(
    "Navigate",
    ["Education", "Projects", "Skills", "Certifications", "Contact"],
)

# ---------- EDUCATION ----------
if section == "Education":
    st.header("Education")

    education = [
        ("Computer Science (Undergraduate)", "Oct 2024 – Present", "COMSATS University Lahore"),
        ("Engineering (Intermediate)", "Aug 2022 – Aug 2024", "Govt. Graduate College Township-Lahore"),
        ("Biology (Matriculation)", "Aug 2020 – Aug 2022", "Ch. Rehmat Ali Memorial Trust-Lahore"),
    ]

    for title, date, institution in education:
        st.markdown(f"""
        <div class="card">
            <h3>{title}</h3>
            <p class="accent" style="margin:0;">{date}</p>
            <p class="muted" style="margin:0;"><i>{institution}</i></p>
        </div>
        """, unsafe_allow_html=True)

# ---------- PROJECTS ----------
elif section == "Projects":
    st.header("Academic Projects")

    projects = [
        ("Console based Classroom", "Programming Fundamentals",
         "Developed a terminal-driven system to manage student data, attendance logs, "
         "and marks calculation using robust procedural logic layouts.",
         ["C++", "Console"]),
        ("Govt Complaint System", "Object Oriented Programming",
         "Designed an application featuring ticket generation, user registration, and "
         "role management built around polymorphism, inheritance, and encapsulation abstractions.",
         ["Java", "OOP"]),
        ("Swift Delivery System", "Data Structures & Algorithms",
         "Implemented optimization logic for routing and package distribution tracking, "
         "leveraging efficient dynamic data structures to reduce processing overhead.",
         ["Java", "DSA"]),
        ("E Thana", "Database Management Systems",
         "Created a centralized police station management system to securely track, log, "
         "and query criminal records, complaints, and officer assignments.",
         ["MySQL", "DBMS"]),
        ("AI Career Guiding System", "Artificial Intelligence",
         "Created an intelligent decision routing system that evaluates student skill matrix "
         "benchmarks to dynamically suggest professional development paths.",
         ["Java", "AI Logic"]),
    ]

    cols = st.columns(2)
    for i, (title, tag, desc, tech) in enumerate(projects):
        with cols[i % 2]:
            badges = "".join(f"<span class='badge'>{t}</span>" for t in tech)
            st.markdown(f"""
            <div class="card">
                <h3 style="margin-bottom:0.1rem;">{title}</h3>
                <p class="accent" style="font-size:0.85rem; text-transform:uppercase; margin:0 0 0.6rem 0;">{tag}</p>
                <p class="muted">{desc}</p>
                {badges}
            </div>
            """, unsafe_allow_html=True)

# ---------- SKILLS ----------
elif section == "Skills":
    st.header("Skills & Competencies")

    st.subheader("Technical Skills")
    technical = ["C++", "Java", "MySQL", "Microsoft Office"]
    st.markdown("".join(f"<span class='skill-pill'>{s}</span>" for s in technical), unsafe_allow_html=True)

    st.subheader("Professional & Soft Skills")
    soft = ["Customer Service", "Communication Skills", "Cash Handling", "Cashiering"]
    st.markdown("".join(f"<span class='skill-pill'>{s}</span>" for s in soft), unsafe_allow_html=True)

    st.subheader("Languages")
    languages = ["Punjabi (Native)", "Urdu (Native)", "English (Intermediate)"]
    st.markdown("".join(f"<span class='skill-pill'>{s}</span>" for s in languages), unsafe_allow_html=True)

# ---------- CERTIFICATIONS ----------
elif section == "Certifications":
    st.header("Certifications")
    st.markdown("""
    <div class="card">
        <h3>Computer Networks</h3>
        <p class="accent" style="margin:0;">In Progress (Started Jun 2026)</p>
        <p class="muted" style="margin:0;"><i>Introduction and Basics of Networking Course by CISCO</i></p>
    </div>
    """, unsafe_allow_html=True)

# ---------- CONTACT ----------
elif section == "Contact":
    st.header("Let's Connect")
    st.write("I am currently seeking entry-level software development roles, internships, or networking opportunities.")
    st.markdown("**Email:** salmangujjar100303@gmail.com")
    st.markdown("**Phone:** +92 326 5328176")
    st.markdown("**GitHub:** [github.com/M-Sulman-Tariq](https://github.com/M-Sulman-Tariq)")
    st.link_button("📧 Send an Email", "mailto:salmangujjar100303@gmail.com")

st.divider()
st.markdown("<p class='muted' style='text-align:center;'>© 2026 Sulman Tariq. Built clean and optimized.</p>", unsafe_allow_html=True)