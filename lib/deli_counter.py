katz_deli = []

def take_a_number(list_of_people, person_joining):
    list_of_people.append(person_joining)
    position = len(list_of_people)
    print(f"Welcome, {person_joining}. You are number {position} in line.") 

def line(current_line):
    if not current_line:
        print("The line is currently empty")
    else:
        line_status = "The line is currently: " + ", ".join(f"{i+1}. {name}" for i, name in enumerate(current_line))
        print(line_status)

def now_serving(line):
    if not line:
        print("There is nobody waiting to be served!")
    else:
        serving_person = line.pop(0)
        print(f"Currently serving {serving_person}")

# Take a number on the qeue
take_a_number(katz_deli, "Ada") 
take_a_number(katz_deli, "Grace") 
take_a_number(katz_deli, "Kent")

# Check out the line status
line(katz_deli)

# Check who is serving at the moment or rather who is first in line
now_serving(katz_deli)

# Check line status; when someone is served we remove them from list
line(katz_deli)


now_serving(katz_deli)

take_a_number(katz_deli, "Anne")

line(katz_deli)