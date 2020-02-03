#------------Imports----------------------------------#
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
#-----------------------------------------------------#

count =0                        #Global Count to keep track of chunk array 
plot = plt.figure()             #Creating a figure to plot on
axes = plot.add_subplot(111)    #Add a subplot to the figure
plot.suptitle('Lets Plot Eh? ', fontsize=14, fontweight='bold') #Main title of graph

#----Getting the Data Source---------------------------------------------------#
def getDataSource(): 
    fileName = sys.argv[1]               #get the first argument from the command line which is filename
    xaxis =[];                           #empty array to store x axis value
    yaxis =[];                           #empty array to store y axis value
    with open(fileName, 'r') as lines:   #open the file sent in command line in readmode 
        next(lines);                     #skip the firs line because they are headers
        for data in lines:               #for each line in file
            if(len(data) >1):            #if length of data is not blank
                x,y = data.split(',');   #split on comma  and store in x and y         
                xaxis.append(float(x));  #append x value
                yaxis.append(float(y));  #append y value
    return xaxis,yaxis                   #return x axis and y axis values
#------------------------------------------------------------------------------------#

#------Divide data in chunks---------------------------------------------------------#
def chunks(chunk, n):
    """This function divdies the data in chunks of n"""
    for i in range(0, len(chunk), n):
        yield chunk[i:i + n]
#------------------------------------------------------------------------------------#  

#----------Animate function called by animate----------------------------------------#   
def animate(i):
    global count            #Using global count 
    plotx =[]               #To save chunks of x value
    ploty=[]                #To save chunks of y value
    x,y=getDataSource()     #Store x and y axis values
    fx=[]                   #Store x plotting values
    fy=[]                   #Store y plotting value
    for i in chunks(x,30):  #Get value of x in chunks of 30
        plotx.append(i)     #For each value yielded by chunk add it to plotx
    for i in chunks(y,30):  #Get value of y in chunks of 30
        ploty.append(i)     #For each value yielded by chunk add it to ploty
    if(count < len(plotx)): #if count is less than length 
        fx = plotx[count]   #get the value at count position of plotx
        fy = ploty[count]   #get the value at count position of ploty
        count = count+1     #increment counter by 1
    else:
        count = 0           #set count to zero
        fx = plotx[count]   #get the value at count position of plotx
        fy = ploty[count]   #get the value at count position of ploty
        count = count+1     #increment counter by 1
    
    axes.clear()            #clear the axes which has old values 
    axes.set_title("Data set  {}".format(count))    #Show the data set on which we are working
    axes.set_xlabel('Max = {}   Min = {}'.format(max(fx),min(fx)))  #Show the max and min of x axis as label
    axes.set_ylabel('Max = {}   Min = {}'.format(max(fy),min(fy)))  #Show the max and min of y axis as label
    axes.plot(fx,fy)        #plot the values on graph
#-----------------------------------------------------------------------------------------#    

ani = animation.FuncAnimation(plot,animate,interval =1000)  #Start the animation at interval of 1 second
plt.show()  #show the graph