import csv

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    return render_template("Homepage.html")

@app.route("/game_web")
def game_web():
    return render_template("game_web.html")

@app.route("/hotel")
def hotel_screen():
    hotels = [
        {"name": "Luxury Hotel", "price": 120},
        {"name": "Beach Resort", "price": 90},
        {"name": "City Hotel", "price": 70}
    ]
    return render_template('hotel_screen.html', hotels=hotels)

@app.route('/new')
def new_screen():
    """Renders the destination page."""
    return render_template('new_screen.html')
@app.route('/homework')
def homework():
    # students = []
    # choice = 0
    # while choice != "6":
    #     print("\n--- School Trip Menu ---")
    #     print("Students:")
    #     for i in range(len(students)):
    #         print(f"{i + 1}.{students[i]}")
    #     print("****Options****")
    #     print("1. Add student to end")
    #     print("2. Add priority student to front")
    #     print("3. Remove a student")
    #     print("4. Save data (as CSV file)")
    #     print("5. Remove all student")
    #     print("6. Exit")
    #
    #     choice = input("\nEnter your choice (1-6): ")
    #     if choice == "1":
    #         # Ask for a name and add it to the end of the list
    #         new_student = input("Enter a student name to add to the end of the list:")
    #         students.append(new_student)
    #     elif choice == "2":
    #         # Ask for a name and insert it at the front
    #         priority_student = input("Enter a student name to insert it at front:")
    #         students.insert(0, priority_student)
    #     elif choice == "3":
    #         # Ask the user if they want to remove a student 'y' then ask of a name to remove
    #         remove_student = input("Do you want to remove a student (y/n):").lower()
    #         if remove_student == "y":
    #             student_to_remove = input("Enter a student to remove:")
    #             if student_to_remove not in students:
    #                 print("There are no student with that name!")
    #             else:
    #                 students.remove(student_to_remove)
    #         else:
    #             print("There are no option like that!")
    #     elif choice == "4":
    #         with open('students.csv', 'w', newline='') as file:
    #             writer = csv.writer(file)
    #             for student in students:
    #                 writer.writerow(student)
    #
    #     elif choice == "5":
    #         check_remove_all = input("Do you really want to remove all student  (y/n)?")
    #         if check_remove_all == "y":
    #             students.clear()
    #     elif choice == "6":
    #         print("Exiting program...")
    #     else:
    #         print("Invalid choice. Please try again.")
    """Renders the destination page."""
    return render_template('homework.html')



if __name__ == "__main__":
    app.run(debug=True)

