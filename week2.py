#//Assignment 1//
#Question 1
prices = [30, 60, 100, 45, 80]

# filter prices above or equal to $50
filtered = list(filter(lambda p: p >= 50, prices))

# apply 10% discount
discounted = list(map(lambda p: p * 0.9, filtered))

print(discounted)


#Question 2
hours = [38, 40, 45, 50, 35]

# filter employees who worked 40 or more hours
filtered = list(filter(lambda h: h >= 40, hours))

# convert to overtime hours
overtime = list(map(lambda h: h - 40, filtered))

print(overtime)


#Question 3
feedback = [
    "Great product.",
    "Absolutely loved it, will buy again.",
    "Okay",
    "The service was excellent and fast."
]

# filter messages with 20 or more characters
filtered = list(filter(lambda f: len(f) >= 20, feedback))

# convert to lowercase
lowered = list(map(lambda f: f.lower(), filtered))

print(lowered)


#//Assignment 2//
#Question 1
employees = {
    "Abhishek": 55000,
    "Ronik": 75000,
    "Aayush": 60000,
    "Sam": 90000
}

# filter employees with salary >= 60000
filtered = dict(filter(lambda item: item[1] >= 60000, employees.items()))

# apply 5% raise
raised = dict(map(lambda item: (item[0], item[1] * 1.05), filtered.items()))

print(raised)


#Question 2
scores = [45, 67, 89, 92, 55, 73, 40]

# filter passing scores (>= 50)
filtered = list(filter(lambda s: s >= 50, scores))

# map scores to letter grades
grades = list(map(lambda s: 
    'A' if s >= 90 else 
    'B' if s >= 80 else 
    'C' if s >= 70 else 
    'D' if s >= 60 else 
    'E', filtered))

print(grades)
