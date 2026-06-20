from agents.threat_agent import detect_threats
from agents.vulnerability_agent import assess_vulnerabilities
from agents.advisor_agent import generate_recommendations
from agents.report_agent import generate_pdf


def run_cybershield(log_data):

    threats = detect_threats(log_data)

    vulnerabilities = assess_vulnerabilities(
        threats
    )

    recommendations = generate_recommendations(
        vulnerabilities
    )

    pdf = generate_pdf(
        threats,
        vulnerabilities,
        recommendations
    )

    return {
        "threats": threats,
        "vulnerabilities": vulnerabilities,
        "recommendations": recommendations,
        "pdf": pdf
    }