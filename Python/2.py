tries = int(input())
plays = []
for i in range(tries):
	a = input()
	plays.append(a)
for play in plays:
	if play == 'Martelo':
		print('Plastico')
	elif play == 'Alicate':
		print('Martelo')
	elif play == 'Plastico':
		print('Alicate')