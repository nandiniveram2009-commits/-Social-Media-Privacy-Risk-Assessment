
#Social Media Privacy Risk Assessment Framework (SM-PRAF)


## Overview 

The Social Media Privacy Risk Assessment Framework (SM-PRAF) is an enterprise-grade, defensive cybersecurity and privacy engineering platform designed to evaluate social-media exposure, account-security practices, social-engineering risk, digital-footprint vulnerability, and personalized privacy improvements. Built with modern web technologies and a rigorous backend engine, SM-PRAF empowers individuals, students, and organizations to quantify and mitigate online exposure risks safely.
## Problem statement 

Modern internet users routinely suffer from unmanaged digital exposure, accidental Personally Identifiable Information (PII) leakage, and weak account authentication configurations. Without structured risk audits, individuals remain highly vulnerable to OSINT (Open Source Intelligence) data harvesting, social engineering attacks, account takeovers, and identity theft. Traditional platforms lack transparent, self-assessment tooling that educates users without violating privacy boundaries.
##  Objectives 

Provide a structured self-assessment questionnaire spanning 10 critical security and privacy categories.

Quantify privacy posture into a transparent, weighted 

risk score (0–100) with standardized risk tiers.
Generate automated, actionable, and prioritized remediation recommendations.

Offer an interactive simulation engine to preview risk reduction prior to modifying live settings.

Demonstrate robust Privacy-by-Design and data-minimized software architecture.
## Cybersecurity Relevance 

•SM-PRAF bridges the gap between technical security controls and human-centric privacy awareness. It mirrors daily workflows executed by GRC (Governance, Risk, and Compliance) Analysts, Privacy Engineers, SOC Analysts, and Security Consultants, translating behavioral configurations into quantifiable risk metrics and auditable remediation roadmaps.
## Previcy vs security 

Privacy governs who has access to data and how it is collected, shared, exposed, and used.

Security protects systems, accounts, and information from unauthorized access or misuse.

Key Distinction: An account secured with a 64-character password and hardware MFA possesses high security, but if the profile is set to public and exposes a home address and phone number, it has low privacy. Strong account security does not equal strong privacy.
## Feature 

Comprehensive Questionnaire: 40+ structured questions evaluating 10 distinct privacy and security vectors.

Weighted Scoring Engine: Quantifies risk from 0 (Low Exposure) to 100 (Critical Exposure).

Findings & Recommendation Engine: Instantly maps exposure vectors to prioritized remediation steps (Immediate, Important, Good Practice).

Improvement Simulator: Allows users to preview score reductions based on hypothetical hardening actions.

Executive Dashboard: Visualizes risk distribution, category averages, and operational telemetry using Chart.js.

Printable Privacy Checklist: Provides a tangible hardening checklist for users.

Privacy-by-Design Storage: Strictly enforces zero PII retention in backend databases
## Architecture 

[[ Frontend (HTML5, Tailwind CSS, Chart.js) ]
                     │
                     ▼ (HTTP / REST API via FastAPI)
[ Backend Engine (FastAPI, Python 3.10+) ]
  ├── Scoring & Feature Extraction Services
  ├── Recommendation & Findings Engine
  └── Improvement Simulation Service
                     │
                     ▼
[ SQLite Database (Anonymized Audit Logs & Telemetry) ]
## Technology stack

-Frontend: HTML5, CSS3, JavaScript (ES6+), Tailwind CSS, Chart.js

-Backend: Python, FastAPI, Uvicorn, Pydantic
Database: SQLite (anonymized storage, zero PII footprint)

-Testing: Pytest
Data Analysis: Pandas
## Previcy Questionnaire 

The framework evaluates user posture across 10 categories, asking whether specific sensitive attributes (phone numbers, full birthdays, real-time locations) are publicly exposed rather than collecting the sensitive data itself.
## Risk Categories 

Profile Visibility (Public indexing, search discoverability)

Personal Information (Phone, email, birthday, workplace exposure)

Location Privacy (Real-time check-ins, travel itineraries, geotagging)

Posts & Content (Historical footprints, public archives)

Connections (Unknown follower acceptance, network size)

Tagging (Involuntary tagging permissions, mention controls)

Account Security (MFA usage, password reuse, login alerts)

Third-Party Apps (Stale OAuth integrations, overly 
permissive access)

Social Engineering (Suspicious link awareness, DM vetting)

Digital Footprint (Dormant accounts, indexed public comments)
Risk
## Risk scoring 

Overall risk is calculated using weighted category aggregations normalized to a 0–100 scale:

0–20: LOW (Robust privacy posture)
21–40: MODERATE (Minor exposure vulnerabilities)
41–70: HIGH (Significant attack surface)
71–100: CRITICAL (Immediate risk of exploitation or compromise)
## Previcy findings 

The application analyzes questionnaire payloads to automatically surface explicit configuration weaknesses, such as exposed phone numbers, disabled MFA, or active real-time location broadcasting, tagging each with severity levels (Low, Moderate, High, Critical).
## Recommendation engine 

Remediation actions are categorized into three priority tiers:

IMMEDIATE: Critical vulnerabilities requiring urgent attention (e.g., enabling MFA, hiding public phone numbers).

IMPORTANT: High-priority hardening steps (e.g., restricting connection requests, enabling tag review).

GOOD PRACTICE: Hygiene improvements (e.g., auditing third-party apps, reviewing old posts)
## Improvement simulator 

The Privacy Improvement Simulator enables users to select hypothetical security changes (e.g., "Enable MFA", "Make Profile Private") and instantly calculate projected risk score reductions and new risk tiers.
## Digital footprint 

The framework evaluates both active footprints (deliberately shared content) and passive footprint risks (indexed comments, unreviewed historical posts, and stale third-party app integrations), encouraging periodic privacy audits.
## Social engineering awarness 

SM-PRAF includes dedicated educational modules explaining how attackers aggregate public data points (employers, travel plans, family references) to construct highly convincing spear-phishing pretexts, bypass knowledge-based authentication, and execute social engineering attacks.
## Account security

The application explicitly separates privacy from security while emphasizing their intersection. It evaluates multi-factor authentication (MFA) adoption, password reuse indicators, login alert configurations, and active session hygiene.
## previcy dashboard 

The interactive executive dashboard provides real-time metrics including total assessments conducted, average risk scores across synthetic datasets, risk level distribution donut charts, and category exposure radar charts.
## Previcy report 
Users can generate and export a structured, anonymized assessment report containing their overall risk score, category breakdowns, detected findings, and prioritized action plans in HTML or printable format.
## Previcy by design 

SM-PRAF is engineered around core privacy principles:
Data Minimization: No PII (phone numbers, home addresses, real names) is ever stored in the database.
Purpose Limitation: Data is used exclusively for risk calculation and educational feedback.
Privacy by Default: Zero tracking or active profiling of real individuals.
## Usage
# Start backend API server
uvicorn backend.app:app --reload --host 127.0.0.1 --port 8000

# Start frontend static server (in a separate terminal)
python -m http.server 3000 --directory frontend

# Access application at http://localhost:3000/assessment.html

 

## Testing 

Automated unit and integration tests are executed using pytest:
## Security & previcy testing 

Schema Audits: Verified complete absence of PII storage columns in SQLite.

Input Validation: Validated via Pydantic type checking.

CORS & Headers: Enforced secure cross-origin resource sharing policies.
## Results 

Execution of the framework against synthetic test profiles demonstrates accurate risk stratification, effective score reduction via the improvement simulator, and robust analytical reporting.
## Limitations 

Evaluations rely on self-reported user posture rather than direct API inspection.

Risk weights represent educational assumptions and should be customized for enterprise threat landscapes.


## Future improvement 

Integration with custom enterprise policy frameworks (e.g., ISO 27701, NIST Privacy Framework).

Exportable PDF reporting via ReportLab.

Advanced OSINT threat emulation guides.

## Learning outcomes 

Mastery of privacy-by-design and data minimization engineering.
Proficiency in designing scoring algorithms and heuristic risk engines.
Full-stack development experience utilizing FastAPI, Tailwind CSS, and Chart.js.

## Risk scoring 

Overall risk is calculated using weighted category aggregations normalized to a 0–100 scale:

0–20: LOW (Robust privacy posture)
21–40: MODERATE (Minor exposure vulnerabilities)
41–70: HIGH (Significant attack surface)
71–100: CRITICAL (Immediate risk of exploitation or compromise)

#API Documentation

The FastAPI backend automatically generates interactive API documentation via Swagger UI. Once the backend is running, navigate to:
http://localhost:8000/docs

## Limitations 

Evaluations rely on self-reported user posture rather than direct API inspection.

Risk weights represent educational assumptions and should be customized for enterprise threat landscapes.
## Disclaimer 

This project is designed for defensive cybersecurity and privacy education. It uses synthetic or voluntarily provided assessment responses and does not scrape, track, or profile real social-media users.
## Author

* **GitHub:** [nandiniveram2009](https://github.com)
* **LinkedIn:** [Nandini Verma](https://linkedin.com)
