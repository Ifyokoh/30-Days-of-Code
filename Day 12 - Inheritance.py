#TASK
# You are given two classes, Person and Student, where Person is the base class and Student is the derived class. 

# Complete the Student class by writing the following:

# A Student class constructor, which has  parameters:
# A string, firstName.
# A string, lastName.
# An integer, id.
# An integer array (or vector) of test scores, scores.
# A char calculate() method that calculates a Student object's average and returns the grade character representative of 
# their calculated average:


#SOLUTION
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        a = sum(self.scores)/ len(self.scores)
        if 90 <= a <= 100:
            return 'O'
        elif 80 <= a < 90:
            return 'E'
        elif 70 <= a < 80:
            return 'A'
        elif 55 <= a < 70:
            return 'P'
        elif 40 <= a < 55:
            return 'D'
        else:
            return 'T'
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) 
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())