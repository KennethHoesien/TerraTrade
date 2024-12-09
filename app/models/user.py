from flask_login import UserMixin
from app.db_manager import fetchone

class User(UserMixin):
    
    def __init__(self, user_id, password, name, address, role):
        self.user_id = user_id
        self.password = password
        self.name = name
        self.address = address
        self.role = role

    @staticmethod 
    def findMatchOR(keys, values):
        # Build the SQL query
        sql = "SELECT `UserId`, `Password`, `Name`, `Address`, `Role` FROM Users WHERE "
        where = ' OR '.join(map(lambda k: f"`{k}` = %s", keys))
        query = sql + where
        print(f"Executing SQL: {query}")
        # Execute the query and fetch one result
        result = fetchone(query, values)
    
        # If no result is found, return None
        if not result:
            return None
        # Unpack the result into the User constructor
        return User(*result)