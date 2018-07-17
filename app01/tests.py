from django.test import TestCase

# Create your tests here.


class Animal(object):

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return self.name+": "+str(self.age)



alex=Animal("alex",111)
egon=Animal("egon",111)
print(alex)
print(egon)