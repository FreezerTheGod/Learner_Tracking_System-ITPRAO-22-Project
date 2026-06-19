# Learner Progress Tracking System 📚

A Python-based CLI application designed to manage, track, and evaluate student progress. This project was developed as part of the curriculum requirements at **Eduvos** to demonstrate core Object-Oriented Programming (OOP) and algorithmic design practices.

---

## 👨‍💻 Project Details
* **Programmer Name:** Kamohelo Kotelo
* **Start Date:** 03 June 2026 (10:19 AM)
* **Completion Date:** 06 June 2026 (08:24 AM)
* **Development Environment:** Python 3.12+ with Tkinter UI dialog modules

---

## 🛠️ Key Technical Features Implemented

* **Object-Oriented Programming (OOP):**
  * **Inheritance:** A base `Person` class handles shared identity attributes (`name`, `age`), while the derived `Learner` class inherits and extends functionality.
  * **Encapsulation:** Protects internal metrics (like `__average_mark` and `__learner_status`) using private attributes accessed safely via dedicated getter methods (`getAverage()` / `getStatus()`).
* **Algorithmic Recursion:** Implements a custom recursive summation algorithm (`recursiveSum`) to calculate the dynamic totals of learner academic marks without standard iterative structures (`for`/`while`).
* **Persistent Local Data Storage:** Automatically writes and appends newly generated learner records out to an external plain-text file (`students.txt`) to maintain historical system records.
* **Hybrid Interface Design:** Runs via an interactive Command Line Interface (CLI) menu system while using `tkinter` message boxes for success notifications, confirmation windows, and certification warnings.

---

## 🚀 System Functionality Overview

The terminal dashboard provides an administrator panel equipped with 8 operations:
1. **Add Learner:** Captures structural variables (`ID`, `Name`, `Age`, `Course`), builds the local instance object, saves to file, and commits memory into a central execution matrix.
2. **Enter Marks:** Dynamically searches the database array and lets administrators input a user-defined quantity of evaluation scores (guarded by 0–100 error bounds).
3. **View All Learners:** Evaluates global profiles, printing structural metrics, raw mark lists, individual averages, and credential logic states.
4. **Search Learner:** Fast profile querying using unique alphanumeric `Learner ID` metrics.
5. **Update Learner Details:** Allows real-time editing and modifying of student names, ages, and courses.
6. **Remove Learner:** Dynamically deletes targeted indices directly from the database registry array.
7. **Show Learner Result:** Processes and outputs precision rounded grade analysis calculations and toggles certification eligibility dialogs.
8. **Exit:** Safeguarded system shutdown utility driven by double-checking confirmation handlers.

---

## 💻 How to Run the Application

1. Make sure Python is installed on your operating system.
2. Place your main script inside a folder workspace.
3. Open a system terminal or shell window inside that directory and run:
   ```bash
   python theprojectcode.py
