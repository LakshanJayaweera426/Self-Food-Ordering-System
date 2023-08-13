print("------------ Welcome to Chamathka Food Center ------------")

def menu():
    print("\n----- Select your food categary -----\n")

    print("1. Bakery items...")
    print("2. Rice and curries...")
    print("3. Cake items...")
    print("4. Drinks...")
    print("5. Checkout ")
    print("0. Exit \n")
   
def bakeryItemTot():
    print("\n-----------------------------------------------------")
    print("Iteam    : Quntity : Price\n")
    arrLen=len(bakeryItemArr)
    for i in range(arrLen):
        print (bakeryItemArr[i]," = ",bakeryCountArr[i]," = Rs.",bakeryTot[i])
        allTot=0
        for i in range(arrLen):
            allTot+=bakeryTot[i]              
    print("\nTotal of Bakery Items : Rs.",allTot)
    print("-----------------------------------------------------")

def riceItemTot():
    print("\nIteam    : Quntity : Price\n")
    arrLen=len(riceItemArr)
    for i in range(arrLen):
        print (riceItemArr[i]," = ",riceCountArr[i]," = Rs.",riceTot[i])
        allTot=0
        for i in range(arrLen):
            allTot+=riceTot[i]
    print("\nTotal of Rice & curries Items : Rs.",allTot)
    print("-----------------------------------------------------")

def cakeItemTot():
    print("\nIteam    : Quntity : Price\n")
    arrLen=len(cakeItemArr)
    for i in range(arrLen):
        print (cakeItemArr[i]," = ",cakeCountArr[i]," = Rs.",cakeTot[i])
        allTot=0
        for i in range(arrLen):
            allTot+=cakeTot[i]         
    print("\nTotal of Cake Items : Rs.",allTot)
    print("-----------------------------------------------------")

def drinkItemTot():
    #print("\n-----------------------------------------------------")
    print("\nIteam    : Quntity : Price\n")
    arrLen=len(drinkItemArr)
    for i in range(arrLen):
        print (drinkItemArr[i]," = ",drinkCountArr[i]," = Rs.",drinkTot[i])
        allTot=0
        for i in range(arrLen):
            allTot+=drinkTot[i]        
    print("\nTotal of Drink Items : Rs.",allTot)
    print("-----------------------------------------------------")

menu()


choice= int(input ("Enter number of preferred type : "))
bakeryNo,riceNo,cakeNo,drinkNo=0,0,0,0
bakeryCountArr,riceCountArr,cakeCountArr,drinkCountArr=[],[],[],[]
bakeryItemArr,riceItemArr,cakeItemArr,drinkItemArr=[],[],[],[]
bakeryTot,riceTot,cakeTot,drinkTot=[],[],[],[]
name=""
lastTotalAmount=0

while choice !=5:
    if choice == 1:
        print()
        print("     ------- Bakery Items ------")
        print("     1. Bread     ---> Rs.180.00")
        print("     2. Bun       ---> Rs. 80.00")
        print("     3. Rolls     ---> Rs. 60.00")
        print("     4. Pasties   ---> Rs. 80.00")
        print("     5. Donuts    ---> Rs.100.00")
        print("     6. Cookies   ---> Rs. 30.00")
        print("     0. Exit or Checkout        ")

        bakeryNo=1
        bakeryNo=int(input("\nEnter number of preferred type : "))
        while bakeryNo!=0:
            while bakeryNo !=0:  
                bakeryCount=int(input("Enter number of items : "))
                if bakeryNo==1:
                    bakeryItem="Bread   "
                    bakeryItemArr.append(bakeryItem)
                    bakeryCountArr.append(bakeryCount)
                    total=180*bakeryCount
                    bakeryTot.append(total)
                    lastTotalAmount+=total
                elif bakeryNo==2:
                    bakeryItem="Bun     "
                    bakeryItemArr.append(bakeryItem)
                    bakeryCountArr.append(bakeryCount)
                    total=80*bakeryCount
                    bakeryTot.append(total)
                    lastTotalAmount+=total
                elif bakeryNo==3:
                    bakeryItem="Rolls   "
                    bakeryItemArr.append(bakeryItem)
                    bakeryCountArr.append(bakeryCount)
                    total=60*bakeryCount
                    bakeryTot.append(total)
                    lastTotalAmount+=total
                elif bakeryNo==4:
                    bakeryItem="Pasties "
                    bakeryItemArr.append(bakeryItem)
                    bakeryCountArr.append(bakeryCount)
                    total=80*bakeryCount
                    bakeryTot.append(total)
                    lastTotalAmount+=total
                elif bakeryNo==5:
                    bakeryItem="Donuts  "
                    bakeryItemArr.append(bakeryItem)
                    bakeryCountArr.append(bakeryCount)
                    total=100*bakeryCount
                    bakeryTot.append(total)
                    lastTotalAmount+=total
                elif bakeryNo==6:
                    bakeryItem="Cookies "
                    bakeryItemArr.append(bakeryItem)
                    bakeryCountArr.append(bakeryCount)
                    total=30*bakeryCount
                    bakeryTot.append(total)
                    lastTotalAmount+=total
                else:
                    print("The preferred number you entered is not valid!\n")
                bakeryNo=int(input("Enter number of preferred type : "))

            bakeryItemTot()
            
            

            bakeryAgain=input("\nDo you want buy again bakery items?(y/n) : ")
            if bakeryAgain=="y":
                bakeryNo=int(input("\nEnter number of preferred type : "))
            elif bakeryAgain=="n":
                bakeryNo=0

        #-----------------------------Categary 1 done-------------------------------------
             
              
    elif choice ==2:
        print()
        print("     ----- Rice and Curries -----")
        print("     1. Vegitable rice & curries  ---> Rs.250.00")
        print("     2. Fish rice & curries       ---> Rs.350.00")
        print("     3. Chicken rice & curries    ---> Rs.450.00")
        print("     4. Vegitable friedrice       ---> Rs.250.00")
        print("     5. Egg friedrice             ---> Rs.350.00")
        print("     6. Chicken friedrice         ---> Rs.480.00")
        print("     0. Exit or Checkout                        ")

        riceNo=1
        riceNo=int(input("\nEnter number of preferred type : "))
        while riceNo!=0:
            while riceNo !=0:  
                riceCount=int(input("Enter number of items : "))
                if riceNo==1:
                    riceItem="Vegitable rice & curries "
                    riceItemArr.append(riceItem)
                    riceCountArr.append(riceCount)
                    total=250*riceCount
                    riceTot.append(total)
                    lastTotalAmount+=total
                elif riceNo==2:
                    riceItem="Fish rice & curries      "
                    riceItemArr.append(riceItem)
                    riceCountArr.append(riceCount)
                    total=350*riceCount
                    riceTot.append(total)
                    lastTotalAmount+=total
                elif riceNo==3:
                    riceItem="Chicken rice & curries   "
                    riceItemArr.append(riceItem)
                    riceCountArr.append(riceCount)
                    total=450*riceCount
                    riceTot.append(total)
                    lastTotalAmount+=total
                elif riceNo==4:
                    riceItem="Vegitable friedrice      "
                    riceItemArr.append(riceItem)
                    riceCountArr.append(riceCount)
                    total=250*riceCount
                    riceTot.append(total)
                    lastTotalAmount+=total
                elif riceNo==5:
                    riceItem="Egg friedrice            "
                    riceItemArr.append(riceItem)
                    riceCountArr.append(riceCount)
                    total=350*riceCount
                    riceTot.append(total)
                    lastTotalAmount+=total
                elif riceNo==6:
                    riceItem="Chicken friedrice        "
                    riceItemArr.append(riceItem)
                    riceCountArr.append(riceCount)
                    total=480*riceCount
                    riceTot.append(total)
                    lastTotalAmount+=total
                else:
                    print("The preferred number you entered is not valid!")
                riceNo=int(input("Enter number of preferred type : "))

            riceItemTot()
            
            

            riceAgain=input("\nDo you want buy again bakery items?(y/n) : ")
            if riceAgain=="y":
                riceNo=int(input("\nEnter number of preferred type : "))
            elif riceAgain=="n":
                riceNo=0

        #-----------------------------Categary 2 done-------------------------------------
        
    elif choice == 3:
        print()
        print("     -----  Cake items -------")
        print("     1. Chocolate cake   ---> Rs.3500.00")
        print("     2. Vanilla cake     ---> Rs.3000.00")
        print("     3. Red velvet cake  ---> Rs.4500.00")
        print("     4. Lemon cake       ---> Rs.3800.00")
        print("     5. Cheese cake      ---> Rs.5800.00")
        print("     6. Pound cake       ---> Rs.6200.00")
        print("     0. Exit or Checkout                ")

        cakeNo=1
        cakeNo=int(input("\nEnter number of preferred type : "))
        while cakeNo!=0:
            while cakeNo !=0:  
                cakeCount=int(input("Enter number of items : "))
                if cakeNo==1:
                    cakeItem="Chocolate cake  "
                    cakeItemArr.append(cakeItem)
                    cakeCountArr.append(cakeCount)
                    total=3500*cakeCount
                    cakeTot.append(total)
                    lastTotalAmount+=total
                elif cakeNo==2:
                    cakeItem="Vanilla cake    "
                    cakeItemArr.append(cakeItem)
                    cakeCountArr.append(cakeCount)
                    total=3000*cakeCount
                    cakeTot.append(total)
                    lastTotalAmount+=total
                elif cakeNo==3:
                    cakeItem="Red velvet cake "
                    cakeItemArr.append(cakeItem)
                    cakeCountArr.append(cakeCount)
                    total=4500*cakeCount
                    cakeTot.append(total)
                    lastTotalAmount+=total
                elif cakeNo==4:
                    cakeItem="Lemon cake      "
                    cakeItemArr.append(cakeItem)
                    cakeCountArr.append(cakeCount)
                    total=3800*cakeCount
                    cakeTot.append(total)
                    lastTotalAmount+=total
                elif cakeNo==5:
                    cakeItem="Cheese cake     "
                    cakeItemArr.append(cakeItem)
                    cakeCountArr.append(cakeCount)
                    total=5800*cakeCount
                    cakeTot.append(total)
                    lastTotalAmount+=total
                elif cakeNo==6:
                    cakeItem="Pound cake      "
                    cakeItemArr.append(cakeItem)
                    cakeCountArr.append(cakeCount)
                    total=6200*cakeCount
                    cakeTot.append(total)
                    lastTotalAmount+=total
                else:
                    print("The preferred number you entered is not valid!")
                cakeNo=int(input("Enter number of preferred type : "))

            cakeItemTot()
            
            

            cakeAgain=input("\nDo you want buy again bakery items?(y/n) : ")
            if cakeAgain=="y":
                cakeNo=int(input("\nEnter number of preferred type : "))
            elif cakeAgain=="n":
                cakeNo=0

        #-----------------------------Categary 3 done-------------------------------------
    elif choice == 4:
        print()
        print("     ------  Drink Items -------")
        print("     1. Coffee       ---> Rs.150.00")
        print("     2. Tea          ---> Rs. 80.00")
        print("     3. Milkshake    ---> Rs.250.00")
        print("     4. Energy drink ---> Rs.800.00")
        print("     5. Iced tea     ---> Rs.350.00")
        print("     6. Mocktails    ---> Rs.180.00")
        print("     0. Exit or Checkout           ")

        drinkNo=1
        drinkNo=int(input("\nEnter number of preferred type : "))
        while drinkNo!=0:
            while drinkNo !=0:  
                drinkCount=int(input("Enter number of items : "))
                if drinkNo==1:
                    drinkItem="Coffee        "
                    drinkItemArr.append(drinkItem)
                    drinkCountArr.append(drinkCount)
                    total=150*drinkCount
                    drinkTot.append(total)
                    lastTotalAmount+=total
                elif drinkNo==2:
                    drinkItem="Tea           "
                    drinkItemArr.append(drinkItem)
                    drinkCountArr.append(drinkCount)
                    total=80*drinkCount
                    drinkTot.append(total)
                    lastTotalAmount+=total
                elif drinkNo==3:
                    drinkItem="Milkshake     "
                    drinkItemArr.append(drinkItem)
                    drinkCountArr.append(drinkCount)
                    total=250*drinkCount
                    drinkTot.append(total)
                    lastTotalAmount+=total
                elif drinkNo==4:
                    drinkItem="Energy drink  "
                    drinkItemArr.append(drinkItem)
                    drinkCountArr.append(drinkCount)
                    total=800*drinkCount
                    drinkTot.append(total)
                    lastTotalAmount+=total
                elif drinkNo==5:
                    drinkItem="Iced tea      "
                    drinkItemArr.append(drinkItem)
                    drinkCountArr.append(drinkCount)
                    total=350*drinkCount
                    drinkTot.append(total)
                    lastTotalAmount+=total
                elif drinkNo==6:
                    drinkItem="Mocktails     "
                    drinkItemArr.append(drinkItem)
                    drinkCountArr.append(drinkCount)
                    total=180*drinkCount
                    drinkTot.append(total)
                    lastTotalAmount+=total
                else:
                    print("The preferred number you entered is not valid!")
                drinkNo=int(input("Enter number of preferred type : "))

            drinkItemTot()
            
            

            drinkAgain=input("\nDo you want buy again bakery items?(y/n) : ")
            if drinkAgain=="y":
                drinkNo=int(input("\nEnter number of preferred type : "))
            elif drinkAgain=="n":
                drinkNo=0

        #-----------------------------Categary 4 done-------------------------------------

    elif choice == 0:
        print ("\n------ Have a nice day! -----")
        break
    else:
        print("Sorry! Invalid number.")
        

    menu()
    choice= int(input ("Enter number of preferred type : "))
               
else:   
    countMenuItem=0
    if bakeryCountArr:
        bakeryItemTot()
        countMenuItem+=1
    if riceCountArr:
        riceItemTot()
        countMenuItem+=1
    if cakeCountArr:    
        cakeItemTot()
        countMenuItem+=1
    if drinkCountArr:
        drinkItemTot()
        countMenuItem+=1
    if countMenuItem==0:
        print("You didn't select any Items!")
                
    if countMenuItem>0:
        print("\nThe total of all items : Rs. ",lastTotalAmount)
        name=input("\nEnter name for your order : ")
        print("\n-----------------------------------------------------")
        print("\n-- Thank you for using our services. Stay with us. --\n\nYour order be ready within 5 minutes.")
    

    

 