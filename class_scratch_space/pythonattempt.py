fname = open("/c/Users/nimis/peer_production_course/class_scratch_space/test_file.txt")
words=0

with open(fname, 'r') as f:
	for line in f:
		word = line.split()
		words += len(word)
print("number of words:",words)
