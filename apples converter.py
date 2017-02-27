# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 23:23:47 2017

@author: andag_000
"""

def convert_temp():
    """Converts temperatures."""
    print()
    print("Select operation:")
    print("  a) Fahrenheit to Celsius")
    print("  b) Celsius to Fahrenheit")
    print()
    
    choice2 = input("Selection: ")
    print()
    
    if choice2.lower() == 'a':
        try:
            tempf = float(input("Enter Fahrenheit temperature: "))
            tempfc = (tempf-32) * 5 / 9
            print(tempf,"degrees F is equivalent to",float("%.1f" % tempfc),"degrees C.")
        except:
            print("I'm sorry, that input is invalid.")           
    elif choice2.lower() == 'b':
        try:
            tempc = float(input("Enter Celsius temperature: "))
            tempcf = tempc * 1.8 + 32
            print(tempc,"degrees C is equivalent to",float("%.1f" % tempcf),"degrees F.")
        except:
            print("I'm sorry, that input is invalid.")
    else:
        print("I'm sorry,",choice2,"is an invalid selection.")
        return None

def convert_length():
    """Converts lengths."""
    print()
    print("Select operation:")
    print("  a) miles to kilometers")
    print("  b) kilometers to miles")
    print("  c) feet to meters")
    print("  d) meters to feet")
    print("  e) inches to centimeters")
    print("  f) centimeters to inches")
    print()
    
    choice3 = input("Selection: ")
    print()
    
    if choice3.lower() == 'a':
        try:
            lengthm = float(input("Enter length in miles: "))
            lengthmk = lengthm * 1.60934
            print(lengthm,"miles is equivalent to",float("%.1f" % lengthmk),"kilometers.")
        except:
            print("I'm sorry, that input is invalid.")
    elif choice3.lower() == 'b':
        try:
            lengthk = float(input("Enter length in kilometers: "))
            lengthkm = lengthk * 0.62137
            print(lengthk,"kilometers is equivalent to",float("%.1f" % lengthkm),"miles.")
        except:
            print("I'm sorry, that input is invalid.")
    elif choice3.lower() == 'c':
        try:
            lengthf = float(input("Enter length in feet: "))
            lengthfme = lengthf * 0.3048
            print(lengthf,"feet is equivalent to",float("%.1f" % lengthfme),"meters.")
        except:
            print("I'm sorry, that input is invalid.")
    elif choice3.lower() == 'd':
        try:
            lengthme = float(input("Enter length in meters: "))
            lengthmef = lengthme * 1/0.3048
            print(lengthme,"meters is equivalent to",float("%.1f" % lengthmef),"feet.")        
        except:
            print("I'm sorry, that input is invalid.")
    elif choice3.lower() == 'e':
        try:
            lengthi = float(input("Enter length in inches: "))
            lengthic = lengthi * 2.54
            print(lengthi,"inches is equivalent to",float("%.1f" % lengthic),"centimeters.")
        except:
            print("I'm sorry, that input is invalid.")
    elif choice3.lower() == 'f':
        try:
            lengthc = float(input("Enter length in centimeters: "))
            lengthci = lengthc * 1/2.54
            print(lengthci,"centimeters is equivalent to",float("%.1f" % lengthci),"inches.")
        except:
            print("I'm sorry, that input is invalid.")
    else:
        print("I'm sorry,",choice3,"is an invalid selection.")
        return None
    
def convert_mass():
    """Converts masses and weights."""
    print()
    print("Select operation:")
    print("  a) pounds to kilograms")
    print("  b) kilograms to pounds")
    print("  c) ounces to grams")
    print("  d) grams to ounces")
    print()
    
    choice4 = input("Selection: ")
    print()
    
    if choice4.lower() not in ['a','b','c','d']:
        print("I'm sorry, that selection is invalid.")
        return None
    elif choice4.lower() == 'a':
        massp = float(input("Enter mass/weight in pounds: "))
        masspk = massp * 0.453592
        print(massp,"pounds is equivalent to",float("%.1f" % masspk),"kilograms.")
    elif choice4.lower() == 'b':
        massk = float(input("Enter mass/weight in kilograms: "))
        masskp = massk * 1/0.453592
        print(massk,"kilograms is equivalent to",float("%.1f" % masskp),"pounds.")
    elif choice4.lower() == 'c':
        masso = float(input("Enter mass/weight in ounces: "))
        massog = masso * 28.3495
        print(massog,"ounces is equivalent to",float("%.1f" % massog),"grams.")
    elif choice4.lower() == 'd':
        massg = float(input("Enter mass/weight in grams: "))
        massgo = massg * 1/28.3495
        print(massg,"grams is equivalent to",float("%.1f" % massgo),"ounces.")

def convert_volume():
    """Converts volumes."""
    print()
    print("Select operation:")
    print("  a) gallons to liters")
    print("  b) liters to gallons")
    print("  c) quarts to liters")
    print("  d) liters to quarts")
    print("  e) cups to milliliters")
    print("  f) milliliters to cups")
    print("  g) fluid ounces to milliliters")
    print("  h) milliliters to fluid ounces")
    print()
    
    choice5 = input("Selection: ")
    print()
    
    if choice5.lower() not in ['a','b','c','d','e','f','g','h']:
        print("I'm sorry, that selection is invalid.")
        return None
    elif choice5.lower() == 'a':
        volg = float(input("Enter volume in gallons: "))
        volgl = volg * 3.78541
        print(volg,"gallons is equivalent to",float("%.1f" % volgl),"liters.")
    elif choice5.lower() == 'b':
        voll = float(input("Enter volume in liters: "))
        vollg = voll * 1/3.78541
        print(voll,"liters is equivalent to",float("%.1f" % vollg),"gallons.")
    elif choice5.lower() == 'c':
        volq = float(input("Enter volume in quarts: "))
        volql = volq * 0.946353
        print(volq,"quarts is equivalent to",float("%.1f" % volql),"liters.")
    elif choice5.lower() == 'd':
        volL = float(input("Enter volume in liters: "))
        volLq = volL * 1/0.946353
        print(volL,"liters is equivalent to",float("%.1f" % volLq),"quarts.")
    elif choice5.lower() == 'e':
        volc = float(input("Enter volume in cups: "))
        volcm = volc * 236.588
        print(volc,"cups is equivalent to",float("%.1f" % volcm),"milliliters.")
    elif choice5.lower() == 'f':
        volm = float(input("Enter volume in milliliters: "))
        volmc = volm * 1/236.588
        print(volm,"milliliters is equivalent to",float("%.1f" % volmc),"cups.")
    elif choice5.lower() == 'g':
        volf = float(input("Enter volume in fluid ounces: "))
        volfm = volf * 29.5735
        print(volf,"fluid ounces is equivalent to",float("%.1f" % volfm),"milliliters.")
    elif choice5.lower() == 'h':
        volM = float(input("Enter volume in milliliters: "))
        volMf = volM * 1/29.5735
        print(volM,"milliliters is equivalent to",float("%.1f" % volMf),"fluid ounces.")

def main_menu():
    """Root menu to choose what to convert"""
    print()
    print("What would you like to do?")
    print("  a) convert temperature")
    print("  b) convert length")
    print("  c) convert mass")
    print("  d) convert volume")
    print("  q) quit")
    
    choice = input("Selection: ")
    if choice.lower() in ['a','b','c','d','q']:
        return choice.lower()
    else:
        print("I'm sorry,",choice,"is an invalid selection.")
        return None
    
def main():
    while True:
        choice = main_menu()
        if choice == None:
            continue
        if choice == 'q':
            print("See ya!")
            break
        elif choice == 'a':
            convert_temp()
        elif choice == 'b':
            convert_length()
        elif choice == 'c':
            convert_mass()
        elif choice == 'd':
            convert_volume()

if __name__ == '__main__':
    main()
