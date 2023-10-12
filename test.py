# a=6
# b=5
# a=a+b
# b=a-b
# a=a-b
# print(a,b)
# a=int(input("asosni kiriting: "))
# n=int(input("darajani kiriting: "))
# natija=a**n
# print("natija-",natija)
# ism=input("ismizni kiriting: ")
# print(ism[len(ism)//2:]+ism[:len(ism)//2:])
class Solution:
    def isPalindrome(self, x: int) -> bool:
        str=x 
        if str(x).reverse()== str(x):
            return True
        else:
            return False