#!/usr/bin/env python3
"""Generate a professionally formatted PDF from the README.md."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import os
import re

DARK_BLUE = HexColor("#1a237e")
MED_BLUE = HexColor("#283593")
LIGHT_BLUE = HexColor("#e8eaf6")
ACCENT = HexColor("#ff9900")
WHITE = HexColor("#ffffff")
BLACK = HexColor("#000000")
GRAY = HexColor("#666666")
LIGHT_GRAY = HexColor("#f5f5f5")
BORDER_GRAY = HexColor("#cccccc")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def build_styles():
    base = getSampleStyleSheet()
    return {
        'title': ParagraphStyle("Title", parent=base["Title"],
            fontSize=24, textColor=DARK_BLUE, spaceAfter=4,
            fontName="Helvetica-Bold", alignment=TA_LEFT),
        'subtitle': ParagraphStyle("Sub", parent=base["Normal"],
            fontSize=12, textColor=GRAY, spaceAfter=16, fontName="Helvetica-Oblique"),
        'h1': ParagraphStyle("H1", parent=base["Heading1"],
            fontSize=18, textColor=DARK_BLUE, spaceBefore=18, spaceAfter=8,
            fontName="Helvetica-Bold"),
        'h2': ParagraphStyle("H2", parent=base["Heading2"],
            fontSize=14, textColor=MED_BLUE, spaceBefore=14, spaceAfter=6,
            fontName="Helvetica-Bold"),
        'h3': ParagraphStyle("H3", parent=base["Heading3"],
            fontSize=11, textColor=BLACK, spaceBefore=10, spaceAfter=4,
            fontName="Helvetica-Bold"),
        'body': ParagraphStyle("Body", parent=base["Normal"],
            fontSize=10, textColor=BLACK, spaceAfter=4, fontName="Helvetica", leading=14),
        'bullet': ParagraphStyle("Bullet", parent=base["Normal"],
            fontSize=10, textColor=BLACK, leftIndent=24, bulletIndent=12,
            spaceAfter=3, leading=13, fontName="Helvetica"),
        'numbered': ParagraphStyle("Num", parent=base["Normal"],
            fontSize=10, textColor=BLACK, leftIndent=24,
            spaceAfter=3, leading=13, fontName="Helvetica"),
        'footer': ParagraphStyle("Foot", parent=base["Normal"],
            fontSize=8, textColor=GRAY, alignment=TA_CENTER),
    }


def san(text):
    """Sanitize text for ReportLab XML."""
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'`(.+?)`', r'<font name="Courier" size="9">\1</font>', text)
    text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<link href="\2">\1</link>', text)
    return text


def parse_table(lines, idx):
    rows = []
    i = idx
    while i < len(lines) and '|' in lines[i]:
        cells = [c.strip() for c in lines[i].split('|')[1:-1]]
        if cells and not all(set(c) <= set('- :') for c in cells):
            rows.append(cells)
        i += 1
    return rows, i


def build_pdf():
    readme_path = os.path.join(BASE_DIR, 'README.md')
    output_path = os.path.join(BASE_DIR, 'Amazon-Seller-Skill-Suite-README.pdf')

    with open(readme_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    s = build_styles()
    story = []

    story.append(Paragraph("Amazon Seller Skill Suite", s['title']))
    story.append(Paragraph("v1.0", s['subtitle']))
    story.append(HRFlowable(width="100%", thickness=2, color=ACCENT, spaceAfter=12))

    i = 0
    while i < len(lines):
        line = lines[i].rstrip('\n')

        if i == 0 and line.startswith('# '):
            i += 1
            continue

        if not line.strip():
            story.append(Spacer(1, 4))
            i += 1
            continue

        if line.startswith('## '):
            story.append(Paragraph(san(line[3:].strip()), s['h1']))
            story.append(HRFlowable(width="100%", thickness=1, color=LIGHT_BLUE, spaceAfter=6))
            i += 1
            continue

        if line.startswith('### '):
            story.append(Paragraph(san(line[4:].strip()), s['h2']))
            i += 1
            continue

        if line.startswith('#### '):
            story.append(Paragraph(san(line[5:].strip()), s['h3']))
            i += 1
            continue

        if '|' in line and i + 1 < len(lines) and '---' in lines[i + 1]:
            table_data, end_idx = parse_table(lines, i)
            if table_data:
                nc = len(table_data[0])
                avail = 6.5 * inch
                if nc == 3 and table_data[0][0].strip().lower() in ('step', '#'):
                    cw = [0.5 * inch, 1.8 * inch, 4.2 * inch]
                elif nc == 3:
                    cw = [1.8 * inch, 0.8 * inch, 3.9 * inch]
                elif nc == 2:
                    cw = [2.5 * inch, 4.0 * inch]
                else:
                    cw = [avail / nc] * nc

                clean = []
                for row in table_data:
                    cr = [Paragraph(san(c), s['body']) for c in row]
                    while len(cr) < nc:
                        cr.append(Paragraph('', s['body']))
                    clean.append(cr[:nc])

                t = Table(clean, colWidths=cw, repeatRows=1)
                t.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), DARK_BLUE),
                    ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 9),
                    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LIGHT_GRAY]),
                    ('GRID', (0, 0), (-1, -1), 0.5, BORDER_GRAY),
                    ('TOPPADDING', (0, 0), (-1, -1), 4),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
                    ('LEFTPADDING', (0, 0), (-1, -1), 6),
                    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ]))
                story.append(t)
                story.append(Spacer(1, 8))
            i = end_idx
            continue

        if re.match(r'^\d+\. ', line.strip()):
            story.append(Paragraph(san(line.strip()), s['numbered']))
            i += 1
            continue

        if line.strip().startswith('- ') or line.strip().startswith('* '):
            story.append(Paragraph(san(line.strip()[2:]), s['bullet'], bulletText='\u2022'))
            i += 1
            continue

        story.append(Paragraph(san(line.strip()), s['body']))
        i += 1

    story.append(Spacer(1, 20))
    story.append(HRFlowable(width="40%", thickness=0.5, color=BORDER_GRAY, spaceAfter=8))
    story.append(Paragraph(
        "Adapted from The Agency (github.com/msitarzewski/agency-agents)", s['footer']))

    doc = SimpleDocTemplate(output_path, pagesize=letter,
        topMargin=0.75*inch, bottomMargin=0.75*inch,
        leftMargin=0.85*inch, rightMargin=0.85*inch)
    doc.build(story)
    print(f"PDF: {output_path} ({os.path.getsize(output_path):,} bytes)")


if __name__ == '__main__':
    build_pdf()
