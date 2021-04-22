import numpy as np

def ask_user():
    dimension = int(input('insert the dimension of the array: '))
    if dimension <1:
        raise ValueError('input dimension must be grather than 1')
    return dimension 

def matrix(dim):
    array = np.ones((dim,dim))
    return array

def multiplication(array):
    for i in range(1, len(array)+1):
        for j in range(1, len(array)+1):
            array[i-1][j-1] = i*j
    return array

def main():
    d = ask_user()
    m = matrix(d)
    mm = multiplication(m)
    print(f'multiplication table:\n{mm}')
if __name__=='__main__':
    main()
