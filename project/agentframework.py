# functions to import
import random

# make agent class to define attributes and functions
class Agent:

    def __init__ (self, environment, agents):
        self.environment = environment 
        self.stomach = 0
        self._x = random.randint(0,(len(environment[0])))
        self._y = random.randint(0,(len(environment[1])))
        self.agents = agents      
 
# implement a property attribute for self     
    def set_x(self, value):
        self._x = value
    def set_y(self, value):
        self._y = value
    def get_x(self):
        return self._x
    def get_y(self):
        return self._y

# define move function, where the agent randomly moves one space on x and y axis           
    def move(self):
        if random.random() < 0.5:
            self._x = (self._x + 1) % len(self.environment[0])  #create donut boundaries the size of the environment
        else:
            self._x = (self._x - 1) % len(self.environment[0])
        
        if random.random() < 0.5:
            self._y = (self._y + 1) % len(self.environment[1])
        else:
            self._y = (self._y - 1) % len(self.environment[1])
 
# define eat function           
    def eat(self):
        if self.environment[self._y][self._x] > 10:             # only eat if there is more than 10 left in environment
            self.environment[self._y][self._x] -= 10            # take 10 from environment value
            self.stomach += 10                                  # add 10 to agent's stomach
        
        if 0 > self.environment[self._y][self._x] < 10:         # if there is less than 10 left, eat only remaining amount
            self.stomach+= self.environment[self._y][self._x]
            self.environment[self._y][self._x]-= self.environment[self._y][self._x]

# define vomit function        
    def vom(self):
        if self.stomach > 1000:                                 # if agent has eaten more than 1000
            self.environment[self._y][self._x] = self.environment[self._y][self._x]+self.stomach     # add agent's stomach content to environment value   
            self.stomach = 0                                    # set agen's stomach to 0 

# create function that calculates distance between agents 
    def distance_between(self, agent):
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5        
            
               
 # define sharing function       
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:                                   
            distance = self.distance_between(agent)             # call distance function to calculate how far away other agents are
            if distance <= neighbourhood:                       # if distance is within neighbourhood parameter
                sum = self.stomach + agent.stomach              # calculate total value of agents' stomach contents
                average = sum/2                                 # calculate the average
                self.stomach = average                          # set stomch of both agents to the average
                agent.stomach = average
                
