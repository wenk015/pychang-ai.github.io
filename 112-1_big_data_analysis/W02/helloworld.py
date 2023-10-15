def main():
    print("hellworld, my phone")
    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}
    C = A & B
    C = A.intersection(B)
    C = A.union(B)
    print(C)


class Student:
    def __init__(self, name: str, grade: int):
        self.name = name
        self.__grade = grade

    # def __init__(self, name: str, grade: int, private_grade: int):
    #     self.name = name
    #     self.grade = grade
    #     self.__grade = private_grade

    def displayStudent(self):
        print("Name = " + self.name)
        print("Grade = " + self.grade)

    def whoami(self):
        return self.name

    def getGrade(self):
        print(self.__grade)


if __name__ == '__main__':
    print("nothing")
    s = Student("jack", 60)
    print("Who am I " + s.whoami())
    
    # import os, sys
    # print(sys.path)
