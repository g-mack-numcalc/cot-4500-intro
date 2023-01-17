import numpy as np  #importing numpy for matrix functions

three_by_three = np.array([ #defining the 3x3 matrix
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
])

i = 0 #defining values to loop through the matrix
j = 0

while i < 3: #loop through the 3 rows
    while j <= i: #loop through columns within each row
        if i == j: #check if they are equal
            three_by_three[i][j] += 1 #add 1 to the correct spots
            j += 1 #go to the next column
        else:
            j += 1 #go to the next column
    i += 1 #go to the next row


for row in three_by_three: 
    print(row) #print each row separately for correct formatting

i = 0 #go back to row 1

while i < 3: #loop through the rows
    j = 0 #go back to column 1
    while j < 3: #loop through the columns
        if j != i: #check if they are not equal
            three_by_three[i][j] += 3 #add 3 to the correct spots
            j += 1 #go to the next column
        else:
            j += 1 #go to the next column
    i += 1 #go to the next row

for row in three_by_three:
    print(row) #print the matrix in the correct formatting

three_by_two = np.delete(three_by_three, 2, 1) #making a new matrix from
#deleting third column

for row in three_by_two:
    print(row) #printing the new 3x2 matrix in the correct formatting
