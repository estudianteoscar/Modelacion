#Hallar las dimensiones de un rectagulo, cuyo perimetro
#mide 36 cm y su area sea maxima

#datos
#{
# 2b+2h=36
#f(b,h) =b.h
# }

#2b + 2h = 36
#2b=36-2h
#b=36/2 - 2h/2
import math
from fractions  import Fraction

a= Fraction(36, 2)
print("El resultado de la fraccion homogenea es: ")
print(a)

#18-h

print("F(n)=(18-h)-h")
print("Despejar nos daria 18h-h²")
print("El resultado es: 18-2h")

#18-2h
div=18/2
print("La altura es: ")
print(div)

print("------------------------")
print("Volvemos a utilizar la formula 2b+2h=36")
print("2b+18=36")
res=36-18
print(res)
div1=18/2
print("La base es: ")
print(div1)
print("-----------------------------")
print("Su aerea maxima es:")
sum1=9*9
print(sum1,"m²")






