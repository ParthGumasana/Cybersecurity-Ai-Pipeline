import subprocess
from utils.logging_config import logger

def run_nmap_scan(target):
    logger.info(f"Starting Nmap scan on {target}...")
    try:
        result = subprocess.run(
            ["nmap", "-sV", target], capture_output=True, text=True, check=True
        )
        logger.info(f"Nmap scan completed: {result.stdout}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        logger.error(f"Nmap scan failed: {e.stderr}")
        return None
