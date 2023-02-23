Language = input("Language: choose between english(eng) or Brazilian Portuguese(br): ")
if (Language == 'eng'):


 print("WARNING: This calculators is very simple, it can only suport, adition(+), subtraction(-), multiplication(*) and division. The characteres must be use as specified")
 
 STBU = (input("Which math operation should be used? "))
 N1 = int(input("Input number 1: "))
 N2 = int(input("Input number 2: "))
 

 if STBU == '*':
  NR = N1 * N2
  print("the result is:",NR)
 elif STBU == '/':
  NR = N1 / N2
  print("The result is:",NR)
 elif STBU == '+':
  NR = N1 + N2
  print("The result is:",NR)
 elif STBU == '-':
  NR = N1 - N2
  print("The result is:",NR)

 EXIT = input("Press enter to close.")
elif Language == 'br':
 
 
 print("AVISO: Essa calculadora é bem simples, ela só consegue surportar, adição(+), subtração(-), multiplicação(*) e divisão. Os caracteres devem ser usados como especificados nos ()")
 
 STBU = (input("Qual operação matematica sera utilizada? "))
 N1 = int(input("Coloque o primeiro numero: "))
 N2 = int(input("Coloque o segundo numero: "))
 

 if STBU == '*':
  NR = N1 * N2
  print("O resultado é:",NR)
 elif STBU == '/':
  NR = N1 / N2
  print("O resultado é:",NR)
 elif STBU == '+':
  NR = N1 + N2
  print("O resultado é:",NR)
 elif STBU == '-':
  NR = N1 - N2
  print("O resultado é:",NR)

 EXIT = input("Pressione enter para sair.")
    
