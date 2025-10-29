Quiz Management System - Detailed Project Report
1.Introduction
The Quiz Management System is a Python-based application designed to automate and simplify
the process of conducting quizzes. It provides a user-friendly interface for administrators to managequiz questions and for users to participate in quizzes, view scores, and compare results through aleaderboard system.

2.Objective
The main objective of the Quiz Management System is to streamline quiz creation, participation,and result management.It eliminates manual efforts in evaluating quiz results and offers quick access to performance analytics.

3.Technology Stack
Component & Technology Used
1.Programming Language - Python 3
2.Database - SQLite3 (Quiz.db)
3.Data File - CSV file (quiz.csv)
4.IDE/Environment - PyCharm
5.Packaging Tool-PyInstaller(build directory)

4.File Structure Overview
The project includes multiple Python modules, a database, and configuration files. Each file servesa specific function within the system:

File Name Purpose
1.main.py - Serves as the entry point for running the entire quiz application.
2.admin.py - Handles administrative tasks such as adding or modifying quiz questions.
3.quiz.py - Contains the logic for quiz execution and question presentation.
4.leaderboard.py - Manages user scores and displays rankings.
5.quizmgmt.py - Integrates the admin and quiz functionalities into a cohesive system.
6.quiz.csv - Stores quiz questions and answers in CSV format for easy updates.
7.Quiz.db - SQLite database for storing quiz data, user information, and results.

5.Functional Modules
The Quiz Management System is divided into several core modules that handle different
operations:
1. Admin Module: Allows the admin to add, edit, or delete quiz questions. Data is stored in theSQLite database.
2. Quiz Module: Presents quiz questions to the user, collects responses, and evaluates the final score.
3. Leaderboard Module: Displays top scorers and maintains competition transparency.
4. Data Module: Manages reading/writing quiz questions from the CSV file and syncing with the
database.
5. Main Controller: Acts as the system launcher, connecting all modules for smooth execution.

6.Database Design
The system uses SQLite (Quiz.db) to store user data and quiz results. The database typically
includes tables such as: 
•questions: Stores quiz questions, options, and correct answers. 
•results: Records user scores and timestamps. •users: Maintains user credentials and access
levels.

7.System Workflow
1. The admin initializes the system and adds questions.
2. Users can log in or register to take quizzes.
3. The quiz module fetches questions and options from the database or CSV.
4. After completion, results are automatically evaluated.
5. The leaderboard updates with new scores and displays rankings.

8.Advantages
- Simplifies quiz creation and evaluation.
- Stores data securely in a local database.
- Easy to extend or migrate to a web-based version.
- Provides instant result generation and performance analysis.

9.Future Enhancements
- Integration with web frameworks like Flask or Django for online access.
- Timer-based quizzes and question randomization.
- Exporting reports in Excel or PDF automatically.
- Adding user authentication and admin dashboards with analytics.

10.Conclusion
The Quiz Management System effectively demonstrates modular programming, database
integration, and automation in a simple yet powerful educational tool. It serves as a valuable project for understanding Python-based system development.