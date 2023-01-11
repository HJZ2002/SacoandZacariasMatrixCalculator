import numpy as  np

#Addition
def Addition(A, B):
    if ((len(A) == len(B)) and (len(A[0]) == len(B[0]))):
        Add = np.add(A,B)
        print(Add)
    else:
        print("Not Possible")

mat1 = np.array([ [2,1,3] , [3,-2,1] , [-1,0,1] ])
mat2 = np.array([ [1,-2] , [2,1] , [4,-2] ])
mat3 = np.array([ [2,-1] , [3,0] , [-5,2] ])
mat4 = np.array([ [1,6] , [-1,-2] , [0,-3] ])

#Results
print(" Answer = ",end='');Addition(mat1,mat2)
print(" Text 1 = ",end='');Addition(mat3,mat4)


#Subtraction
def Subtraction(A,B):
    if (len(A) == len(B) and len(A[0]) == len(B[0])):
        less = np.subtract(A, B)
        print(less)
    else:
        print("Not Possible")

minus = np.array([[3,-1] , [-2,2]])
sub = np.array([ [2,0] , [1,4]])

#Results
print(" Result = ",end='');Subtraction(minus,sub)



# Multiplication
def Multiplication(A,B):
    if (len(A[0]) == len(B)):
        product = np.matmul(A,B)
        print(product)
    else:
        print("Not Possible")
times1 = np.array([ [2,1,3] ])
times2 = np.array([ [-2] , [1] , [-3]])
times3 = np.array([ [1,0,-3] , [-2,4,1]])
times4 = np.array([ [1,0,4,1] , [-2, 3 ,-1, 5] , [0,-1,2,1] ])
times5 = np.array([ [1,-2] , [0,4] , [-3,1] ])
times6 = np.array([ [2,-1] , [3,0]])


#Results
print("Answer 3 =", end = ''); Multiplication(times1,times2)
print("Answer 4 =", end = ''); Multiplication(times3,times4)
print("\nDC=\n", end = ''); Multiplication(times6,times5)














