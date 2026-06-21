from wordfilter import Wordfilter
import os, random

wordfilter = Wordfilter()

# Our data lists are in four files.
with open('first_name_first_pieces.txt') as f:
    first_name_first_pieces = [line.rstrip() for line in f]
with open('first_name_last_pieces.txt') as f:
    first_name_last_pieces = [line.rstrip() for line in f]
with open('last_name_first_pieces.txt') as f:
    last_name_first_pieces = [line.rstrip() for line in f]
with open('last_name_last_pieces.txt') as f:
    last_name_last_pieces = [line.rstrip() for line in f]

# Now shuffle them.
random.shuffle(first_name_first_pieces)
random.shuffle(first_name_last_pieces)
random.shuffle(last_name_first_pieces)
random.shuffle(last_name_last_pieces)

name = ''
for i in range(0,20):
	while not name: 
		if random.randint(0,100) < 40:
			# Some players have a first name with one piece.
			name = first_name_first_pieces.pop().capitalize() + ' '
		elif random.randint(0,100) > 80:
			# Some players have a first name with three pieces.
			name = '{}{}{} '.format(first_name_first_pieces.pop(), first_name_first_pieces.pop(), first_name_last_pieces.pop()).capitalize()
		else:
			# Most players have a first name with two pieces.
			name = '{}{} '.format(first_name_first_pieces.pop(), first_name_last_pieces.pop()).capitalize()
	
		nickname_chance = random.randint(0,100)
		# Some players have nicknames.
		if nickname_chance > 92:
			name += '"{}" '.format(first_name_first_pieces.pop().capitalize())
		elif nickname_chance > 84:
			name += '"{}" '.format(first_name_last_pieces.pop().capitalize())
			
		if random.randint(0,100) > 90:
			# Some players have a last name with three pieces.
			name += '{}{}{}'.format(last_name_first_pieces.pop(), last_name_first_pieces.pop(), last_name_last_pieces.pop()).capitalize()
		else:
			# Most players have a first name with two pieces.
			name += '{}{}'.format(last_name_first_pieces.pop(), last_name_last_pieces.pop()).capitalize()
			
		# No accidental slurs please.
		if wordfilter.blacklisted(name):
			name = ''
			
	print(name)
	name = ''