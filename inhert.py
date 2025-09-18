class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(f"{self.name} makes a sound.")

george=Animal("Buddy")


class Dog(Animal):
    def __init__(self, breed):
        self.breed=breed
    def speak(self):
        print(f"{george.name} barks. He is a {self.breed}")

dog=Dog("Daschund")
dog.speak()