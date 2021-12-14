yeslist = ['yes','Yes','yeah','Yeah','Y','y']
nolist = ['no', 'No','N','n']

def coffee_menu():
    global coffee_list
    infile = open('Espresso_Drinks.txt', 'r')
    coffee_list = infile.readlines()
    infile.close
    for index in range (len(coffee_list)):
        coffee_list[index] = coffee_list[index].rstrip('\n')
 

def tea_menu():
    global tea_list
    infile = open('Hot_Tea_Drinks.txt', 'r')
    tea_list = infile.readlines()
    infile.close
    for index in range (len(tea_list)):
        tea_list[index] = tea_list[index].rstrip('\n')
   

def drink_determination(tea_list, coffee_list, yeslist, nolist):
    global drink
    global altcream
    global altsug
    teachoice = ['tea','Tea']
    coffeechoice = ['coffee','Coffee']
    drinkchoice = str(input("Firstly, would you like tea or coffee today? "))
    while drinkchoice not in coffeechoice and drinkchoice not in teachoice:
        print('That is an invalid entry.')
        drinkchoice = str(input("Would you like tea or coffee today? "))
    if drinkchoice in teachoice:
        print('These are your tea options', tea_list) 
        drink = str(input('which drink would you like today? '))
        if drink not in tea_list:
            print("I'm sorry that is not on my tea list! ")
            drink = str(input('which drink would you like today? '))
        else:
            print('Excellent choice!')
    elif drinkchoice in coffeechoice:
        print('These are your coffee options', coffee_list) 
        drink = str(input('which drink would you like today? '))
        if drink not in coffee_list:
            print("I'm sorry that is not on my coffee list! ")
            drink = str(input('which drink would you like today? '))
        else:
            print('Excellent choice!')
    
        

    milk = ['2%','Wholemilk','Oatmilk','Soymilk','Coconutmilk','Almondmilk']
    sugar = ['Sugar','Stevia','SweetNLow','Equal','SPLENDA'] 

    altcreamsug = str(input('Would you like to see some of the milk and sugar alternatives? '))
    if altcreamsug in yeslist:
        altcreamsug = True
    if altcreamsug in nolist:
        altcreamsug = False
        altsug = False
        altcream = False
    print(altcreamsug)
    
    if altcreamsug:
        print('We offer these milk substitutes: ', milk, '\nAnd these sugar substitutes: ', sugar)
        altcreamchoice = str(input('Would you like to add an alternative milk? '))
        while altcreamchoice not in yeslist and altcreamchoice not in nolist:
            print('That is an invalid entry.')
            altcreamchoice = str(input('Would you like to add an alternative milk? '))
        if altcreamchoice in yeslist:
            altcream = str(input('Which milk would you like? '))
            if altcream not in milk:
                print("I'm sorry, we do not offer that milk!")
                altcream = str(input('Which milk would you like?.'))
        if altcreamchoice in nolist:
            altcream = False

        altsugchoice = str(input('Are you adding a sugar or sugar substitute today?'))
        while altsugchoice not in yeslist and altsugchoice not in nolist:
            print('That is an invalid entry.')
            altsugchoice = str(input('Would you like to add a sugar or sugar substitute to the order?'))
        if altsugchoice in yeslist:
            altsug = str(input('Which sugar would you like to add? '))
            if altsug not in sugar:
                print("I'm sorry, we do not offer that option!")
                altsug = str(input('Which sugar would you like?.'))
        if altsugchoice in nolist:
            altsug = False
        print('Those are all of our options, your drink recipe is on the way!')
        drink_bar(drink, altcream, altsug)
    elif not altcreamsug:
        print('Those are all of our options, your drink recipe is on the way!')
        drink_bar(drink, altcream, altsug)
    

def drink_bar(drink, altcream, altsug):
    print('\n')
    infile = open('Recipes.txt', 'r')
    for line in infile:
            if line == ' ':
                infile.close  
            elif line != ' ':
                words = line.split()
                if words[0] == drink:
                    print(line.lstrip(drink))
            
    
    
    if altcream and altsug:
        print('Now add 2 ounces of', altcream, 'and 2 ounces of', altsug, '\n')
    elif altcream and not altsug:
        print('Now add 3 ounces of', altcream, '\n')
    elif altsug and not altcream:
        print('Now add 3 ounces of', altsug, '\n')
    print('Enjoy your beverage!')


coffee_menu()
tea_menu()
drink_determination(tea_list, coffee_list, yeslist, nolist)