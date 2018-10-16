import random

agents = []

y0 = random.randint(0,99)
x0 = random.randint(0,99)

agents.append([y0,x0])

if random.random() < 0.5:
    agents[0][0] +=1
else:
    agents[0][0] -=1
    
if random.random() < 0.5:
    agents[0][1] +=1
else:
    agents[0][1] -=1
    
print (agents)
    


