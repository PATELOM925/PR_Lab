import numpy as np

def user_matrix():
    print("Eigen Values can be calculated only of square matrix, Thus N=M")
    N = int(input("Enter no. of Rows (N)"))
    M = int(input("Enter no. of columns (M)"))
    
    if N != M:
        print("Error: Matrix A is not square.")
    
    A = []
    print("Enter the elements row by row (each element separated by a space):")
    
    for i in range(N):
        while True:
            row = input().strip().split()
            if len(row) != M:
                print(f"Error: You must enter exactly {M} elements.")
            else:
                A.append([float(x) for x in row])
                break
             
    return np.array(A)

def main():
    A = user_matrix()
    ans = np.linalg.eigvals(A).round(4)
    print("Eigen Values for your Matrix is : ",ans)
    
if __name__ == "__main__":
    main()