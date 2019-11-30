from matplotlib import pyplot

'''
matplotlib is required to run this code.
install by using:
pip install matplotlib
@author Kyle Jolicoeur
'''
'''
dev_x = [1,2,3,4,5]

dev_y = [60,70,80,90,100]
#pyplot.plot(dev_x,dev_y)
pyplot.scatter(dev_x,dev_y)

pyplot.xlabel('XAxis')
pyplot.ylabel('YAxis')
pyplot.title('sample plot 1')
#pyplot.legend(['first','second'])
pyplot.show()
'''
class DataPlotter:

	def __init__(self):
		#G1: Fitness vs iteration
		self.fitnessIterationx = []
		self.fitnessIterationy = []
		self.particleListx = [1]
		self.particleListy = [1]
		self.qValx = []
		self.qValy = []
		self.qStep = 0
		'''
		qValPlot = pyplot.figure()
		x = [1,2,3,4]
		y=[2,3,4,5]
		#laxes = qValPlot.add_axes([0,0,1,1])
		pyplot.plot(x,y)
		particlePlot = pyplot.figure()
		#paxes = particlePlot.add_axes([0,0,1,1])
		pyplot.plot([2,3,4,5,6,7,8],[1,2,3,4,5,6,7])
		pyplot.show()
		'''

	def outputGraphs(self):
		fitnessPlot = pyplot.figure()
		fitnessPlot.suptitle("Fitness Function Value vs Iterations")
		pyplot.scatter(self.fitnessIterationx,self.fitnessIterationy)
		pyplot.ylabel("Fitness Function Value")
		pyplot.xlabel("Iteration Number")

		fitnessPlot2 = pyplot.figure()
		fitnessPlot2.suptitle("Fitness Function Value vs Iterations")
		pyplot.scatter(self.fitnessIterationx,self.fitnessIterationy)
		pyplot.ylabel("Fitness Function Value (log scale)")
		pyplot.xlabel("Iteration Number")
		pyplot.yscale("log")

		particlePlot = pyplot.figure()
		particlePlot.suptitle("Particle position")
		pyplot.scatter(self.particleListx,self.particleListy)
				
		qPlot = pyplot.figure()
		qPlot.suptitle("Q Values vs Iterations")
		pyplot.ylabel("Q Values")
		pyplot.xlabel("Iteration Number")
		pyplot.scatter(self.qValx,self.qValy)
		pyplot.show()
		
	def appendQVal(self, valy, episodex, n_step):
		self.qStep = n_step
		#if (episodex % n_step) is 0:
		self.qValx.append(episodex)
		self.qValy.append(valy)
	def appendToList(self, xVal,yVal, listName):
		if listName == "fitness":
			#generate Qvalue values into list
			self.fitnessIterationx.append(xVal)
			self.fitnessIterationy.append(yVal)
		if listName == "particle":
			self.particleListx.append(xVal)
			self.particleListy.append(yVal)
