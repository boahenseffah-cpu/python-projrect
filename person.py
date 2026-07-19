class Person():
    def __init__(self,name,country,age,email,phonenumber):
        self.name=name
        self.country=country
        self.age=age
        self.email=email
        self.phonenumber=phonenumber

    def display(self):
        print(self.name,self.country,self.age,self.email,self.phonenumber)
person1=Person("ransford","france",14,"ransford834@gmail.com",745912114)
person1.display()

person2=Person("david","france",10,"david835@gmail.com",145896378)
person2.display()