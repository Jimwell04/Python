# List in Python

ProgrammingLanguages = ["C","C++","C#","Python","Java","Kotlin","Ruby"]

print(type(ProgrammingLanguages))

List = ["string", 265, 56.87, True]

print(ProgrammingLanguages[3])
print(List[3])
print(ProgrammingLanguages, List)

List.append("appended")
print(List)

List.extend(["extended", "extended"])
print(List)

List.insert(0, "inserted")
List.insert(-1, "inserted")
print(List)

List.remove("extended")
print(List)
List.pop(0)
print(List)

List.clear()
print(List)