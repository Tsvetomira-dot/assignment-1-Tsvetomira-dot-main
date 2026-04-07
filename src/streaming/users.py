"""
users.py
--------
Implement the class hierarchy for platform users.

Classes to implement:
  - User (base class)
    - FreeUser
    - PremiumUser
    - FamilyAccountUser
    - FamilyMember
"""
class User:
    def __init__(self, user_id: str, name: str, age: int):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.sessions = []

    def add_session(self, session):
        self.sessions.append(session)

class FreeUser(User):
    Max_Skips_Per_Hour = 6

class PremiumUser(User):
    def __init__(self, user_id: str, name: str, age: int, subscription_start):
        super().__init__(user_id, name, age)
        self.subscription_start = subscription_start

class FamilyAccountUser(User):
    def __init__(self, user_id: str, name: str, age: int):
        super().__init__(user_id, name, age)
        self.sub_users = []

    def add_sub_user(self, sub_user):
        self.sub_users.append(sub_user)

class FamilyMember(User):
    def __init__(self, user_id: str, name: str, age: int, parent):
        super().__init__(user_id, name, age)
        self.parent = parent