#student information manager
students = {}

def student_information():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    marks = list(map(int, input("Enter 3 subjects marks (space-separated): ").split()))

    students[name] = {
        "age": age,
        "marks": marks
    }
    print(f'{name} added successfully!')

def count_vowels_in_name(name):
    count = 0
    for letter in name:
        if letter in 'AEIOUaeiou':
            count += 1
    print(f'{name} has {count} vowel(s).')

def calculate_grade(marks):
    total=sum(marks)
    average=total/len(marks)
    if total>=90:
        return 'A'
    elif total>=75:
        return 'B'
    elif total>=50:
        return 'C'
    else:
        return 'Fail'
def remove_duplicate(name):
    new_list=[]
    for names in name:
        if names not in name:
            names.append(name)   
    

# Adding students
while True:
    student_information()
    again = input("Do you want to add another student? (yes/no): ").lower()
    if again != 'yes':
        break

# Displaying all students
print("\nAll students:")
top_scorer=None
highest_avg=-1
for name,info in students.items():
    marks=info["marks"]
    average=total/len(marks)
    grade=calculate_grade(marks)
    print(f'{name} --> Age: {info["age"]}, Marks: {info["marks"]}')
    count_vowels_in_name(name)
    remove_duplicate(name)
    if average>highest_avg:
        highest_avg=average
        top_scorer=name

print(f"\nTop Scorer: {top_scorer} with an average of {highest_avg:.2f}")

    
