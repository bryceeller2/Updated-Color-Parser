
'''

	This file/function takes an old list of colors and compares it to a new list.
	It outputs any color code changes

	by Bryce Eller 3/8/2017

'''

o = open('Results.txt', 'w')

our_colors = []
f = open('catalogitemcolors.csv')
for line in f:
	values = line.split(',')
	color = values[2][1:-1]
	colorCode = values[3][1:-1]
	millId = values[4]

	our_colors.append([color.lower(), colorCode, millId])

colors_changed = []

f = open('recommendedChanges.csv')
tasks = f.read().split('label')

for label in tasks:
	if "Update color" in label:
		l = label.split('from')
		color =l[0][16:-1]

		fields = label.split(',')

		colorCode = fields[6][1:-1]
		test = fields[8]
		if "]" not in test:             #sometimes theres an extra comma in the color
			colorCode = fields[7][1:-1]
			millId = fields[10][1:-2]
		else:
			millId = test[1:-2]

		colors_changed.append([color.lower(), colorCode, millId])

logs = []
for changed in colors_changed:
	for ours in our_colors:
		if (changed[0] == ours[0]) and (changed[2] == ours[2]) and (changed[1] != ours[1]):
			changelog = "%s was %s but it is now %s - millId is %s \n" %(changed[0], ours[1], changed[1], changed[2])
			if changelog not in logs:
				logs.append(changelog)
changednum=0
for line in logs:
	o.write("%d. "%changednum)
	o.write(line)
	changednum+=1
