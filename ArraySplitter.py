#Array Splitter Class. The number of splits is determined by the number passed into the method.
class ArraySplitter:

#Method for array splitting. 
    def splitArray(arrayToSplit, numberOfSplits):
        #get the length of the passed in array.
        length = len(arrayToSplit)
        #Declaration of the array this method will be returning
        split = []
        #Detemine how big each group should be
        sizeOfArrays = length // numberOfSplits
        #Loop through to the number of splits
        for i in range(numberOfSplits):
            #If the length of the array is grater than the division number
            if len(arrayToSplit) > sizeOfArrays:
                #Add entries 0 through to the element equal to the size of the array as their own array in "split"
                split.append(arrayToSplit[0:sizeOfArrays])
                #Remove those entries from the current array
                arrayToSplit = arrayToSplit[sizeOfArrays:]
            
        #Add any remainders to the "split" array
        split.append(arrayToSplit)
        return split

