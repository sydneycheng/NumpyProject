import numpy as np
import random


arr01 = np.array([[1,2,3],
                [4,5,6]]) #we have 2 rows and 3 columns here --> each value separated by a comma is one row

arr02 = np.array([0.0, 0.1, 0.2, 0.3, 0.4]) 

for row in arr01:
    print(row)
    for col in row: #goes through each element in the row
        print(col,end= ' ')
    print()


for i in arr01.flat:    #no longer in columns and rows
    print(i)



arr03 = np.zeros(5)


arr04 = np.ones((2,4), dtype=int)   #we want an array of 2 rows and 4 columns


arr05 = np.full((3,5), 13)  #3 rows, 5 columns

#EXERCISE
#############

# create a 2 dimensional array of 5 integer elements each using the random module
# and list comprehension

#this is the "range" function in numpy
arr06 = np.arange(5)

arr07 = np.arange(5, 10)

arr08 = np.arange(10, 1, -2)

arr09 = np.linspace(0.0, 1.0, num=5)

arr10 = np.arange(1,21).reshape(4,5)    #reshaped from one element to 2 (4,5) -- this is a 4 by 5



num01 = np.arange(1,6)

num02 = num01*2

num03 = num01**3    #this is broadcasting - takes a scalar value and expands it to match the same number of elements in the array
                    #it's the same as... num02=num01 x [2,2,2,2,2]

num01 += 10

num04 = num01 * num02

num05 = num01 > 13

num06 = num03 > num01

#Here we have an array of 4 students grades on 3 exams
#row = studnet
#col = exam
grades = np.array([[87,96,70], [100,87,90],
                    [94,77,90],[100,81,82]])


print(grades.sum())
print(grades.mean())
print(grades.std()) #standard deviation
print(grades.var()) #variance

#calculate average on all rows for each column --> axis 0
grades_by_exam = grades.mean(axis=0)

#calculate average on all columns for each row --> axis 1
grades_by_student = grades.mean(axis=1)


num07 = np.array([1, 4, 9, 16, 25, 36])
num08 = np.sqrt(num07)  #square root

num09 = np.array([10,20,30,40,50,60])   #1 dimensional array of 6 values
num10 = np.add(num07,num09)
#same as
num10 = num07 + num09

num11 = np.multiply(num09, 5)
#same as
num11 = num09 * 5   #this is broadcasting

num12 = num09.reshape(2,3)  #now 2 rows and 3 columns
num13 = np.array([2,4,6])

num14 = np.multiply(num12, num13)


print()
