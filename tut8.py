class square:
    def __init__(self,height="0",width="0"):
        self.height=height
        self.width=width

        #this is getter
    @property
    def height(self):
        print("retrieving the height") 

        #put a__before this private field
        return self.__height
    #this is the setter
    @height.setter
    def height(self,value):
        if value.isdigit():
            self.__height= value
        else:
            print("please only enter number for height")
    #getter
    @property
    def width(self):
        print("retrieving the width") 

        #put a__before this private field
        return self.__width
    #this is the setter
    @width.setter
    def width(self,value):
        if value.isdigit():
            self.__width= value
    def getarea(self):
        return int(self.__width)*int(self.__height)
def main():
    aSquare=square()
    height=input("enter height:")
    width=input("enter width:")
    aSquare.height=height
    aSquare.width=width
    print("height"),aSquare.height
    print("width"),aSquare.width
    print("the area is",aSquare.getarea())
main()

