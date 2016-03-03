f = open("input.txt", 'r')
lines = f.readlines()
message = f.read()
f.close()
f = open("output.txt", "w")
for line in lines:
	if len(line) <= 10:
		f.write(line)

f.close()