# Hardcoded preset runes

# Store the presets in a dictionary, character presets will be dictionaries as well
presets = {}
presets["Manic Fate"] = ["W Demon", "W Fate", "W Devotion"]
presets["Eternal Sanctity"] = ["W Angel", "W Sovereign", "W Tranquility", "W Fate", "W Devotion"]
presets["Sealing Sacrifice"] = ["W Tranquility", "W Protection", "W Demon"]
presets["Rest In Peace"] = ["W Angel", "W Sovereign", "W Tranquility"]
presets["Mortal Fate"] = ["B Fallen", "B Dominion", "B Death", "B Destiny", "B Burn" ]
presets["Fallen Death"] = ["B Fallen", "B Dominion", "B Death"]
presets["Holy Seal"] = ["W Tranquility", "W Protection", "W Demon", "W Angel", "W Devotion"]
presets["Evil Fate"] = ["B Devil", "B Destiny", "B Burn", "B Fallen", "B Dominion"]
presets["Penalty of Death"] = ["B Death", "B Resistance", "B Devil", "B Fallen", "B Burn"]
presets["Burning Justice"] = ["W Demon", "W Fate", "W Devotion", "W Angel", "W Sovereign"]
presets["Fallen Immortality"] = ["B Death", "B Resistance", "B Devil"]
presets["Sinful Fate"] = ["B Devil", "B Destiny", "B Burn"]

# sort the preset list
for key in presets:
	presets[key].sort()

# Reserved for character runes (in the future)



# Function definitions for cleaner code
def matcher(runelist, runepreset):
	# Make a local copy of the inputs to modify // Pass by reference sucks my dude
	runepresetlocal = runepreset
	runelistlocal = runelist
	
	# For each rune in our user's list
	for rune in runelistlocal:
		# If the rune is in the preset list
		if rune in runepresetlocal:
			# Remove the rune from the local preset list
			runepresetlocal.pop(runepresetlocal.index(rune))
	
	# If the local preset list is empty, remove the elements from the list passed in
	if not runepresetlocal:
		for rune in runepreset:
			runelist.pop(runelist.index(rune))
		return True
	else:
		return False