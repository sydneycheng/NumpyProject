## Numpy Exercise 2
import numpy as np

## This array documnets the last 5 sales for each of Superstore's four cash registers. 
salesArray = np.array([[150.68,207.99,107.88,58.99,60.59],
                        [20.89,98.99,258.62,19.76,101.59],
                        [70.66,190.10,134.54,200.14,15.59],
                        [10.52,201.59,140.55,13.99,45.98]])

## Step 1: Print the total sales for the store.
print("-----------------------------------------------   STEP ONE   -----------------------------------------------")

print(salesArray.sum())
print()

## Step 2: What was Superstore's smallest and largest sale? Print them.
print("-----------------------------------------------   STEP TWO   -----------------------------------------------")

#smallest sale
print(salesArray.min())
#largest sale
print(salesArray.max())
print()

## Step 3: Print an array that will show which sales are greater than or equal to $100.
print("-----------------------------------------------   STEP THREE  -----------------------------------------------")

arr01 = salesArray >= 100
print(arr01)
print()

## Step 4: Print the total sales for each register.
print("-----------------------------------------------   STEP FOUR   -----------------------------------------------")

sales_by_register = salesArray.sum(axis=1)
print(sales_by_register)
print()

## Step 5: Superstore is a cashless store and needs to calculate their owed credit card fees. Each sale is subject to a 2% credit card fee.
#           Using the salesArray, create a new array that stores the 2% fee for each sale and register. Print the array and then print the total fees.
print("-----------------------------------------------   STEP FIVE  -----------------------------------------------")

card_fee = salesArray * .02
print(card_fee)

total_fees = card_fee.sum()
print()
print("Total Fees: ", total_fees)
print()

## Step 6: Using your fee array and salesArray, calculate how much profit Superstore made for each sale after paying credit card fees. Store this in a new array and print it.
print("-----------------------------------------------   STEP SIX  -----------------------------------------------")

profit = salesArray - card_fee
print(profit)
print()

## Step 7: Print the sales only for the second and forth cash register
print("-----------------------------------------------   STEP SEVEN  -----------------------------------------------")

register2 = salesArray[1]
register4 = salesArray[3]
print("Sales for register 2: ", register2)
print("Sales for register 4: ", register4)

#OR
#registers2and4 = salesArray[[1,3]]
#print(registers2and4)
print()

## Step 8: Superstore has added a 5th cash register who's data is stored in the array newRegister. Add the new register to the original array. Print the updated salesArray.
print("-----------------------------------------------   STEP EIGHT  -----------------------------------------------")
newRegister = np.array([17.89,13.59,107.89,176.88,56.78])

salesArray = np.vstack((salesArray,newRegister))
print(salesArray)
print()

## Step 9: Register #3 had an error and recorded it's fourth sale ($200.14) incorrectly. The sale should have been $20.14. Update the array to correct this error.
#           Print the array before and after the update to see the change.
print("-----------------------------------------------   STEP NINE  -----------------------------------------------")
print(salesArray)
register3_update = salesArray[2][3] = 20.14
print(salesArray)
print()

