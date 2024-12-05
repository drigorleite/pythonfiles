def main():
    # Dictionaries for course details
    roomNumbers = {
        "CS101": "3004",
        "CS102": "4501",
        "CS103": "6755",
        "NT110": "1244",
        "CM241": "1411"
    }

    instructors = {
        "CS101": "HAYNES",
        "CS102": "ALVARADO",
        "CS103": "RICH",
        "NT110": "BURKE",
        "CM241": "LEE"
    }

    meetingTimes = {
        "CS101": "8:00AM",
        "CS102": "9:00AM",
        "CS103": "10:00AM",
        "NT110": "11:00AM",
        "CM241": "1:00PM"
    }

    # User input for course number
    courseNumber = input("Enter a course number (e.g., CS101): ").upper()

    # Displaying the course information
    if courseNumber in roomNumbers and courseNumber in instructors and courseNumber in meetingTimes:
        print(f"Room Number: {roomNumbers[courseNumber]}")
        print(f"Instructor: {instructors[courseNumber]}")
        print(f"Meeting Time: {meetingTimes[courseNumber]}")
    else:
        print("Course number not found. Please enter a valid course number.")

if __name__ == "__main__":
    main()
