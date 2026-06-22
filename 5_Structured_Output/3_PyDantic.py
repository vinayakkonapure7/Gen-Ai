from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):

    name:str
    age: int =24                                #Deafult Value
    gender:Optional[str]=None                   #Optional
    email:EmailStr                              #EmailVaildation
    cgpa:float=Field(gt=0,lt=10,default=5.0,description="decimal value of student")    #Constraint | DeafultValue | Description(annotation)


new_student={"name":"john","age":'30',"email":"john@gmail.com","cgpa":9.6}

student=Student(**new_student)
student_json=student.model_dump_json()
print(student)
print(student_json)