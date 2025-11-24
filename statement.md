Problem statement

In many classrooms, student marks are stored manually or in scattered files, making it difficult for teachers or tutors to quickly compute totals, averages, or grades for each student. This slows down progress tracking and makes identifying top performers, weak performers, and duplicated or inconsistent records error‑prone. There is also no simple built‑in way in many basic tools to explore numeric utilities such as prime checks, factorials, or Fibonacci, which are useful for teaching and practicing programming and math skills.​

Scope of the project

This project implements a simple, menu‑driven, console‑based “Student Performance Analyzer” that works with up to five subject marks per student. It supports adding student records interactively, loading and saving records via CSV files, computing total and average marks, assigning grades, sorting by total, finding the 
k
kth highest or lowest total, removing duplicate total scores, and offering basic number‑theory utilities (prime, GCD, factorial, Fibonacci). The system runs locally using text input/output, does not provide a graphical interface, networking, predictive analytics, attendance tracking, or integration with external ERP/LMS systems.​

Target users

The primary users are students and beginners in programming laboratories who need a small, understandable application to analyze marks and practice algorithms on real‑looking data. Secondary users include instructors or teaching assistants who want a light‑weight tool to demonstrate data handling (CSV I/O), basic statistics on marks, and algorithmic operations such as searching, sorting, and numeric utilities in a classroom or lab.​

High-level features

Add student records interactively with validation for five subjects per student.​
Load sample student data from a CSV file and save updated records back to CSV for reuse.​
Display a tabular report showing each student’s name, total marks, average, and computed grade.​
Sort students in descending order of total marks to easily view top performers.​
Compute the 
k
kth highest or 
k<img width="919" height="749" alt="Screenshot 2025-11-24 215535" src="https://github.com/user-attachments/assets/23f25da5-aa4e-45d1-94fc-d0375784d11a" />

kth lowest total score using helper algorithms on the list of totals.​
Remove students with duplicate total marks, keeping only unique‑total records to simplify rank analysis.​
Provide a utilities menu offering prime check, greatest common divisor, factorial, and Fibonacci calculations as supporting math/programming tools
