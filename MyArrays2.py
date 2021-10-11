import numpy as np

#ROWS - Each student (student0, student1, student2, student3)
#COLS - Each Test (Test0, Test1, Test2)
grades = np.array([[87, 96, 70], [100,87,90], [94,77,90], [100,81,82]])



student1 = grades[1]    #this gives all of student1's grades

student0_test1 = grades[0,1]

students0_1 = grades[0:2]   #grades for students0 through student1
                            #the lower bound is not included; the colon means for rows 0 and rows1
                            #we didn't specify which columns, so it will grab all the columns

students1and3 = grades[[1,3]]   #outer brackets are for rows and columns
                                #inner brackets represents rows
                                #here, bcs 1 and 3 are not sequential, we put them in double brackets

#to select students 1 and 3 but only test 2
students1and3_test2 = grades [[1,3] ,2]     #grades[row,col]
                                            #these can be further broken down if we don't want them sequential rows
                                            #like this: grades[ [], [] ]
                                            #if you give it a colon, python knows you want the upper bound and lower bound
all_students_test0 = grades[:,0]

all_students_test1_2 = grades[:,1:3]    #the colon means all rows
                                    #we represent rows 1 and 2 using 1:3

all_students_test0and2 = grades[:,[0,2]]

'''
Use NumPy randon-number generation to create an array of twelve random grades in the range 60
through 100, then reshape the result into a 3-by-4 array.  Calculate the average of all the grades,
the averages of the grades for each test and the averages of the grades for each student.
'''
grades = np.random.randint(60,101,12).reshape(3,4)

grades.mean()


#avg by column (test score)
grades.mean(axis=0)     


#average by row (student)
grades.mean(axis=1)


#SHALLOW COPY
numbers = np.arange(1,6)

numbers_view = numbers.view()

numbers[1] *= 10

#whatever you do to the shallow copy affects the original
numbers_view[1] /= 10

#create a slice of values
numbers_slice = numbers[0:3]


numbers[1] *= 20

#DEEP COPIES
numbers_copy = numbers.copy()

#when we make a change to the original, it will not affect the deep copy
numbers[1] *= 10

grades = np.array([[87,96,70], [100,87,90]])
#Reshape and Resize

#the RESHAPE method produces a shallow copy
grades_reshaped = grades.reshape(1,6)   #reshapes a 2D array into a 1D array

#the RESIZE method changes the original array
grades.resize(1, 6)


#Flatten creates a deep copy
flattended = grades.flatten()

#Raavel creates a shallow copy
raveled = grades.ravel()

raveled[0] = 100
flattended[1] = 100

grades = np.array([[87,96,70], [100,87,90]])

#transpose methode
grades.T    #flips the array


#H-STACK and V-STACK
grades2 = np.array([[94,77,90], [100,81,82]])

h_grades = np.hstack((grades, grades2)) #adds more columns

v_grades = np.vstack((grades, grades2)) #adds more rows



print()