# Resistor Calculator
# Created by IcE puNk dEsiGns

voltage = input("enter incomming voltage:voltage")

Q = input("is this for an led? (y/n):Q")

if 'y' in Q:
   Q1 = input("Is this a series of LED's? (y/n):Q1")
   if 'y' in Q1:
       Q2 = input("How many? (up to 5):Q2")
       Q2 = int(Q2)
       if Q2 == 2:
           LED = input("What color is the 1st LED:LED")
           LED1 = input("What color is the 2nd LED:LED1")
       elif Q2 == 3:
           LED = input("What color is the 1st LED:LED")
           LED1 = input("What color is the 2nd LED:LED1")
           LED2 = input("What color is the 3rd LED:LED1")
       elif Q2 == 4:
           LED = input("What color is the 1st LED:LED") 
           LED1 = input("What color is the 2nd LED:LED1")
           LED2 = input("What color is the 3rd LED:LED2")
           LED3 = input("What color is the 4th LED:LED3") 
       else:
           LED = input("What color is the 1st LED:LED") 
           LED1 = input("What color is the 2nd LED:LED1")
           LED2 = input("What color is the 3rd LED:LED2")
           LED3 = input("What color is the 4th LED:LED3")
           LED4 = input("What color is the 5th LED:LED4")

           if 'IR' in LED1:
            v = 1.5
           if 'Red' in LED1:
            v = 2.0
           if 'Orange' in LED1:
            v = 2.0
           if 'Yellow' in LED1:
            v = 2.1
           if 'Green' in LED1:
            v = 2.2
           if 'True_Green' in LED1:
            v = 3.3
           if 'Blue' in LED1:
            v = 3.3
           if 'White' in LED1:
            v = 3.3
           if 'UV' in LED1:
            v = 3.3
           if '430nm' in LED1:
            v = 4.6
    
   else:
   #LED = ['IR, Red, Orange, Yellow, Green, True_Green, Blue, White, UV, 430nm']
    LED = input("What color is the LED:LED")
    if 'IR' in LED:
        v = 1.5
   if 'Red' in LED:
        v = 2.0
   if 'Orange' in LED:
        v = 2.0
   if 'Yellow' in LED:
        v = 2.1
   if 'Green' in LED:
        v = 2.2
   if 'True_Green' in LED:
        v = 3.3
   if 'Blue' in LED:
        v = 3.3
   if 'White' in LED:
        v = 3.3
   if 'UV' in LED:
        v = 3.3
   if '430nm' in LED:
        v = 4.6

else:
    x = input("Enter voltage usage of component, for multiple in a series enter total:v")
    v = x

voltage = float(voltage)
v = float(v)



if v > voltage:
  print ("Load to large, increase power source, or split components")

else:
  resistor = (voltage-v)/.018
  print (resistor)


bands = input("Number of bands on the resistor (4,5,6):bands")

band_1 = ('0, 1, 2, 3, 4, 5, 6, 7, 8, 9')
band_2 = ('0, 1, 2, 3, 4, 5, 6, 7, 8, 9')
band_3 = ('0, 1, 2, 3, 4, 5, 6, 7, 8, 9')
band_4 = ('0.01, 0.1,1, 10, 100, 1000, 10000, 100000, 1000000, 10000000')
band_5 = ('0.1, 0.25, 0.5, 1, 2, 5, 10')
band_6 = ('1, 5, 10, 15, 25, 50, 100, 200')

if 0 < resistor <= 0.1:
     if '5' in bands:
        band_1 = 1
        band_2 = 0
        band_4 = 0.01
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 0
        band_2 = 1
        band_3 = 0
        band_4 = 0.01
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 0
        band_2 = 1
        band_3 = 0
        band_4 = 0.01
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 0.1 < resistor <= 0.22:
     if '4' in bands:
        band_1 = 2
        band_2 = 2
        band_4 = 0.01
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 0
        band_2 = 2
        band_3 = 2
        band_4 = 0.01
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 0
        band_2 = 2
        band_3 = 2
        band_4 = 0.01
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 0.22 < resistor <= 1:
     if '4' in bands:
        band_1 = 1
        band_2 = 0
        band_4 = 0.1
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 1
        band_2 = 0
        band_3 = 0
        band_4 = 0.01
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 1
        band_2 = 0
        band_3 = 0
        band_4 = 0.01
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 1 < resistor <= 1.5:
     if '4' in bands:
        band_1 = 1
        band_2 = 5
        band_4 = 0.1
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 1
        band_2 = 5
        band_3 = 0
        band_4 = 0.01
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 1
        band_2 = 5
        band_3 = 0
        band_4 = 0.01
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 1.5 < resistor <= 2:
     if '4' in bands:
        band_1 = 2
        band_2 = 0
        band_4 = 0.1
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 2
        band_2 = 0
        band_3 = 0
        band_4 = 0.01
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 2
        band_2 = 0
        band_3 = 0
        band_4 = 0.01
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 2 < resistor <= 2.2:
     if '4' in bands:
        band_1 = 2
        band_2 = 2
        band_4 = 0.1
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 2
        band_2 = 2
        band_3 = 0
        band_4 = 0.01
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 2
        band_2 = 2
        band_3 = 0
        band_4 = 0.01
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 2.2 < resistor <= 3.3:
     if '4' in bands:
        band_1 = 3
        band_2 = 3
        band_4 = 0.1
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 3
        band_2 = 3
        band_3 = 0
        band_4 = 0.01
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 3
        band_2 = 3
        band_3 = 0
        band_4 = 0.01
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 3.3 < resistor <= 4.7:
     if '4' in bands:
        band_1 = 4
        band_2 = 7
        band_4 = 0.1
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 4
        band_2 = 7
        band_3 = 0
        band_4 = 0.01
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 4
        band_2 = 7
        band_3 = 0
        band_4 = 0.01
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 4.7 < resistor <= 5.1:
     if '4' in bands:
        band_1 = 5
        band_2 = 1
        band_4 = 0.1
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 5
        band_2 = 1
        band_3 = 0
        band_4 = 0.01
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 5
        band_2 = 1
        band_3 = 0
        band_4 = 0.01
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 5.1 < resistor <= 10:
     if '4' in bands:
        band_1 = 1
        band_2 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 1
        band_2 = 0
        band_3 = 0
        band_4 = 0.1
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 1
        band_2 = 0
        band_3 = 0
        band_4 = 0.1
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 10 < resistor <= 20:
     if '4' in bands:
        band_1 = 2
        band_2 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 2
        band_2 = 0
        band_3 = 0
        band_4 = 0.1
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 2
        band_2 = 0
        band_3 = 0
        band_4 = 0.1
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 20 < resistor <= 22:
     if '4' in bands:
        band_1 = 2
        band_2 = 2
        band_4 = 1
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 2
        band_2 = 2
        band_3 = 0
        band_4 = 0.1
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 2
        band_2 = 2
        band_3 = 0
        band_4 = 0.1
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 22 < resistor <= 33:
     if '4' in bands:
        band_1 = 3
        band_2 = 3
        band_4 = 1
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 3
        band_2 = 3
        band_3 = 0
        band_4 = 0.1
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 3
        band_2 = 3
        band_3 = 0
        band_4 = 0.1
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 33 < resistor <= 47:
     if '4' in bands:
        band_1 = 4
        band_2 = 7
        band_4 = 1
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 4
        band_2 = 7
        band_3 = 0
        band_4 = 0.1
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 4
        band_2 = 7
        band_3 = 0
        band_4 = 0.1
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 47 < resistor <= 51:
     if '4' in bands:
        band_1 = 5
        band_2 = 1
        band_4 = 1
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 5
        band_2 = 1
        band_3 = 0
        band_4 = 0.1
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 5
        band_2 = 1
        band_3 = 0
        band_4 = 0.1
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 51 < resistor <= 100:
     if '5' in bands:
        band_1 = 1
        band_2 = 0
        band_4 = 10
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 1
        band_2 = 0
        band_3 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 1
        band_2 = 0
        band_3 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 100 < resistor <= 120:
     if '4' in bands:
        band_1 = 1
        band_2 = 2
        band_4 = 10
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 1
        band_2 = 2
        band_3 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 1
        band_2 = 2
        band_3 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 120 < resistor <= 150:
     if '4' in bands:
        band_1 = 1
        band_2 = 5
        band_4 = 10
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 1
        band_2 = 5
        band_3 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 1
        band_2 = 5
        band_3 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 150 < resistor <= 200:
     if '4' in bands:
        band_1 = 2
        band_2 = 0
        band_4 = 10
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 2
        band_2 = 0
        band_3 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 2
        band_2 = 0
        band_3 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 200 < resistor <= 220:
     if '4' in bands:
        band_1 = 2
        band_2 = 2
        band_4 = 10
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 2
        band_2 = 2
        band_3 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 2
        band_2 = 2
        band_3 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 220 < resistor <= 240:
     if '4' in bands:
        band_1 = 2
        band_2 = 4
        band_4 = 10
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 2
        band_2 = 4
        band_3 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 2
        band_2 = 4
        band_3 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 240 < resistor <= 270:
     if '4' in bands:
        band_1 = 2
        band_2 = 7
        band_4 = 10
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 2
        band_2 = 7
        band_3 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 2
        band_2 = 7
        band_3 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 270 < resistor <= 300:
     if '4' in bands:
        band_1 = 3
        band_2 = 0
        band_4 = 10
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 3
        band_2 = 0
        band_3 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 3
        band_2 = 0
        band_3 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 300 < resistor <= 330:
     if '4' in bands:
        band_1 = 3
        band_2 = 3
        band_4 = 10
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 3
        band_2 = 3
        band_3 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 3
        band_2 = 3
        band_3 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 330 < resistor <= 360:
     if '4' in bands:
        band_1 = 3
        band_2 = 6
        band_4 = 10
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 3
        band_2 = 6
        band_3 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 3
        band_2 = 6
        band_3 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 360 < resistor <= 390:
     if '4' in bands:
        band_1 = 3
        band_2 = 9
        band_4 = 10
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 3
        band_2 = 9
        band_3 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 3
        band_2 = 9
        band_3 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 390 < resistor <= 470:
     if '4' in bands:
        band_1 = 4
        band_2 = 7
        band_4 = 10
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 4
        band_2 = 7
        band_3 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 4
        band_2 = 7
        band_3 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 470 < resistor <= 510:
     if '4' in bands:
        band_1 = 5
        band_2 = 1
        band_4 = 10
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 5
        band_2 = 1
        band_3 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 5
        band_2 = 1
        band_3 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 510 < resistor <= 560:
     if '4' in bands:
        band_1 = 5
        band_2 = 6
        band_4 = 10
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 5
        band_2 = 6
        band_3 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 5
        band_2 = 6
        band_3 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 560 < resistor <= 680:
     if '4' in bands:
        band_1 = 6
        band_2 = 8
        band_4 = 10
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 6
        band_2 = 8
        band_3 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 6
        band_2 = 8
        band_3 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 680 < resistor <= 820:
     if '4' in bands:
        band_1 = 8
        band_2 = 2
        band_4 = 10
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 8
        band_2 = 2
        band_3 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 8
        band_2 = 2
        band_3 = 0
        band_4 = 1
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 820 < resistor <= 1000:
     if '4' in bands:
        band_1 = 1
        band_2 = 0
        band_4 = 100
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 1
        band_2 = 0
        band_3 = 0
        band_4 = 10
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 1
        band_2 = 0
        band_3 = 0
        band_4 = 10
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 1000 < resistor <= 1200:
     if '4' in bands:
        band_1 = 1
        band_2 = 2
        band_4 = 100
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 1
        band_2 = 2
        band_3 = 0
        band_4 = 10
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 1
        band_2 = 2
        band_3 = 0
        band_4 = 10
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 1200 < resistor <= 1500:
     if '4' in bands:
        band_1 = 1
        band_2 = 5
        band_4 = 100
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 1
        band_2 = 5
        band_3 = 0
        band_4 = 10
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 1
        band_2 = 5
        band_3 = 0
        band_4 = 10
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 1500 < resistor <= 2000:
     if '4' in bands:
        band_1 = 2
        band_2 = 0
        band_4 = 100
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 2
        band_2 = 0
        band_3 = 0
        band_4 = 10
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 2
        band_2 = 0
        band_3 = 0
        band_4 = 10
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 2000 < resistor <= 2200:
     if '4' in bands:
        band_1 = 2
        band_2 = 2
        band_4 = 100
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 2
        band_2 = 2
        band_3 = 0
        band_4 = 10
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 2
        band_2 = 2
        band_3 = 0
        band_4 = 10
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 2200 < resistor <= 2400:
     if '4' in bands:
        band_1 = 2
        band_2 = 4
        band_4 = 100
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 2
        band_2 = 4
        band_3 = 0
        band_4 = 10
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 2
        band_2 = 4
        band_3 = 0
        band_4 = 10
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 2400 < resistor <= 2700:
     if '4' in bands:
        band_1 = 2
        band_2 = 7
        band_4 = 100
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 2
        band_2 = 7
        band_3 = 0
        band_4 = 10
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 2
        band_2 = 7
        band_3 = 0
        band_4 = 10
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 2700 < resistor <= 3000:
     if '4' in bands:
        band_1 = 3
        band_2 = 0
        band_4 = 100
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 3
        band_2 = 0
        band_3 = 0
        band_4 = 10
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 3
        band_2 = 0
        band_3 = 0
        band_4 = 10
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 3000 < resistor <= 3300:
     if '4' in bands:
        band_1 = 3
        band_2 = 3
        band_4 = 100
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 3
        band_2 = 3
        band_3 = 0
        band_4 = 10
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 3
        band_2 = 3
        band_3 = 0
        band_4 = 10
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 3300 < resistor <= 4700:
     if '4' in bands:
        band_1 = 4
        band_2 = 7
        band_4 = 100
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 4
        band_2 = 7
        band_3 = 0
        band_4 = 10
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 4
        band_2 = 7
        band_3 = 0
        band_4 = 10
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 4700 < resistor <= 5100:
     if '4' in bands:
        band_1 = 5
        band_2 = 1
        band_4 = 100
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 5
        band_2 = 1
        band_3 = 0
        band_4 = 10
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 5
        band_2 = 1
        band_3 = 0
        band_4 = 10
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 5100 < resistor <= 6800:
     if '4' in bands:
        band_1 = 6
        band_2 = 8
        band_4 = 100
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 6
        band_2 = 8
        band_3 = 0
        band_4 = 10
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 6
        band_2 = 8
        band_3 = 0
        band_4 = 10
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 6800 < resistor <= 9100:
     if '4' in bands:
        band_1 = 9
        band_2 = 1
        band_4 = 100
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 9
        band_2 = 1
        band_3 = 0
        band_4 = 10
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 9
        band_2 = 1
        band_3 = 0
        band_4 = 10
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 9100 < resistor <= 10000:
     if '4' in bands:
        band_1 = 1
        band_2 = 0
        band_4 = 1000
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 1
        band_2 = 0
        band_3 = 0
        band_4 = 100
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 1
        band_2 = 0
        band_3 = 0
        band_4 = 100
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 10000 < resistor <= 15000:
     if '4' in bands:
        band_1 = 1
        band_2 = 5
        band_4 = 1000
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 1
        band_2 = 5
        band_3 = 0
        band_4 = 100
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 1
        band_2 = 5
        band_3 = 0
        band_4 = 100
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 15000 < resistor <= 20000:
     if '4' in bands:
        band_1 = 2
        band_2 = 0
        band_4 = 1000
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 2
        band_2 = 0
        band_3 = 0
        band_4 = 100
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 2
        band_2 = 0
        band_3 = 0
        band_4 = 100
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 20000 < resistor <= 22000:
     if '4' in bands:
        band_1 = 2
        band_2 = 2
        band_4 = 1000
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 2
        band_2 = 2
        band_3 = 0
        band_4 = 100
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 2
        band_2 = 2
        band_3 = 0
        band_4 = 100
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 22000 < resistor <= 30000:
     if '4' in bands:
        band_1 = 3
        band_2 = 0
        band_4 = 1000
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 3
        band_2 = 0
        band_3 = 0
        band_4 = 100
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 3
        band_2 = 0
        band_3 = 0
        band_4 = 100
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 30000 < resistor <= 33000:
     if '4' in bands:
        band_1 = 3
        band_2 = 3
        band_4 = 1000
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 3
        band_2 = 3
        band_3 = 0
        band_4 = 100
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 3
        band_2 = 3
        band_3 = 0
        band_4 = 100
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 33000 < resistor <= 47000:
     if '4' in bands:
        band_1 = 4
        band_2 = 7
        band_4 = 1000
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 4
        band_2 = 7
        band_3 = 0
        band_4 = 100
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 4
        band_2 = 7
        band_3 = 0
        band_4 = 100
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 47000 < resistor <= 51000:
     if '4' in bands:
        band_1 = 5
        band_2 = 1
        band_4 = 1000
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 5
        band_2 = 1
        band_3 = 0
        band_4 = 100
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 5
        band_2 = 1
        band_3 = 0
        band_4 = 100
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 51000 < resistor <= 68000:
     if '4' in bands:
        band_1 = 6
        band_2 = 8
        band_4 = 1000
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 6
        band_2 = 8
        band_3 = 0
        band_4 = 100
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 6
        band_2 = 8
        band_3 = 0
        band_4 = 100
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 68000 < resistor <= 100000:
     if '4' in bands:
        band_1 = 1
        band_2 = 0
        band_4 = 10000
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 1
        band_2 = 0
        band_3 = 0
        band_4 = 1000
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 1
        band_2 = 0
        band_3 = 0
        band_4 = 1000
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 100000 < resistor <= 150000:
     if '4' in bands:
        band_1 = 1
        band_2 = 5
        band_4 = 10000
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 1
        band_2 = 5
        band_3 = 0
        band_4 = 1000
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 1
        band_2 = 5
        band_3 = 0
        band_4 = 1000
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 150000 < resistor <= 200000:
     if '4' in bands:
        band_1 = 2
        band_2 = 0
        band_4 = 10000
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 2
        band_2 = 0
        band_3 = 0
        band_4 = 1000
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 2
        band_2 = 0
        band_3 = 0
        band_4 = 1000
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 200000 < resistor <= 220000:
     if '4' in bands:
        band_1 = 2
        band_2 = 2
        band_4 = 10000
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 2
        band_2 = 2
        band_3 = 0
        band_4 = 1000
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 2
        band_2 = 2
        band_3 = 0
        band_4 = 1000
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 220000 < resistor <= 300000:
     if '4' in bands:
        band_1 = 3
        band_2 = 0
        band_4 = 10000
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 3
        band_2 = 0
        band_3 = 0
        band_4 = 1000
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 3
        band_2 = 0
        band_3 = 0
        band_4 = 1000
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 300000 < resistor <= 330000:
     if '4' in bands:
        band_1 = 3
        band_2 = 3
        band_4 = 10000
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 3
        band_2 = 3
        band_3 = 0
        band_4 = 1000
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 3
        band_2 = 3
        band_3 = 0
        band_4 = 1000
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 330000 < resistor <= 390000:
     if '4' in bands:
        band_1 = 3
        band_2 = 9
        band_4 = 10000
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 3
        band_2 = 9
        band_3 = 0
        band_4 = 1000
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 3
        band_2 = 9
        band_3 = 0
        band_4 = 1000
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 390000 < resistor <= 470000:
     if '4' in bands:
        band_1 = 4
        band_2 = 7
        band_4 = 10000
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 4
        band_2 = 7
        band_3 = 0
        band_4 = 1000
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 4
        band_2 = 7
        band_3 = 0
        band_4 = 1000
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 470000 < resistor <= 680000:
     if '4' in bands:
        band_1 = 6
        band_2 = 8
        band_4 = 10000
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 6
        band_2 = 8
        band_3 = 0
        band_4 = 1000
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 6
        band_2 = 8
        band_3 = 0
        band_4 = 1000
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 680000 < resistor <= 1000000:
     if '4' in bands:
        band_1 = 1
        band_2 = 0
        band_4 = 100000
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 1
        band_2 = 0
        band_3 = 0
        band_4 = 10000
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 1
        band_2 = 0
        band_3 = 0
        band_4 = 10000
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 1000000 < resistor <= 2200000:
     if '4' in bands:
        band_1 = 2
        band_2 = 2
        band_4 = 100000
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 2
        band_2 = 2
        band_3 = 0
        band_4 = 10000
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 2
        band_2 = 2
        band_3 = 0
        band_4 = 10000
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
elif 2200000 < resistor <= 4700000:
     if '4' in bands:
        band_1 = 4
        band_2 = 7
        band_4 = 100000
        band_5 = input("Enter Tolerance :")
     elif '5' in bands:
        band_1 = 4
        band_2 = 7
        band_3 = 0
        band_4 = 10000
        band_5 = input("Enter Tolerance :")
     else:
        band_1 = 4
        band_2 = 7
        band_3 = 0
        band_4 = 1000
        band_5 = input("Enter Tolerance :")
        band_6 = input("Enter temp coeffcient:")
else: 
     print ("Voltage source too large, will need lower source or multiple resistors")

if '4' in bands:
   print (band_1, band_2, band_4, band_5)
elif '5' in bands:
   print (band_1, band_2, band_3, band_4, band_5)
else:
   print (band_1, band_2, band_3, band_4, band_5, band_6)

band_1 = (str(band_1))
band_2 = (str(band_2))
band_3 = (str(band_3))
band_4 = (str(band_4))
band_5 = (str(band_5))
band_6 = (str(band_6))

col1 = band_1
col2 = band_2
col3 = band_3
col4 = band_4
col5 = band_5
col6 = band_6

if '0' in band_1:
  col1 = "black"
if '1' in band_1:
  col1 = "brown"
if '2' in band_1:
  col1 = "red"
if '3' in band_1:
  col1 = "orange"
if '4' in band_1:
  col1 = "yellow"
if '5' in band_1:
  col1 = "green"
if '6' in band_1:
  col1 = "blue"
if '7' in band_1:
  col1 = "purple"
if '8' in band_1:
  col1 = "grey"
if '9' in band_1:
  col1 = "white"

if '0' in band_2:
  col2 = "black"
if '1' in band_2:
  col2 = "brown"
if '2' in band_2:
  col2 = "red"
if '3' in band_2:
  col2 = "orange"
if '4' in band_2:
  col2 = "yellow"
if '5' in band_2:
  col2 = "green"
if '6' in band_2:
  col2 = "blue"
if '7' in band_2:
  col2 = "purple"
if '8' in band_2:
  col2 = "grey"
if '9' in band_2:
  col2 = "white"
  
if '0' in band_3:
  col3 = "black"
if '1' in band_3:
  col3 = "brown"
if '2' in band_3:
  col3 = "red"
if '3' in band_3:
  col3 = "orange"
if '4' in band_3:
  col3 = "yellow"
if '5' in band_3:
  col3 = "green"
if '6' in band_3:
  col3 = "blue"
if '7' in band_3:
  col3 = "purple"
if '8' in band_3:
  col3 = "grey"
if '9' in band_3:
  col3 = "white"

if '0.01' in band_4:
  col4 = "silver"
if '0.1' in band_4:
  col4 = "gold"
if '1' in band_4:
  col4 = "black"
if '10' in band_4:
  col4 = "brown"
if '100' in band_4:
  col4 = "red"
if '1000' in band_4:
  col4 = "orange"
if '10000' in band_4:
  col4 = "yellow"
if '100000' in band_4:
  col4 = "green"
if '10000000' in band_4:
  col4 = "blue"
if '100000000' in band_4:
  col4 = "purple"

if '0.1' in band_5:
  col5 = "purple"
if '0.25' in band_5:
  col5 = "blue"
if '0.5' in band_5:
  col5 = "green"
if '1' in band_5:
  col5 = "brown"
if '2' in band_5:
  col5 = "red"
if '5' in band_5:
  col5 = "gold"
if '10' in band_5:
  col5 = "silver"

if '1' in band_6:
  col6 = "grey"
elif '5' in band_6:
  col6 = "purple"
elif '10' in band_6:
  col6 = "blue"
elif '15' in band_6:
  col6 = "orange"
elif '25' in band_6:
  col6 = "yellow"
elif '50' in band_6:
  col6 = "red"
elif '100' in band_6:
  col6 = "brown"
elif '200' in band_6:
  col6 = "black"
else:
  col6 = "error"

if '4' in bands:
   print (col1, col2, col4, col5)
elif '5' in bands:
   print (col1, col2, col3, col4, col5)
else:
   print (col1, col2, col3, col4, col5, col6)
