from tkinter import*
import random
import time;
import datetime
from tkinter import Tk, StringVar, ttk
from tkinter.messagebox import showinfo

root=Tk()
root.geometry("1350x750+0+0")
root.title("Cafe Management System")

Tops = Frame (root, width = 1350, height=100, bd= 6, relief="raise")
Tops.pack(side=TOP)
lblTitle = Label(Tops, font=('arial', 50, 'bold'), text="\tCafe Management System\t\t\t")
lblTitle.grid(row =0, column =0)

BottomMainFrame = Frame (root, width = 1350, height=650, bd= 6, relief="raise")
BottomMainFrame.pack(side=BOTTOM)

f1 = Frame (BottomMainFrame, width = 450, height=650, bd= 2, relief="raise")
f1.pack(side=LEFT)
f2 = Frame (BottomMainFrame, width = 450, height=650, bd= 2, relief="raise")
f2.pack(side=LEFT)
f2TOP = Frame (f2, width = 450, height=350, bd= 2, relief="raise")
f2TOP.pack(side=TOP)
f2BOTTOM = Frame (f2, width = 450, height=300, bd= 1, relief="raise")
f2BOTTOM.pack(side=BOTTOM)

f3 = Frame (BottomMainFrame, width = 450, height=650, bd= 0, relief="raise")
f3.pack(side=RIGHT)

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=StringVar()
var23=IntVar()

var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var16.set(0)
var17.set(0)
var18.set(0)
var19.set(0)
var20.set(0)
var21.set(0)
var22.set("")
var23.set(0)

varFries =StringVar()
varSalad =StringVar()
varHamburger =StringVar()
varOnionRings =StringVar()
varChickenSalad =StringVar()
varFishSandwich =StringVar()
varCheeseSandwich =StringVar()
varChickenSandwich =StringVar()

varHashBrown =StringVar()
varToastedBagel =StringVar()
varPancakesSyrup =StringVar()
varPineappleStick =StringVar()
varChocolateMuffin =StringVar()

varTea= StringVar()
varCola= StringVar()
varCoffee= StringVar()
varOrange= StringVar()
varBottleWater= StringVar()

varVanillaCone =StringVar()
varVanillaShake =StringVar()
varStrawberryShake =StringVar()

varChange= StringVar()
varSubTotal= StringVar()
varTotal= StringVar()
varVAT= StringVar()
varTax= StringVar()
varPayment= IntVar()


varFries.set("0")
varSalad.set("0")
varHamburger.set("0")
varOnionRings.set("0")
varChickenSalad.set("0")
varFishSandwich.set("0")
varCheeseSandwich.set("0")
varChickenSandwich.set("0")
varTotal.set("0")
varPayment.set(" ")

varHashBrown.set("0")
varToastedBagel.set("0")
varPancakesSyrup.set("0")
varPineappleStick.set("0")
varChocolateMuffin.set("0")

varTea.set("0")
varCola.set("0")
varCoffee.set("0")
varOrange.set("0")
varBottleWater.set("0")
varVanillaCone.set("0")
varVanillaShake.set("0")
varStrawberryShake.set("0")

varVAT.set("")
varTax.set("0")
varTotal.set("0")
varChange.set("0")
varSubTotal.set("0")

def qexit():   
        root.destroy()
       

def Reset():
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var23.set(0)

    
    varFries.set("0")
    varSalad.set("0")
    varHamburger.set("0")
    varOnionRings.set("0")
    varChickenSalad.set("0")
    varFishSandwich.set("0")
    varCheeseSandwich.set("0")
    varChickenSandwich.set("0")
    varTotal.set("0")

    varHashBrown.set("0")
    varToastedBagel.set("0")
    varPancakesSyrup.set("0")
    varPineappleStick.set("0")
    varChocolateMuffin.set("0")

    varTea.set("0")
    varCola.set("0")
    varCoffee.set("0")
    varOrange.set("0")
    varBottleWater.set("0")
    varVanillaCone.set("0")
    varVanillaShake.set("0")
    varStrawberryShake.set("0")

    varVAT.set("")
    varTax.set("0")
    varTotal.set("0")
    varChange.set(" ")
    varSubTotal.set("0")
    varPayment.set(" ")
    
    txtFries.configure(state =DISABLED)
    txtSalad.configure(state =DISABLED)
    txtHamburger.configure(state =DISABLED)
    txtOnionRings.configure(state =DISABLED)
    txtChickenSalad.configure(state =DISABLED)
    txtFishSandwich.configure(state =DISABLED)
    txtCheeseSandwich.configure(state =DISABLED)
    txtChickenSandwich.configure(state =DISABLED)
    txtHashBrown.configure(state =DISABLED)
    txtToastedBagel.configure(state =DISABLED)
    txtPancakesSyrup.configure(state =DISABLED)
    txtPineappleStick.configure(state =DISABLED)
    txtChocolateMuffin.configure(state =DISABLED)
    txtTea.configure(state =DISABLED)
    txtCola.configure(state =DISABLED)
    txtCoffee.configure(state =DISABLED)
    txtOrange.configure(state =DISABLED)
    txtBottleWater.configure(state =DISABLED)
    txtVanillaCone.configure(state =DISABLED)
    txtVanillaShake.configure(state =DISABLED)
    txtStrawberryShake.configure(state =DISABLED)
    #txtPayment.configure(state =DISABLED)
    txtChange.configure(state =DISABLED)
    txtTax.configure(state =DISABLED)
    txtSubTotal.configure(state =DISABLED)
    txtTotal.configure(state =DISABLED)
    var8.get() == 0

def chkFries():
    if (var1.get() == 1):
        txtFries.configure(state = NORMAL)
        varFries.set("")
    elif(var1.get() == 0):
        txtFries.configure(state = DISABLED)
        varFries.set("0")

def chkSalad():
    if (var2.get() == 1):
        txtSalad.configure(state = NORMAL)
        varSalad.set("")
    elif(var2.get() == 0):
        txtSalad.configure(state = DISABLED)
        varSalad.set("0")

def chkHamburger():
    if (var3.get() == 1):
        txtHamburger.configure(state = NORMAL)
        varHamburger.set("")
    elif(var3.get() == 0):
        txtHamburger.configure(state = DISABLED)
        varHamburger.set("0")

def chkOnionRings():
    if (var4.get() == 1):
        txtOnionRings.configure(state = NORMAL)
        varOnionRings.set("")
    elif(var4.get() == 0):
        txtOnionRings.configure(state = DISABLED)
        varOnionRings.set("0")

def chkChickenSalad():
    if (var5.get() == 1):
        txtChickenSalad.configure(state = NORMAL)
        varChickenSalad.set("")
    elif(var5.get() == 0):
        txtChickenSalad.configure(state = DISABLED)
        varChickenSalad.set("0")

def chkFishSandwich():
    if (var6.get() == 1):
        txtFishSandwich.configure(state = NORMAL)
        varFishSandwich.set("")
    elif(var6.get() == 0):
        txtFishSandwich.configure(state = DISABLED)
        varFishSandwich.set("0")


def chkCheeseSandwich():
    if (var7.get() == 1):
        txtCheeseSandwich.configure(state = NORMAL)
        varCheeseSandwich.set("")
    elif(var7.get() == 0):
        txtCheeseSandwich.configure(state = DISABLED)
        varCheeseSandwich.set("0")

def chkChickenSandwich():
    if (var8.get() == 1):
        txtChickenSandwich.configure(state = NORMAL)
        varChickenSandwich.set("")
    elif(var8.get() == 0):
        txtChickenSandwich.configure(state = DISABLED)
        varChickenSandwich.set("0")

def chkHashBrown():
    if (var9.get() == 1):
        txtHashBrown.configure(state = NORMAL)
        varHashBrown.set("")
    elif(var9.get() == 0):
        txtHashBrown.configure(state = DISABLED)
        varHashBrown.set("0")

def chkToastedBagel():
    if (var10.get() == 1):
        txtToastedBagel.configure(state = NORMAL)
        varToastedBagel.set("")
    elif(var10.get() == 0):
        txtToastedBagel.configure(state = DISABLED)
        varToastedBagel.set("0")

def chkPancakesSyrup():
    if (var11.get() == 1):
        txtPancakesSyrup.configure(state = NORMAL)
        varPancakesSyrup.set("")
    elif(var11.get() == 0):
        txtPancakesSyrup.configure(state = DISABLED)
        varPancakesSyrup.set("0")

def chkPineappleStick():
    if (var12.get() == 1):
        txtPineappleStick.configure(state = NORMAL)
        varPineappleStick.set("")
    elif(var12.get() == 0):
        txtPineappleStick.configure(state = DISABLED)
        varPineappleStick.set("0")    

def chkChocolateMuffin():
    if (var13.get() == 1):
        txtChocolateMuffin.configure(state = NORMAL)
        varChocolateMuffin.set("")
    elif(var13.get() == 0):
        txtChocolateMuffin.configure(state = DISABLED)
        varChocolateMuffin.set("0")

def chkTea():
    if (var14.get() == 1):
        txtTea.configure(state = NORMAL)
        varTea.set("")
    elif(var14.get() == 0):
        txtTea.configure(state = DISABLED)
        varTea.set("0")

def chkCola():
    if (var15.get() == 1):
        txtCola.configure(state = NORMAL)
        varCola.set("")
    elif(var15.get() == 0):
        txtCola.configure(state = DISABLED)
        varCola.set("0")

def chkCoffee():
    if (var16.get() == 1):
        txtCoffee.configure(state = NORMAL)
        varCoffee.set("")
    elif(var16.get() == 0):
        txtCoffee.configure(state = DISABLED)
        varCoffee.set("0")

def chkOrange():
    if (var17.get() == 1):
        txtOrange.configure(state = NORMAL)
        varOrange.set("")
    elif(var17.get() == 0):
        txtOrange.configure(state = DISABLED)
        varOrange.set("0")

def chkBottleWater():
    if (var18.get() == 1):
        txtBottleWater.configure(state = NORMAL)
        varBottleWater.set("")
    elif(var18.get() == 0):
        txtBottleWater.configure(state = DISABLED)
        varBottleWater.set("0")

def chkVanillaCone():
    if (var19.get() == 1):
        txtVanillaCone.configure(state = NORMAL)
        varVanillaCone.set("")
    elif(var19.get() == 0):
        txtVanillaCone.configure(state = DISABLED)
        varVanillaCone.set("0")

def chkVanillaShake():
    if (var20.get() == 1):
        txtVanillaShake.configure(state = NORMAL)
        varVanillaShake.set("")
    elif(var20.get() == 0):
        txtVanillaShake.configure(state = DISABLED)
        varVanillaShake.set("0")

def chkStrawberryShake():
    if (var21.get() == 1):
        txtStrawberryShake.configure(state = NORMAL)
        varStrawberryShake.set("")
    elif(var21.get() == 0):
        txtStrawberryShake.configure(state = DISABLED)
        varStrawberryShake.set("0")

def costofmeal():
    meal1 = float(varFries.get())
    meal2 = float(varSalad.get())
    meal3 = float(varHamburger.get())
    meal4 = float(varOnionRings.get())
    meal5 = float(varChickenSalad.get())
    meal6 = float(varFishSandwich.get())
    meal7 = float(varCheeseSandwich.get())
    meal8 = float(varChickenSandwich.get())
    meal9 = float(varHashBrown.get())
    meal10 = float(varToastedBagel.get())
    meal11 = float(varPancakesSyrup.get())
    meal12 = float(varPineappleStick.get())
    meal13 = float(varChocolateMuffin.get())
    meal14 = float(varTea.get())
    meal15 = float(varCola.get())
    meal16 = float(varCoffee.get())
    meal17 = float(varOrange.get())
    meal18 = float(varBottleWater.get())
    meal19 = float(varVanillaCone.get())
    meal20 = float(varVanillaShake.get())
    meal21 = float(varStrawberryShake.get())


    iTotal1=((meal1 * 1.20) + (meal2 * 2.10) + (meal3 * 3.30) + (meal4 * 1.30))
    iTotal2=((meal5 * 3.50) + (meal6 * 3.60) + (meal7 * 3.40) + (meal8 * 3.60))
    iTotal3=((meal9 * 1.40) + (meal10 * 1.60) + (meal11 * 1.20) + (meal12 * 1.40))
    iTotal4=((meal13 * 2.40) + (meal14 * 1.50) + (meal15 * 1.30) + (meal16 * 1.59))
    iTotal5=((meal17 * 1.20) + (meal18 * 0.99) + (meal19 * 2.10) + (meal20 * 2.10) + (meal21 * 2.20))

    if (var22.get() == "Cash"):
        iChange = float(varPayment.get())
        iCost = (iTotal1 + iTotal2 + iTotal3 + iTotal4 + iTotal5)
        iTax = (iCost * 3.4)/100
        iTaxq="৳", str('%.2f'%(iTax))
        varTax.set(iTaxq)

        iCostq = "৳", str('%.2f'%(iCost))
        varSubTotal.set(iCostq)
        iTotalq="৳", str('%.2f'%((iCost + iTax)))
        varTotal.set(iTotalq)
        cChange = (iChange - (iCost + iTax))
        cChangeq = "৳", str('%.2f'%(cChange))
        varChange.set(cChangeq)
    elif(var22.get() == "Master Card" or "Visa card" or "Debit Card"):
        varPayment.set("")
        iCost = (iTotal1 + iTotal2 + iTotal3 + iTotal4 + iTotal5)
        iTax = (iCost * 3.4)/100
        iTaxq="৳", str('%.2f'%(iTax))
        varTax.set(iTaxq)
        iCostq = "৳", str('%.2f'%(iCost))
        varSubTotal.set(iCostq)
        iTotalq="৳", str('%.2f'%((iCost + iTax)))
        varTotal.set(iTotalq)
        varChange.set("")
 

#======================================================Frame 1====================================================================================================

lblMeal = Label(f1, font=('arial', 20, 'bold'), text="\nFast Food Meal & Vegitable\n")
lblMeal.grid(row =0, column=0)

Fries =Checkbutton(f1, text="Fries\t\tTk. 1.20", variable=var1, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=chkFries).grid(row=1, column=0, sticky=W)
txtFries = Entry(f1,font=('arial',18,'bold'), textvariable =varFries, width =6, justify='right', state =DISABLED)
txtFries.grid(row =1, column =1)

Salad =Checkbutton(f1, text="Salad\t\tTk. 2.10", variable=var2, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'),command=chkSalad).grid(row=2, column=0, sticky=W)
txtSalad = Entry(f1,font=('arial',18,'bold'), textvariable =varSalad, width =6, justify='right', state =DISABLED)
txtSalad.grid(row =2, column =1)

Hamburger =Checkbutton(f1, text="Hamburger\tTk. 3.30", variable=var3, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'),command=chkHamburger).grid(row=3, column=0, sticky=W)
txtHamburger = Entry(f1,font=('arial',18,'bold'), textvariable =varHamburger, width =6, justify='right', state =DISABLED)
txtHamburger.grid(row =3, column =1)

OnionRings =Checkbutton(f1, text="Onion Rings\tTk. 1.30", variable=var4, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'),command=chkOnionRings).grid(row=4, column=0, sticky=W)
txtOnionRings = Entry(f1,font=('arial',18,'bold'), textvariable =varOnionRings, width =6, justify='right', state =DISABLED)
txtOnionRings.grid(row =4, column =1)

ChickenSalad =Checkbutton(f1, text="ChickenSalad\tTk. 3.50", variable=var5, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'),command=chkChickenSalad).grid(row=5, column=0, sticky=W)
txtChickenSalad = Entry(f1,font=('arial',18,'bold'), textvariable =varChickenSalad, width =6, justify='right', state =DISABLED)
txtChickenSalad.grid(row =5, column =1)

lblSandwich = Label(f1, font=('arial', 20, 'bold'), text="\nSandwich\n")
lblSandwich.grid(row =6, column =0)

FishSandwich =Checkbutton(f1, text="FishSandwich\tTk. 3.60", variable=var6, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'),command=chkFishSandwich).grid(row=7, column=0, sticky=W)
txtFishSandwich = Entry(f1,font=('arial',18,'bold'), textvariable =varFishSandwich, width =6, justify='right', state =DISABLED)
txtFishSandwich.grid(row =7, column =1)

CheeseSandwich =Checkbutton(f1, text="CheseSandwich\tTk. 3.40", variable=var7, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'),command = chkCheeseSandwich).grid(row=8, column=0, sticky=W)
txtCheeseSandwich = Entry(f1,font=('arial',18,'bold'), textvariable =varCheeseSandwich, width =6, justify='right', state =DISABLED)
txtCheeseSandwich.grid(row =8, column =1)

ChickenSandwich =Checkbutton(f1, text="ChickenSandwich\tTk. 3.60", variable=var8, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'),command = chkChickenSandwich).grid(row=9, column=0, sticky=W)
txtChickenSandwich = Entry(f1,font=('arial',18,'bold'), textvariable =varChickenSandwich, width =6, justify='right', state =DISABLED)
txtChickenSandwich.grid(row =9, column =1)

lblspace=Label(f1, text="\n\n\n\n\n\n\n")
lblspace.grid(row =10, column=0)

#======================================================Frame 2====================================================================================================
lblMeal = Label(f2TOP, font=('arial', 18, 'bold'), text="Desserts\n\n")
lblMeal.grid(row =0, column=0)

HashBrown = Checkbutton(f2TOP, text="Hash Brown\tTk. 1.40", variable=var9, onvalue =1, offvalue=0,
                        font=('arial', 18, 'bold'),command = chkHashBrown).grid(row=1, column=0, sticky=W)
txtHashBrown = Entry(f2TOP, font=('arial', 18, 'bold'), textvariable =varHashBrown, width =6, justify='right', state = DISABLED)
txtHashBrown.grid(row =1, column =1)

ToastedBagel = Checkbutton(f2TOP, text="ToastedBagel\tTk. 1.60", variable=var10, onvalue =1,offvalue=0,
                        font=('arial', 18, 'bold'),command = chkToastedBagel).grid(row=2, column=0, sticky=W)
txtToastedBagel = Entry(f2TOP, font=('arial', 18, 'bold'), textvariable =varToastedBagel, width =6, justify='right', state = DISABLED)
txtToastedBagel.grid(row =2, column =1)

PancakesSyrup = Checkbutton(f2TOP, text="Pancakes Syrup\tTk. 1.20", variable=var11, onvalue =1, offvalue=0,
                        font=('arial', 18, 'bold'),command = chkPancakesSyrup).grid(row=3, column=0, sticky=W)
txtPancakesSyrup = Entry(f2TOP, font=('arial', 18, 'bold'), textvariable =varPancakesSyrup, width =6, justify='right', state = DISABLED)
txtPancakesSyrup.grid(row =3, column =1)

PineappleStick = Checkbutton(f2TOP, text="Pineapple Stick\tTk. 1.40", variable=var12, onvalue =1, offvalue=0,
                        font=('arial', 18, 'bold'),command = chkPineappleStick).grid(row=4, column=0, sticky=W)
txtPineappleStick = Entry(f2TOP, font=('arial', 18, 'bold'), textvariable =varPineappleStick, width =6, justify='right', state = DISABLED)
txtPineappleStick.grid(row =4, column =1)


ChocolateMuffin = Checkbutton(f2TOP, text="Chocolate Muffin\tTk. 2.40", variable=var13, onvalue =1, offvalue=0,
                        font=('arial', 18, 'bold'),command=chkChocolateMuffin).grid(row=5, column=0, sticky=W)

txtChocolateMuffin = Entry(f2TOP, font=('arial', 18, 'bold'), textvariable =varChocolateMuffin, width =6, justify='right', state = DISABLED)
txtChocolateMuffin.grid(row =5, column =1)

#=======================================================Frame 3=================================================================

lblMeal = Label(f3, font=('arial', 18, 'bold'), text="Drinks\n")
lblMeal.grid(row =0, column=0)

Tea = Checkbutton(f3, text="Tea\t\tTk. 1.50", variable=var14, onvalue =1, offvalue=0,
                        font=('arial', 18, 'bold'),command=chkTea).grid(row=1, column=0, sticky=W)
txtTea = Entry(f3, font=('arial', 18, 'bold'), textvariable =varTea, width =6, justify='right', state = DISABLED)
txtTea.grid(row =1, column =1)

Cola = Checkbutton(f3, text="Cola\t\tTk. 1.30", variable=var15, onvalue =1,offvalue=0,
                        font=('arial', 18, 'bold'),command=chkCola).grid(row=2, column=0, sticky=W)
txtCola = Entry(f3, font=('arial', 18, 'bold'), textvariable =varCola, width =6, justify='right', state = DISABLED)
txtCola.grid(row =2, column =1)

Coffee = Checkbutton(f3, text="Coffe\t\tTk. 1.59", variable=var16, onvalue =1, offvalue=0,
                        font=('arial', 18, 'bold'),command=chkCoffee).grid(row=3, column=0, sticky=W)
txtCoffee = Entry(f3, font=('arial', 18, 'bold'), textvariable =varCoffee, width =6, justify='right', state = DISABLED)
txtCoffee.grid(row =3, column =1)

Orange = Checkbutton(f3, text="Orange\t\tTk. 1.20", variable=var17, onvalue =1, offvalue=0,
                        font=('arial', 18, 'bold'),command=chkOrange).grid(row=4, column=0, sticky=W)
txtOrange = Entry(f3, font=('arial', 18, 'bold'), textvariable =varOrange, width =6, justify='right', state = DISABLED)
txtOrange.grid(row =4, column =1)


BottleWater = Checkbutton(f3, text="Bottle Water\tTk. 0.99", variable=var18, onvalue =1, offvalue=0,
                        font=('arial', 18, 'bold'),command=chkBottleWater).grid(row=5, column=0, sticky=W)

txtBottleWater = Entry(f3, font=('arial', 18, 'bold'), textvariable =varBottleWater, width =6, justify='right', state = DISABLED)
txtBottleWater.grid(row =5, column =1)

lblShakes = Label(f3, font=('arial', 20, 'bold'), text="\nShakes\n")
lblShakes.grid(row =6, column=0)

VanillaCone = Checkbutton(f3, text="Vanilla Cone\tTk. 2.10", variable=var19, onvalue =1, offvalue=0,
                        font=('arial', 18, 'bold'),command=chkVanillaCone).grid(row=7, column=0, sticky=W)
txtVanillaCone = Entry(f3, font=('arial', 18, 'bold'), textvariable =varVanillaCone, width =6, justify='right', state = DISABLED)
txtVanillaCone.grid(row =7, column =1)

VanillaShake = Checkbutton(f3, text="Vanilla Shake\tTk. 2.10", variable=var20, onvalue =1,offvalue=0,
                        font=('arial', 18, 'bold'),command=chkVanillaShake).grid(row=8, column=0, sticky=W)
txtVanillaShake = Entry(f3, font=('arial', 18, 'bold'), textvariable =varVanillaShake, width =6, justify='right', state = DISABLED)
txtVanillaShake.grid(row =8, column =1)

StrawberryShake = Checkbutton(f3, text="Strawberry Shake\tTk. 2.20", variable=var21, onvalue =1, offvalue=0,
                        font=('arial', 18, 'bold'),command=chkStrawberryShake).grid(row=9, column=0, sticky=W)
txtStrawberryShake = Entry(f3, font=('arial', 18, 'bold'), textvariable =varStrawberryShake, width =6, justify='right', state = DISABLED)
txtStrawberryShake.grid(row =9, column =1)


lblspace = Label(f3, text="\n\n\n\n\n\n\n\n\n")
lblspace.grid(row =10, column=0)

#===================================================Frame 2 Bottom==================================================================================================
lblPaymentMethod = Label(f2BOTTOM, font=('arial', 14, 'bold'), text="Payment Method", bd=10, width= 16, anchor= 'w')
lblPaymentMethod.grid(row =0, column=0)

lblChange = Label(f2BOTTOM, font=('arial', 14, 'bold'), text="Change", bd=10, anchor= 'w')
lblChange.grid(row =0, column=1)
txtChange = Entry(f2BOTTOM,font=('arial', 18,'bold'), textvariable =varChange, width= 6, justify='right', state =DISABLED)
txtChange.grid(row =0, column=2)


cmbPaymentMethod = ttk.Combobox(f2BOTTOM, textvariable = var22, state='readonly', font=('arial', 10, 'bold'), width= 20)
cmbPaymentMethod['value']=('cash', 'Master Card', 'Visa Card', 'Debit Card')
cmbPaymentMethod.current(0)
cmbPaymentMethod.grid(row=1, column=0)

lblTax = Label(f2BOTTOM, font=('arial', 14, 'bold'), text="Tax    ", bd=10, anchor='w')
lblTax.grid(row =1, column=1)
txtTax = Entry(f2BOTTOM, font=('arial', 18, 'bold'), textvariable =varTax, width= 6, justify='right',  state =DISABLED)
txtTax.grid(row =1, column=2)

txtPayment = Entry(f2BOTTOM, font=('arial',18, 'bold'), textvariable =varPayment, width =6, justify='right')#, state=DISABLED)
txtPayment.grid(row=2, column=0)
lblSubTotal = Label(f2BOTTOM, font=('arial', 14, 'bold'), text="Sub Total", bd=10, width =8,anchor='w')
lblSubTotal.grid(row =2, column=1)
txtSubTotal = Entry(f2BOTTOM, font=('arial', 18, 'bold'), textvariable =varSubTotal, width= 6, justify='right',  state =DISABLED)
txtSubTotal.grid(row =2, column=2)

lblTotal = Label(f2BOTTOM, font=('arial', 14, 'bold'), text="Total", bd=10, width =6,anchor='w')
lblTotal.grid(row =3, column=1)
txtTotal = Entry(f2BOTTOM, font=('arial', 18, 'bold'), textvariable =varTotal, width =6, justify='right', state =DISABLED)
txtTotal.grid(row =3, column=2)

#================================================Button======================================================================
btnTotal=Button(f2BOTTOM,padx=16,pady=1, bd=4, fg="black", font=('arial', 16,'bold'), width=5,
                text="Total ", command = costofmeal).grid(row=4, column=0)

btnReset=Button(f2BOTTOM, padx=16,pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5,
                text="Reset", command=Reset).grid(row=4, column=1)

btnExit=Button(f2BOTTOM, padx=16,pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5,

                text="Exit",command=qexit).grid(row=4, column=2)




lblspace = Label( f2BOTTOM, text="\n\n\n\n\n\n\n")
lblspace.grid(row =6, column=0)

root.mainloop()
