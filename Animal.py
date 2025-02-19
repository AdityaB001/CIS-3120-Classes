class Animal:
    def __init__(self,name): 
        self.__name= name
        print("hello, I am", self.__name)

    def walk(self):
        print("tik tok")

    def eat(self):
        print("chomp chomp")

    def scratch(self):
        print("scratch scratch!!")

    def fart(self):
        print("Puff puff")

    def sleep(self):
        print ("zzz zzz")

    def talk(self):
        print("hi")