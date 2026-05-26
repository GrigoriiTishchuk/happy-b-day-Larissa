from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    Table,
    TableStyle,
    HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from utils.loaders import load_json
from datetime import datetime
from io import BytesIO


def generate_observation_report():
    observations = load_json("data/observations.json", default=[])

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=50,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()
    elements = []

    # COVER
    elements.append(Paragraph("<font size=24><b>Field Observation Archive</b></font>", styles["Title"]))
    elements.append(Spacer(1, 20))

    elements.append(Paragraph("Longitudinal Behavioral & Emotional Study", styles["BodyText"]))
    elements.append(Spacer(1, 10))

    elements.append(
        Paragraph(
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 30))

    elements.append(
        Paragraph(
            "This archive contains reconstructed behavioral observations and emotional anomalies.",
            styles["BodyText"]
        )
    )

    elements.append(PageBreak())

    # OBSERVATIONS
    for obs in observations:

        elements.append(
            Paragraph(f"<b>Observation #{obs['id']}</b>", styles["Heading2"])
        )
        elements.append(Spacer(1, 10))

        meta = Table([
            ["Category", obs["category"]],
            ["Severity", obs["severity"]]
        ])

        meta.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('PADDING', (0, 0), (-1, -1), 6),
        ]))

        elements.append(meta)
        elements.append(Spacer(1, 12))

        elements.append(Paragraph("<b>Observed Phenomenon</b>", styles["Heading3"]))
        elements.append(Paragraph(obs["observation"], styles["BodyText"]))
        elements.append(Spacer(1, 12))

        elements.append(Paragraph("<b>Details</b>", styles["Heading3"]))
        for d in obs["details"]:
            elements.append(Paragraph(f"• {d}", styles["BodyText"]))

        elements.append(Spacer(1, 12))

        elements.append(Paragraph("<b>Conclusion</b>", styles["Heading3"]))
        elements.append(Paragraph(obs["conclusion"], styles["BodyText"]))

        elements.append(Spacer(1, 20))
        elements.append(HRFlowable(width="100%"))
        elements.append(Spacer(1, 20))

    doc.build(elements)

    buffer.seek(0)
    return buffer