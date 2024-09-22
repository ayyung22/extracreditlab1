# -------------------------------------------------------- #
# Extra Credit Lab Assignment: Advanced Python Collections
# CIS 103: Introduction to Programming
# Instructor: Md Ali
# Student Name: Annie Yung
# Date: 9/21/2024

from collections import defaultdict

#Task 1: Inventory Management System

print("Part 1: Lists and Tuples")
print("1. Task: Inventory Management System")
inventory = ["sword", "shield", "potion", "bow", "arrow", "helmet"]
print(inventory)

#adding magic ring to the list
inventory.append("magic ring")
print(inventory)

#removing potion from the list
inventory.remove("potion")
print(inventory)

#upgrading bow to crossbow
inventory[2] = "crossbow"
print(inventory)

#printing list alphabetically
inventory.sort()
print(inventory)

#removing the first item on the list (removing "arrow")
inventory.remove("arrow")
print(inventory)

print()
print()

print("2. Task: Tuple Manipulation")
#creating tuple with original character stats
character_stats=(100, 50, 30)
print(character_stats)

#creating a new tuple called upgraded_stats
upgraded_stats=(100, 60, 35)
print(upgraded_stats)

print()
print()

print("Part 2: Sets and Dictionaries")
print("1. Task: Unique Visitors Tracking")

#creating a set
visitors = {"Alice", "Bob", "Charlie", "Diana", "Edward"}
print(visitors)

#adding Fiona to the set
visitors.add("Fiona")
print(visitors)

#adding George to the set
visitors.add("George")
print(visitors)

#trying to add Charlie to the set
visitors.add("Charlie")
print(visitors)
#Charlie will not print twice since sets will only allow for one unique element

#removing Diana from the set
visitors.remove("Diana")
print(visitors)

#calculating the total number of unique visitors
print("Total unique visitors:", len(visitors))

print()
print()

print("2. Task: Student Grades Dictionary")
#making a dictionary out of student grades
student_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 87,
    "Diana": 78
}

print(student_grades)

#adding Edward's score of 90 to the dictionary list
student_grades["Edward"] = 90
print(student_grades)

#updating Bob's grade
student_grades.update({"Bob": 95})
print(student_grades)

#deleting Diana from the dictionary
del student_grades["Diana"]
print(student_grades)

#calculating and printing the average grade of all students remaining in the dictionary


#printing the name of the student with the highest grade

print()
print()

print("Part 3: Real-World Scenario: Movie Database")
#creating a dictionary of movies and directors

movies = {
    "Inception": "Christopher Nolan",
    "Pulp Fiction": "Quentin Tarantino",
    "The Godfather": "Francis Ford Coppola",
    "The Dark Knight": "Christopher Nolan"
}

print(movies)

#adding two new movies to the dictionary
movies["Interstellar"] = "Christopher Nolan"
movies["Kill Bill"] = "Quentin Tarantino"
print(movies)

#updating "The Godfather" director to Sofia Coppola
movies.update({"The Godfather": "Sophia Coppola"})
print(movies)

#printing all movies directed by Christopher Nolan
value_groups = defaultdict(list)
for key, value in movies.items():
    value_groups[value].append(key)

    for value, keys in value_groups.items():
        if len(keys) > 1:
            print (f"Value: {value}, Keys: {keys}")

#code printed all keys and values that appear more than once instead of just movies directed by Christopher Nolan