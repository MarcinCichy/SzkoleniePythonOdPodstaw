#-------------------------------------------------------------
# Zadanie 17
## Rozwiąż przykładowe zadanie na serwisie Codility:
## https://app.codility.com/demo/take-sample-test/



# """
# This is a demo task.

# Write a function:

#     def solution(A)

# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:

#         N is an integer within the range [1..100,000];
#         each element of array A is an integer within the range [−1,000,000..1,000,000].

# """
def solution (A):
    lista=[]                                
    for i in range(0,len(A)):               
        lista.append(A[i])
    lista.sort()              
                  
    if min(lista) < -1_000_000 or max(lista) > 1_000_000:   
        print("List is out of range!!!")
    else:
        if max(lista) < 0:                  
            k=1                             
        elif max(lista) == 1:                                             
            k = max(lista)+1               
        else:
            rangelist = max(lista)+1        
            for k in range(1,rangelist+1):  
                if k not in lista:                   
                    break        
        return k      
    


# Listy do testowania
#a=[-145,-258,-654,-55,-2,-548,-3,-555,-255]
#a=[-145,-258,-654,-55,-2,-548,-3,-555,-255,1]
#a=[1_000_001,50,-3,56,23,-2,3,9,55,-23,67,12,-11,345,1,0,2,4,5,6,7,8,10,11,12,13,14]
#a=[-48752,50,-3,56,7,23,15,-2,3,9,55,-23,67,12,0,-11,345,2,5,6,4,8,10,12,1,13,14]
a=[1,2,57,9,45,7,23,8,962,4,5,3]

# Listy do testowania - przypadki z Codility
#a=[1, 3, 6, 4, 1, 2]
#a=[1, 2, 3]
#a=[-1,-3]

# Poniższej linijki nie dawałem do Codility
print("The smallest positive integer (greater than 0) that does not occur in A, is:",solution(a),".")
