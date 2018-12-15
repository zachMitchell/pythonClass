#This is one possible answer to this mission. Get creative and build your own! :D

#If you still want to solve this for yourself; look away!!
class house(object):
    def __init__(self,name,price):
        self.name=""
        #Search through the string and find the name:
        for word in name.split(" "):
            if not word == "The" and not word == "house":
                self.name=word
                break
        
        self.price=price
        self.total=0
        self.items=[]
        self.bedrooms = []
    def getMaterials(self,materialList):
        if len(self.items) > 0:
            self.items = []
        tempPrice = self.price
        #The Priciest item you can buy; this is the key for the materialList
        while not tempPrice == 0:
            mostExpensiveItem = ""
            #Let's figure out the most expensive item we can purchase, then buy from there
            for material in materialList:
                # print(material)
                if ( mostExpensiveItem=="" or materialList[material] > materialList[mostExpensiveItem]) and tempPrice >= materialList[material]:
                    mostExpensiveItem = material
            #If we can't purchase anything, we can't just run this again, it will be an error!
            if mostExpensiveItem == "" or materialList[mostExpensiveItem] > tempPrice:
                break
            else:
                tempPrice-=materialList[mostExpensiveItem]
                self.total+=materialList[mostExpensiveItem]
                self.items.append(mostExpensiveItem)

    #Fill in our list of bedrooms with True for boys, and False for girls:
    def makeBedrooms(self,boys,girls):
        boyOrGirl = True
        for bg in [boys,girls]:
            for i in range(bg):
                self.bedrooms.append(boyOrGirl)
            boyOrGirl = False