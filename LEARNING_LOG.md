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

## October 28, 2025 - Markdown & Documentation Workflow

### What I Accomplished:

1. **Markdown Syntax & Best Practices:**
   - Learned Markdown syntax for professional documentation
   - Understood how Markdown renders in VS Code preview
   - Learned how GitHub renders Markdown for README files and documentation

2. **Pandoc Document Conversion:**
   - Set up Pandoc in VS Code for document conversion
   - Can now convert .md files to Word documents (.docx)
   - Can convert to OneNote format for easy sharing
   - Enables sharing technical documentation in business-friendly formats

3. **Documentation Workflow:**
   - Write documentation in Markdown (clean, version-controlled)
   - Preview in VS Code for immediate feedback
   - Convert to Word/OneNote when sharing with non-technical stakeholders
   - Maintain single source of truth in Git

**Status:** Documentation workflow established ✅

---

## November 11, 2025 - Development Environment Setup & Python Pipeline Planning

### What I Accomplished:

1. **Verified Repository Status:**
   - Compared local vs remote repository using `git fetch origin` and `git status`
   - Confirmed local and GitHub are in sync

2. **Virtual Environment Setup:**
   - Created conda environment: `clinical-data-projects`
   - Exported dependencies to `environment.yml`
   - Learned conda stores environments centrally (not in project folder)

3. **VS Code Configuration:**
   - Configured Git Bash as integrated terminal
   - Selected Python interpreter from conda environment
   - Ready for development work

4. **Next Steps Planning:**
   - Reviewed project README and roadmap
   - Ready to start `python-pipeline/` project
   - Considering pipeline options: validation, ETL, or query generation

**Status:** Environment complete ✅ | Ready to begin Python pipeline development

---

## 📚 SQL Learning Path (Paused - To Be Resumed Later)

### Week 1: SQL Basics - LeetCode SQL 50 (October 24-27, 2025)
**Status:** ⏸️ Paused (7/50 exercises completed)

**LeetCode SQL 50 Exercises:**
- ✅ 7/50 exercises completed ([SQL 50 Study Plan](https://leetcode.com/studyplan/top-sql-50/))
- Solutions repo: [SQL-50-leetcode](https://github.com/TiagoRoad66-lab/SQL-50-leetcode)
- Concepts mastered: SELECT, WHERE, ORDER BY, basic JOINs
- In progress: continuing to exercises 20-25
- Next concepts: CTEs, Window Functions (in advanced exercises)

**Progress:**
- Start date: October 24, 2025
- Time invested: ~2 hours
- Target pace: 7-10h/week

**Blockers encountered:**
(None at the moment)

**Personal notes:**
First day of self-paced learning on LeetCode. Basic exercises going well, progressing gradually. In parallel, developed the Clinical Data Pipeline project which applies these SQL concepts in a real context.

---

### Week 2: Advanced SQL (CTEs + Window Functions) (October 28 - November 3, 2025)
**Status:** ⏸️ Paused - Prioritizing Python pipeline development

**Learning objectives:**
- [ ] CTEs (Common Table Expressions) – structure queries with WITH
- [ ] Window Functions – ROW_NUMBER(), RANK(), LAG(), LEAD()
- [ ] Difference between JOIN vs Subqueries
- [ ] EXPLAIN PLAN – basic optimization

**Resources used:**
- LeetCode SQL 50 (exercises 20-35)
- Mode Analytics SQL Tutorial (if clarification needed)

**Planned exercises:**
- [ ] LeetCode exercises 8-25 (focus CTEs + Window Functions)
- [ ] "Mock CRF Validator" project in SQL (end of week 2)

**Next steps (when resumed):**
- Complete first 25 exercises of SQL 50
- Download clinical Kaggle dataset
- Create 6 validation queries in `sql-validator/`

---

## Portfolio Overview

### Completed Work
1. ✅ Clinical Data Pipeline (Multi-site trial simulator) - October 2025
2. ✅ Git setup and repository structure
3. ✅ Development environment setup (Conda, Git Bash, VS Code) - November 2025
4. ✅ LeetCode SQL 50: 7/50 exercises

### In Progress
1. 🔄 Python Pipeline Development (November 2025)

### Paused (To Resume Later)
1. ⏸️ LeetCode SQL 50: 7/50 completed, targeting 25/50
2. ⏸️ SQL Advanced concepts (CTEs, Window Functions)
3. ⏸️ Mock CRF Validator SQL project

### Upcoming
1. Python pipeline with logging and CLI
2. Data Quality scorecard with Power BI
3. Governance documentation

---

## Skills Tracking

### Technical Skills Acquired
- ✅ Python data generation (Faker library)
- ✅ Pandas data manipulation
- ✅ PostgreSQL database design
- ✅ Power BI dashboard creation
- ✅ Git version control
- ✅ Conda virtual environments
- ✅ Development workflow (Git Bash, VS Code integration)
- ✅ Markdown documentation (syntax, formatting, GitHub rendering)
- ✅ Pandoc document conversion (.md to .docx, OneNote)
- ✅ SQL basics (SELECT, WHERE, JOIN, ORDER BY)
- ⏸️ SQL advanced (CTEs, Window Functions) - paused
- 🔄 Python logging and CLI tools - in progress
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
- ✅ VSCode (project setup, extensions, terminal integration, Markdown preview)
- ✅ Pandoc (document conversion, .md to .docx/OneNote)
- ✅ DBeaver (PostgreSQL GUI)
- ✅ Power BI (data import, visualizations, DAX basics)
- ✅ Python (data generation, ETL, file I/O)
- ✅ Conda (environment management, dependency tracking)
- ⏸️ PostgreSQL (queries, joins, CTEs) - paused
- 🔄 Python production (logging, CLI, type hints) - in progress

---

## Reflection & Next Steps

### What's Going Well
- Successfully completed first major portfolio project (Clinical Data Pipeline)
- Established solid Git workflow and repository structure
- Set up professional development environment with proper tooling
- Good understanding of virtual environment management
- Making strategic decisions about project priorities

### Areas for Improvement
- Need to maintain consistent documentation of technical decisions
- Should practice explaining projects verbally (for interviews)
- Balance between breadth (trying multiple topics) and depth (completing full projects)

### Immediate Next Steps (Next 7 days)
1. Design and structure Python pipeline project
2. Implement modular pipeline components
3. Add proper logging and error handling
4. Create CLI interface for automation
5. Document code and create project README

### Long-term Goals (6 months)
- Complete full roadmap: SQL, Python pipelines, Data Quality, Governance
- Build portfolio of 5-6 substantial projects
- Secure Clinical Data Manager role
- Obtain relevant certifications (considering PL-300, DP-900)
- Resume and complete SQL learning path

---

## Notes on Learning Strategy

**Current Focus:** Python Pipeline Development
- Prioritizing hands-on project work over theoretical exercises
- Building production-quality code skills (logging, CLI, documentation)
- Will return to SQL exercises after completing Python pipeline project

**Rationale:** 
- Real projects demonstrate job-ready skills more effectively
- Python pipeline complements completed Clinical Data Pipeline project
- SQL fundamentals already established through initial exercises and pipeline project