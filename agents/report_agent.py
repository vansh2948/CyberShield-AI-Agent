from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(
    threats,
    vulnerabilities,
    recommendations
):

    pdf_file = "CyberShield_Report.pdf"

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "CyberShield Security Report",
            styles["Title"]
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            f"<b>Threats</b><br/>{threats}",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            f"<b>Vulnerabilities</b><br/>{vulnerabilities}",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            f"<b>Recommendations</b><br/>{recommendations}",
            styles["BodyText"]
        )
    )

    doc.build(story)

    return pdf_file