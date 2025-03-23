import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee['salary'].drop_duplicates().sort_values(ascending=False).reset_index(drop=True)

    new_column = f'getNthHighestSalary({N})'

    if N <= 0 or N > len(employee):
        return pd.DataFrame({new_column: [None]})

    return pd.DataFrame({new_column: [employee.iloc[N-1]]})


data_1 = [(1,100),(2,100),(3,200),(4,300)]
data_2 = [(1,100),(2,100)]
N = 2

print(nth_highest_salary(pd.DataFrame(data_1, columns=['id', 'salary']), N))
