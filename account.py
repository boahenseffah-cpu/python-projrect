class Bankaccount():
    def __init__(self,balance,name,typeofaccount):
        self.balance=balance
        self.name=name
        self.typeofaccount=typeofaccount

    def display(self):
        print(self.name,self.balance,self.typeofaccount)


bankaccount1=Bankaccount(500,"ransford","current account")
bankaccount1.display()
    


