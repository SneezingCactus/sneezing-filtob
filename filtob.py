import json
import re

# open config
configjson = open('config.json',)
config = json.load(configjson)

wordsjson = open('words_dictionary.json',)
words = json.load(wordsjson)

tofilter = input("Enter a phrase: ")

def filter(str):
	str_chararray = list(str)
	modstr_chararray = []
	sweardtct_str = ""
	sweargetindex_str = ""
	
	if config["strictLevel"] == 0:
		modstr_chararray = list(remove_possible_false_positives(replace_similar(str)))
	else:
		modstr_chararray = list(replace_similar(str))
	
	# Just a note here: "unmod" indexes follow str_chararray while the normal indexes follow modstr_chararray.
	# This is done because swear words get replaced by "bonk" in str_chararray, so the index desyncs between the two arrays.
	
	for1_index = 0
	for1_unmodindex = 0
	for2_index = 0
	for2_unmodindex = 0
	for char in modstr_chararray:
		if re.match('[^A-Za-z]', char) == None:
			sweardtct_str += char
		if sweardtct_str.endswith(tuple(config["filteredWords"])):
			for2_index = for1_index
			for2_unmodindex = for1_unmodindex
			for char2 in modstr_chararray[for1_index:0:-1]:
				if re.match('[^A-Za-z]', char2) == None:
					sweargetindex_str = char2 + sweargetindex_str
				if sweargetindex_str in config["filteredWords"]:
					break
				for2_index -= 1
				for2_unmodindex -= 1
			str_chararray = str_chararray[0:for2_unmodindex] + ["bonk"] + str_chararray[for1_unmodindex+1:] 
			for1_unmodindex = for2_unmodindex
			sweargetindex_str = ""
			sweardtct_str = ""
		for1_index += 1
		for1_unmodindex += 1
	return "".join(str_chararray)
	
def replace_similar(str):
	str_array = list(str)
	curr_char_index = 0
	for char in str_array:
		for s in config["similarChars"]:
			if char in s[1]:
				str_array[curr_char_index] = s[0]
		curr_char_index += 1
	
	return "".join(str_array)
	
def remove_possible_false_positives(str):
	result = str.lower()
	for fp in config["falsePositives"]:
		result = result.replace(fp, "")
	
	str_array = re.sub('[^A-Za-z]', ' ', result).split(' ')
	curr_word_index = 0
	for word in str_array:
		if word in words:
			str_array[curr_word_index] = " " * len(str_array[curr_word_index])
		curr_word_index += 1
	
	return " ".join(str_array)

print(filter(tofilter))