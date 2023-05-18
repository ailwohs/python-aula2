'''PEDIR A MEDIDAS E IMPRIMIR QUAL TRIANGULO É DE ACORDO COM O USUARIO'''

a=int(input("Digite a primeira medida \n > "))
b=int(input("Digite a segunda medida \n >"))
c=int(input("Digite a terceira medida \n >"))

#if a<=0 or b<=0 or c<=0:
   #print("Lados nulos ou negativos nao sao aceitos.")
if a==b and b==c:
   print("Triangulo equilatero.")
elif a==b or b==c or c==a:
   print("Triangulo isosceles.")
else:
   print("Triangulo escaleno.")


'''PEDIR A MEDIDAS E IMPRIMIR QUAL TRIANGULO É DE ACORDO COM O USUARIO'''  

#CORREÇÃO DO PROFESSOR 

a=int(input("Digite a primeira medida \n > "))
b=int(input("Digite a segunda medida \n >"))
c=int(input("Digite a terceira medida \n >"))

if a==b and b==c:
   print("Triangulo equilatero.")
 
elif a!=b and b!=c and c!=a:
      print("Triangulo escaleno.")
     
elif a==b or b==c or c==a:
   print("Triangulo isosceles.")  
 
else:
  print("algo de errado aconteceu:")
  

'''SE O USUARIO DIGITAR 1 ELE RECEBE BOM DIA SE ELE DIGITAR 2 BOA TARDE SE DIGITAR 3 BOA NOITE QUALQUER COISA FORA DISSO INVALIDO'''

op=input("Digite um número de 1 a 3 \n >")

if (op=="1"):
 print("Bom dia")

elif (op=="2"):
   print("Boa tarde")
   
elif (op=="3"):
    print("Boa noite")

else:
    print("Inválido")