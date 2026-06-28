class student():
    def __init__(self,country,age,contact,name):
        self.country=country
        self.age=age
        self.contact=contact
        self.name=name
        

    def display(self):
        print(self.country,self.age,self.contact,self.name)

    
    
student1=student("france",12,1404896123,"david")
student1.display()

student2=student("england",13,6034895671,"jordan")
student2.display()              