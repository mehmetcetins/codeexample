class example:
    
    def __init__(self):
        pass


    def swit(c,f,e):
        tmp = e[f]
        e[f] = e[c]
        e[c] = tmp
        return e
    
    def middle(array): 
        if len(array) % 2 == 1:
            m = int((len(array) - 1) / 2)
        else : 
            m = int(((len(array) -1 ) / 2) + 1)
        return m

    def quicksort(A,p,r):
        if(p<r):
            q=example.partition(A,p, r)
            example.quicksort(A,p, q-1)
            example.quicksort(A,q+1, r)
        return A
    def partition(A,p,r):
        x = A[r]
        i = p-1

        for j in range(p,r):
        
            if(A[j]<=x):
                i+=1
                example.swit(i,j,A)
            
        example.swit(i+1,r,A)
        return i+1