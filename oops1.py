#initiate a class

class employee:
    #special method/magic method/dunder method - constructor
    def __init__(self):
        print("Started executing attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("attributes/data have been initiated")

    def travel(self):
        print(f"Employee is now travelling to Delhi")

# create an instance/object of the class
sam = employee()
print(id(sam))
sam.name="Sam Kumar"
print(sam.name)

# shaktiman=employee()

# print(id(shaktiman))

#printing the atrributes
#print(sam.id)

#calling a method
# sam.travel()

# print(type(sam))