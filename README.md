# **Agentic Cybersecurity Pipeline 🔐🚀**  
An AI-powered, automated **cybersecurity scanning pipeline** using **LangGraph, LangChain, Nmap, and Gobuster**, ensuring **efficient and controlled security assessments**.

---

## **📌 Features**  
✅ **Automated Task Breakdown:** Uses LangGraph to dynamically execute security scans.  
✅ **Multi-Tool Scanning:** Integrates **Nmap & Gobuster** for network and directory enumeration.  
✅ **Scope Enforcement:** Prevents unauthorized scans and limits actions to defined targets.  
✅ **Failure Handling & Logging:** Ensures smooth execution and maintains logs for analysis.  
✅ **PDF Report Generation:** Automatically generates **security reports** after scans.  

---

## **📂 Project Structure**  
```plaintext
📂 cybersecurity-ai-pipeline
│── 📂 results                # Stores scan results & logs
│── 📂 utils                  # Helper modules (scope enforcement, logging, reporting)
│── ├── __init__.py
│── ├── logging_config.py     # Logging setup
│── ├── report_generator.py   # Generate PDF reports
│── ├── scope_checker.py      # Prevents out-of-scope actions
│── 📂 scans                  # Modules for cybersecurity scans
│── ├── __init__.py
│── ├── nmap_scan.py          # Nmap scanning logic
│── ├── gobuster_scan.py      # Gobuster scanning logic
│── ├── scan_executor.py      # Handles task execution
│── main.py                   # Entry point (LangGraph pipeline)
│── requirements.txt           # Dependencies
│── README.md                  # Project documentation
│── demo.mp4                   # Project demonstration video
