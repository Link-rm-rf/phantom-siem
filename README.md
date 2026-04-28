# Phantom-SIEM

A custom, lightweight SIEM (Security Information and Event Management) tool I built to ingest logs, detect threats, and visualize network traffic in real time 

I built this full-stack project to demonstrate how a Security Operations Center (SOC) processes and flags malicious traffic under the hood

## What it does
* **Live Log Ingestion:** Parses incoming web request logs instantly
* **Threat Detection:** Uses a custom Regex engine to catch SQL Injections, XSS, and Path Traversal attacks before they hit the database
* **SOC Dashboard:** A dark-themed, live-updating frontend that visualizes the threat feed
* **Attack Simulation:** Includes a custom Python botnet script that fires randomized clean and malicious traffic to stress-test the engine

## How it's built
* **Backend:** FastAPI (Python), Uvicorn
* **Database:** SQLite managed with SQLAlchemy ORM
* **Frontend:** Next.js (React), Tailwind CSS
* **Detection:** Custom Python threat modeling engine

## How to Run it
You need three terminal tabs to run the full stack:

1. **Backend:** `cd backend && uvicorn main:app --reload`
2. **Frontend:** `cd frontend && npm run dev`
3. **Attack Simulator:** `python attack_sim.py`
