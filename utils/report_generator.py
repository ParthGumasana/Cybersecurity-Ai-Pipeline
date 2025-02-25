from fpdf import FPDF
from utils.logging_config import logger

def generate_pdf_report(scan_results, output_file="results/scan_results.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, "Cybersecurity Scan Report", ln=True, align="C")
    pdf.ln(10)
    
    for task, result in scan_results.items():
        pdf.multi_cell(0, 10, f"{task.upper()} RESULT:\n{result}\n")
        pdf.ln(5)

    pdf.output(output_file)
    logger.info(f"PDF report generated at {output_file}")
