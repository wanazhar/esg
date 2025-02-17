# utils/pdf_parser.py
import pdfplumber

class PDFESGParser:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def extract_esg_data(self):
        esg_data = {}
        with pdfplumber.open(self.pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                # Example: Look for specific patterns in text
                if 'ESG Score' in text:
                    esg_data.update(self._parse_esg_scores(text))
        return esg_data

    def _parse_esg_scores(self, text):
        data = {}
        lines = text.split('\n')
        for line in lines:
            if 'Environmental' in line:
                data['Environmental'] = self._extract_score(line)
            elif 'Social' in line:
                data['Social'] = self._extract_score(line)
            elif 'Governance' in line:
                data['Governance'] = self._extract_score(line)
        return data

    def _extract_score(self, line):
        # Simplified example: extract score from line
        return float(line.split(':')[-1].strip())