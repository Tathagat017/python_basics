employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

employees_dict = {emp: defaults for emp in employees}

print(employees_dict)
