import random
import matplotlib.pyplot as plt
import numpy as np
from word_list import word_list
from steps import stages
from steps import logo

#Funkcje
def RPS():

	print("Welcome to \n~Rock~Paper~Scissors~Game\nby Piotr DevStudio")
	print("Players, please make a choice now. \n r for Rock, p for Paper, s for Scissors")

	p1ch = input("Player 1 choice: ")
	p2chai = random.randint(0, 2)
	    #print(f"player2 ch = {p2chai}")

	if p2chai == 0:
	    p2ch = "r"
	elif p2chai == 1:
	    p2ch = "p"
	elif p2chai == 2:
	    p2ch = "s"

	print(f"Computer plays: {p2ch}")

	if p1ch == p2ch:
	    print("Remis")
	    restartRPS()
	elif p1ch == "r":
		if p2ch == "s":
		    print("Wygrałeś!")
		    restartRPS()
		elif p2ch == "p":
			print("Przegrałeś!")
			restartRPS()
	elif p1ch == "s":
		if p2ch == "p":
			print("Wygrałeś!")
			restartRPS()
		elif p2ch == "r":
			print("Przegrałeś!")
			restartRPS()
	elif p1ch == "p":
		if p2ch == "r":
			print("Wygrałeś!")
			restartRPS()
		elif p2ch == "s":
			print("Przegrałeś!")
			restartRPS()
	else:
	    print("Coś poszło nie tak")
	    restartRPS()
	
def restartRPS():
	restartRPS = input("\nChcesz zagrać jeszcze raz?[y]/[n] ")
	if restartRPS == "y" or restartRPS == "yes":
	    print("Powodzenia!")
	    RPS()
	if restartRPS == "n" or restartRPS == "no":
	    menu()

def fibo():

	nterms = int(input("Podaj długość ciągu: "))
	fibbo = []
	x, y = 0, 1
	count = 0
	
	if nterms <= 0:
		print("Podaj wartość większą od 0")
		fibo()
	else:
		while nterms > 0:
			fibbo.append(x)
			parz = [x for x in fibbo if x%2 == 0]
			nieparz = [x for x in fibbo if x%2 == 1]
			nth = x + y
			x = y 
			y = nth
			count +=1 
			if count == nterms:
				print(f"\nTwój wygenerowany ciąg Fibonnaciego o długości {nterms}:\n{fibbo}\n")
				print(f"[*] liczby parzyste w tym ciagu to {parz}")
				print("[*]Zamknij wykres aby przejść dalej[*]")
				b = fibbo # y
				p = len(b)
				v = np.arange(0,p,1) # x
				# plotting the points 
				plt.plot(v, b)
				# naming the x axis
				plt.xlabel('Krok')
				# naming the y axis
				plt.ylabel('Wartość')
				# giving a title to my graph
				plt.title(f'Wykres ciągu Fibonnaciego dla {p} kroków')
				# function to show the plot
				plt.show()
				print(f"[*] Liczby nieparzyste w tym ciągu to {nieparz}")
				if  len(nieparz) > len(parz):
					print(f"wiecej jest liczb nieparzystych {len(nieparz)} a parzystych jest {len(parz)}, a stosunek nieparzyste/parzyste wynosi {round(len(nieparz)/len(parz),4)}\n")
				elif len(nieparz) < len(parz):
					print("wiecej jest liczb parzystych")
				else:
					print("Tyle samo liczb parzystych co nieparzystych")
				restartFibo()

def restartFibo():
	ans = input("\nCzy chcesz sprawdzić inną długość ciągu? [y]/[n]")
	if ans == "y" or ans == "yes":
		print("*Wznawianie programu*\n")
		fibo()
	elif ans == "n" or ans == "no":
		print("\nDziękuję za skorzystanie z programu\nDo następnego!\n*OPUSZCZANIE PROGRAMU*")
		menu()
	else:
		print("Wprowadzono zły znak")
		restart()

def kalkulator():
		print("\nIle kilometrów chcesz przeliczyć na mile?\n ")
		ktm = input()
		mk = 1.60934
		obl = float(ktm)/mk
		obl = round(obl, 2) # zaokrąglenie do 2go miejsca po przecinku
		miles = str(obl)
		print(f"{ktm} kilometrów to {obl} mil")
		restartKalk()

def restartKalk():
	restartKalk = input("Czy chcesz przeliczyć ponownie?[y]/[n]\n")
	if restartKalk == "y" or restartKalk == "yes":
		kalkulator()
	if restartKalk == "n" or restartKalk == "no":
		menu()

def Hangman():
	words = word_list
	display = []
	chosen_word = random.choice(words)
	word_lenght = len(chosen_word)
	lives = 6
	guessed_letters = []
	print(f" psssh the answer is {chosen_word}")
	
	print(logo)
	for letter in range(word_lenght):
		display += "_"
	print(display)
	print(stages[6])
	end_of_game = False

	while not end_of_game:
		guess = str(input("Wpisz literę ")).lower()

		for position in range(word_lenght):
			letter = chosen_word[position]
			if letter == guess:
				display[position] = letter
		if guess in guessed_letters:
			print(f"Już wpisałeś literę {guess}")		
		if guess in display:
			print(f'{stages[lives]}')
			guessed_letters.append(guess)
		if guess not in display:
			if guess != " ":
				lives -= 1
				guessed_letters.append(guess)
				print(f'The letter you guessed *{guess}* is not in the generated word, you lose 1 live\n{stages[lives]}')
		if "_" not in display:
			print("[*]WYGRAŁEŚ[*]")
			print(display)
			end_of_game = True
			restartHangman()
		if lives == 0:
			print("[*]Koniec gry[*]\n[*]PRZEGRAŁEŚ[*]]")
			print(f"{stages[0]}")
			print(f"Słowo, które było do zgadnięcia to > {chosen_word} <")
			restartHangman()
			end_of_game = True
		print(display)

def restartHangman():
	ans = input("Chcesz zagrać jeszcze raz?[y]/[n]: ")
	if ans == "y" or ans == "yes":
		print("Powodzenia")
		Hangman()
	else:
		print("Do zobaczenia!")
		menu()

def menu():
	start = input("\nWybierz program z menu \n[1] Kamień papier nożyce na komputer\n[2] Ciąg Fibonnaciego\n[3] Kalkulator kilometry na mile\n[4] Hangman\n[Inny] Wyjście ")
	if start == "1":
		RPS()
	elif start == "2":
		fibo()
	elif start == "3":
		kalkulator()
	elif start == "4":
		Hangman()
	else:
		print("\nDo zobaczenia!")
		quit()



#Menu programu
menu()
