def multiplication(li, fa):
    for wert in li:
        print(wert * fa)

liste = [1,3,5,7,9,11]
faktor = 3

print(type(liste))
multiplication(liste, faktor)


def addition (a=0,b=0,c=0,d=0):
    print("--- Berechnung ---")
    print(a+b*2+c*3+d*4)

w = 4
x = 23
y = 5
z = 12

addition(w,x,y)
addition(x,y,w)
addition(w,y,x)
addition(w,w,w,w)