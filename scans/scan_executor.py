from scans.nmap_scan import run_nmap_scan
from scans.gobuster_scan import run_gobuster_scan
from utils.logging_config import logger

def execute_task(task):
    logger.debug(f"Processing task: {task}")
    target = task["target"]
    
    if task["task"] == "nmap_scan":
        return run_nmap_scan(target)
    elif task["task"] == "gobuster_scan":
        return run_gobuster_scan(target)
    else:
        logger.warning(f"Unknown task: {task['task']}")
        return None
