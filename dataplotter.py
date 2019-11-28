from matplotlib import pyplot

'''
matplotlib is required to run this code.
install by using:
pip install matplotlib

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
		pyplot.plot(self.fitnessIterationx,self.fitnessIterationy)
		print self.fitnessIterationx

		particlePlot = pyplot.figure()
		particlePlot.suptitle("Particle position")
		pyplot.scatter(self.particleListx,self.particleListy)
		pyplot.show()
		

	def appendToList(self, xVal,yVal, listName):
		if listName == "fitness":
			#generate Qvalue values into list
			self.fitnessIterationx.append(xVal)
			self.fitnessIterationy.append(yVal)
		if listName == "particle":
			self.particleListx.append(xVal)
			self.particleListy.append(yVal)
