class Aeraport:
    def __init__(self,name="international",location="Tashkent") -> None:
         self.names=name
         self.place=location


    def get_info(self):
        print(f"Name of Airpirt:  {self.names}Location of Airport:  {self.place}")
        
class Airplane:
    def __init__(self, nome, time,where,to):
        self.names = nome
        self.times = time
        self.wh =where
        self.to_city =to

    def info(self):
                print(f"""Plane name: {self.names}\nTime: {self.times}\nWhere from:{self.wh}\nWHere to:{self.to_city}""")
        
lst = []
for i in range(int(input("Enter How many plane flight : "))):
    obj = Airplane(nome=input("Enter the plane name : "),time=input("When : "),where=input("Where from:  "),to=input("Where to:  "))
    lst.append(obj)

for i in lst:
    i.info()
odj1=Aeraport("International","Tashkent")