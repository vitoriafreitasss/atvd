#altuta*altura/peso 
#float pq é num quebrado

peso = float(input("digite o peso (kg):"))

altura = float(input("digite a altura:"))

imc = peso / (altura ** 2)  #** pq é potencia (altura*altura)

if imc < 18.5 :
   print("abaixo do peso") 

elif imc < 25:
   print("peso normal") 


elif imc < 
