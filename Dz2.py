# Структурный подход (процедурный стиль)

def multiply(x, y):
    return x * y


def generate_row(i, n):
    row = []
    for j in range(1, n + 1):
        row.append(multiply(i, j))
    return row


def generate_table(n):
    table = []
    for i in range(1, n + 1):
        table.append(generate_row(i, n))
    return table


def print_table(table):
    for i, row in enumerate(table, start=1):
        for j, value in enumerate(row, start=1):
            print(f"{i} * {j} = {value}")


n = int(input("Введите число n: "))

table = generate_table(n)
print_table(table)

