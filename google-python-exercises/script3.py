# 6. Filtering with conditions

""" import numpy as np

array = np.random.randint(1, 101, 20)
print(array)
print(array[array % 5 ==0])
print(np.sort(array[array % 5 ==0])[::-1]) """

# 5. Merging DataFrames

""" import pandas as pd

data1 = {
    'ID': [1, 2, 3],
    'Name': ["Alice", "Bob", "Charlie"]
}

data2 = {
    'ID': [1, 2, 3],
    'Score': [85, 72, 90]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

df_merged =pd.merge(df1, df2, on = "ID")
print(df_merged)

print(df_merged.loc[df_merged['Score'] > 80, 'Name']) """

# 10. OOP + pandas Integration

""" import pandas as pd

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def to_dict(self):
        return {
            'Name': self.name,
            'Age': self.age,
            'Score': self.score
        }
    
    def __str__(self):
        return f"Student {self.name}, Age: {self.age}, Score: {self.score}"
    
    def __repr__(self):
        return f"Student({self.name!r}, {self.age}, {self.score})"
    
student1 = Student("Alice", 20, 85)
student2 = Student("Bob", 21, 72)
student3 = Student("Charlie", 19, 90)

# STR -> nice for print
print(student1)  
# Output: Student Alice, Age: 20, Score: 85

# REPR -> nice for lists, debugging
print([student1, student2, student3])
# Output: [Student('Alice', 20, 85), Student('Bob', 21, 72), Student('Charlie', 19, 90)]

# Convert to DataFrame
df = pd.DataFrame([s.to_dict() for s in [student1, student2, student3]])
print(df) """

# list = [1, 2, 3, 4]
# print(list)
# print(type(list))
# list1 = list(range(1,21))
# print(list1)
# print(type(list1))

# dicto = {
#     "Robert": 15,
#     "Claude": 11,
#     "Paul": 8
# }

# print(dicto)
# print(type(dicto))

""" # Cria um dicionário onde a chave e o valor são o mesmo número
dicto = {i: i for i in range(1, 3)}

print(dicto)
# Saída: {1: 1, 2: 2}

dicto_modificado = {chave: (lambda x: x + 3)(valor) for chave, valor in dicto.items()}

print(dicto_modificado)
# Saída: {1: 4, 2: 5} """

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [24, 19, 22, 20],
    'Score': [85, 72, 90, 67]
}

print(data)
print(type(data))