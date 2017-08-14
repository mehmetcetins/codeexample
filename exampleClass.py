class example:
    
    def __init__(self):
        pass


    def swit(c,f,e):
        tmp = e[f]
        e[f] = e[c]
        e[c] = tmp
        return e
