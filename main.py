import langgraph
from scans.scan_executor import execute_task
from utils.scope_checker import is_within_scope
from utils.report_generator import generate_pdf_report
from utils.logging_config import logger
from langgraph.graph import Graph

def cybersecurity_pipeline(task_list):
    logger.info("Starting AI cybersecurity pipeline...")
    workflow = Graph()
    valid_tasks = [task for task in task_list if is_within_scope(task["target"])]
    if not valid_tasks:
        logger.error("No valid tasks within scope. Aborting execution.")
        return None

    scan_results = {}
    for task in valid_tasks:
        result = execute_task(task)
        scan_results[task["task"]] = result

    generate_pdf_report(scan_results)

    logger.info("Cybersecurity scan completed. Report generated.")
    return scan_results

if __name__ == "__main__":
    tasks = [
        {"task": "nmap_scan", "target": "google.com"},
        {"task": "gobuster_scan", "target": "google.com"},
    ]
    cybersecurity_pipeline(tasks)
