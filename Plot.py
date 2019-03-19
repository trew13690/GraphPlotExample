from graphics import *
import math

def main():

    app = App()
    app.run()



class App():
    """
    ===========================
    Class App:


        Data:
        window (GraphWin): Represents the window
        circle (GraphicsObject): Represent the circle
        coordinateAxis (CoordinateAxis): Represents the coordinateAxis
        
        Methods:
        run(self): Run the application 
        listenToMouse(self): Call the getMouse on the window Object which will return the GraphicsObject
        drawObjects(self, widgets): Draw all object to window
        drawCoordinates(self, CoordinateAxis): Draw the Coordinates on the window
    """
    def __init__(self):
        self.radius = float(input("What is your desired radius 1 - 10? "))
        print('Creating windows')
        self.window =   GraphWin("Plotter", 400,400)
        self.window.setBackground('white')
        self.window.setCoords(-10.0,-10.0, 11,11)
        print('Creating axes to orient yourself!')
        self.coordinateAxis = CoordinateAxis(window=self.window)
        print('Creating circles in the sand!')
        self.circle = Circle(Point(0,0), self.radius)
        self.text = Text(Point(0,10), "The current location is: ")
        self.info = Text(Point(0,-9), "Info: Click for radius")
        self.window.bind("<Motion>", self.on_enter)
        self.window.bind("<Button-1>", self.on_click_circle)
        
    def on_click_circle(self,event):
       self.info.setText("Info: " + str(self.radius))
       self.info.draw(self.window)

    def drawObjects(self):
        print("Drawing shapes in the sky!")
        self.circle.draw(self.window)
        self.text.draw(self.window)
        self.info.draw(self.window)

    def on_enter(self, event):
        print(str(event))
        print("Converting coordinates" + str(self.window.toWorld(event.x,event.y)))
        points =self.window.toWorld(event.x,event.y)
        points = [round(p,2) for p in points]
        print(str(points))
        self.text.setText("The Current location is: "+ str(points))
  
        
        

    def y_intercept(self):
        y = math.sqrt(self.radius**2-0)
        topY = Line(Point(-5,y),Point(5,y))
        topY.setArrow("both")
        topY.setOutline('red')
        topY.draw(self.window)

        bottomY = Line(Point(-5,-y), Point(5,-y))
        bottomY.setArrow("both")
        bottomY.setOutline("red")
        bottomY.draw(self.window)

    def x_intercept(self):
        x = math.sqrt(self.radius**2-0)
        topX = Circle(Point(x,0),.1)
        bottomX = Circle(Point(-x,0), .1)
        topX.setFill('red')
        bottomX.setFill('red')
        topX.draw(self.window)
        bottomX.draw(self.window)

    def run(self):
        print('We are Running Boss!')
        self.drawObjects()
        self.y_intercept()
        self.x_intercept()
        self.window.getMouse()


class CoordinateAxis:

    """
        =============================
        CoordinateAxis ~ Object Representing a coordinate Grid

        Data:
            Transform ~ Transform coordinates for ease
            Y-Axis(Line) ~ Line for the Y-Axis
            X-Axis (Line)~ Line for the X-Axis
            
        Methods:
            drawAxis(self) 
            

    """

    def __init__(self, window):
        print('Prepping the lines!')
        self.window = window
        self.windowHeight = window.getHeight()
        print('Your window is height: '+ str(self.windowHeight))
        self.windowWidth = window.getWidth()
        print('Your window is width: '+ str(self.windowWidth))
        self.x_axis = Line(Point(-10,0), Point(10,0))
        self.y_axis = Line(Point(0,-10), Point(0,10))
        self.drawAxis()
        
    def drawAxis(self):
        self.x_axis.draw(self.window)
        self.y_axis.draw(self.window)
        for i in range(-10,10):
            newLine = Line(Point(-.5,i),Point(.5,i))
            secondLine = Line(Point(i,.5), Point(i,-.5))
            newLine.draw(self.window)
            secondLine.draw(self.window)
       


main()