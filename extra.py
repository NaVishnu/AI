def plot(self, xmin, xmax):
        x = np.arange(xmin, xmax, 0.1)
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.set_title(self.name)
        for _set in self.sets:
            y = self(_set, x)
            ax.plot(x, y)
        plt.show()
       
def plot(self, xmin, xmax, fuzzyValues):
        x = np.arange(xmin, xmax, 0.1)
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.set_title(self.output.name + " = " + str(self.defuzzify(xmin, xmax, fuzzyValues, 0.001)))
        for _set in self.output.sets:
            y = self.output(_set, x)
            ax.plot(x, y)
        y = self.defuzzifyFunction(x, fuzzyValues)
        ax.plot(x, y, color="black")
        plt.show()

    def defuzzifyFunction(self, x, fuzzyValues):
        values = np.zeros(x.shape)
        for _set in self.output.sets:
            if _set in fuzzyValues.keys():
                values = np.maximum(values, np.minimum(fuzzyValues[_set], self.output(_set, x)))
        return values

    def defuzzify(self, xmin, xmax, fuzzyValues, w=0.01):
        # Find the defuzzifiedValue of the function
        x = np.arange(xmin, xmax, w)
        y = self.defuzzifyFunction(x, fuzzyValues)

        centroid = 0
        areas = 0
        for _x, _y in zip(x, y):
            area = w * _y
            centroid += ((_x + (w / 2)) * area)
            areas += area

        return centroid / areas
