from runes import *
from itertools import permutations
import time

inputrunes = ["B Fallen", "B Death", "B Dominion", "W Demon", "W Fate", "W Devotion", "B Destiny", "B Burn", "B Destiny", "B Destiny", "B Fallen", "W Angel", "W Sovereign", "W Tranquility", "B Death", "W Tranquility"]
clonedrunes = inputrunes
# Preprocessing for character dictionaries would go here
# Merge the dictionaries
# presets.update(<char dictionaries go here>)

# Empty list of keys
runesetkeys = []

# Empty list of answers
answers = []

# Python magic
temp_answers = []	

# Get the key names in the preset dictionary
for keys in presets:
	runesetkeys.append(keys)
	

	
# For each list permutation
for i in permutations(runesetkeys):
	start_time = time.time()
	# For each element in the permutation list 
	for j in i:
		# if the runes do match
		if matcher(clonedrunes, presets[j]):
			# store the match to our answers database
			temp_answers.append(j)
	
	# sort the temporary answers that we've received
	temp_answers.sort()
	
	if temp_answers in answers:
		# do nothing, reinitialize variables for next iteration
		temp_answers = []
		clonedrunes = inputrunes
		continue;
	else:
		answers.append(temp_answers)
		print("Rune set(s) found! In progress answer: ")
		print(answers)
		temp_answers = []
		clonedrunes = inputrunes		
		
print(answers)