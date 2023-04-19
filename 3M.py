"""
3M.py

Calculating frequences for 3M and 2M tables.

For 3M tables you roll three of the same die, using the minimum, medium, or
maximum of the three dice rolled depending on the circumstances. For 2M tables
you roll two dice, using the minimum or the maximum of the two dice rolled.

Functions:
dice_freq: Print the absolute and relative frequences for dice rolls. (None)
three_em: Calculate the min, medium, and max for three dice. (dict)
two_em: Calculate the min and max for two dice. (dict or str: list of int)
"""

def dice_freq(data, sides):
	"""
	Print the absolute and relative frequences for dice rolls. (None)

	Parameters:
	data: A list of dice rolls. (list of int)
	sides: How many sides the rolled die had. (int)
	"""
	print()
	for roll in range(1, sides + 1):
		count = data.count(roll)
		print(roll, count, count / len(data))

def three_em(sides = 12):
	"""
	Calculate the min, medium, and max for three dice. (dict)

	The output has three lists of all possible die rolls, keyed to min, med,
	and max.

	Parameters:
	sides: How many sides each die has. (int)
	"""
	# Prep the output.
	data = {'min': [], 'med': [], 'max': []}
	# Get all possible combinations of the dice.
	# Yeah, I could use itertools, but I'm too lazy to look up the docs.
	for first in range(1, sides + 1):
		for second in range(1, sides + 1):
			for third in range(1, sides + 1):
				# Store the min, medium and max for each roll.
				dice = sorted([first, second, third])
				data['min'].append(dice[0])
				data['med'].append(dice[1])
				data['max'].append(dice[2])
	# Print frequency table for each way to read the rolls.
	dice_freq(data['min'], sides)
	dice_freq(data['med'], sides)
	dice_freq(data['max'], sides)
	return data

def two_em(sides = 12):
	"""
	Calculate the min and max for two dice. (dict or str: list of int)

	The output has two lists of all possible die rolls, keyed to min and max.

	Parameters:
	sides: How many sides each die has. (int)
	"""
	# Prep the output.
	data = {'min': [], 'max': []}
	# Get all possible combinations of the dice.
	for first in range(1, sides + 1):
		for second in range(1, sides + 1):
				# Store the min and max for each roll.
				dice = sorted([first, second])
				data['min'].append(dice[0])
				data['max'].append(dice[1])
	# Print frequency table for each way to read the rolls.
	dice_freq(data['min'], sides)
	dice_freq(data['max'], sides)
	return data

if __name__ == '__main__':
	#three_em()
	two_em()
