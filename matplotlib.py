
import operator  
import random
import matplotlib.pyplot


agents = []


agents.append([random.randint(0,99), random.randint(0,99) ])
agents.append([random.randint(0,99), random.randint(0,99) ])


if random.random() < 0.5:
    agents[0][0] +=1
else:
    agents[0][0] -=1
    
if random.random() < 0.5:
    agents[0][1] +=1
else:
    agents[0][1] -=1
    

if random.random() < 0.5:
    agents[1][0] +=1
else:
    agents[1][0] -=1
    
if random.random() < 0.5:
    agents[1][1] +=1
else:
    agents[1][1] -=1
    
print (agents) 

print (max (agents))
print(max(agents, key=operator.itemgetter(1)))

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0], color='blue')
matplotlib.pyplot.scatter(agents[1][1],agents[1][0], color='red')
matplotlib.pyplot.show()

