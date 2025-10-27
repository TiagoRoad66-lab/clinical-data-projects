# Learning Log – Clinical Data Projects

## ✅ Major Completed Project (October 2025)

### Clinical Data Pipeline - Multi-Site Trial Simulator
**Repository:** [clinical-data-pipeline](https://github.com/TiagoRoad66-lab/clinical-data-pipeline)

**What I built:**
- Complete end-to-end clinical data management system simulation
- Multi-site trial data generator (120 subjects across 3 US sites)
- Automated data quality management with query generation
- Power BI dashboards for site performance monitoring

**Technical implementation:**
- **Data Generation:** Python Faker library for realistic CRF data (Screening, Demographics, Dosing, Vital Signs, Completion)
- **Data Quality:** Introduced realistic data issues (missing values, out-of-range, inconsistencies)
- **Query Management:** Automated query generation following GCP principles (NO auto-correction, requires site resolution)
- **Database:** PostgreSQL with 6 normalized tables
- **Visualization:** Power BI dashboards with site-level metrics

**Key features:**
- Staggered site activation (US01: Jan 1, US02: Jan 15, US03: Feb 1)
- Proper Day of Study calculation (First dose = Day 0)
- Multi-site enrollment distribution (40%, 35%, 25%)
- Cross-site data quality monitoring
- Query tracking with priority levels (Critical/High/Medium)

**Skills demonstrated:**
- Python data generation and ETL
- Relational database design
- Clinical trial workflow understanding
- Data quality management principles
- Power BI dashboard creation
- Git version control

**Time invested:** ~15-20 hours over 1 week

**Documentation:**
- Complete README with project overview
- Technical Design Document (production implementation considerations)
- Interview Preparation Guide
- Project Layout Diagram

**Challenges overcome:**
- Understanding proper Day of Study calculation methodology
- Implementing realistic multi-site variations
- Designing query management system following GCP (no auto-correction)
- Creating normalized database schema
- Building meaningful Power BI visualizations

---

## Week 1 : SQL Basics - LeetCode SQL 50 (October 24-27, 2025)

### Exercices LeetCode SQL 50
- ✅ 7/50 exercices complétés ([SQL 50 Study Plan](https://leetcode.com/studyplan/top-sql-50/))
- Repo solutions : [SQL-50-leetcode](https://github.com/TiagoRoad66-lab/SQL-50-leetcode)
- Concepts maîtrisés : SELECT, WHERE, ORDER BY, basic JOINs
- En cours : poursuivre jusqu'à exercice 20-25
- Prochains concepts : CTEs, Window Functions (dans exercices avancés)

### Progression
- Date début : 24 Oct 2025
- Temps investi : ~2h
- Rythme cible : 7-10h/semaine

### Blocages rencontrés
(Rien pour le moment)

### Notes personnelles
Premier jour d'apprentissage autonome sur LeetCode. Les exercices basiques vont bien, j'avance progressivement. En parallèle, j'ai développé le Clinical Data Pipeline project qui applique ces concepts SQL dans un contexte réel.

---

## Week 2 : SQL Avancé (CTEs + Window Functions) (October 28 - November 3, 2025)

### Objectifs apprentissage
- [ ] CTEs (Common Table Expressions) – structurer requêtes avec WITH
- [ ] Window Functions – ROW_NUMBER(), RANK(), LAG(), LEAD()
- [ ] Différence JOIN vs Subqueries
- [ ] EXPLAIN PLAN – optimisation basique

### Ressources utilisées
- LeetCode SQL 50 (exercices 20-35)
- Mode Analytics SQL Tutorial (si besoin clarification)

### Exercices planifiés
- [ ] LeetCode exercices 8-25 (focus CTEs + Window Functions)
- [ ] Projet "Mock CRF Validator" en SQL (fin semaine 2)

### Prochaines étapes
- Finir 25 premiers exercices SQL 50
- Télécharger dataset Kaggle clinique
- Créer 6 requêtes validation dans `sql-validator/`

---

## Portfolio Overview

### Completed Work
1. ✅ Clinical Data Pipeline (Multi-site trial simulator) - October 2025
2. ✅ Git setup and repository structure
3. ✅ LeetCode SQL 50: 7/50 exercises

### In Progress
1. 🔄 LeetCode SQL 50: targeting 25/50 by end of Week 2
2. 🔄 SQL Advanced concepts (CTEs, Window Functions)

### Upcoming
1. Mock CRF Validator SQL project
2. Python pipeline development
3. Data Quality scorecard with Power BI

---

## Skills Tracking

### Technical Skills Acquired
- ✅ Python data generation (Faker library)
- ✅ Pandas data manipulation
- ✅ PostgreSQL database design
- ✅ Power BI dashboard creation
- ✅ Git version control
- ✅ SQL basics (SELECT, WHERE, JOIN, ORDER BY)
- 🔄 SQL advanced (CTEs, Window Functions)
- ⏳ Python logging and CLI tools
- ⏳ Data quality frameworks

### Domain Knowledge
- ✅ Clinical trial workflow (screening, dosing, visits, completion)
- ✅ Multi-site trial management
- ✅ Day of Study calculation
- ✅ GCP principles (query management, no auto-correction)
- ✅ Data quality management in clinical context
- 🔄 CDISC standards
- ⏳ Regulatory compliance (21 CFR Part 11, GDPR)

### Tools Proficiency
- ✅ Git/GitHub (repository management, commits, push/pull)
- ✅ VSCode (project setup, extensions)
- ✅ DBeaver (PostgreSQL GUI)
- ✅ Power BI (data import, visualizations, DAX basics)
- ✅ Python (data generation, ETL, file I/O)
- 🔄 PostgreSQL (queries, joins, CTEs)
- ⏳ Python production (logging, CLI, type hints)

---

## Reflection & Next Steps

### What's Going Well
- Successfully completed first major portfolio project (Clinical Data Pipeline)
- Established solid Git workflow and repository structure
- Making steady progress on LeetCode SQL fundamentals
- Good balance between theory (LeetCode) and practice (pipeline project)

### Areas for Improvement
- Need to increase LeetCode exercise pace to hit 25/50 by end of Week 2
- Should document more detailed technical decisions in project READMEs
- Need to practice explaining projects verbally (for interviews)

### Immediate Next Steps (Next 7 days)
1. Complete LeetCode exercises 8-25 (focus Window Functions, CTEs)
2. Download Kaggle clinical dataset
3. Start Mock CRF Validator SQL project
4. Update Clinical Data Pipeline README with interview talking points
5. Practice 2-minute project explanation

### Long-term Goals (6 months)
- Complete full roadmap: SQL, Python pipelines, Data Quality, Governance
- Build portfolio of 5-6 substantial projects
- Secure Clinical Data Manager role
- Obtain relevant certifications (considering PL-300, DP-900)