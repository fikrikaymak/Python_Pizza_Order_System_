import datetime
import csv

print("Welcome to Copernican Pizza\n")

# Pizza Super Classini olusturduk
class Pizza:
    def __init__(self,price,details):
        self.price = price
        self.details = details
    def get_price(self):
        return self.price
    def get_details(self):
        return self.details

# Pizza secimi icin Pizza Classin dan kalitim alan yeni alt siniflar olusturduk
class ClassicPizza(Pizza):
    def __init__(self):
        super().__init__(30,"Pizza sauce,mozzarella cheese,salami,mushroom")

class MargaritaPizza(Pizza):
    def __init__(self):
        super().__init__(25,"Pizza sauce,mozzarella cheese,green basil,olive oil")

class TurkishPizza(Pizza):
    def __init__(self):
        super().__init__(40,"Pizza sauce,mozzarella cheese,pepperoni,salami,mini kebab balls,mushroom,green pepper,onion,olive")

class PlainPizza(Pizza):
    def __init__(self):
        super().__init__(24,"Pizza sauce,mozzarella cheese")

class SpecialPizza(Pizza):
    def __init__(self):
        super().__init__(120,"Tomato sause with Adiyaman Red Pepper,Izmir Tulum cheese,Kastamonu garlic,green pepper,sujuk,salami,black olive,onion, corn")


# Extralar icin Extras super class olusturduk

class Extras(Pizza):
    def __init__(self, ingredients,price,details):

        self.ingredients = ingredients
        self.price = price
        self.details = details
    def get_details(self):
        return self.ingredients.get_details() + ' and ' + Pizza.get_details(self)
    def get_price(self):
        return self.ingredients.get_price() + Pizza.get_price(self)
    
# Extralari Extras classindan kalitim alarak yeni nesneler olusturduk
class Olives(Extras):
    def __init__(self, ingredients):
        Extras.__init__(self,ingredients,2,"Olives")

class Mushrooms(Extras):
    def __init__(self, ingredients):
        Extras.__init__(self,ingredients,4,"Mushrooms")

class GoatCheese(Extras):
    def __init__(self, ingredients):
        Extras.__init__(self,ingredients,5,"GoatCheese")

class Beef(Extras):
    def __init__(self, ingredients):
        Extras.__init__(self,ingredients,1,"Beef")

class Onions(Extras):
    def __init__(self, ingredients):
        Extras.__init__(self,ingredients,15,"Onions")

class Corn(Extras):
    def __init__(self, ingredients):
        Extras.__init__(self,ingredients,8,"Corn")
class Nothing(Extras):
    def __init__(self, ingredients):
        Extras.__init__(self,ingredients,0,"None")
        


def main():
# Menuyu dosyasini okuma ve yazma modunda acip print ediyoruz
    with open("Menu.txt", "r+") as f:
        menu = f.read()
        print(menu)
    
# Pizza secimi ve Extra secimi icin input almaliyiz  
    order = int(input("Please choose your pizza base from Menu `1, 2, 3, 4, 5`: "))
    while order not in [1,2,3,4,5]:
        order = int(input("Please specify a valid Pizza option 1 or 2, 3, 4, 5: ")) 
    if order == 1:
        choice = ClassicPizza()
    elif order == 2:
        choice = MargaritaPizza()
    elif order == 3:
        choice = TurkishPizza()
    elif order == 4:
        choice = PlainPizza()
    elif order == 5:
        choice = SpecialPizza()


    bill = 0
    orderExtra = int(input("What would you like for extra? If you wouldnt like, write 0: "))
    while orderExtra not in [11,12,13,14,15,16,0]:
        orderExtra = int(input("Please select a valid option (11,12,13,14,15,16 or 0): ")) 
    if orderExtra == 11:
        details = Olives(choice).get_details()
        bill += Olives(choice).get_price()
    elif orderExtra == 12:
        details = Mushrooms(choice).get_details()
        bill += Mushrooms(choice).get_price()
    elif orderExtra == 13:
        details = GoatCheese(choice).get_details()
        bill += GoatCheese(choice).get_price()
    elif orderExtra == 14:
        details = Beef(choice).get_details()
        bill += Beef(choice).get_price()
    elif orderExtra == 15:
        details = Onions(choice).get_details()
        bill += Onions(choice).get_price()
    elif orderExtra == 16:
        details = Corn(choice).get_details()
        bill += Corn(choice).get_price()
    elif orderExtra == 0:
        details = Nothing(choice).get_details()
        bill += Nothing(choice).get_price()
    print("Your Order: ",bill,"TRY",details)

    time = datetime.datetime.now()
    date = datetime.datetime.strftime(time, '%c')
    
# Kisisel ve odeme bilgileri

    name = input("Please enter your name and surname: ")
    idNo = input("Please enter your ID number: ")
    digits = ["0","2","4","6","8"]
    while len(idNo) != 11 or idNo[-1] not in digits:
        idNo = input("Please enter a valid ID: ")

    creditcardNo=input("Please enter your 16-digit credit card number: ")
    while len(creditcardNo) != 16:
        creditcardNo = input("Please enter a valid credit card number: ")

    cardPassword = input("Please enter your credit card password: ")
    while len(cardPassword) != 4:
        cardPassword = input("Please enter a valid credit card password: ")
#Siparis bilgi yazildi ve order database e eklendi.
    print("\n Your Order Receipt \n")
    data = [{'Name':name,'ID':idNo,'CreditCardNo':creditcardNo,'CardPassword':cardPassword,'Order':details,'Date':date}]

    with open("Orders_DB.csv", "a") as file:  
        writer = csv.DictWriter(file, fieldnames=['Name','ID','CreditCardNo','CardPassword','Order','Date'])
        writer.writerows(data)
        file.close()
    with open("Orders_DB.csv", "r") as f:
        menu = f.read()
        print(menu)
        f.close()
main()
