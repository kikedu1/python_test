# 1. Lists and Tuples
""" list_1 = list(range(1,21))
print(list_1)

pairs_tuple = tuple(filter(lambda x: x%2 == 0, list_1))
print(pairs_tuple)

pairs_tuple_1 = tuple(x for x in list_1 if x % 2 == 0) 
print(pairs_tuple_1)

pairs_tuple_2 = []
for number in list_1:
    if number % 2 == 0:
        pairs_tuple_2.append(number)
print(pairs_tuple_2) """

# lista = [n for n in range(10)]
# print(lista)

# 2. Dictionaries

""" students = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "Diana": 67
}
students["Eve"] = 78

print(students)
print(max(students, key=students.get))

students = {aluno: nota + 5 for aluno, nota in students.items()} # Dictionary comprehention. Unpack the tuple
# {item: item + 5 for item in students.items()} Wrong way, is a tuple. ERROR: ('Alice', 85) + 5
print(students) """

# NumPy Arrays

""" import numpy as np

array = np.random.randint(1, 11, size=(3,3))
print(array)

print(array.mean(axis=1))
#print(array.mean(axis=0))

print(np.where(array>5,1,0)) """

# 4. pandas DataFrame

""" import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [24, 19, 22, 20],
    'Score': [85, 72, 90, 67]
}

df = pd.DataFrame(data)
print(df)

# print(df.describe())

print(df.loc[df['Score'] > 80])
print(df.iloc[:2,:2])

df['Pass'] = df['Score'] >= 70
print(df) """

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

print(df_merged.loc[df_merged['Score'] > 80]) """

# 6. Filtering with conditions

""" import numpy as np

array = np.random.randint(1, 101, 20)
print(array)
print(array[array % 5 ==0])
print(np.sort(array[array % 5 ==0])) """

# 7. SciPy – Statistics

""" from scipy import stats
import numpy as np

data = [12, 15, 20, 22, 25, 30, 35, 40]

print(f"Dados: {data}")
print(f"Média: {np.mean(data):.2f}")
print(f"Mediana: {np.median(data):.2f}")
print(f"Desvio Padrão Amostral (NumPy): {np.std(data, ddof=1):.2f}")  # ddof=1
print(f"Média (SciPy): {stats.tmean(data):.2f}")
print(f"Mediana (SciPy): {stats.scoreatpercentile(data, 50):.2f}") 
print(f"Desvio Padrão Amostral (SciPy): {stats.tstd(data):.2f}") """

# 8. SciPy – Linear Algebra

""" import numpy as np
from scipy import linalg

A = np.array([[3, 2], [1, 4]])

print(A)
print(linalg.det(A))
print(linalg.eigvals(A)) """

# 9. Object-Oriented Programming
""" class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f"Deposit of ${amount} succesfully executed")
        else:
            print("Deposit must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be positive")
        elif self.balance >= amount:
            self.balance -= amount
            print(f"Withdraw ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient balance funds")

    def __str__(self):
        return f"Owner: {self.owner}, Balance: ${self.balance}"


account = BankAccount("Alice", 500)
print(account)
account.deposit(200)
print(account)
account.withdraw(500)
print(account) """

# 10. OOP + pandas Integration

import pandas as pd

""" class Student:
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
    
student1 = Student("Alice", 20, 85)
student2 = Student("Bob", 21, 72)
student3 = Student("Charlie", 19, 90)

dict1 = student1.to_dict()
dict2 = student2.to_dict()
dict3 = student3.to_dict()

df = pd.DataFrame([dict1, dict2, dict3])

print(df)
print(df['Score'].mean()) """


