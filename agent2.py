import random

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
