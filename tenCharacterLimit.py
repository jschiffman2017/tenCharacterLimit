f = open("input.txt", 'r')
lines = f.readlines()
f.close()
f = open("output.txt", "w")
for line in lines:
	output = ""
	index = 0
	if len(line) <= 10:
		output = line
		f.write(output)
	else:
		while index < 10:
			output += line[index]
			index += 1
		f.write(output)
		f.write("\n")

f.close()