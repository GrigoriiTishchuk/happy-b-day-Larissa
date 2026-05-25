from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    Table,
    TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus.flowables import HRFlowable
from utils.loaders import load_json
from datetime import datetime

# OBSERVATION PDF GENERATOR
def generate_observation_report(output_path="field_observations_report.pdf"):
    observations = load_json("data/observations.json",default=[])
    # DOCUMENT
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=50,
        bottomMargin=40
    )
    styles = getSampleStyleSheet()
    elements = []
    # COVER PAGE
    title = Paragraph(
        """
        <font size=24>
        <b>Field Observation Archive</b>
        </font>
        """,
        styles["Title"]
    )
    subtitle = Paragraph(
        """
        Longitudinal Behavioral & Emotional Study
        """,
        styles["BodyText"]
    )
    generated_at = Paragraph(
        f"""
        Generated:
        {datetime.now().strftime("%Y-%m-%d %H:%M")}
        """,
        styles["BodyText"]
    )

    elements.append(title)
    elements.append(Spacer(1, 20))
    elements.append(subtitle)
    elements.append(Spacer(1, 10))
    elements.append(generated_at)
    elements.append(Spacer(1, 40))
    intro = Paragraph(
        """
        This archive contains reconstructed behavioral observations,
        environmental interactions, emotional anomalies,
        and documented affection-related phenomena observed
        during the study period.
        """,
        styles["BodyText"]
    )

    elements.append(intro)
    elements.append(Spacer(1, 40))
    warning = Paragraph(
        """
        <font color='red'>
        CONFIDENTIAL — Researcher objectivity may be compromised.
        </font>
        """,
        styles["BodyText"]
    )
    elements.append(warning)
    elements.append(PageBreak())
    # OBSERVATIONS
    for obs in observations:
        # HEADER
        obs_title = Paragraph(
            f"""
            <font size=18>
            <b>Observation #{obs['id']}</b>
            </font>
            """,
            styles["Heading2"]
        )
        elements.append(obs_title)
        elements.append(Spacer(1, 8))
        meta_data = [
            ["Category", obs["category"]],
            ["Severity", obs["severity"]]
        ]
        meta_table = Table(
            meta_data,
            colWidths=[120, 300]
        )
        meta_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
        ]))
        elements.append(meta_table)
        elements.append(Spacer(1, 18))

        # OBSERVATION TEXT
        observation_title = Paragraph(
            "<b>Observed Phenomenon</b>",
            styles["Heading3"]
        )
        observation_text = Paragraph(
            obs["observation"],
            styles["BodyText"]
        )
        elements.append(observation_title)
        elements.append(Spacer(1, 6))
        elements.append(observation_text)
        elements.append(Spacer(1, 18))

        # DETAILS
        details_title = Paragraph(
            "<b>Additional Notes</b>",
            styles["Heading3"]
        )
        elements.append(details_title)
        elements.append(Spacer(1, 6))
        for detail in obs["details"]:
            detail_paragraph = Paragraph(
                f"• {detail}",
                styles["BodyText"]
            )
            elements.append(detail_paragraph)
        elements.append(Spacer(1, 18))

        # CONCLUSION
        conclusion_title = Paragraph(
            "<b>Research Conclusion</b>",
            styles["Heading3"]
        )
        conclusion_text = Paragraph(
            obs["conclusion"],
            styles["BodyText"]
        )
        elements.append(conclusion_title)
        elements.append(Spacer(1, 6))
        elements.append(conclusion_text)
        elements.append(Spacer(1, 18))

        footer = Paragraph(
            """
            <font size=9 color='grey'>
            Research Integrity Score: 94%<br/>
            Peer Review Status: emotionally compromised
            </font>
            """,
            styles["BodyText"]
        )

        elements.append(footer)
        elements.append(Spacer(1, 24))
        elements.append(HRFlowable(width="100%"))
        elements.append(Spacer(1, 24))

    # FINAL PAGE
    final_title = Paragraph(
        """
        <font size=20>
        <b>Final Remarks</b>
        </font>
        """,
        styles["Heading2"]
    )

    final_text = Paragraph(
        """
        Longitudinal observations indicate increasing emotional
        synchronization, stable mutual curiosity,
        and dangerously high attachment formation.
        Further data collection strongly recommended.
        Researcher bias can no longer be ruled out.
        """,
        styles["BodyText"]
    )
    elements.append(final_title)
    elements.append(Spacer(1, 20))
    elements.append(final_text)
    # BUILD PDF
    doc.build(elements)