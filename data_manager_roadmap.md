# Roadmap 6 mois – Clinical Data Manager
## Checklist + Milestones + Tracking

---

## SETUP INITIAL (À FAIRE CETTE SEMAINE)

### Infrastructure
- [ ] Installer PostgreSQL (Windows : postgresql.org/download/windows)
- [ ] Installer DBeaver Community (dbeaver.io)
- [ ] Installer VSCode (code.visualstudio.com)
- [ ] Installer Anaconda / Python 3.11+ (anaconda.com)
- [ ] Installer Git (git-scm.com)
- [ ] Vérifier : `python --version`, `psql --version`, `git --version` (terminal/cmd)

### Compte & Repo
- [ ] Créer GitHub account (si pas déjà)
- [ ] Créer repo "clinical-data-projects" (public, MIT license)
- [ ] Clone localement : `git clone <url>`
- [ ] Créer structure folders :
  ```
  clinical-data-projects/
  ├── README.md
  ├── sql-validator/
  ├── python-pipeline/
  ├── data-quality-scorecard/
  └── governance/
  ```
- [ ] Premier commit : `git add . && git commit -m "Initial setup"`

### Learning
- [ ] S'inscrire Kaggle (kaggle.com) – gratuit
- [ ] S'inscrire LeetCode (leetcode.com) – gratuit suffit
- [ ] Mode Analytics SQL Tutorial (mode.com/sql-tutorial) – bookmark
- [ ] Lire/imprimer ce plan complet

### Calendrier
- [ ] Bloquer 3 créneaux/semaine (ex: lun 20h, mer 21h, sam 9h)
- [ ] Ajouter dans calendrier : "LEARNING TIME – do not disturb"

---

## MOIS 1-2 : SQL AVANCÉ
### Objectif : Maîtriser CTE, Window Functions, ETL thinking

#### Semaine 1-2 : Fondations SQL Avancé
**Concepts à apprendre :**
- [ ] CTEs (Common Table Expressions) – theory
- [ ] Window Functions – theory (ROW_NUMBER, RANK, LAG, LEAD, SUM OVER)
- [ ] Subqueries vs JOINs – theory
- [ ] EXPLAIN PLAN / Optimisation basique

**Ressources :**
- [ ] Mode Analytics : CTE section (read + all exercises) → 2-3h
- [ ] Mode Analytics : Window Functions section (read + all exercises) → 3-4h
- [ ] Real Python : "SQL Window Functions" (if needed clarification)

**Exercices :**
- [ ] LeetCode Database : 10 exercises (difficulty: Medium) → CTEs + Window Functions
  - [ ] Exercise 1 : CTE basics
  - [ ] Exercise 2-3 : Window functions ROW_NUMBER
  - [ ] Exercise 4-5 : LAG/LEAD
  - [ ] Exercise 6-10 : Mixed

**Projet Semaine 1-2 : Mock Clinical Data Quality Report (SQL)**

*Deliverable:* `sql-validator/01_mock_crf_validator.sql`

Setup:
- [ ] Télécharger dataset Kaggle : "Diabetes" ou "Heart Disease" ou créer mock
- [ ] Importer dans PostgreSQL via DBeaver
- [ ] Examiner structure (tables, colonnes)

Requêtes à écrire (1 par jour environ) :
- [ ] Q1 : Patients avec données manquantes par variable (COUNT NULL)
- [ ] Q2 : Doublons potentiels (ROW_NUMBER PARTITION BY)
- [ ] Q3 : Valeurs aberrantes (CASE WHEN, percentiles)
- [ ] Q4 : Gaps temporels entre visites (LAG, DATEDIFF)
- [ ] Q5 : Évolution temporelle incohérente (LAG + CASE)
- [ ] Q6 : Résumé final (CTE + JOIN)

Documentation:
- [ ] Commenter chaque requête (logique + cas d'usage)
- [ ] Créer fichier "QUERIES_EXPLANATION.md" → explique chaque validation
- [ ] Export results → CSV

GitHub:
- [ ] Commit avec message : `feat: SQL validator – mock clinical data`

---

#### Semaine 3-4 : SQL + Clinical Thinking
**Concepts :**
- [ ] Schémas cliniques (patients, visits, labs, adverse_events, concomeds)
- [ ] CDISC standards (basics) – parcourir structure
- [ ] Data model thinking vs spreadsheet thinking

**Ressources :**
- [ ] CDISC (cdisc.org) : parcourir "Standards Overview" → 30min
- [ ] Kaggle : trouver dataset avec >2 tables (ex: "Clinical Trial Simulation")
- [ ] "SQL for Data Scientists" Ch. 2-3 (if you bought it) → 2h

**Exercices :**
- [ ] LeetCode : 10 exercises supplémentaires (Medium-Hard)
- [ ] Réfléchir : "Comment j'joindrais ces tables pour voir inconsistances?"

**Projet Semaine 3-4 : ETL Multi-CRF Simulator (SQL)**

*Deliverable:* `sql-validator/02_multi_crf_etl.sql`

Setup:
- [ ] Créer 3-4 fichiers CSV simulant CRFs différents (Demography, Labs, Visits, AEs)
- [ ] Importer dans PostgreSQL

Requêtes à écrire :
- [ ] Schema : créer tables standardisées (CDISC-like)
- [ ] Transform : réconcilier format entre CRFs
- [ ] Validate : flags pour inconsistances
- [ ] Q1 : Joindre demography + labs, checker dates cohérentes
- [ ] Q2 : Visits alignées avec labs (timing check)
- [ ] Q3 : Flaguer patients avec AEs mais pas visitées
- [ ] Q4 : Standardiser units (mg → μg conversion example)
- [ ] Q5 : Créer table "CLEAN" final + audit trail

Documentation:
- [ ] Fichier "ETL_LOGIC.md" : schema, transformations, validations
- [ ] Diagram simple (dessin ASCII ok) : CRF Input → Validate → Clean Output

GitHub:
- [ ] Commit : `feat: ETL multi-CRF validator – clinical workflow`

---

#### Checkpoint Fin Mois 2
- [ ] ✅ 20 LeetCode exercices complétés (CTE + Window Functions)
- [ ] ✅ 2 projets SQL dans GitHub
- [ ] ✅ Pouvez expliquer : "CTE c'est quoi? Window function? Pourquoi c'est utile pour data quality?"
- [ ] ✅ GitHub repo en bon état (README rempli, dossiers organisés)

**Entretien-style check :**
- [ ] Draw on paper : "Écris requête SQL qui trouve patients avec labs hors range et aucune visite suivi"
- [ ] Explique : "Comment optimiseriez cette requête?" (parlez index, EXPLAIN PLAN)

---

## MOIS 3 : PYTHON PIPELINES
### Objectif : Automatiser validations, penser "reproductibilité"

#### Semaine 5-6 : Python Pandas + File Handling
**Concepts :**
- [ ] Pandas as ETL tool (not just EDA)
- [ ] Reading/writing Excel, CSV, Parquet
- [ ] Data cleaning, merging, groupby
- [ ] Memory efficiency, chunking
- [ ] Functional programming (apply, pipe, map)

**Ressources :**
- [ ] "Pandas for Everyone" Ch. 4-8 (if bought) → 5-6h read + practice
- [ ] Real Python : "Pandas Tutorial" (filtré) → 2-3h
- [ ] Official docs : focus `merge()`, `groupby()`, `apply()`, `pipe()` → 1h reference

**Setup Python Environment :**
- [ ] Créer folder `python-pipeline/`
- [ ] `python -m venv venv` (create virtual environment)
- [ ] Activate venv (`.venv\Scripts\activate` on Windows)
- [ ] `pip install pandas openpyxl sqlalchemy psycopg2`
- [ ] Créer `requirements.txt` : `pip freeze > requirements.txt`

**Exercices :**
- [ ] Jupyter notebook : 5 exercices Pandas (reading, merging, cleaning)
  - [ ] Ex1 : Read multiple CSVs, concat
  - [ ] Ex2 : Merge on keys, handle duplicates
  - [ ] Ex3 : Groupby + aggregation
  - [ ] Ex4 : Apply custom function
  - [ ] Ex5 : Pipe chaining (functional style)

**Projet Semaine 5-6 : Clinical Data Validator (Python)**

*Deliverable:* `python-pipeline/validator.py` + example notebooks

Setup:
- [ ] Télécharger 2-3 Excel files (Kaggle dataset ou mock CRFs)
- [ ] Créer Jupyter notebook "01_exploration.ipynb" : explore data

Build:
- [ ] Créer module `src/validator.py` avec functions:
  ```python
  def load_crf(filepath): ...
  def check_missing_data(df): ...
  def check_duplicates(df): ...
  def check_value_ranges(df, rules_dict): ...
  def merge_crfs(df_list): ...
  def generate_report(validation_results): ...
  ```
- [ ] Écrire dans Jupyter : enchaîner functions, explorer outputs
- [ ] Créer config file `config/validation_rules.yaml` :
  ```yaml
  age:
    min: 0
    max: 150
  lab_glucose:
    min: 50
    max: 500
  ```
- [ ] Load config en Python, utiliser dans validation

Documentation:
- [ ] Docstrings dans functions (Google style)
- [ ] Jupyter notebook commenté

GitHub:
- [ ] Commit : `feat: Python Pandas validator – refactored from SQL`
- [ ] Push Jupyter + validator.py + config

---

#### Semaine 7-8 : Production-Ready + Logging + CLI
**Concepts :**
- [ ] Scripts != Notebooks (structure proper code)
- [ ] Logging (DEBUG, INFO, WARNING, ERROR)
- [ ] Configuration management (externaliser hardcoded values)
- [ ] CLI tools (Click library)
- [ ] Error handling, exceptions

**Ressources :**
- [ ] Real Python : "Logging in Python" → 1.5h
- [ ] Real Python : "Click Tutorial" → 1.5h
- [ ] Official docs : logging module → reference

**Setup :**
- [ ] Organiser structure :
  ```
  python-pipeline/
  ├── src/
  │   ├── __init__.py
  │   ├── validator.py (core logic)
  │   ├── logger.py (logging setup)
  │   └── config.py (load YAML)
  ├── config/
  │   └── validation_rules.yaml
  ├── main.py (CLI entry point)
  ├── requirements.txt
  ├── README.md
  └── tests/ (optional but good)
  ```

**Exercices :**
- [ ] Ajouter logging à validator.py (info au chaque step)
- [ ] Créer logger.py qui setup logging (file + console)
- [ ] Tester : run script, regardez fichier `.log` créé

**Projet Semaine 7-8 : Production-Ready Validator**

*Deliverable:* `python-pipeline/main.py` avec CLI

Build:
- [ ] Refactor validator.py en "clean code"
  - [ ] Type hints : `def load_crf(filepath: str) -> pd.DataFrame:`
  - [ ] Docstrings complets
  - [ ] Error handling : try/except
- [ ] Créer `logger.py` :
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
- [ ] Créer `main.py` avec Click CLI :
  ```python
  import click
  @click.command()
  @click.option('--input', type=click.Path(exists=True), help='Input data folder')
  @click.option('--config', type=click.Path(exists=True), help='Validation rules YAML')
  @click.option('--output', type=click.Path(), help='Output report path')
  def validate(input, config, output):
      """Run clinical data validator"""
      # Your logic here
      click.echo(f"Validation complete. Report: {output}")
  
  if __name__ == '__main__':
      validate()
  ```
- [ ] Test CLI : `python main.py --input ./data --config ./config/rules.yaml --output ./report.xlsx`
- [ ] Générer Excel report (usar openpyxl ou xlsxwriter)

Documentation:
- [ ] README :
  ```markdown
  # Clinical Data Validator
  Automated validation of clinical trial CRF data.
  
  ## Usage
  python main.py --input <folder> --config <yaml> --output <report>
  
  ## Setup
  pip install -r requirements.txt
  ```
- [ ] Créer example config + example data pour quelqu'un d'autre puisse utiliser

GitHub:
- [ ] Commit : `refactor: production-ready validator – logging, CLI, type hints`
- [ ] Tag : `v1.0`

---

#### Checkpoint Fin Mois 3
- [ ] ✅ Pandas functions : read, merge, groupby, apply, pipe
- [ ] ✅ Logging setup + fichier .log créé
- [ ] ✅ CLI tool fonctionne : `python main.py --help` affiche usage
- [ ] ✅ Code clean : type hints, docstrings, error handling
- [ ] ✅ GitHub : 2-3 commits, repo organisé

**Entretien-style check :**
- [ ] "Pourquoi tu utilises Pandas plutôt que SQL pour ça?"
- [ ] "Show me your logger code – comment tu gérerais erreur?"
- [ ] "Comment tu structurerais ce code pour quelqu'un d'autre?"

---

## MOIS 4 : DATA QUALITY + LEAN SIX SIGMA
### Objectif : Domain expertise "data manager" + thinking process

#### Semaine 9-10 : Data Quality Frameworks
**Concepts :**
- [ ] Dimensions data quality (Accuracy, Completeness, Consistency, Timeliness, Validity)
- [ ] Validation vs Monitoring
- [ ] Data quality metrics, scorecards
- [ ] Root Cause Analysis (RCA)
- [ ] RACI matrix (data ownership)

**Ressources :**
- [ ] "The Fundamentals of Data Quality" by David Loshin → 4-5h (if bought)
- [ ] Ou : Coursera "Data Governance & Quality" 1-2 cours → 6-8h (if doing)
- [ ] DAMA DMBOK "Data Quality" section (gratuit partiellement) → 2h reference

**Concepts Practice :**
- [ ] Créer document : "5 Dimensions of DQ – Examples"
  - [ ] Accuracy : what does it mean in clinical context?
  - [ ] Completeness : % data available, by variable
  - [ ] Consistency : no contradictions across tables
  - [ ] Timeliness : data available when needed
  - [ ] Validity : conforms to format/range
  - [ ] Pour chaque : 1-2 examples cliniques + how to measure

**Projet Semaine 9-10 : Data Quality Scorecard**

*Deliverable:* `data-quality-scorecard/scorecard.py` + Power BI dashboard

Build:
- [ ] Télécharger clinical dataset (Kaggle)
- [ ] Python script `scorecard.py` qui calcule :
  ```python
  def calculate_completeness(df): return 100 - (df.isnull().sum() / len(df) * 100)
  def calculate_consistency(df): # check for contradictions
  def calculate_timeliness(df): # time since last update
  def calculate_validity(df, rules): # % records meeting validation rules
  def generate_scorecard(df, rules): # combined metrics
  ```
- [ ] Output : CSV avec scores par dimension + overall DQ score
- [ ] Example : "Completeness: 95%, Validity: 87%, Overall: 91%"

Power BI:
- [ ] Import CSV output
- [ ] Créer dashboard simple :
  - [ ] Card visual : Overall DQ Score
  - [ ] Gauge : per dimension (Completeness, Validity, etc.)
  - [ ] Table : metrics by variable
  - [ ] Trend over time (if applicable)
- [ ] Screenshot + save .pbix file

GitHub:
- [ ] Push `scorecard.py` + example output CSV
- [ ] Document : "DATA_QUALITY_FRAMEWORK.md"
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

#### Semaine 11-12 : Lean Six Sigma + RCA
**Concepts :**
- [ ] DMAIC cycle (Define, Measure, Analyze, Improve, Control)
- [ ] Root Cause Analysis (5 Whys, Fishbone)
- [ ] Process thinking
- [ ] Metrics + targets

**Ressources :**
- [ ] LinkedIn Learning : "Lean Six Sigma Fundamentals" → 2h
- [ ] YouTube : "DMAIC Explained" videos → 1h
- [ ] Medium : articles on data quality RCA → 1h

**Case Study Document :**

*Deliverable:* `governance/RCA_CASE_STUDY.md`

Scenario (fictif ou inspiré réel) :
"Study X : 15% of baseline visit records have missing lab values. This delays interim analysis."

Document (2-3 pages) :
- [ ] **Define :** Problem statement + impact
- [ ] **Measure :** Quantify issue (15% missing, by site, by lab type, trend)
- [ ] **Analyze :** Root causes
  - [ ] 5 Whys analysis (ask "why?" 5 times)
  - [ ] Fishbone diagram (causes : People, Process, Data, System)
  - [ ] Example findings : "Site A has 30% missing, others 10% → training issue?"
- [ ] **Improve :** Proposed solutions
  - [ ] Enhanced validation at data entry
  - [ ] Site training on SOP
  - [ ] System automation (your validator!)
- [ ] **Control :** How to ensure stays fixed
  - [ ] Monitor weekly % missing labs
  - [ ] Alert if >10% for any site
  - [ ] Quarterly SOP review

Presentation:
- [ ] Include simple diagrams (ASCII art OK, or Markdown tables)
- [ ] Make it "presentable" (good grammar, structure)

GitHub:
- [ ] Push RCA_CASE_STUDY.md
- [ ] Commit : `docs: Lean Six Sigma RCA case study`

---

#### Checkpoint Fin Mois 4
- [ ] ✅ Data Quality dimensions : can explain 5 dimensions with examples
- [ ] ✅ Scorecard Python script : works, outputs metrics
- [ ] ✅ Power BI dashboard : visualizes DQ scores
- [ ] ✅ RCA case study : complete, structured, presentable
- [ ] ✅ GitHub : organized, good documentation

**Entretien-style check :**
- [ ] "Explain 5 dimensions of data quality – which is most important in clinical trials?"
- [ ] "You see 20% missing data in lab values – walk me through RCA approach"
- [ ] "How would you monitor that data quality stays good?"

---

## MOIS 5 : DATA GOVERNANCE + PORTFOLIO
### Objectif : "Manager" skills + final polish

#### Semaine 13-14 : Data Governance Basics
**Concepts :**
- [ ] Data ownership, stewardship, custodianship
- [ ] Metadata, data catalog
- [ ] Access control, privacy (GDPR basics)
- [ ] Documentation standards, SOPs
- [ ] Compliance (21 CFR Part 11 for clinical context)

**Ressources :**
- [ ] Gartner "Data Governance Essentials" (free articles) → 1.5h
- [ ] DAMA DMBOK "Metadata Management" section → 1.5h
- [ ] Udemy "Data Governance Fundamentals" ($15 on sale) → 2-3h

**Document :**

*Deliverable:* `governance/DATA_GOVERNANCE_CHARTER.md`

Template (3-5 pages) :
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
- Completeness : >95% required
- Timeliness : data within 48h of visit
- Validation : per attached rules

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
- [ ] Commit : `docs: Data Governance Charter template`

---

#### Semaine 15-16 : Consolidation + Capstone + Portfolio
**Portfolio Building :**
- [ ] Review tout votre travail (SQL, Python, Quality, Governance)
- [ ] Nettoyer, améliorer READMEs
- [ ] Vérifier : tous les commits sont bons, messages clairs
- [ ] Organiser GitHub repo :
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

**Capstone Project (8-10h) :**

*Deliverable:* `CAPSTONE_PROJECT.md` (folder ou README principal)

Concept : Integrated Clinical Data Solution
- Combine ALL skills : SQL + Python + Quality + Governance
- Imagine scenario : "You're data manager for new study"
- Deliverables :
  1. [ ] **Data Model** (schema SQL)
  2. [ ] **Validator** (Python pipeline)
  3. [ ] **Quality Metrics** (Power BI dashboard)
  4. [ ] **Governance Doc** (roles, SOP)
  5. [ ] **Process Flow** (diagram : data in → validate → clean → analyze)

Document structure :
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
- Step 1 : Design (schema, rules)
- Step 2 : Build (SQL + Python)
- Step 3 : Monitor (Power BI, logging)
- Step 4 : Govern (roles, SOP)

## 4. Results & Metrics
- Example outputs (screenshots)
- Performance (time to validate 10K records?)
- Quality improvements

## 5. Lessons Learned & Next Steps
- What worked
- What to improve
- Scaling considerations
```

Push all:
- [ ] Commit : `feat: Capstone project – integrated clinical data solution`
- [ ] Create release : `git tag -a v1.0-capstone -m "Final portfolio"`

**GitHub Pages (Optional but impressive):**
- [ ] Enable GitHub Pages for your repo
- [ ] Create simple `index.html` or use README as homepage
- [ ] Share portfolio URL : `https://github.com/yourusername/clinical-data-projects`

---

#### Checkpoint Fin Mois 5
- [ ] ✅ GitHub repo : professional, well-documented, 5+ projects
- [ ] ✅ Capstone : complete, integrated
- [ ] ✅ Can talk about : your entire approach, trade-offs, lessons learned

**Final Check Before Interviews :**
- [ ] ✅ Révisez tout votre code (clean? readable? commented?)
- [ ] ✅ Testez votre validator sur données nouvelles (fonctionne?)
- [ ] ✅ Préparez "story" : "Why data manager? Why I want this?"
- [ ] ✅ Comptez : "In 6 months, I built X, learned Y, ready for Z"

---

## MOIS 6 : FLEX / INTERVIEWS / NEXT STEPS

### Semaine 17-20 : Interview Prep + Depth
**If ICON calls (technical interview) :**
- [ ] Revisit : SQL window functions (write live query)
- [ ] Revisit : Python basics + your code
- [ ] Revisit : Data quality concepts
- [ ] Practice : "Walk me through your validator"

**If Internal Role (interviews) :**
- [ ] Prepare : "Why I want data manager role? What value add?"
- [ ] Prepare : "My 12 years clinical + new technical skills = ?"
- [ ] Prepare : Live demo (if possible) of one of your tools

**Learning Buffer :**
- [ ] Pick 1-2 areas where you felt weak, deepen
- [ ] Examples :
  - [ ] Airflow/orchestration (advanced SQL/Python)
  - [ ] Advanced stats (if going data scientist route)
  - [ ] AWS certifications (if going cloud engineer)

### Semaine 21-24 : Transition
- [ ] Decide : which role/company to pursue?
- [ ] Keep repo updated (shows active learning)
- [ ] Network : reach out to ICON alumni, pharma data folks
- [ ] Negotiate : salary, location, progression

---

## QUICK REFERENCE – WHAT TO DO EACH WEEK

| Week | Focus | Time | Project | Deliverable |
|------|-------|------|---------|-------------|
| 1-2 | SQL basics (CTEs, Window Fn) | 6-8h | Mock validator | SQL script |
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

✅ **Technical :**
- [ ] Write complex SQL queries (CTE, window functions, optimization)
- [ ] Build Python pipeline (clean code, logging, CLI)
- [ ] Understand data quality frameworks
- [ ] Apply Lean Six Sigma thinking
- [ ] Document governance & compliance

✅ **Portfolio :**
- [ ] 5+ GitHub projects, well-documented
- [ ] README, docstrings, type hints (professional code)
- [ ] Power BI dashboard example
- [ ] Capstone project (integrated)

✅ **Interview Ready :**
- [ ] Technical questions : can answer + explain thinking
- [ ] Show code : walk through, discuss trade-offs
- [ ] Domain knowledge : clinical + data = combined strength
- [ ] Story : clear narrative on why this role, why you're ready

✅ **Jobs :**
- [ ] ICON interview : pass technical round, get offer
- [ ] Internal role : selected + promoted
- [ ] External roles : can apply confidently (if ICON doesn't work out)

---

## NOTES FINALES

1. **This is a guide, not a prison.** If you want to skip ahead, deep-dive one area, or pivot – do it. The spirit is "concept + project" not "follow steps exactly."

2. **Stuck?** 
   - Stack Overflow for coding problems
   - r/datascience, r/SQL for concepts
   - YouTube tutorials for specific concepts (5-10 min clips OK)
   - Just don't fall into tutorial hell again

3. **Family first.** 7-10h/week is enough. Don't sacrifice family time. Better to be consistent 6h/week than start with 10h/week and burn out.

4. **Celebrate wins.** When you finish each project, even small – commit, push, note it. Momentum matters.

5. **Show your work.** GitHub public + portfolio = your best marketing. Especially for ICON or external roles.

---

**You got this. 6 months, consistent effort, and you're ready. Let's go! 🚀**
