import pandas as pd

# Примерные данные
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 31, 33, 49],
    'Score': [85.5, 90.3, 78.9, 92.1]
}

# Создаём DataFrame
df = pd.DataFrame(data)

# Выводим таблицу
print("Полная таблица:")
print(df)

# Средний возраст
print("\nСредний возраст:", df['Age'].mean())

# Максимальный балл
print("Максимальный балл:", df['Score'].max())
