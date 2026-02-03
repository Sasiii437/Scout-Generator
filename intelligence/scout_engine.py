from intelligence.rules import evaluate_series
from models.scout_report import ScoutReport

def generate_scout_report(series_list):
    reports = []

    for series in series_list:
        score, reasons = evaluate_series(series)
        report = ScoutReport(series, score, reasons)
        reports.append(report)

    return reports
