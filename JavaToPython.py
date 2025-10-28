class Dog:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def bark(self):
        print("Woof! Woof!")
        
    def celebrateBirthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")
        
        
    def getInfo(self):
        return f"{self.name} is {self.age} years old."

    
def main():
    my_dog = Dog("Buddy", 3)
    my_dog.bark()
    print(my_dog.getInfo())
    my_dog.celebrateBirthday()
    print(my_dog.getInfo())


if __name__ == "__main__":
    main()
