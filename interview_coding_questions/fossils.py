def interpolation(d, x):
    output = d[0][1] + (x - d[0][0]) * ((d[1][1] - d[0][1])/(d[1][0] - d[0][0]))
 
    return output
 
# Driver Code
data=[[2019, 12124],[2021, 5700]]
 
year_x=2020

def mean(data):
    return sum(data) / len(data)
def median(data):
    n = len(data)
    index = n // 2
    if n % 2:
        return sorted(data)[index]
    return sum(sorted(data)[index - 1:index + 1]) / 2

def variance(data):
    n = len(data)
    mean = sum(data) / n
    deviations = [(x - mean) ** 2 for x in data]
    variance = sum(deviations) / n
    return variance

def stdev(data):
    var = variance(data)
    std_dev = math.sqrt(var)
    return std_dev