#Inspired by http://stackoverflow.com/questions/15389768/standard-deviation-of-a-list
import csv
import sys

def sum_digits(digit):
        return sum(int(x) for x in digit if x.isdigit())
def mean(data):
    """Return the sample arithmetic mean of data."""
    n = len(data)
    if n < 1:
        raise ValueError('mean requires at least one data point')
    total=0.0
    for element in data:
        total+=float(element)
    return total/float(n) # in Python 2 use sum(data)/float(n)

def _ss(data):
    """Return sum of square deviations of sequence data."""
    c = mean(data)
    ss = sum((float(x)-c)**2 for x in data)
    return ss

def pstdev(data):
    """Calculates the population standard deviation."""
    n = len(data)
    if n < 2:
        raise ValueError('variance requires at least two data points')
    ss = _ss(data)
    pvar = ss/n # the population variance
    return pvar**0.5
def stderr(data):
    """Calculates the population standard deviation."""
    n = len(data)
    if n < 2:
        raise ValueError('variance requires at least two data points')
    ss = _ss(data)
    pvar = ss/n # the population variance
    return pstdev(data)/n**0.5

with open(sys.argv[1],"r") as csvfile:
        csvreader = csv.reader(csvfile,delimiter=",")
        for row in csvreader:
                print ",".join((row[0],str(mean(row[1:])),str(stderr(row[1:]))))
