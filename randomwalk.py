import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys

# the function get dim end steps from user and print this graph. 

class RandomWalk:
	def __init__(self, max_steps, dim):      # define dimensions and length of the walk.
		self.max_steps = max_steps
		self.dim = dim
		self.coordinates = [[0] for s in list(range(dim))] 
	
    

	def build(self):              # build lists of steps. 
	
		for n in range(self.max_steps):
    			for s in self.coordinates:
        			s.append(s[-1]+random.randint(-1,1))

     
	def display(self):                       # print the graphs or coordinates.
		if self.dim == 1:		

			plt.scatter(self.coordinates , list(range(self.max_steps+1)),c='green', marker='+')
			plt.show()
		
		elif self.dim == 2:

			plt.scatter(*self.coordinates,c='red',marker='^')
			plt.show()

		elif self.dim == 3:
				
			fig = plt.figure()
			ax = fig.add_subplot(111, projection='3d')

			ax.scatter3D(*self.coordinates,c=self.coordinates[2],marker='^')
			plt.show()


		elif self.dim > 3:

                    for n in range(self.max_steps):
                        print(f"step {n+1}:" , end=' ')
                        print([s[n] for s in self.coordinates])
                        


if len(sys.argv) != 3:
	print("error!\nenter only 2 arguments!")
	exit()

rw = RandomWalk(int(sys.argv[1]),int(sys.argv[2]))
rw.build()
rw.display()





