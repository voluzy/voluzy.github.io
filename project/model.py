# functions to import
import operator
import random
#import matplotlib
#matplotlib.use('macosx')
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv

# create empty lists that are needed later     
environment = []
agents = []

# set parameters of model
num_of_agents = 50
iterations = 100
neighbourhood = 20

# open and read in environment file
file = open('in.txt', newline='')
reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:              #append values to 2D list
    rowlist = []
    for item in row:
        rowlist.append(item)
    environment.append(rowlist)
file.close()

fig = matplotlib.pyplot.figure(figsize = (7,7))     # create figure with size
ax = fig.add_axes([0,0,1,1])                        # add fixed axes to figure

# create agents with attributes
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

# define an update function to create animation
def update(frame_number):
    fig.clear()                             # clear figure so next iteration can be displayed
    random.shuffle(agents)                  # randomise order in which agents are passed in
    for i in range(num_of_agents):          # create for loop that calls the agent functions from agent framework
        agents[i].move()
        agents[i].eat()
        agents[i].vom()
        agents[i].share_with_neighbours(neighbourhood) 
    matplotlib.pyplot.xlim(0, 300)          # set limits of plot
    matplotlib.pyplot.ylim(0, 300)
    matplotlib.pyplot.imshow(environment)   # display the environment as background
    for i in range(num_of_agents):          # for loop to display each agents new position as scatterplot
        matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y,color='r') # set colour of all agents to red

# make the animation by calling the update function
# to make the animation run indefinitely, set repeat to 'True'        
animation = matplotlib.animation.FuncAnimation(fig, update, interval = 1, repeat=False, frames=iterations)     
fig.show()
