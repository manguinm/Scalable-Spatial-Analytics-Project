# Imports
import subprocess

def main():

    # Parse the price data
    ############################## 
    # Read in the "Master Calibration Set" specification file
    fill = open('mcsSpec.csv','rU')
    priceList = fill.readlines()
    fill.close()
    
    # Split the columns of each row
    for index, line in enumerate(priceList):
        priceList[index] = line.split(',')
    ##############################
    
    # Parse the demand data
    ############################## 
    # Read in the "Master Calibration Set" specification file
    fill = open('mcsSpec.csv','rU')
    demandList = fill.readlines()
    fill.close()
    
    # Split the columns of each row
    for index, line in enumerate(demandList):
        demandList[index] = line.split(',')
    ##############################
    
    # Print statements to check the type
    print type(demandList)
    print type(demandList[1])
    print type(demandList[1][1])
    
    print demandList[0]
    print demandList[0]
    
    # Now you have two lists of lists with the elements of the embedded list being strings with the value between the commas
    
    # Open a file to print full data 
    priceDemandData = open('priceDemand.csv','w')
    
    # Loop through price list and check for corresponding demand, if not existant, throw the price element away
    for price in priceList:
        # Get the current price time pair
        day = price[0]
        hour = price[1]
        priceValue = price[2]
        
        # Loop through the demand list and find the matching day and hour
        for demand in demandList:
            if(demand[0]==day and demand[0]==hour):
                priceDemandData.write(str(hour)+','+str(hour)+','+str(priceValue)+','+str(demand[2])+'\n')
    
    # Close the price demand file
    priceDemandData.close()       

# Boiler plate used to run script as function.
if __name__ == "__main__":
    main()
