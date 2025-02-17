# reporting/global_reports.py
class ESGReportGenerator:
    FORMATS = ['pdf', 'xlsx', 'html', 'json']
    LANGUAGES = ['en', 'zh', 'es', 'ar', 'fr']
    
    def generate(self, analysis, format='pdf', lang='en'):
        """Multi-format, multi-lingual reporting"""
        builder = ReportBuilder(
            template='global_esg_template',
            style=ReportStyle.credible()
        )
        return builder.compile(
            analysis,
            format=format,
            translation=lang
        )
# reporting/global_reports.py
def generate_refinitiv_table(report: RefinitivESGScores) -> Table:
    """Rich table for detailed Refinitiv scores"""
    table = Table(title="Refinitiv ESG Breakdown", show_header=True)
    table.add_column("Category", style="cyan")
    table.add_column("Score", justify="right")
    
    table.add_row("Overall ESG Score", f"{report.esg_score:.1f}")
    table.add_row("Environmental Pillar", f"{report.environmental_pillar:.1f}")
    table.add_row("  Resource Use", f"{report.resource_use or 0:.1f}")
    table.add_row("  Emissions", f"{report.emissions or 0:.1f}")
    table.add_row("  Innovation", f"{report.innovation or 0:.1f}")
    # Repeat for other pillars
    
    return table