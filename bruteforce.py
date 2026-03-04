from itertools import permutations

students = ["Alice", "Bob", "Carol", "Dave", "Eve"]

friends = {("Alice", "Bob"), ("Bob", "Carol"), ("Carol", "Dave"), ("Dave", "Eve")}
same_city = {("Alice", "Carol"), ("Bob", "Eve")}

def is_valid(arrangement):
    for i in range(len(arrangement) - 1):
        a = arrangement[i]
        b = arrangement[i + 1]
        if (a, b) in friends or (b, a) in friends:
            return False
        if (a, b) in same_city or (b, a) in same_city:
            return False
    return True

all_arrangements = list(permutations(students))
print(f"Students     : {', '.join(students)}")
print(f"Friends      : {[a + ' & ' + b for a, b in friends]}")
print(f"Same City    : {[a + ' & ' + b for a, b in same_city]}")
print(f"\nTotal arrangements checked (5!) : {len(all_arrangements)}")

valid = []
for arrangement in all_arrangements:
    if is_valid(arrangement):
        valid.append(arrangement)

print(f"Valid arrangements found        : {len(valid)}")
print("\n--- Valid Seating Orders ---")
for i, arrangement in enumerate(valid, 1):
    print(f"  Option {i}: {' --> '.join(arrangement)}")
print("\nAll other arrangements had friends or same-city students sitting next to each other.")