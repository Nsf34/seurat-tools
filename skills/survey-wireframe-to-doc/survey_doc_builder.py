"""
Survey Document Builder — python-docx engine for Seurat Group survey documents.

Generates a correctly formatted, programmer-ready survey document (.docx) from
structured question data. Used by the survey-wireframe-to-doc skill.

Formatting matches BIAH Shopper Journey Survey Document v1.0 exactly:
  - Font: Franklin Gothic Book (document default)
  - Header tables: qst_answers2 style — BFBFBF borders, blue (B4C6E7) R0 shading
  - Response tables: Table Grid Light12 style — BFBFBF borders
  - RED (FF0000) text: topic labels, question numbers, programming notes,
    logic notes, NEW SCREEN, row numbers in Col 0, notes in Col 2
  - BLACK text: question text (R2 Col 1), response option text (Col 1)
  - Selection instructions: italic, black

Usage:
    from survey_doc_builder import SurveyDocBuilder

    builder = SurveyDocBuilder()
    builder.set_study_info(title="Study Name", date="March 2026")
    builder.add_overview(objectives=[...], structure=[...], criteria=[...])
    builder.add_section_header("Screener", objectives=[...])
    builder.add_message("Introduction Message", "M1.", "Thank you...", "Show to all.")
    builder.add_question(q_number="S1.", topic="Age", ...)
    builder.save("output.docx")
"""

from docx import Document
from docx.shared import Pt, Inches, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml
import os

# Constants
RED = RGBColor(0xFF, 0x00, 0x00)
BLACK = RGBColor(0x00, 0x00, 0x00)
BLUE_FILL = "B4C6E7"       # Light blue for header R0 shading
BORDER_COLOR = "BFBFBF"    # Light gray for all table borders
FONT_NAME = "Franklin Gothic Book"
FONT_SIZE = Pt(11)         # 139700 EMU
HEADING2_COLOR = RGBColor(0x2F, 0x54, 0x96)  # Dark blue for Heading 2

# Column widths for 3-col response tables (in dxa / twentieths of a point)
COL0_WIDTH = 576     # Narrow number column
COL1_WIDTH = 6031    # Wide option text column
COL2_WIDTH = 2748    # Medium notes column


class SurveyDocBuilder:
    """Builds a formatted survey document .docx matching Seurat standards."""

    def __init__(self):
        self.doc = Document()
        self._setup_styles()
        self._first_block = True

    def _setup_styles(self):
        """Configure document-level styles."""
        # Normal style
        style = self.doc.styles['Normal']
        font = style.font
        font.name = FONT_NAME
        font.size = FONT_SIZE

        pf = style.paragraph_format
        pf.space_before = Pt(0)
        pf.space_after = Pt(0)
        pf.line_spacing = 1.0

        # Page margins (1 inch = 914400 EMU)
        for section in self.doc.sections:
            section.left_margin = Inches(1)
            section.right_margin = Inches(1)
            section.top_margin = Inches(1)
            section.bottom_margin = Inches(1)

    # ── Helpers for red/black text ────────────────────────────

    def _add_red_text(self, paragraph, text, bold=False, italic=False):
        """Add a run of red text to a paragraph."""
        run = paragraph.add_run(text)
        run.font.color.rgb = RED
        run.font.name = FONT_NAME
        run.font.size = FONT_SIZE
        if bold:
            run.bold = True
        if italic:
            run.italic = True
        return run

    def _add_black_text(self, paragraph, text, bold=False, italic=False):
        """Add a run of black text to a paragraph."""
        run = paragraph.add_run(text)
        run.font.name = FONT_NAME
        run.font.size = FONT_SIZE
        if bold:
            run.bold = True
        if italic:
            run.italic = True
        return run

    def _set_cell_red(self, cell, text):
        """Set cell text to red (clearing any existing content)."""
        p = cell.paragraphs[0]
        p.clear()
        self._add_red_text(p, text)

    def _set_cell_black(self, cell, text):
        """Set cell text to black (clearing any existing content)."""
        p = cell.paragraphs[0]
        p.clear()
        self._add_black_text(p, text)

    def _set_cell_shading(self, cell, fill_color):
        """Apply background shading to a cell."""
        shading_elm = parse_xml(
            f'<w:shd {nsdecls("w")} w:fill="{fill_color}" w:val="clear" w:color="auto"/>'
        )
        cell._tc.get_or_add_tcPr().append(shading_elm)

    def _set_cell_width(self, cell, width_dxa):
        """Set the width of a cell in dxa units."""
        tc = cell._tc
        tcPr = tc.get_or_add_tcPr()
        tcW = tcPr.find(qn('w:tcW'))
        if tcW is None:
            tcW = parse_xml(f'<w:tcW {nsdecls("w")} w:w="{width_dxa}" w:type="dxa"/>')
            tcPr.append(tcW)
        else:
            tcW.set(qn('w:w'), str(width_dxa))
            tcW.set(qn('w:type'), 'dxa')

    # ── Table border / style helpers ─────────────────────────

    def _set_table_borders(self, table):
        """Set BFBFBF borders on all sides of a table."""
        tbl = table._tbl
        tbl_pr = tbl.tblPr if tbl.tblPr is not None else parse_xml(
            f'<w:tblPr {nsdecls("w")}/>'
        )

        borders_xml = f'''<w:tblBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="4" w:space="0" w:color="{BORDER_COLOR}"/>
            <w:left w:val="single" w:sz="4" w:space="0" w:color="{BORDER_COLOR}"/>
            <w:bottom w:val="single" w:sz="4" w:space="0" w:color="{BORDER_COLOR}"/>
            <w:right w:val="single" w:sz="4" w:space="0" w:color="{BORDER_COLOR}"/>
            <w:insideH w:val="single" w:sz="4" w:space="0" w:color="{BORDER_COLOR}"/>
            <w:insideV w:val="single" w:sz="4" w:space="0" w:color="{BORDER_COLOR}"/>
        </w:tblBorders>'''

        borders = parse_xml(borders_xml)

        existing = tbl_pr.find(qn('w:tblBorders'))
        if existing is not None:
            tbl_pr.remove(existing)
        tbl_pr.append(borders)

    def _build_header_table(self, topic, q_number, question_text_runs, programming_note):
        """
        Build a 4-row header table matching Seurat format.

        Args:
            topic: Topic label text (RED, blue background)
            q_number: Question number like "S1.", "Q101.", "M1." (RED)
            question_text_runs: List of (text, is_italic) tuples for R2
            programming_note: Programming note text (RED)
        """
        table = self.doc.add_table(rows=4, cols=1)
        self._set_table_borders(table)

        # R0: Topic — RED text on blue background
        r0_cell = table.cell(0, 0)
        self._set_cell_red(r0_cell, topic)
        self._set_cell_shading(r0_cell, BLUE_FILL)

        # R1: Question number — RED text
        r1_cell = table.cell(1, 0)
        if q_number:
            self._set_cell_red(r1_cell, q_number)
        else:
            r1_cell.text = ""

        # R2: Question text (black) + selection instruction (italic black)
        r2_cell = table.cell(2, 0)
        p = r2_cell.paragraphs[0]
        p.clear()
        for text, is_italic in question_text_runs:
            self._add_black_text(p, text, italic=is_italic)

        # R3: Programming note — RED text
        r3_cell = table.cell(3, 0)
        self._set_cell_red(r3_cell, programming_note)

        return table

    # ── NEW SCREEN ────────────────────────────────────────────

    def _add_new_screen(self):
        """Add 'NEW SCREEN' paragraph in red between question blocks, with spacing."""
        self.doc.add_paragraph()  # blank line before
        p = self.doc.add_paragraph()
        self._add_red_text(p, "NEW SCREEN")

    # ── Logic notes ───────────────────────────────────────────

    def _add_logic_note(self, text, bold=False):
        """Add a red logic/programming note paragraph."""
        p = self.doc.add_paragraph()
        self._add_red_text(p, text, bold=bold)

    # ── Study Info ────────────────────────────────────────────

    def set_study_info(self, title: str, date: str, doc_type: str = "Quantitative Survey Document"):
        """Add the title page header."""
        # Title
        p = self.doc.add_paragraph()
        run = p.add_run(title)
        run.bold = True
        run.font.name = FONT_NAME
        run.font.size = Pt(14)

        # Doc type
        p = self.doc.add_paragraph()
        run = p.add_run(doc_type)
        run.bold = True
        run.font.name = FONT_NAME
        run.font.size = Pt(12)
        run.font.color.rgb = BLACK

        # Date
        p = self.doc.add_paragraph()
        run = p.add_run(date)
        run.font.name = FONT_NAME
        run.font.size = Pt(12)
        run.font.color.rgb = BLACK

        self.doc.add_paragraph()  # blank line

    # ── Overview ──────────────────────────────────────────────

    def add_overview(self, objectives: list, structure: list, criteria: list):
        """Add the Study Overview section."""
        h = self.doc.add_heading("Survey Overview", level=1)
        for run in h.runs:
            run.font.size = Pt(12)

        # Objectives
        h2 = self.doc.add_heading("Objectives", level=2)
        for obj in objectives:
            p = self.doc.add_paragraph(style='List Paragraph')
            run = p.add_run(obj)
            run.font.name = FONT_NAME
            run.font.size = FONT_SIZE

        # Survey Structure
        h2 = self.doc.add_heading("Survey Structure", level=2)
        for section_name, sub_bullets in structure:
            p = self.doc.add_paragraph(style='List Paragraph')
            run = p.add_run(section_name)
            run.bold = True
            run.font.name = FONT_NAME
            run.font.size = FONT_SIZE
            for sub in sub_bullets:
                sp = self.doc.add_paragraph()
                sp.paragraph_format.left_indent = Inches(0.5)
                run = sp.add_run(sub)
                run.font.name = FONT_NAME
                run.font.size = FONT_SIZE

        # Respondent Criteria & Quotas
        h2 = self.doc.add_heading("Respondent Criteria & Quotas", level=2)
        for crit in criteria:
            p = self.doc.add_paragraph()
            run = p.add_run(crit)
            run.font.name = FONT_NAME
            run.font.size = FONT_SIZE

    # ── Section Headers ───────────────────────────────────────

    def add_section_header(self, section_name: str, objectives: list):
        """Add a section header with objective bullets."""
        self.doc.add_paragraph()

        h = self.doc.add_heading(section_name, level=2)

        # Objectives label
        p = self.doc.add_paragraph()
        run = p.add_run("Objectives:")
        run.bold = True
        run.font.name = FONT_NAME
        run.font.size = FONT_SIZE

        for obj in objectives:
            p = self.doc.add_paragraph(style='List Paragraph')
            run = p.add_run(obj)
            run.font.name = FONT_NAME
            run.font.size = FONT_SIZE

        # Reset first_block so first question in section doesn't get NEW SCREEN
        # Actually we want NEW SCREEN before every question/message after a section header
        # But the hold terminates note comes first, so leave _first_block as-is

    # ── Hold Terminates Note ──────────────────────────────────

    def add_hold_terminates_note(self):
        """Add the standard hold terminates note (RED, bold)."""
        p = self.doc.add_paragraph()
        self._add_red_text(
            p,
            "Please hold all terminations until end of screener unless otherwise specified.",
            bold=True
        )

    # ── Message Blocks ────────────────────────────────────────

    def add_message(self, topic: str, q_number: str, message_text: str, show_condition: str):
        """
        Add a message/transition screen.

        Args:
            topic: e.g., "Introduction Message", "Message"
            q_number: e.g., "M1.", "M2." (RED in R1)
            message_text: The message body text (black in R2)
            show_condition: e.g., "Show to all respondents." (RED in R3)
        """
        if not self._first_block:
            self._add_new_screen()
        self._first_block = False

        self._build_header_table(
            topic=topic,
            q_number=q_number,
            question_text_runs=[(message_text, False)],
            programming_note=show_condition
        )

    # ── Question Blocks ───────────────────────────────────────

    def add_question(
        self,
        q_number: str,
        topic: str,
        question_text: str,
        selection_instruction: str,
        programming_note: str,
        response_options: list = None,
        grid_headers: list = None,
        logic_notes: list = None,
        question_type: str = "simple",
        scale_labels: list = None,
        bipolar_pairs: list = None,
    ):
        """
        Add a complete question block.

        Args:
            q_number: "S1.", "Q101.", "D1." etc. — goes in R1 in RED
            topic: Topic label — goes in R0 with blue shading, RED text
            question_text: Question wording (BLACK)
            selection_instruction: e.g., "Select one." (italic BLACK)
            programming_note: Goes in R3 in RED
            response_options: List of tuples. Format depends on question_type:
                - simple: [(option_text, note), ...]
                - 2col_grid: [(option_text, c1_note, c2_note), ...]
                - 3col_grid: [(option_text, c1_note, c2_note, c3_note), ...]
            grid_headers: For grids, list of column header strings.
            logic_notes: List of logic instruction strings (added as RED paragraphs)
            question_type: "simple"|"2col_grid"|"3col_grid"|"scale"|"bipolar"|"dropdown"|"open_end"
            scale_labels: For "scale" type, list of scale point labels.
            bipolar_pairs: For "bipolar" type, list of (left, right) tuples.
        """
        if not self._first_block:
            self._add_new_screen()
        self._first_block = False

        # Build R2 runs: question text (normal) + space + selection instruction (italic)
        r2_runs = [(question_text + " ", False), (selection_instruction, True)]

        # Header table
        self._build_header_table(
            topic=topic,
            q_number=q_number,
            question_text_runs=r2_runs,
            programming_note=programming_note
        )

        # Response table
        if question_type == "simple" and response_options:
            self._add_simple_response_table(response_options)

        elif question_type == "2col_grid" and response_options:
            self._add_grid_response_table(response_options, grid_headers, num_data_cols=2)

        elif question_type == "3col_grid" and response_options:
            self._add_grid_response_table(response_options, grid_headers, num_data_cols=3)

        elif question_type == "scale" and scale_labels and response_options:
            self._add_scale_table(scale_labels, response_options)

        elif question_type == "bipolar" and bipolar_pairs:
            self._add_bipolar_table(bipolar_pairs)

        # dropdown and open_end: no response table

        # Logic notes (RED paragraphs after the table)
        if logic_notes:
            for note in logic_notes:
                self._add_logic_note(note)

    # ── Response Table Builders ───────────────────────────────

    def _add_simple_response_table(self, options: list):
        """
        Simple response table: N rows × 3 cols.
        Col 0: Row number (RED) — "1.", "2.", etc.
        Col 1: Option text (BLACK)
        Col 2: Note (RED)
        """
        table = self.doc.add_table(rows=len(options), cols=3)
        self._set_table_borders(table)

        for i, (opt_text, note) in enumerate(options):
            # Col 0: Row number in RED
            c0 = table.cell(i, 0)
            self._set_cell_red(c0, f"{i + 1}.")
            self._set_cell_width(c0, COL0_WIDTH)

            # Col 1: Option text in BLACK
            c1 = table.cell(i, 1)
            self._set_cell_black(c1, opt_text)
            self._set_cell_width(c1, COL1_WIDTH)

            # Col 2: Note in RED
            c2 = table.cell(i, 2)
            if note:
                self._set_cell_red(c2, note)
            else:
                c2.text = ""
            self._set_cell_width(c2, COL2_WIDTH)

    def _add_grid_response_table(self, options: list, headers: list, num_data_cols: int):
        """
        Grid response table with header row.

        Total columns = 2 + num_data_cols (blank + option + C1 + C2 [+ C3])
        Header row: blank | blank | C1 header (RED) | C2 header (RED) [| C3 header (RED)]
        Data rows: blank | option (BLACK) | c1_note (RED) | c2_note (RED) [| c3_note (RED)]
        """
        total_cols = 2 + num_data_cols
        num_rows = len(options) + 1  # +1 for header
        table = self.doc.add_table(rows=num_rows, cols=total_cols)
        self._set_table_borders(table)

        # Header row
        table.cell(0, 0).text = ""
        table.cell(0, 1).text = ""
        if headers:
            for h_idx, h_text in enumerate(headers):
                col_idx = h_idx + 2
                if col_idx < total_cols:
                    self._set_cell_red(table.cell(0, col_idx), h_text)

        # Data rows
        for i, option_data in enumerate(options):
            row_idx = i + 1
            # Col 0: Row number in RED
            self._set_cell_red(table.cell(row_idx, 0), f"{i + 1}.")
            self._set_cell_width(table.cell(row_idx, 0), COL0_WIDTH)

            # Col 1: option text (BLACK)
            self._set_cell_black(table.cell(row_idx, 1), option_data[0])

            # Remaining columns: notes (RED)
            for c in range(1, len(option_data)):
                col_idx = c + 1
                if col_idx < total_cols and option_data[c]:
                    self._set_cell_red(table.cell(row_idx, col_idx), option_data[c])

    def _add_scale_table(self, scale_labels: list, statements: list):
        """
        Agreement scale: 2-row scale table + statement table.

        Scale table R0: numbers (1, 2, 3...) in RED
        Scale table R1: labels (Strongly disagree, etc.) in BLACK
        Statement table: blank | statement (BLACK) | condition (RED)
        """
        num_points = len(scale_labels)

        # Scale label table (2 rows × N cols)
        scale_table = self.doc.add_table(rows=2, cols=num_points)
        self._set_table_borders(scale_table)

        for i, label in enumerate(scale_labels):
            # R0: number in RED
            self._set_cell_red(scale_table.cell(0, i), str(i + 1))
            # R1: label text in BLACK
            self._set_cell_black(scale_table.cell(1, i), f"{i + 1} {label}")

        # Statement table (N rows × 3 cols)
        stmt_table = self.doc.add_table(rows=len(statements), cols=3)
        self._set_table_borders(stmt_table)

        for i, (stmt_text, condition) in enumerate(statements):
            # Col 0: Row number in RED
            self._set_cell_red(stmt_table.cell(i, 0), f"{i + 1}.")
            self._set_cell_width(stmt_table.cell(i, 0), COL0_WIDTH)
            # Col 1: Statement text in BLACK
            self._set_cell_black(stmt_table.cell(i, 1), stmt_text)
            # Col 2: Condition in RED
            if condition:
                self._set_cell_red(stmt_table.cell(i, 2), condition)

    def _add_bipolar_table(self, pairs: list):
        """
        Bipolar/slider scale: each row = row# (RED) | left (BLACK) | scale (RED numbers) | right (BLACK).
        """
        table = self.doc.add_table(rows=len(pairs), cols=4)
        self._set_table_borders(table)

        for i, (left, right) in enumerate(pairs):
            self._set_cell_red(table.cell(i, 0), f"{i + 1}.")
            self._set_cell_width(table.cell(i, 0), COL0_WIDTH)
            self._set_cell_black(table.cell(i, 1), left)
            self._set_cell_red(table.cell(i, 2), "1 — 2 — 3 — 4 — 5")
            self._set_cell_black(table.cell(i, 3), right)

    # ── Save ──────────────────────────────────────────────────

    def save(self, filepath: str):
        """Save the document to the specified path."""
        directory = os.path.dirname(filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        self.doc.save(filepath)
        print(f"Survey document saved to: {os.path.abspath(filepath)}")
        return filepath


# ── Wireframe Parser ──────────────────────────────────────────

def parse_wireframe(filepath: str) -> dict:
    """
    Parse a wireframe .docx and extract structured question data.

    Returns:
        dict with keys:
            - title: str
            - overview: dict with objectives, structure, criteria
            - sections: list of dicts, each with name, objectives, questions
    """
    doc = Document(filepath)

    result = {
        'title': '',
        'overview': {'objectives': [], 'structure': [], 'criteria': []},
        'sections': []
    }

    for p in doc.paragraphs[:5]:
        text = p.text.strip()
        if text and not result['title']:
            result['title'] = text
            break

    for table in doc.tables:
        section = _parse_wireframe_table(table)
        if section and section['questions']:
            result['sections'].append(section)

    return result


def _parse_wireframe_table(table) -> dict:
    """Parse a single wireframe table into a section dict."""
    rows = table.rows
    if len(rows) < 2:
        return None

    header_cells = [cell.text.strip().lower() for cell in rows[0].cells]
    num_cols = len(header_cells)

    topic_col = question_col = response_col = objective_col = number_col = None

    for i, h in enumerate(header_cells):
        if 'topic' in h:
            topic_col = i
        elif 'question' in h and 'number' not in h:
            question_col = i
        elif 'response' in h or 'sample' in h:
            response_col = i
        elif 'objective' in h or 'rationale' in h:
            objective_col = i
        elif 'number' in h or '#' in h:
            number_col = i

    if topic_col is None and num_cols >= 3:
        if number_col is not None:
            topic_col = topic_col or 1
            question_col = question_col or 2
            response_col = response_col or 3
            objective_col = objective_col or (4 if num_cols > 4 else None)
        else:
            topic_col = 0
            question_col = 1
            response_col = 2
            objective_col = 3 if num_cols > 3 else None

    if topic_col is None or question_col is None:
        return None

    section_name = ""
    questions = []

    for row_idx in range(1, len(rows)):
        cells = [cell.text.strip() for cell in rows[row_idx].cells]

        topic = cells[topic_col] if topic_col < len(cells) else ""
        question_text = cells[question_col] if question_col is not None and question_col < len(cells) else ""
        response = cells[response_col] if response_col is not None and response_col < len(cells) else ""
        objective = cells[objective_col] if objective_col is not None and objective_col < len(cells) else ""
        number = cells[number_col] if number_col is not None and number_col < len(cells) else ""

        if not topic and not question_text:
            continue

        if topic and not question_text and not response:
            if not section_name:
                section_name = topic
            continue

        questions.append({
            'number': number,
            'topic': topic,
            'question_text': question_text,
            'response_options_raw': response,
            'objective_rationale': objective,
        })

    return {
        'name': section_name or "Section",
        'objectives': [],
        'questions': questions,
    }


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python survey_doc_builder.py <wireframe.docx> [output.docx]")
        sys.exit(1)

    wireframe_path = sys.argv[1]
    result = parse_wireframe(wireframe_path)

    print(f"Title: {result['title']}")
    print(f"Sections: {len(result['sections'])}")
    for sec in result['sections']:
        print(f"\n  {sec['name']} ({len(sec['questions'])} questions)")
        for q in sec['questions']:
            topic = q['topic'][:40]
            qtext = q['question_text'][:60]
            print(f"    {q['number']:>4} | {topic:<40} | {qtext}")
