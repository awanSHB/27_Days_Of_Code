class User:
    def __init__(self, user_id, username) -> None:
        self.id = user_id
        self.name = username
    
user_1 = User("0003", "Sohaib")
print(user_1.id, user_1.name)
print(user_1.name)
