import subprocess
from utils.logging_config import logger

def run_gobuster_scan(target):
    logger.info(f"Starting Gobuster scan on {target}...")
    try:
        result = subprocess.run(
            ["gobuster", "dir", "-u", f"http://{target}", "-w", "/home/hulk/cybersecurity-ai-pipeline/common.txt"],
            capture_output=True, text=True, check=True
        )
        logger.info(f"Gobuster scan completed: {result.stdout}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        logger.error(f"Gobuster scan failed: {e.stderr}")
        return None
