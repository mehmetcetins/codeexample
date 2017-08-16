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