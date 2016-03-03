f = open("input.txt", 'r')
lines = f.readlines()
message = f.read()
f.close()
f = open("output.txt", "w")
output = ""
for line in lines:
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
	
	output = ""

f.close()
exit()