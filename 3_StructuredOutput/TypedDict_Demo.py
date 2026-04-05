from typing import TypedDict

class User(TypedDict):
    id: int
    name: str
    email: str

my_user: User = {
    "id": 1,
    "name": "Alice",
    "email": "ishtiaq.uaar55@gmail.com"
}

print(my_user)