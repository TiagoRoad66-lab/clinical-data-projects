# 6-Month Roadmap – Clinical Data Manager
## Checklist + Milestones + Progress Tracking

**Start Date:** October 24, 2025  
**Target Role:** Clinical Data Manager/Engineer  
**Time Commitment:** 7-10 hours/week, long sessions  
**Current Status:** Week 1 Complete + Bonus Major Project

---

## 🎯 PROGRESS OVERVIEW

### ✅ Completed (October 24-27, 2025)
- **Initial Setup** - All infrastructure installed and configured
- **Git/GitHub** - Repository created, linked, first commits
- **LeetCode SQL** - 7/50 exercises completed
- **🌟 BONUS: Clinical Data Pipeline** - Complete multi-site trial simulator (15-20 hours)

### 🔄 In Progress
- **LeetCode SQL** - Targeting 25/50 by end of Week 2
- **SQL Advanced Concepts** - CTEs, Window Functions

### 📅 Upcoming
- Mock CRF Validator SQL project
- Python pipeline development
- Data Quality scorecard
- Governance documentation

---

## INITIAL SETUP (WEEK 0) - ✅ COMPLETED

### Infrastructure
- [x] Install PostgreSQL (Windows: postgresql.org/download/windows)
- [x] Install DBeaver Community (dbeaver.io)
- [x] Install VSCode (code.visualstudio.com)
- [x] Install Anaconda / Python 3.11+ (anaconda.com)
- [x] Install Git (git-scm.com)
- [x] Verify in terminal/cmd: `python --version`, `psql --version`, `git --version`

### Git Account & Repository
- [x] Create GitHub account
- [x] Create repository "clinical-data-projects" (public, MIT license)
- [x] Clone locally: `git clone <url>`
- [x] Create folder structure:
  ```
  clinical-data-projects/
  ├── README.md
  ├── LEARNING_LOG.md
  ├── data_manager_roadmap.md
  ├── sql-validator/
  ├── python-pipeline/
  ├── data-quality-scorecard/
  └── governance/
  ```
- [x] First commit: `git add . && git commit -m "Initial setup"`

### Learning Platforms
- [x] Sign up for Kaggle (kaggle.com) – free
- [x] Sign up for LeetCode (leetcode.com) – free tier sufficient
- [x] Bookmark Mode Analytics SQL Tutorial (mode.com/sql-tutorial)
- [x] Read/print this complete plan

### Calendar
- [x] Block 3 fixed time slots per week (e.g.: Mon 8pm, Wed 9pm, Sat 9am)
- [x] Add to calendar: "LEARNING TIME – do not disturb"

---

## 🌟 BONUS PROJECT COMPLETED (October 2025)

### Clinical Data Pipeline - Multi-Site Trial Simulator
**Status:** ✅ COMPLETE  
**Repository:** [clinical-data-pipeline](https://github.com/TiagoRoad66-lab/clinical-data-pipeline)  
**Time Invested:** 15-20 hours

**What Was Built:**
- Multi-site clinical trial data generator (120 subjects, 3 US sites)
- Realistic CRF data across 5 domains (Screening, Demographics, Dosing, Vital Signs, Completion)
- Automated data quality management with query generation
- Power BI dashboards for site monitoring
- Complete documentation (README, Technical Design Doc, Interview Guide)

**Technical Implementation:**
- Python (Faker, Pandas, SQLite)
- PostgreSQL database (6 normalized tables)
- Power BI visualizations
- Git version control

**Skills Demonstrated:**
- Python data generation and ETL pipelines
- Relational database design
- Clinical trial workflow understanding (GCP principles)
- Multi-site data management
- Data quality and query management
- Power BI dashboard creation

**Key Features:**
- Staggered site activation dates
- Proper Day of Study calculation (First dose = Day 0)
- Realistic data quality issues (missing values, out-of-range, inconsistencies)
- Query tracking system (Critical/High/Medium priority)
- Cross-site performance monitoring

**Deliverables:**
- [x] Complete Python pipeline code
- [x] PostgreSQL database with 6 tables
- [x] Power BI dashboard
- [x] Comprehensive README
- [x] Technical Design Document
- [x] Interview Preparation Guide
- [x] Project Layout Diagram

---

## MONTHS 1-2: ADVANCED SQL

### Week 1-2: SQL Foundations - ✅ PARTIALLY COMPLETE

**Concepts to Learn:**
- [x] Basic SQL (SELECT, WHERE, ORDER BY, JOINs) - **Completed via LeetCode**
- [ ] CTEs (Common Table Expressions) – theory
- [ ] Window Functions (ROW_NUMBER, RANK, LAG, LEAD, SUM OVER)
- [ ] Subqueries vs JOINs – comparison
- [ ] Basic optimization (indexes, EXPLAIN PLAN)
**Resources:**
- [x] LeetCode SQL 50 - First 7 exercises completed
- [ ] Mode Analytics: CTE section (read + all exercises) → 2-3h
- [ ] Mode Analytics: Window Functions section (read + all exercises) → 3-4h
- [ ] Real Python: "SQL Window Functions" (if clarification needed)

**Exercises:**
- [x] LeetCode Database: 7/50 exercises completed (Basic SELECT, WHERE, JOIN)
- [ ] LeetCode exercises 8-20 (focus on CTEs + Window Functions)
- [ ] Additional 5 Medium exercises with Window Functions

**Project Weeks 1-2: Mock Clinical Data Quality Report (SQL)**

*Deliverable:* `sql-validator/01_mock_crf_validator.sql`

Setup:
- [ ] Download Kaggle dataset: "Diabetes" or "Heart Disease" (or create mock)
- [ ] Import into PostgreSQL via DBeaver
- [ ] Examine structure (tables, columns)

Queries to write (approximately one per day):
- [ ] Q1: Patients with missing data by variable (COUNT NULL)
- [ ] Q2: Potential duplicates (ROW_NUMBER PARTITION BY)
- [ ] Q3: Out-of-range values (CASE WHEN, percentiles)
- [ ] Q4: Temporal gaps between visits (LAG, DATEDIFF)
- [ ] Q5: Inconsistent temporal evolution (LAG + CASE)
- [ ] Q6: Final summary (CTE + JOIN)

Documentation:
- [ ] Comment each query (logic + clinical use case)
- [ ] Create file "QUERY_EXPLANATIONS.md" explaining each validation
- [ ] Export results to CSV

GitHub:
- [ ] Commit with message: `feat: SQL validator – mock clinical data`

**🎯 Current Progress:**
- ✅ 7/50 LeetCode exercises (Basic SQL)
- ✅ Repository structure created
- 🔄 Targeting 25/50 by end of Week 2

---

### Week 3-4: SQL + Clinical Reality

**Concepts:**
- [ ] Typical clinical schemas (patients, visits, labs, adverse events, concomitant meds)
- [ ] CDISC standards (basics) – review structure
- [ ] Thinking in data models vs thinking in spreadsheets

**Resources:**
- [ ] CDISC (cdisc.org): browse "Standards Overview" → 30 min
- [ ] Kaggle: find multi-table dataset (e.g., "Clinical Trial Simulation")
- [ ] "SQL for Data Scientists" Ch. 2-3 (if purchased) → 2h

**Exercises:**
- [ ] LeetCode: 10 additional exercises (Medium-Hard)
- [ ] Reflect: "How would I join these tables to detect inconsistencies?"

**Project Weeks 3-4: Multi-CRF ETL Simulator (SQL)**

*Deliverable:* `sql-validator/02_multi_crf_etl.sql`

Setup:
- [ ] Create 3-4 CSV files simulating different CRFs (Demographics, Labs, Visits, Adverse Events)
- [ ] Import into PostgreSQL

Queries to write:
- [ ] Schema: create standardized tables (CDISC-like)
- [ ] Transform: reconcile formats between CRFs
- [ ] Validate: flag inconsistencies
- [ ] Q1: Join demographics + labs, verify date consistency
- [ ] Q2: Visits aligned with labs (timing check)
- [ ] Q3: Flag patients with adverse events but no follow-up visit
- [ ] Q4: Standardize units (e.g., mg → μg conversion)
- [ ] Q5: Create final "CLEAN" table + audit trail

Documentation:
- [ ] File "ETL_LOGIC.md": schema, transformations, validations
- [ ] Simple diagram (ASCII art acceptable): CRF Input → Validate → Clean Output

GitHub:
- [ ] Commit: `feat: multi-CRF ETL validator – clinical workflow`

---

### Checkpoint End of Month 2
- [ ] ✅ 20 LeetCode exercises completed (CTE + Window Functions)
- [ ] ✅ 2 SQL projects in GitHub
- [ ] ✅ Can explain: "What's a CTE? Window function? Why useful for data quality?"
- [ ] ✅ GitHub repo in good state (README filled, folders organized)

**Interview-style check:**
- [ ] Write on paper: "Write SQL query finding patients with out-of-range labs and no follow-up visit"
- [ ] Explain: "How would you optimize this query?" (talk about indexes, EXPLAIN PLAN)

---

## MONTH 3: PYTHON PIPELINES

### Week 5-6: Python Pandas + File Handling

**Concepts:**
- [ ] Pandas as ETL tool (not just data exploration)
- [ ] Reading/writing Excel, CSV, Parquet
- [ ] Data cleaning, merging, grouping
- [ ] Memory efficiency, chunking
- [ ] Functional programming (apply, pipe, map)

**Resources:**
- [ ] "Pandas for Everyone" Ch. 4-8 (if purchased) → 5-6h reading + practice
- [ ] Real Python: "Pandas Tutorial" (filtered) → 2-3h
- [ ] Official docs: focus on `merge()`, `groupby()`, `apply()`, `pipe()` → 1h reference

**Python Environment Setup:**
- [ ] Create folder `python-pipeline/`
- [ ] `python -m venv venv` (create virtual environment)
- [ ] Activate venv (`.venv\Scripts\activate` on Windows)
- [ ] `pip install pandas openpyxl sqlalchemy psycopg2`
- [ ] Create `requirements.txt`: `pip freeze > requirements.txt`

**Exercises:**
- [ ] Jupyter notebook: 5 Pandas exercises (reading, merging, cleaning)
  - [ ] Ex1: Read multiple CSVs, concatenate
  - [ ] Ex2: Merge on keys, handle duplicates
  - [ ] Ex3: Groupby with aggregation
  - [ ] Ex4: Apply custom function
  - [ ] Ex5: Pipe chaining (functional style)

**Project Weeks 5-6: Clinical Data Validator (Python)**

*Deliverable:* `python-pipeline/validator.py` + example notebooks

Setup:
- [ ] Download 2-3 Excel files (Kaggle dataset or mock CRFs)
- [ ] Create Jupyter notebook "01_exploration.ipynb": explore data

Build:
- [ ] Create module `src/validator.py` with functions:
  ```python
  def load_crf(filepath): ...
  def check_missing_data(df): ...
  def check_duplicates(df): ...
  def check_value_ranges(df, rules_dict): ...
  def merge_crfs(df_list): ...
  def generate_report(validation_results): ...
  ```
- [ ] Write in Jupyter: chain functions, explore outputs
- [ ] Create config file `config/validation_rules.yaml`:
  ```yaml
  age:
    min: 0
    max: 150
  lab_glucose:
    min: 50
    max: 500
  ```
- [ ] Load config in Python, use in validation

Documentation:
- [ ] Docstrings in functions (Google style)
- [ ] Commented Jupyter notebook

GitHub:
- [ ] Commit: `feat: Python Pandas validator – refactored from SQL`
- [ ] Push Jupyter + validator.py + config

---

### Week 7-8: Production-ready + Logging + CLI

**Concepts:**
- [ ] Scripts ≠ Notebooks (professional code structure)
- [ ] Logging (DEBUG, INFO, WARNING, ERROR)
- [ ] Configuration management (externalize hardcoded values)
- [ ] CLI tools (Click library)
- [ ] Error handling, exceptions

**Resources:**
- [ ] Real Python: "Logging in Python" → 1.5h
- [ ] Real Python: "Click Tutorial" → 1.5h
- [ ] Official docs: logging module → reference

**Setup:**
- [ ] Organize structure:
  ```
  python-pipeline/
  ├── src/
  │   ├── __init__.py
  │   ├── validator.py (main logic)
  │   ├── logger.py (logging setup)
  │   └── config.py (load YAML)
  ├── config/
  │   └── validation_rules.yaml
  ├── main.py (CLI entry point)
  ├── requirements.txt
  ├── README.md
  └── tests/ (optional but recommended)
  ```

**Exercises:**
- [ ] Add logging to validator.py (info at each step)
- [ ] Create logger.py that sets up logging (file + console)
- [ ] Test: run script, verify `.log` file created

**Project Weeks 7-8: Production-Ready Validator**

*Deliverable:* `python-pipeline/main.py` with CLI

Build:
- [ ] Refactor validator.py into "clean code"
  - [ ] Type hints: `def load_crf(filepath: str) -> pd.DataFrame:`
  - [ ] Complete docstrings
  - [ ] Error handling: try/except
- [ ] Create `logger.py`:
  ```python
  import logging
  def setup_logger(name, log_file='validator.log'):
      logger = logging.getLogger(name)
      handler = logging.FileHandler(log_file)
      formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
      handler.setFormatter(formatter)
      logger.addHandler(handler)
      return logger
  ```
- [ ] Create `main.py` with Click CLI:
  ```python
  import click
  @click.command()
  @click.option('--input', type=click.Path(exists=True), help='Input data folder')
  @click.option('--config', type=click.Path(exists=True), help='YAML validation rules file')
  @click.option('--output', type=click.Path(), help='Output report path')
  def validate(input, config, output):
      """Run clinical data validator"""
      # Your logic here
      click.echo(f"Validation complete. Report: {output}")
  
  if __name__ == '__main__':
      validate()
  ```
- [ ] Test CLI: `python main.py --input ./data --config ./config/rules.yaml --output ./report.xlsx`
- [ ] Generate Excel report (use openpyxl or xlsxwriter)

Documentation:
- [ ] README:
  ```markdown
  # Clinical Data Validator
  Automated validation of clinical trial CRF data.
  
  ## Usage
  python main.py --input <folder> --config <yaml> --output <report>
  
  ## Setup
  pip install -r requirements.txt
  ```
- [ ] Create example config + example data so someone else can use it

GitHub:
- [ ] Commit: `refactor: production-ready validator – logging, CLI, type hints`
- [ ] Tag: `v1.0`

---

### Checkpoint End of Month 3
- [ ] ✅ Pandas functions: read, merge, groupby, apply, pipe
- [ ] ✅ Logging setup in place, .log file created
- [ ] ✅ CLI tool works: `python main.py --help` displays usage
- [ ] ✅ Clean code: type hints, docstrings, error handling
- [ ] ✅ GitHub: 2-3 commits, organized repository

**Interview-style check:**
- [ ] "Why use Pandas rather than SQL for this?"
- [ ] "Show me your logging code – how would you handle an error?"
- [ ] "How would you structure this code for someone else?"

---

## MONTH 4: DATA QUALITY + LEAN SIX SIGMA

### Week 9-10: Data Quality Frameworks

**Concepts:**
- [ ] Quality dimensions (Accuracy, Completeness, Consistency, Timeliness, Validity)
- [ ] Validation vs Monitoring
- [ ] Quality metrics and dashboards
- [ ] Root Cause Analysis (RCA)
- [ ] RACI matrix (data ownership)

**Resources:**
- [ ] "The Fundamentals of Data Quality" by David Loshin → 4-5h (if purchased)
- [ ] Or: Coursera "Data Governance & Quality" 1-2 courses → 6-8h
- [ ] DAMA DMBOK "Data Quality" section (partially free) → 2h reference

**Concept Practice:**
- [ ] Create document: "5 Quality Dimensions – Examples"
  - [ ] Accuracy: what does it mean in clinical context?
  - [ ] Completeness: % data available, by variable
  - [ ] Consistency: no contradictions across tables
  - [ ] Timeliness: data available when needed
  - [ ] Validity: conforms to format/range
  - [ ] For each: 1-2 clinical examples + how to measure

**Project Weeks 9-10: Data Quality Scorecard**

*Deliverable:* `data-quality-scorecard/scorecard.py` + Power BI dashboard

Build:
- [ ] Download clinical dataset (Kaggle)
- [ ] Python script `scorecard.py` that calculates:
  ```python
  def calculate_completeness(df): return 100 - (df.isnull().sum() / len(df) * 100)
  def calculate_consistency(df): # check contradictions
  def calculate_timeliness(df): # time since last update
  def calculate_validity(df, rules): # % records meeting validation rules
  def generate_scorecard(df, rules): # combined metrics
  ```
- [ ] Output: CSV with scores per dimension + overall DQ score
- [ ] Example: "Completeness: 95%, Validity: 87%, Overall: 91%"

Power BI:
- [ ] Import CSV output
- [ ] Create simple dashboard:
  - [ ] Card visual: Overall DQ Score
  - [ ] Gauge: per dimension (Completeness, Validity, etc.)
  - [ ] Table: metrics by variable
  - [ ] Trend over time (if applicable)
- [ ] Screenshot + save .pbix file

GitHub:
- [ ] Push `scorecard.py` + example CSV output
- [ ] Document: "DATA_QUALITY_FRAMEWORK.md"
  ```markdown
  # Data Quality Scorecard
  
  ## Dimensions Measured
  - Completeness: % non-null values
  - Validity: % records meeting range rules
  - ...
  
  ## Usage
  python scorecard.py --input data.csv --rules config.yaml
  ```

---

### Week 11-12: Lean Six Sigma + RCA

**Concepts:**
- [ ] DMAIC cycle (Define, Measure, Analyze, Improve, Control)
- [ ] Root Cause Analysis (5 Whys, Fishbone diagram)
- [ ] Process thinking
- [ ] Metrics + targets

**Resources:**
- [ ] LinkedIn Learning: "Lean Six Sigma Fundamentals" → 2h
- [ ] YouTube: "DMAIC Explained" videos → 1h
- [ ] Medium: articles on data quality RCA → 1h

**Case Study Document:**

*Deliverable:* `governance/RCA_CASE_STUDY.md`

Scenario (fictional or reality-inspired):
"Study X: 15% of baseline visit records have missing lab values. This delays interim analysis."

Document (2-3 pages):
- [ ] **Define:** Problem statement + impact
- [ ] **Measure:** Quantify issue (15% missing, by site, by lab type, trend)
- [ ] **Analyze:** Root causes
  - [ ] 5 Whys analysis (ask "why?" 5 times)
  - [ ] Fishbone diagram (causes: People, Process, Data, System)
  - [ ] Example findings: "Site A has 30% missing, others 10% → training issue?"
- [ ] **Improve:** Proposed solutions
  - [ ] Enhanced validation at data entry
  - [ ] Site training on SOP
  - [ ] System automation (your validator!)
- [ ] **Control:** Ensure stays fixed
  - [ ] Monitor % missing labs weekly
  - [ ] Alert if >10% for any site
  - [ ] Quarterly SOP review

Presentation:
- [ ] Include simple diagrams (ASCII art OK, or Markdown tables)
- [ ] Professional format (good grammar, structure)

GitHub:
- [ ] Push RCA_CASE_STUDY.md
- [ ] Commit: `docs: Lean Six Sigma RCA case study`

---

### Checkpoint End of Month 4
- [ ] ✅ Quality dimensions: explain 5 dimensions with examples
- [ ] ✅ Pandas scorecard script: works, outputs metrics
- [ ] ✅ Power BI dashboard: visualizes quality scores
- [ ] ✅ RCA document: complete, structured, professional
- [ ] ✅ GitHub: organized, clear documentation

**Interview-style check:**
- [ ] "Explain 5 quality dimensions – which most important in clinical trials?"
- [ ] "You see 20% missing lab data – walk me through RCA approach"
- [ ] "How would you monitor that quality stays good?"

---

## MONTH 5: DATA GOVERNANCE + PORTFOLIO

### Week 13-14: Data Governance Basics

**Concepts:**
- [ ] Data ownership, stewardship, custodianship
- [ ] Metadata and data catalog
- [ ] Access control and privacy (GDPR basics)
- [ ] Documentation standards and SOPs
- [ ] Compliance (21 CFR Part 11 for clinical context)

**Resources:**
- [ ] Gartner "Data Governance Essentials" (free articles) → 1.5h
- [ ] DAMA DMBOK "Metadata Management" section → 1.5h
- [ ] Udemy "Data Governance Fundamentals" (~$15 on sale) → 2-3h

**Document:**

*Deliverable:* `governance/DATA_GOVERNANCE_CHARTER.md`

Template (3-5 pages):
```markdown
# Data Governance Charter – Clinical Trial XYZ

## 1. Overview
- Purpose of data governance for this study
- Scope (which data, which systems)

## 2. Roles & Responsibilities
| Role | Responsibility |
|------|---|
| Data Steward | Owns data quality, SOP |
| DPO | Privacy, compliance |
| Data Manager (you) | Infrastructure, pipelines |
| Site Coordinator | Data entry accuracy |

## 3. Data Quality Standards
- Completeness: >95% required
- Timeliness: data within 48h of visit
- Validation: per attached rules

## 4. Metadata Requirements
- Variable definitions (CRF + DB)
- Calculation logic (if derived)
- Units, ranges
- Change log

## 5. Access Control
- Who can access what data
- Data classification (public, confidential, restricted)
- Audit trail requirements

## 6. Documentation & SOP
- How data enters system
- How it's validated
- How issues are escalated
- How it's archived

## 7. Compliance
- 21 CFR Part 11 (electronic records)
- GDPR (if EU data)
- Audit requirements
```

GitHub:
- [ ] Push DATA_GOVERNANCE_CHARTER.md
- [ ] Commit: `docs: data governance charter template`

---

### Week 15-16: Consolidation + Capstone + Portfolio

**Portfolio Consolidation:**
- [ ] Review all work (SQL, Python, Quality, Governance)
- [ ] Clean up and improve all READMEs
- [ ] Verify: all commits are good, clear messages
- [ ] Organize GitHub repo:
  ```
  clinical-data-projects/
  ├── README.md (main overview)
  ├── PORTFOLIO.md (links to projects)
  ├── sql-validator/
  │   ├── README.md
  │   └── *.sql
  ├── python-pipeline/
  │   ├── README.md
  │   ├── main.py
  │   └── requirements.txt
  ├── data-quality-scorecard/
  │   ├── README.md
  │   └── scorecard.py
  └── governance/
      ├── README.md
      ├── DATA_GOVERNANCE_CHARTER.md
      └── RCA_CASE_STUDY.md
  ```

**Capstone Project (8-10h):**

*Deliverable:* `CAPSTONE_PROJECT.md` (folder or main README)

Concept: Integrated Clinical Data Solution
- Combine ALL skills: SQL + Python + Quality + Governance
- Imagine scenario: "You're data manager for new study"
- Deliverables:
  1. [ ] **Data Model** (SQL schema)
  2. [ ] **Validator** (Python pipeline)
  3. [ ] **Quality Metrics** (Power BI dashboard)
  4. [ ] **Governance Doc** (roles, SOP)
  5. [ ] **Process Flow** (diagram: data in → validate → clean → analyze)

Document structure:
```markdown
# Clinical Data Management Solution – Capstone

## 1. Context & Objectives
- Study overview (fictitious)
- Data quality challenges
- Solution approach

## 2. Technical Architecture
- Data flow diagram
- Tools & tech stack
- Key validations

## 3. Implementation
- Step 1: Design (schema, rules)
- Step 2: Build (SQL + Python)
- Step 3: Monitor (Power BI, logging)
- Step 4: Govern (roles, SOP)

## 4. Results & Metrics
- Example outputs (screenshots)
- Performance (time to validate 10K records?)
- Quality improvements

## 5. Lessons Learned & Next Steps
- What worked
- What to improve
- Scaling considerations
```

Push everything:
- [ ] Commit: `feat: capstone project – integrated clinical data solution`
- [ ] Create release: `git tag -a v1.0-capstone -m "Final portfolio"`

**GitHub Pages (optional but impressive):**
- [ ] Enable GitHub Pages for your repo
- [ ] Create simple `index.html` or use README as homepage
- [ ] Share portfolio URL: `https://github.com/yourusername/clinical-data-projects`

---

### Checkpoint End of Month 5
- [ ] ✅ GitHub repo: professional, well-documented, 5+ projects
- [ ] ✅ Capstone: complete, integrated
- [ ] ✅ Can talk about: entire approach, trade-offs, lessons learned

**Final Check Before Interviews:**
- [ ] ✅ Review all your code (clean? readable? commented?)
- [ ] ✅ Test your validator on new data (works?)
- [ ] ✅ Prepare "story": "Why data manager? Why I want this?"
- [ ] ✅ Count: "In 6 months, I built X, learned Y, ready for Z"

---

## MONTH 6: FLEX / INTERVIEWS / NEXT STEPS

### Week 17-20: Interview Prep + Depth

**If Technical Interview Coming:**
- [ ] Review: SQL window functions (write live query)
- [ ] Review: Python basics + your code
- [ ] Review: data quality concepts
- [ ] Practice: "Walk me through your validator"

**If Internal Role (interviews):**
- [ ] Prepare: "Why I want data manager role? What value add?"
- [ ] Prepare: "My 12 years clinical + new technical skills = ?"
- [ ] Prepare: live demo (if possible) of one of your tools

**Learning Buffer:**
- [ ] Pick 1-2 areas where you felt weak, deepen
- [ ] Examples:
  - [ ] Orchestration (Airflow – advanced SQL/Python)
  - [ ] Advanced stats (if going data scientist route)
  - [ ] AWS certifications (if going cloud engineer)

### Week 21-24: Transition
- [ ] Decide: which role/company to pursue?
- [ ] Keep repo updated (shows active learning)
- [ ] Network: reach out to pharma data professionals
- [ ] Negotiate: salary, location, progression

---

## QUICK REFERENCE – WHAT TO DO EACH WEEK

| Week | Focus | Time | Project | Deliverable |
|------|-------|------|---------|-------------|
| 0 | Setup | 4-5h | Infrastructure | All tools installed ✅ |
| 1 | SQL basics + **BONUS Project** | 15-20h | LeetCode + Clinical Pipeline | 7/50 exercises + Complete simulator ✅ |
| 2 | SQL basics (CTEs, Window Fn) | 6-8h | Continue LeetCode | 25/50 target |
| 3-4 | SQL advanced (multi-table ETL) | 6-8h | Multi-CRF ETL | SQL script |
| 5-6 | Python Pandas | 6-8h | Python validator | .py file |
| 7-8 | Python production (logging, CLI) | 6-8h | CLI tool | main.py |
| 9-10 | Data Quality frameworks | 6-8h | Scorecard | Python + Power BI |
| 11-12 | Lean Six Sigma + RCA | 4-6h | Case study | MD document |
| 13-14 | Data Governance | 4-6h | Charter | MD document |
| 15-16 | Consolidation + Capstone | 8-10h | Capstone | Complete project |
| 17-24 | Flex / Interviews | 5-10h | As needed | Offers? |

---

## TRACKING & ACCOUNTABILITY

**Weekly Check (5 min):**
- [ ] How many hours did I do? (target: 7-10)
- [ ] Which project did I advance?
- [ ] Did I commit to GitHub?
- [ ] What blocked me?

**Monthly Check (30 min):**
- [ ] Did I complete month's projects?
- [ ] Code quality good?
- [ ] GitHub repo organized?
- [ ] Can I explain what I learned?

**Red Flags (stop & adjust):**
- ⚠️ Skipped 2+ weeks → re-commit or reduce hours
- ⚠️ Code is messy → stop, refactor
- ⚠️ Don't understand concept → go back, re-read, ask online
- ⚠️ Bored → switch topics, variation is OK

---

## SUCCESS CRITERIA – END OF 6 MONTHS

✅ **Technical:**
- [ ] Write complex SQL queries (CTE, window functions, optimization)
- [ ] Build Python pipeline (clean code, logging, CLI)
- [ ] Understand data quality frameworks
- [ ] Apply Lean Six Sigma thinking
- [ ] Document governance & compliance

✅ **Portfolio:**
- [ ] 5+ GitHub projects, well-documented
- [ ] README, docstrings, type hints (professional code)
- [ ] Power BI dashboard example
- [ ] Capstone project (integrated)

✅ **Interview Ready:**
- [ ] Technical questions: can answer + explain thinking
- [ ] Show code: walk through, discuss trade-offs
- [ ] Domain knowledge: clinical + data = combined strength
- [ ] Story: clear narrative on why this role, why you're ready

✅ **Jobs:**
- [ ] Internal role: selected + promoted
- [ ] External roles: can apply confidently

---

## FINAL NOTES

1. **This is a guide, not a prison.** If you want to skip ahead, deep-dive one