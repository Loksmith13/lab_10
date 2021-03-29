#LAB_10
#MASON STODDARD
#ADVANCED EMBEDDED


import matplotlib.pyplot as plt

#STEP 1
plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])     #creates plots for x and y at assigned values
plt.ylabel('Y')                                 #labels y axis
plt.xlabel('X')                                 #labels x axis
plt.axis([0, 4, 0, 16])                         #creates the mins and maxes for ehch plot
plt.show()

#STEP 2

import numpy as np
import matplotlib.pyplot as plt

# This function takes a number as input and returns the result of the equation
def math_fun(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)           #gives the values with 0.1 steps
t2 = np.arange(0.0, 5.0, 0.02)          #gives values with 0.02 steps
plt.figure(1)                           #new window

plt.subplot(211)                        #new plot with a row of 2, col of 1 and indexes at 1
plt.plot(t1, math_fun(t1), 'r+', t2, math_fun(t2), 'k')     #plots with red +, black -
plt.grid()                              #gens grid lines

plt.subplot(212)                        #new plot with row of 2, col 1 and indexes at 2
plt.plot(t2, np.cos(2*np.pi*t2), 'b--') #plots with blue dashes
plt.grid()
plt.show()

#STEP 3

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()                  #creates figure
ax = plt.axes(projection="3d")      # configures for 3 axis

z_line = np.linspace(0, 15, 1000)   #creates line spacing of 15 @1000 samples
x_line = np.exp(-0.1*z_line) * np.cos(z_line)   #uses the zline to create xline
y_line = np.exp(-0.1*z_line) * np.sin(z_line)   #uses x line to creates yline
ax.plot3D(x_line, y_line, z_line, 'red')        #generates 3d in red

ax.set_xlabel("x")                  #labels x axis
ax.set_ylabel("y")                  #labels y axis
ax.set_zlabel("z")                  #lables z axis

plt.show()

#STEP 4  RASP PI

import serial
import matplotlib.pyplot as plt
from drawnow import *

Data1 = []              #values from arduino for red/blue
Data2 = []

def PlotSignal():
    plt.ylim(0,1200)    #limits axix to 1200
    plt.title('Ploting in Streaming AD0 from Arduino')  #title
    plt.grid(True)      #turns on grid lines
    plt.ylabel('Analog Input Value')    #y title
    # Plot 1st set of data, format - red dashed line, label data as A0 input
    plt.plot(Data1, 'r--', label='A0 Input')    #
    # Plot 2nd set of data, format - blue dotted line, label data as A1 input
    plt.plot(Data2, 'b:', label='A1 Input')
    # Create legend and place in upper right
    plt.legend(loc='upper right')

# Main Function
if __name__ == '__main__':

    # Create serial communicaton object at 9600 baudrate
    ser = serial.Serial('COM5', 9600)
    # Turn on interactive mode
    plt.ion()
    # Initialize a data counter variable
    Dcounter=0
    # Fluse Serial comms line
    ser.flush()

    # Loop program
    while True:
        # If no data is being recieved:
        while (ser.inWaiting()==0):
            # Do nothing
            pass
        # Decode and read data from Arduino
        ardData = ser.readline().decode('utf-8')
        # Split incoming string at each "," to get each individual data value
        InputData = ardData.split(',')
        # Convert input data value 1 to float and store in variable
        temp_val1 = float(InputData[0])
        # Convert input data value 2 to float and store in variable
        temp_val2 = float(InputData[1])
        # Add input data1 values to data1 list by appending
        Data1.append(temp_val1)
        # Add input data2 values to data2 list by appending
        Data2.append(temp_val2)

        #  Call drawnow function for PlotSignal
        drawnow(PlotSignal)
        # Short pause
        plt.pause(0.000001)
        # Increment data counter variable by 1
        Dcounter=Dcounter+1
        # if data counter variable is greater than 60:
        if(Dcounter>60):
            # Reset data counter variable to 0
            Dcounter=0
            # Clear data from lists
            Data1.pop(0)
            Data2.pop(0)
    # Close Serial communication
    ser.close()