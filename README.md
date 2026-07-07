# 🏥 AI-Powered Remote Patient Monitoring (RPM) System

An intelligent, real-time patient monitoring platform powered by IBM Granite AI,
built as an academic demonstration project exploring agentic AI in healthcare.

> ⚠️ **Academic/Demonstration Project**: Performance benchmarks represent design 
> targets validated in a simulated environment. Device integrations use mock data 
> streams. Not intended for clinical deployment.

---

## 🌟 Overview

A healthcare monitoring prototype that combines simulated wearable device data, 
AI-powered health analysis, and automated emergency response logic to explore 
24/7 patient monitoring at scale.

### The Problem This Addresses
- **Delayed interventions**: Traditional monitoring misses early deterioration signals
- **Alert fatigue**: Too many false positives overwhelm healthcare providers
- **Emergency response lag**: Critical minutes lost between detection and dispatch

### What This Project Demonstrates
- A working tri-agent AI architecture using IBM Granite and RAG
- Real-time WebSocket data streaming with sub-second latency (tested locally)
- HIPAA-aligned security design: RBAC, AES-256 encryption, audit logging
- Automated risk scoring with configurable emergency alert thresholds

---

## 🤖 AI Architecture — Three Agents

| Agent | Role |
|---|---|
| **Agent 1 — Analyst** | Ingests vital signs, detects trends and anomalies |
| **Agent 2 — Detective** | RAG-powered risk scoring (0–10) against medical guidelines |
| **Agent 3 — Guardian** | Triggers alerts and simulated emergency dispatch when score ≥ 9.0 |

Built with IBM Granite 13B Chat via LangFlow orchestration.

---

## ✨ Key Features

### Real-Time Data Pipeline
- Simulated IoT vitals streamed via WebSocket (<100ms local latency)
- IBM Cloud Object Storage with automatic partitioning
- Designed to mirror Apple Watch, Fitbit, and medical-grade sensor formats

### Emergency Response Logic
- Automated alert trigger when risk score ≥ 9.0
- Simulated ambulance dispatch with paramedic instruction generation
- Multi-stakeholder notifications: doctor, nurse, family, patient

### Security & HIPAA-Aligned Design
- AES-256 encryption at rest, TLS 1.3 in transit
- Role-based access control (Patient / Family / Nurse / Doctor)
- Full audit logging of all PHI access events
- Multi-factor authentication

### Dashboard
- Real-time vitals display with trend visualisation
- Colour-coded risk severity indicators
- Mobile-responsive React frontend


## 🏗️ System Architecture
[Simulated IoT Devices]
      ↓ WebSocket (TLS 1.3)
[Data Streaming Layer — Validation → Encryption → Load Balancer]
      ↓
[IBM Cloud Storage — PostgreSQL | Cloudant | ChromaDB]
      ↓
[AI Layer — Agent 1 → Agent 2 (RAG) → Agent 3]
      ↓
[Application Layer — FastAPI | React | Auth | WebSocket Hub]
      ↓
[Notification Layer — Simulated SMS/Email/Push/EMS Dispatch]

Target end-to-end latency: < 2 seconds (design target, tested locally)



## 🛠️ Tech Stack

**Backend**: Python 3.11, FastAPI, LangFlow, IBM Granite 13B, ChromaDB  
**Frontend**: React 18, TypeScript, Tailwind CSS, Recharts  
**Databases**: PostgreSQL, IBM Cloudant, IBM Cloud Object Storage  
**Infrastructure**: IBM Cloud, Docker, GitHub Actions  
**Security**: AES-256, TLS 1.3, RBAC, JWT Auth  


## 🚀 Getting Started


git clone https://github.com/GavinJ25/[repo-name]
cd rpm-system
cp .env.example .env  # Add your IBM Cloud credentials
pip install -r requirements.txt
uvicorn main:app --reload


## 📁 Project Structure
rpm-system/
├── agents/          # LangFlow agent definitions
├── api/             # FastAPI routes and middleware
├── frontend/        # React application
├── models/          # Data models and schemas
├── security/        # RBAC and encryption logic
├── tests/           # Unit and integration tests
└── docs/            # Architecture diagrams


## 🎓 Academic Context

Built as a personal project exploring agentic AI in healthcare infrastructure.  
Part of B.E. Computer Science portfolio — BMS College of Engineering, Bangalore.



## 📄 License

MIT License — free to use, modify, and build upon with attribution.
