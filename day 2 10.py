def commonWords(sent1, sent2):
	sen1 = set(sent1)
	sen2 = set(sent2)
	common = list(sen1.intersection(sen2))
	
	# Return the list
	return common
def removeCommonWords(sent1, sent2):
	sentence1 = list(sent1.split())
	sentence2 = list(sent2.split())
	commonlist = commonWords(sentence1,
							sentence2)

	word = 0
	for i in range(len(sentence1)):
	
		# If word is common in both lists
		if sentence1[word] in commonlist:
		
			# Remove the word
			sentence1.pop(word)
			
			# Decrease the removed word
			word = word - 1
		word += 1

	word = 0
	for i in range(len(sentence2)):
	
		# If word is common in both lists
		if sentence2[word] in commonlist:
		
			# Remove the word
			sentence2.pop(word)
			
			# Decrease the removed word
			word = word-1
		word += 1
		
	# Print the remaining words
	# in both the sentences
	print(*sentence1)
	print(*sentence2)
S1 = input("enter a string")
S2 = input("enter a string")

removeCommonWords(S1, S2)


