Agentic Cybersecurity Pipeline 🔐🚀
An AI-powered, automated cybersecurity scanning pipeline using LangGraph, LangChain, Nmap, and Gobuster, ensuring efficient and controlled security assessments.

📌 Features
✅ Automated Task Breakdown: Uses LangGraph to dynamically execute security scans.
✅ Multi-Tool Scanning: Integrates Nmap & Gobuster for network and directory enumeration.
✅ Scope Enforcement: Prevents unauthorized scans and limits actions to defined targets.
✅ Failure Handling & Logging: Ensures smooth execution and maintains logs for analysis.
✅ PDF Report Generation: Automatically generates security reports after scans.

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

🚀 Installation & Setup

Step 1: Clone the Repository
git clone https://github.com/ParthGumasana/Agentic-Cybersecurity.git
cd Agentic-Cybersecurity

Step 2: Set Up a Virtual Environment
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

Step 3: Install Dependencies
pip install -r requirements.txt        #Note Gobuster is not a python package so you need to install it seperately

Step 4: Run the Pipeline
python3 main.py --target example.com    #Replace example.com with your actual target

🛠️ Technologies Used
LangGraph & LangChain → AI-driven task execution
Nmap → Network scanning
Gobuster → Directory enumeration
Python (FPDF) → Report generation
Logging & Error Handling → Ensures stability

📑 Example Output
Once executed, the tool will:

Perform Nmap scanning to find open ports.
Execute Gobuster to discover hidden directories.
Save results in the results/ folder.
Generate a PDF report summarizing the findings.

📬 Contact
For any questions or suggestions, connect with me on:
📧 Email: parthgumasana@gmail.com
🔗 GitHub: ParthGumasana
