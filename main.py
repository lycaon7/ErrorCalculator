import math

rawData = [0.285,0.24]
toolError = 0.0025

if __name__ == '__main__':
    if rawData:
        # Calculate Average
        sum = 0
        for i in rawData:
            sum += i
        average = round(sum / len(rawData),11)
        print("Average:", average)

        # Calculate Standard Deviation
        sum = 0
        for i in rawData:
            sum += math.pow((i - average), 2)
        standardDeviation = round(math.sqrt(sum / (len(rawData) - 1)),11)
        print("Standard Deviation:", standardDeviation)

        # Calculate Statistical Error
        statisticalError = round(standardDeviation / math.sqrt(len(rawData)),11)
        print("Statistical Error:", statisticalError)

        # Calculate Final Error
        finalError = round(math.sqrt(math.pow(statisticalError, 2) + math.pow(toolError, 2)),11)
        print("Final Error:", finalError)
