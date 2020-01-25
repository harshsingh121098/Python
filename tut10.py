class animal:
    def __init__(
    self,birthType = "unknown",
    appearence="unknown",
    blooded="unknown"):
        self.__birthType=birthType
        self.__appearence=appearence
        self.__blooded=blooded
    @property
    def birthType(self):
        return self.__birthType
    @birthType.setter
    def birthType(self,birthType):
        self.__birthType=birthType
    @property
    def appearence(self):
        return self.__appearence
    @appearence.setter
    def appearence(self,appearence):
        self.__appearence=appearence
    @property
    def blooded(self):
        return self.__blooded
    @blooded.setter
    def blooded(self, blooded):
        self.__blooded=blooded
    #type(self)
    def __str__(self):
        return "A{} is{} it is {} it is"\
            "{}".format(type(self).__name__,
                            self.birthtype,
                            self.appearence,
                            self.blooded)
class reptile(animal):
    def __init__(
        self,
        birthtype="born ina an egg or born alive",
        appearence="dry scales",
        blooded="cold blooded"):
        animal.__init__(self,birthType,appearence,blooded) 
def main():
    animal1=animal("born alive")
    print(animal1.birthType)
    print(animal1)
    print()                               
    reptile1=reptile()
    print(reptile1.birthType)
    print(reptile1.appearence)
    print(reptile1.blooded)      
    def getBirthType(theobject):
        print("The {} is {}".format(type(theobject).__name__,theobject.birthtype)) 
        getBirthType(reptile1)
main()                                

