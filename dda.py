import pandas as pd
import matplotlib.pyplot as plt

# This program applies the Digital Differential Analyzer Algorithm used in computer graphic rasterization.
# It takes 4 inputs and outputs a DDA Table consistent of all the points to be drawn on the screen, and draws them.
x1, y1 = input("What is your start point? (In the form: x,y): ").split(",")
x2, y2 = input("What is your end point? (In the form: x,y): ").split(",")
print("Thanks! Your line goes from (" + x1 + "," + y1 + ") to (" + x2 + "," + y2 + ").")

x1 = int(x1)
x2 = int(x2)
y1 = int(y1)
y2 = int(y2)

deltax = x2 - x1
deltay = y2 - y1
slope = deltay/deltax

if deltay > deltax:
    steps = deltay
else:
    steps = deltax

dx = deltax/steps
dy = deltay/steps

xlist = [x1]
ylist = [y1]

k = []

for i in range(0, steps+1):
    k.append(i)

i = 0

while i < steps:
    xlist.append(xlist[-1] + dx)
    ylist.append(ylist[-1] + dy)
    i += 1

xrounded = []
yrounded = []
newxlist = []
newylist = []

for j in xlist:
    xrounded.append(round(j))
    newxlist.append(round(j,2))

for j in ylist:
    yrounded.append(round(j))
    newylist.append(round(j,2))

allvalues = {'k': k, 'X Values': newxlist, 'Y Values': newylist, 'X Rounded': xrounded, 'Y Rounded': yrounded}
df = pd.DataFrame(allvalues)

print("Your DDA Table:")
print(df)

xplot = xrounded
yplot = yrounded
offset = 1
plt.grid()
plt.locator_params(axis="both", integer=True,)
plt.xlim([min(xplot)-offset,max(xplot)+offset])
plt.ylim([min(yplot)-offset,max(yplot)+offset])
plt.plot(xplot, yplot)
plt.show()
