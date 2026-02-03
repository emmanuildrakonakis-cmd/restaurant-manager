# Tavern Manager App

A modern, Python-based desktop application designed for efficient restaurant management.
It handles **reservations**, **real-time table status**, **tips calculation**, and **monthly financial reporting**.

Built with **CustomTkinter** for a sleek Dark Mode UI and **JSON** for robust data persistence.

---

## Features

### Reservation Management
* **Add New Bookings:** Quickly input customer details (Name, Date, Time, Pax, Table).
* **Real-Time Status:** Visual indicators for **Open** (🟢) and **Closed/Paid** (🔴) tables.
* **Calendar Filtering:** Search and view reservations for specific dates using the built-in filter.

### Financial Tools & Reporting
* **Checkout System:** Close tables, add tips, and auto-save transaction history.
* **Monthly Reports:** Automatically generates detailed `.txt` reports for end-of-month accounting.
* **Tip Distribution:** Calculates staff shares (Waiters, Kitchen, Cleaning) based on predefined percentages.

### Data Persistence
* **Auto-Save:** All data is stored locally in `history.json`.
* **Crash-Proof:** Data is reloaded automatically upon restarting the application, ensuring no reservations are lost.

---

## Tech Stack

* **Language:** Python 3.10+
* **GUI Framework:** [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) (Modern UI)
* **Database:** JSON (Local Storage)
* **Architecture:** MVC (Model-View-Controller) pattern for clean code structure.

---

##  Installation & Usage

### Prerequisites
You need **Python 3** installed on your system.

### 1. Download Source Code
Download the project files (or unzip the provided folder).

### 2. Install Dependencies
Open your terminal (Command Prompt on Windows / Terminal on Mac) and run:

```bash
pip install customtkinter


 3. Run the Application
Navigate to the project folder and run the main GUI file:

For Windows:
Bash
python gui_app.py



For Mac / Linux:
Bash
python3 gui_app.py





Project Structure
Plaintext
Taverna_Manager/
│
├── gui_app.py        # The Main Application (User Interface)
├── models.py         # The Logic & Database Handler (Backend)
├── history.json      # Auto-generated database (stores reservations)
├── README.md         # Project Documentation
└── .gitignore        # Files to exclude from Git
 
 
 
 
 
 
 
 Monthly Report Example
The application generates reports in the following format (report_YYYY-MM.txt):

Plaintext
=== ΜΗΝΙΑΙΑ ΑΝΑΦΟΡΑ: 2026-02 ===
Σύνολο Κρατήσεων: 45
ΣΥΝΟΛΙΚΑ TIPS:    850.0€
------------------------------
Σερβιτόρος Α:     425.0€
Σερβιτόρος Β:     170.0€
Κουζίνα:          170.0€
Λάντζα:           85.0€
------------------------------
Εκδόθηκε στις: 2026-02-28 23:59





👨‍💻 Author
Developed by Emmanouil Drakonakis
Restaurant Management System v4.0