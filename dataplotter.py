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
        self.particleListx = []
        self.particleListy = []
        self.particleListMapping = []
        self.qValx = []
        self.qValy = []
        self.qStep = 0
        self.iterationStep = 0
        self.maxIteration = 0

    def outputPSOGraphs(self):
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
        pyplot.scatter(self.particleListx,self.particleListy, c=self.particleListMapping, cmap="plasma")
        positionBar = pyplot.colorbar()
        positionBar.set_label("Iteration")
        print(self.particleListMapping)
        pyplot.show()

    def outputQGraphs(self):
        qPlot = pyplot.figure()
        qPlot.suptitle("Q Values vs Iterations")
        pyplot.ylabel("Q Values")
        pyplot.xlabel("Iteration Number")
        pyplot.scatter(self.qValx,self.qValy)

    def appendQVal(self, valy, episodex, n_step):
        self.qStep = n_step
        #if (episodex % n_step) is 0:
        self.qValx.append(episodex)
        self.qValy.append(valy)

    def appendToFitnessList(self, xVal,yVal):
        self.fitnessIterationx.append(xVal)
        self.fitnessIterationy.append(yVal)

    def appendToPositionList(self, xVal,yVal, iteration, maxIteration):
        self.particleListx.append(xVal)
        self.particleListy.append(yVal)
        if self.maxIteration is 0:
            self.maxIteration = maxIteration
        if iteration is 0:
            self.iterationStep = 1
            self.particleListMapping.append(self.iterationStep)
        elif maxIteration % iteration is 0:
            self.iterationStep += 1
            self.particleListMapping.append(self.iterationStep)
        else:
            self.particleListMapping.append(self.iterationStep)
