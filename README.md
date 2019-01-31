# better-lineups-dfs
Contains python programs for optimizing daily fantasy lineups based on a current projection file and current draftkings or fanduel player costs

The general purpose of this library is to enable anybody to use a solution to the "knapsack problem" to build an optimal daily 
fantasy lineup given a set of projections and prices. The primary knapsack file is optimizer.py. I copied this code as is from
and existing Git repository and have not had to change anything to get a working solution. Optimizer uses projections and salaries
and generically builds the "best" lineup that maximizes the total salary cap and spits out the highest possible points. Optimize.py
is a file that I also copied and updated to get working. It wraps Optimizer and provides the layer for the specific sport you care
about. It leverages a constants file to manage certain parameters of the sport and lineup. This program can be used through the
command line, but I prefer to run it via other files where I further set parameters. The balancedlineup files help you control
running multiple scenarios quickly to meet your specific needs. They also provide a good look into what parameters are available in 
Optimize. One thing I disabled was the bulk load of CSVs to the draftkings API. I was having trouble getting this to work and it
was unneccessary for a casual DFS player.
