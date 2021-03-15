from schrodinger.utils import sea
from sys import argv

#Uses the internal schrodinger library to dump the results-sections of st2-files from the analyze-simualation workflow for desmond trajectories. 
for inputfile in argv[1:]:
        Map =sea.Map(open(inputfile).read())
        ind=range(0,len(Map.Keywords))
        for x in ind:
                results=[Map.Keywords[x][key] for key in Map.Keywords[x]]
                num_bins=10
                for result in results:
                        plottype=result.Name.val
                        datapoints=result.Result.val
                        if "RMSF" in plottype:
                                for point in datapoints:
                                        print(point)
