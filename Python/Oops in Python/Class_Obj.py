class Ns(object):
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.course = ["NS", "Loni", "Vijayapur"]
        
    def speak(self):
        print("Hi, I am", self.name, "\nand my age is:", self.age, "\nUSN IS: ", self.usn)
        
    def change_age(self, age):  
        self.age = age
        
    def add_usn(self, usn):  
        self.usn = usn

loni1 = Ns("Nagaraj Loni", 21) 
loni2 = Ns("Loni", 20)

loni1.change_age(20)
loni1.add_usn("3BR22CS***")

loni1.speak()

loni1.change_age(22) 
loni1.add_usn("3BR22CS999") 
