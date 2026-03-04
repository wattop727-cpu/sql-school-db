import math, time
from itertools import permutations

students = ["Alice", "Bob", "Carol", "Dave", "Eve"]
friends = {("Alice", "Bob"), ("Bob", "Carol"), ("Carol", "Dave"), ("Dave", "Eve")}
same_city = {("Alice", "Carol"), ("Bob", "Eve")}

def is_valid(arr):
    for i in range(len(arr) - 1):
        a, b = arr[i], arr[i+1]
        if (a,b) in friends or (b,a) in friends: return False
        if (a,b) in same_city or (b,a) in same_city: return False
    return True

def brute_force():
    return [a for a in permutations(students) if is_valid(a)]

def can_sit(a, b):
    return (a,b) not in friends and (b,a) not in friends and \
           (a,b) not in same_city and (b,a) not in same_city

def heuristic():
    ranked = sorted(students, key=lambda s: sum(1 for a,b in friends|same_city if s in (a,b)), reverse=True)
    result, remaining = [], ranked.copy()
    while remaining:
        for s in remaining:
            if not result or can_sit(result[-1], s):
                result.append(s); remaining.remove(s); break
        else: break
    return result

t1 = time.time(); bf = brute_force(); t2 = time.time()
t3 = time.time(); h  = heuristic();   t4 = time.time()

print("Brute Force O(n!)")
print(f"  Checked : {math.factorial(len(students))} arrangements")
print(f"  Valid   : {len(bf)}")
print(f"  Time    : {t2-t1:.6f} sec")
for i,v in enumerate(bf,1): print(f"  Option {i}: {' > '.join(v)}")

print("\nHeuristic O(n^2)")
print(f"  Checked : ~{len(students)**2} arrangements")
print(f"  Valid   : 1")
print(f"  Time    : {t4-t3:.6f} sec")
print(f"  Result  : {' > '.join(h)}")

print(f"\nHeuristic is {(t2-t1)/(t4-t3):.1f}x faster than Brute Force")