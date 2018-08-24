#Riley
#8/24/18
#Comp Prog 2

global Person

class detes: #name classifier for any given person.
    def __init__(self, initf, initl, inita, initc, initp):
         self.f = initf #first and last names.
         self.l = initl
         self.a = inita
         self.c = initc
         self.p = initp

    def getf(self): #Returns the person's first name.
        return self.f
    def getl(self): #Returns the person's last name.
        return self.l
    def geta(self): #Returns the person's age.
        return self.a
    def getc(self): #Returns the person's city.
        return self.c
    def getp(self): #Returns the person's phone #.
        return self.p
    def __str__(self): #Returns the person's details.
        return ("" +str(self.f)+ " " +str(self.l)+ " is " +str(self.a)+ " years old, lives in " +str(self.c)+ ", and thier phone number is " +str(self.p)+ ".")

Person = detes("Riley","Underwood",15,"Pflugerville",6423879968)

def finish(): #Print's the final product.
    print (Person)

finish()
