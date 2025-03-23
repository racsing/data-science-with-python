import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    print("employees ", employee)

    managers = employee.groupby("managerId", as_index=False).agg(
            counter=("id", "count")).query('counter >= 5')["managerId"]
    
    return employee[employee["id"].isin(managers)][["name"]]



res = find_managers(pd.DataFrame({
    "id": [101, 102, 103, 104, 105, 106],
    "name": ["Alice", "Bob", "Cha", "Dav", "Eve", "Fra"],
    "department": ["A", "A", "A", "A", "A", "B"],
    "managerId": [None, 101, 101, 101, 101, 101],
})) 
print(res)                          