# hra kámen, nůžky, papír pokročilý
# opakuje hru, dokud uživatel nezadá slovo "konec"

from random import choice

tah_hrace = input("Jaký je Tvůj tah? Zadej kámen, nůžky nebo papír. \n"
				  "Pro ukončení zadej konec. \n\nMůj tah je: ")
while tah_hrace != "konec":
	moznosti = ['kámen', 'nůžky', 'papír']
	tah_pocitace = choice (moznosti)
	vyhral_hrac = "Vyhrál jsi! Gratuluji. :-) "
	vyhral_PC = "Vyhrál PC. "

	print("Počítač zadal: " + str(tah_pocitace))

	#porovnání tahů PC vs hráč:
	if tah_hrace not in ("kámen", "nůžky", "papír"):
		print("Tuto možnost neznám. Zadej 'kámen', 'nůžky', 'papír'.")
	elif tah_hrace == tah_pocitace:
		print("Remíza! ")
	elif tah_hrace == "kámen":
		if tah_pocitace == "nůžky":
			print (f'{vyhral_hrac}')
		else:
			print(f'{vyhral_PC}')
	elif tah_hrace == "nůžky":
		if tah_pocitace == "kámen":
			print(f'{vyhral_PC}')
		else:
			print(f'{vyhral_hrac}')
	else:
		if tah_pocitace == "kámen":
			print(f'{vyhral_hrac}')
		else:
			print(f'{vyhral_PC}')

	tah_hrace = input("\nJaký je Tvůj tah? Zadej kámen, nůžky nebo papír. \n"
					  "Pro ukončení zadej konec. \nMůj tah je: ")
