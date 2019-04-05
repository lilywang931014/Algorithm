print("Before import")
import math

print("Before functionA")
def functionA():
    print("FunctionA")

print("Before functionB")
def functionB():
    print("function B {}".format(math.sqrt(100)))

print("Before __name__ guard")
if __name__ == "__main__":
    functionA()
    functionB()
print("After __name__ guard")
