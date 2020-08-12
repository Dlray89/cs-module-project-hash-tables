# To Find the first repeated word in a string  from collections 
from collections import Counter
def no_dups(n):
   # first split given string separated by space into words
   w = n.split()
   con = Counter(w)
   for key in w:
       if con[key]>1:
           print ("REPEATED WORD IS: ", con)
       else:
            return 
    


    
    
    







if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))