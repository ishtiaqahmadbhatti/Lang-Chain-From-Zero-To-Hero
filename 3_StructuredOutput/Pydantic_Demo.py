from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Student(BaseModel):
    name:str = Field(..., description="The name of the student")
    age: int = Field(default=None, description="The age of the student")
    grade: str = Field(..., description="The grade of the student")
    email: Optional[EmailStr] = Field(default=None, description="The email address of the student")

new_student = Student(name="Alice", grade="A", email="alice@tech.co")

print(new_student)
print(new_student.name)
print(new_student.age)
print(new_student.grade)
print(new_student.email)