stu_dat = [
    ("Alice", {"Math": 90, "Science": 85, "History": 78}),
    ("Bob", {"Math": 88, "Science": 92, "History": 80}),
    ("Charlie", {"Math": 78, "Science": 85, "History": 88})
]
#materias
uni_sub = set()
for _, gra in stu_dat:
    uni_sub.update(gra.keys())

# avg
avg_gra = {nam: sum(gra.values()) / len(gra) for nam, gra in stu_dat}

# top student
top_stu = max(avg_gra, key=avg_gra.get)

# Diccionario
sub_gra = {sub: [] for sub in uni_sub}
for _, gra in stu_dat:
    for sub, grade in gra.items():
        sub_gra[sub].append(grade)

print("Expected average grades for each student:", avg_gra)
print("Expected student with the highest average grade: ", top_stu, avg_gra[top_stu])
print("Expected unique subjects:", uni_sub)
print("Subject Grades:", sub_gra)
