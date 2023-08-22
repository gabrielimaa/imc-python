peso = float(input("Insira seu peso em kg: "))
altura = float(input("Insira sua altura em metros: "))
imc = peso/(altura**2)
if(imc<=18.5):
   print(f"{imc:,.2f}: Abaixo do peso")
elif(imc<25):
    print(f"{imc:,.2f}: Peso Normal")
elif(imc<30):
    print(f"{imc:,.2f}: Excesso de peso")
elif(imc<35):
    print(f"{imc:,.2f}: Obesidade Classe I")
elif(imc<40):
    print(f"{imc:,.2f}: Obesidade Classe II")
else:
    print(f"{imc:,.2f}: Obesidade Classe III")


