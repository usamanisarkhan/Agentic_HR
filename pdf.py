from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Define CV content
cv_data = {
    "Alice_DevOps_Engineer.pdf": """
    📄 Curriculum Vitae

    👤 Name: Alice Smith
    🎯 Title: DevOps Engineer
    📍 Location: Helsinki, Finland
    📧 Email: alice.smith@example.com
    📞 Phone: +358 40 1234567

    🧠 Summary:
    Experienced DevOps Engineer with 5+ years of expertise in automating infrastructure, CI/CD pipelines, cloud services, and monitoring solutions.

    💼 Work Experience:
    - DevOps Engineer, CloudCorp (2021–Present)
      - Designed and maintained scalable AWS infrastructure
      - Developed CI/CD pipelines using Jenkins and GitHub Actions

    - System Administrator, TechStart (2018–2021)
      - Maintained Linux servers and introduced automation scripts

    🎓 Education:
    - BSc in Computer Engineering, Aalto University, 2018

    🛠️ Skills:
    - AWS, Docker, Kubernetes, Jenkins, Terraform
    - Python, Bash, Git, Prometheus

    🏆 Certifications:
    - AWS Certified Solutions Architect
    """,

    "Brown_Barber.pdf": """
    📄 Curriculum Vitae

    👤 Name: Brown Johnson
    🎯 Title: Professional Barber
    📍 Location: Tampere, Finland
    📧 Email: brown.johnson@example.com
    📞 Phone: +358 50 9876543

    🧠 Summary:
    Dedicated and friendly barber with 10+ years of experience in modern hair styling, grooming, and customer service.

    💼 Work Experience:
    - Lead Barber, StyleHub Salon (2015–Present)
      - Trained junior barbers and managed scheduling
      - Specialized in beard trims and modern fades

    - Barber, CityCuts (2010–2015)
      - Served 15+ clients daily with high satisfaction

    🎓 Education:
    - Certified Barber Program, Finnish Hairdressing School, 2009

    ✂️ Skills:
    - Scissor & clipper cutting, fades, beard styling, customer service
    """,

    "Charles_Mechanic.pdf": """
    📄 Curriculum Vitae

    👤 Name: Charles Walker
    🎯 Title: Auto Mechanic
    📍 Location: Oulu, Finland
    📧 Email: charles.walker@example.com
    📞 Phone: +358 44 6543210

    🧠 Summary:
    Skilled auto mechanic with 8+ years of hands-on experience diagnosing and repairing various types of vehicles.

    💼 Work Experience:
    - Auto Mechanic, Northern Auto Garage (2019–Present)
      - Specializes in engine diagnostics and brake system repairs

    - Junior Mechanic, SpeedFix Auto (2015–2019)
      - Performed oil changes, tire rotations, and part replacements

    🎓 Education:
    - Diploma in Automotive Technology, Oulu Vocational College, 2015

    🛠️ Skills:
    - Engine diagnostics, brake systems, suspension, electrical repair
    - Tools: OBD-II scanners, hydraulic lifts, torque wrenches
    """
}

# Generate PDFs
for filename, content in cv_data.items():
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    lines = content.strip().split('\n')
    y = height - 50
    for line in lines:
        if y < 50:
            c.showPage()
            y = height - 50
        c.drawString(50, y, line.strip())
        y -= 15
    c.save()
    print(f"✅ Saved: {filename}")
