# Grade Manager CLI Project

import csv
import os

FILENAME = "grades.csv"

def init_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Subject", "Marks"])
    else:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            rows = list(reader)
            if len(rows) > 1:
                print("Last saved entry:", rows[-1])

def add_grade():
    data = input("Enter in format: Name,Subject,Marks:\n")
    try:
        name, subject, marks = data.split(",")
        marks = float(marks)
        with open(FILENAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name.strip(), subject.strip(), marks])
        print("Grade saved.")
    except ValueError:
        print("❌ Invalid input! Use format: Name,Subject,Marks (Marks should be a number)")

def view_all():
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def search_student():
    name = input("Enter name to search: ").strip().lower()
    found = False
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if name in row[0].lower():
                print(row)
                found = True
    if not found:
        print("❌ Student not found.")

def show_average_and_grade():
    total = 0
    count = 0
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            try:
                mark = float(row[2])
                total += mark
                count += 1
            except (ValueError, IndexError):
                continue
    if count == 0:
        print("No data available to calculate average.")
        return
    average = total / count
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "D"
    print(f"Average Marks: {average:.2f}")
    print(f"Overall Grade: {grade}")

def main():
    init_file()
    while True:
        print("\n--- Grade Manager ---")
        choice = input("1. Add Grade\n2. View All\n3. Search by Name\n4. Show Average & Grade\n5. Exit\nChoose: ")
        if choice == "1":
            add_grade()
        elif choice == "2":
            view_all()
        elif choice == "3":
            search_student()
        elif choice == "4":
            show_average_and_grade()
        elif choice == "5":
            print("Thank you! Exiting...")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()