# Given a dictionary of student marks, find the student with the highest score

students = [
    {
        "name": "vijay",
        "subjects": {"maths": 100, "physics": 90, "chemistry": 80}
    },
    {
        "name": "rahul",
        "subjects": {"maths": 70, "physics": 60, "chemistry": 65}
    },
    {
        "name": "anita",
        "subjects": {"maths": 95, "physics": 75, "chemistry": 85}
    },
    {
        "name": "kiran",
        "subjects": {"maths": 88, "physics": 92, "biology": 81}
    },
    {
        "name": "sneha",
        "subjects": {"maths": 78, "chemistry": 82, "biology": 89}
    },
    {
        "name": "arjun",
        "subjects": {"maths": 66, "physics": 72, "biology": 74}
    },
    {
        "name": "meena",
        "subjects": {"maths": 91, "physics": 84, "chemistry": 88}
    },
    {
        "name": "rohit",
        "subjects": {"maths": 73, "physics": 77, "chemistry": 69}
    },
    {
        "name": "pooja",
        "subjects": {"maths": 85, "biology": 90, "chemistry": 87}
    },
    {
        "name": "amit",
        "subjects": {"maths": 68, "physics": 71, "chemistry": 74}
    }
]


def find_topper(my_dict):

    topper = {"marks":0}

    for student in my_dict:
        name = student["name"]
        subjects = student["subjects"]
        sub_total = 0 
        for [sub, marks] in subjects.items():
            sub_total += marks
        if topper["marks"] < sub_total:
            topper["class_topper"] = name
            topper["marks"] = sub_total
    return topper



result = find_topper(students)
print(result)


# {'marks': 270, 'class_topper': 'vijay'}
