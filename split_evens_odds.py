# split evens and odds from a list

groups = {"Evens": [], "Odds": []}
for n in range(15):
    groups["Evens" if n % 2 == 0 else "Odds"].append(n)
print(groups)

