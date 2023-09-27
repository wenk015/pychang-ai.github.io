def main():
    print("hellworld, my phone")
    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}
    C = A & B
    C = A.intersection(B)
    C = A.union(B)
    print(C)
 
class Student:
    def __init__(self, name, grade) :
        self.name = name
        self.grade = grade
    def displayStudent(self):
        print("Name = " + self.name)
        print("Grade = " + self.grade)
    def whoami(self):
       

if __name__ == '__main__':
    main()
