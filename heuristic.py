students = ["Alice", "Bob", "Carol", "Dave", "Eve"]

friends = {("Alice", "Bob"), ("Bob", "Carol"), ("Carol", "Dave"), ("Dave", "Eve")}
same_city = {("Alice", "Carol"), ("Bob", "Eve")}

def are_friends(a, b):
    return (a, b) in friends or (b, a) in friends

def are_same_city(a, b):
    return (a, b) in same_city or (b, a) in same_city

def can_place(student, arrangement):
    if arrangement:
        last = arrangement[-1]
        if are_friends(student, last):
            return False
        if are_same_city(student, last):
            return False
    return True

def count_constraints(student, all_students):
    count = 0
    for other in all_students:
        if other != student:
            if are_friends(student, other):
                count += 1
            if are_same_city(student, other):
                count += 1
    return count

print(f"Students  : {', '.join(students)}")
print(f"Friends   : {[a + ' & ' + b for a, b in friends]}")
print(f"Same City : {[a + ' & ' + b for a, b in same_city]}")

print("\n--- Step 1: Rank students by most constrained first ---")
ranked = sorted(students, key=lambda s: count_constraints(s, students), reverse=True)
for s in ranked:
    print(f"  {s} has {count_constraints(s, students)} constraints")

print("\n--- Step 2: Place students one by one using heuristic ---")
remaining = ranked.copy()
arrangement = []

while remaining:
    placed = False
    for student in remaining:
        if can_place(student, arrangement):
            arrangement.append(student)
            remaining.remove(student)
            print(f"  Placed: {student} --> Seat {len(arrangement)}")
            placed = True
            break
    if not placed:
        print("  No valid placement found, backtracking needed.")
        break

print("\n--- Result ---")
if len(arrangement) == len(students):
    print(f"  Valid arrangement found: {' --> '.join(arrangement)}")
else:
    print("  Could not find a valid arrangement.")