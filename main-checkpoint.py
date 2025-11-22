"""Student Performance Analyzer
Features:
- Add student records or load from CSV
- Compute total, average, grade
- Sort students, find kth highest/lowest
- Remove duplicate total scores
- Prime/GCD/Factorial/Fibonacci utilities
- Simple text-based menu
"""
from utils import *
import csv
import os

DATA_FILE = 'data/sample_students.csv'

def load_from_csv(path):
    students = []
    if not os.path.exists(path):
        return students
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for r in reader:
            name = r.get('name','').strip()
            marks = [int(r.get(s,0)) for s in ['m1','m2','m3','m4','m5'] if r.get(s) is not None]
            students.append({'name': name, 'marks': marks})
    return students

def save_to_csv(path, students):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', newline='') as f:
        fieldnames = ['name','m1','m2','m3','m4','m5']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for s in students:
            row = {'name': s['name']}
            for i, m in enumerate(s['marks'], start=1):
                row[f'm{i}'] = m
            writer.writerow(row)

def input_student():
    name = input('Student name: ').strip()
    marks = []
    for i in range(1,6):
        while True:
            try:
                x = int(input(f'Mark in subject {i} (0-100): '))
                if 0 <= x <= 100:
                    marks.append(x)
                    break
                else:
                    print('Enter between 0 and 100.')
            except:
                print('Invalid input.')
    return {'name': name, 'marks': marks}

def display_report(students):
    if not students:
        print('No data.')
        return
    rows = []
    print('\nName\tTotal\tAverage\tGrade')
    print('-'*40)
    for s in students:
        total = total_marks(s['marks'])
        avg = average_marks(s['marks'])
        grade = compute_grade(avg)
        print(f"{s['name']}\t{total}\t{avg:.2f}\t{grade}")
    print('-'*40)

def main_menu():
    students = load_from_csv(DATA_FILE)
    while True:
        print('\nStudent Performance Analyzer')
        print('1. Add student')
        print('2. Load sample CSV')
        print('3. Display report')
        print('4. Sort by total (desc)')
        print('5. Find Kth highest/lowest')
        print('6. Remove duplicate totals')
        print('7. Utilities (prime, gcd, factorial, fibonacci)')
        print('8. Save to CSV')
        print('9. Exit')
        ch = input('Choose option: ').strip()
        if ch == '1':
            students.append(input_student())
        elif ch == '2':
            students = load_from_csv(DATA_FILE)
            print(f'Loaded {len(students)} students from sample CSV.')
        elif ch == '3':
            display_report(students)
        elif ch == '4':
            students.sort(key=lambda s: total_marks(s['marks']), reverse=True)
            print('Sorted by total (highest first).')
        elif ch == '5':
            if not students:
                print('No students.')
                continue
            k = int(input('Enter k (1 for highest): '))
            choice = input('h for highest, l for lowest: ').strip().lower()
            totals = [total_marks(s['marks']) for s in students]
            if choice == 'h':
                val = kth_largest(totals, k)
                print(f'{k}th highest total = {val}')
            else:
                val = kth_smallest(totals, k)
                print(f'{k}th lowest total = {val}')
        elif ch == '6':
            before = len(students)
            students = remove_duplicate_totals(students)
            print(f'Removed duplicates: {before - len(students)} removed.')
        elif ch == '7':
            utilities_menu()
        elif ch == '8':
            save_to_csv(DATA_FILE, students)
            print('Saved to', DATA_FILE)
        elif ch == '9':
            print('Goodbye.')
            break
        else:
            print('Invalid option.')

if __name__ == '__main__':
    main_menu()
