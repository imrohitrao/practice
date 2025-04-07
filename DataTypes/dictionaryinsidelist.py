# Dictionary Inside a List

data = [
    {'name': 'Alice', 'hobbies': ['reading', 'cycling']},
    {'name': 'Bob', 'hobbies': ['swimming', 'gaming']}
]

for Person in data:
    print(f"Name: {Person['name']}")
    print(f"     -Hobby")
    for Hobbies in Person['hobbies']:
        print(f"         {Hobbies}")



