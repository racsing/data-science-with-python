import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    
    tables = pd.merge(person, address, on="personId", how="left")

    # return tables.loc[: , ["firstName", "lastName", "city", "state"]]

    return tables[['firstName', 'lastName', 'city', 'state']]



# Test Cases
if __name__ == "__main__":
    address = pd.DataFrame({
            "addressId": [1, 2, 3],
            "personId": [3, 1, 2],
            "city": ["New York", "Chicago", "Houston"],
            "state": ["New York", "Illinois", "Texas"]
        })

    person = pd.DataFrame({
            "personId": [1, 2, 3],
            "firstName": ["John", "Dan", "James"],
            "lastName": ["Doe", "Smith", "Brown"]
        })

    print(combine_two_tables(person, address))