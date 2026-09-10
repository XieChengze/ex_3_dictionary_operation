student = {
    "name": "Alice Wong",
    "student_id": "ST1024",
    "age": 21,
    "program": "Software Engineering",
    "city": "Nanjing",
    "gpa": 3.6
}


# First, display the complete record using for loop, printing and some string formatting only

for key in student:
    print(f"  {key}: {student[key]}")


# Check if there's a key called 'email'. If not, ask the user to enter an email

print("")
if 'email' not in student:
    email_input = input("please input email: ")
    # email_input = "alice.wong@university.edu"
    student['email'] = email_input
    print(f"successful add email: {email_input}")

# Ask the user to enter a new city, and update the existing city with this new one
# Make sure the new city is not an empty string

print("")
# new_city = "Shanghai"
new_city = input("input new city: ")
if new_city.strip() != "":
    student['city'] = new_city
    print(f"new city is: {new_city}")
else:
    print("error, city can not be empty.")

# Check if there's 'phone' key in the dictionary. If not, print a message saying "Phone number not found."
# Use the get() method

phone = student.get('phone')
if phone is None:
    print("Phone number not found.")

# Add a new key called 'contact' to the dictionary, which is itself a dictionary containing two keys: 'phone' and 'email'.

student['contact'] = {
    'phone': '13800001111',
    'email': student.get('email')
}


# Add another key called 'courses' to the dictionary, which is itself a dictionary containing three keys: 'Python', 'Databases', and 'Software Engineering', with 88, 91, and 84 as their corresponding scores

student['courses'] = {
    'Python': 88,
    'Databases': 91,
    'Software Engineering': 84
}

# Calculate the average score for the student without built-in functions like sum(). Use a for loop instead. 

total_score = 0
course_count = 0
for score in student['courses'].values():
    total_score += score
    course_count += 1

average_score = total_score / course_count

# Add a new key called 'academic_status' to the dictionary
# It should be a string that indicates the student's academic status based on the average score. 
# If the score is >= 90, the status should be "Excellent".
# If the score is >= 75, the status should be "Good".
# If the score is >= 60, the status should be "Pass".
# If the score is < 60, the status should be "At Risk".

if average_score >= 90:
    academic_status = "Excellent"
elif average_score >= 75:
    academic_status = "Good"
elif average_score >= 60:
    academic_status = "Pass"
else:
    academic_status = "At Risk"

student['academic_status'] = academic_status


# Add the logic to search for a course. 
# If the course is found, print the course name and score. If not, print "Course not found".

print("")
search_course = input("input search course: ")
# search_course = "python"
if search_course in student['courses']:
    print(f"{search_course} : {student['courses'][search_course]}")
else:
    print("Course not found")


# Add the logic to update a course score. 
# Ask the user to enter the course name and the new score. 
# If the course is found, then update the score and print a message indicating the change.
# While adding the new course, make sure the new score is a number between 0 and 100

print("")
update_course = input("please input update course:")
if update_course in student['courses']:
    new_score = input("\nplease input new score:")
    if new_score.isdigit():
        new_score = int(new_score)
        if 0 <= new_score <= 100:
            student['courses'][update_course] = new_score
            print(f"{update_course} new score is {new_score}")
        else:
            print("error, score must be 0 to 100")
    else:
        print("error, input must be number")
else:
    print("Course not found")


# Recaclculate the average score and update the academic status after the course score has been updated.

total_score = 0
course_count = 0
for score in student['courses'].values():
    total_score += score
    course_count += 1

average_score = total_score / course_count

if average_score >= 90:
    academic_status = "Excellent"
elif average_score >= 75:
    academic_status = "Good"
elif average_score >= 60:
    academic_status = "Pass"
else:
    academic_status = "At Risk"

student['academic_status'] = academic_status


# Display the final formatted student record with all the updated information, including the average score and academic status.
# It should look like the following: 

print("=================================")
print("      STUDENT RECORD")
print("================================")
print(f"\nName: {student['name']}")
print(f"Student ID: {student['student_id']}")
print(f"Age: {student['age']}")
print(f"Program: {student['program']}")
print(f"City: {student['city']}")
print(f"GPA: {student['gpa']}")
print("\nCONTACT")
print(f"Phone: {student['contact']['phone']}")
print(f"Email: {student['contact']['email']}")
print("\nCOURSE RESULTS")
for course in student['courses']: 
    print(f"{course}: {student['courses'][course]}")
# for course, score in student['courses'].items():
#     print(f"{course}: {score}")
print(f"\nAverage Score: {average_score:.1f}")
print(f"Academic Status: {student['academic_status']}")
print("===========================")

""" 
=====================================
        STUDENT RECORD
=====================================

Name: Alice Wong
Student ID: ST1024
Age: 21
Program: Software Engineering
City: Shanghai
GPA: 3.6

CONTACT
Phone: 13800001111
Email: alice.wong@university.edu

COURSE RESULTS
Python: 88
Databases: 91
Software Engineering: 84

Average Score: 87.7
Academic Status: Good

===================================== """

