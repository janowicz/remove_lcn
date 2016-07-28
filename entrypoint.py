import sys
import subprocess
import pandas as pd

#Export full network (with the low connectivity nodes) to csv
pass

# Run LCN removal process
subprocess.check_call([sys.executable, 'drop_lcn.py'])

# Read in cleaned nodes/edges
connected_net = pd.HDFStore('lcn_removed.h5')
nodes = connected_net['nodes']
edges = connected_net['edges']

# Continue with rest of your network pipeline
