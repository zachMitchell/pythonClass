#This is where the customer asks for your help! He's responsible for everything, including the materials, and how you built the house
#In other words, this is the checking software ;P It will see if your class works the way it was described in "mission.md"

#If you are caleb; and are reading this... HELLO! Otherwise... you can replace the name ;P
architectName = "Caleb"

from houseClass import *
from random import randrange as rnd
materials=[{
    "Plutonium":32,
    "Cheese":1,
    "Nails":4,
    "The Universe":1000,
    "Metal":16,
    "Caleb's BBQ Chicken Pizza":2,
    "Wood":8,
},
{
    "Pack of gonzolez":6,
    "Chillidog":3,
    "light switch":12,
    "security system":96,
    "fencing":48,
    "Alaska":500,
    "floor tiles":24,
}]

customerNames = ["MonsieurCahleb","Charles","Adam","Joshua","Gracey","Victoria","Zachary","Jessie","Chloe","Nokie","Belac","JohnCena","BobRoss"]

def runCheck():
    okFail = ["FAIL","OK"]
    points = 0
    #Materials, budget and the customer name are all random so the programmer cannot make pre-defined things in the class.
    materialList = materials[ rnd(len(materials)) ]
    customerName = customerNames[rnd(len(customerNames))]

    #We need a minimum of three items, so the lowest budget will be 3 * the least expensive item:
    maxBudget = 0
    minBudget = -1
    for material in materialList:
        if materialList[material] > maxBudget:
            maxBudget = materialList[material]
        if materialList[material] < minBudget or minBudget == -1:
            minBudget = materialList[material]
    minBudget*=3

    customerBudget = rnd(minBudget,maxBudget)

    #Oh, and the bedroom count is also random:
    rndBoys = rnd(11)
    rndGirls = rnd(11)

    #Let's check absolutely everything in dialog format ;P
    print("Hello there "+architectName+"! My name is "+customerName+", and I need a house! It should have pizzaz, and I have a good name for it! I call it: (wait for it...)")
    print('"The '+customerName+' house"')
    print("My budget is $"+str(customerBudget)+" and...")
    try:
        custHouse = house('The '+customerName+' house',customerBudget)
        nameOk = 0
        if custHouse.name == customerName:
            nameOk+=1
            points+=1
        #Check to see if the name was properly processed:
        print("\nName - '"+custHouse.name+"': "+okFail[nameOk])

        print("\nIt needs "+str(rndBoys+rndGirls)+" rooms, "+str(rndBoys)+" for boys and "+str(rndGirls)+" for girls...")

        custHouse.makeBedrooms(rndBoys,rndGirls)

        bgCheck = [0,0]
        for tf in custHouse.bedrooms:
            if tf:
                bgCheck[0]+=1
            else:
                bgCheck[1]+=1
        bedOk = 0
        if bgCheck[0] == rndBoys and bgCheck[1] == rndGirls:
            bedOk+=1
            points+=1
        #Count of the bedrooms to see if everything checks out:
        print("\nBedrooms- B,"+str(bgCheck[0])+" G,"+str(bgCheck[1])+": "+okFail[bedOk])

        print("Here are the materials for the house, (3 or more items required) BUILD AWAY, "+architectName.upper()+"!")

        custHouse.getMaterials(materialList)

        #Go through all the materials and check the total price:
        for item in custHouse.items:
            print(item+" - $"+str(materialList[item]) )
        priceOk = 0
        if custHouse.total <= customerBudget and len(custHouse.items) >=3 and not custHouse.total == 0:
            priceOk = 1
            points+=1
        print("Total - $"+str(custHouse.total)+": "+ okFail[priceOk])

        allOk = 0
        if points == 3:
            allOk=1
        print("\n\nTotal correct - "+str(points)+"/3: "+okFail[allOk])
        if allOk == 1:
            print("Whoah! That house looks awesome!! Your the best, "+architectName+"!\n\n**"+customerName+" skips into the house with a smile on their face!**\n\nMISSION COMPLETE!")
        else:
            print("Hmm, Looks good, but It's a little off... could you try that again "+architectName+"?")
            print("\n\n\033[91mError!\033[0m Looks like the house wasn't built correctly; check out your score above to see what went wrong.")
            
    except NameError as e:
        print("\n...Wait, WHERE'S THE HOUSE?! I DON'T SEE THE HOUSE! IT WAS GONNA BE AWESOME AND... and... :'(")
        print("\n**"+customerName+" walks away crying cuz no house :(**")
        print("\n\033[91mError!\033[0m You forgot to define the house (Or some other value)... please check 'mission.md' for more details.")

        print("Here's what python had to say: \n"+str(e) )


if __name__ == "__main__":
    runCheck()