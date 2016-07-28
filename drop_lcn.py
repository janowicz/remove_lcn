import pandas as pd
import pandana as pdna

# Read in the nodes/edges csv's 
nodes = pd.read_csv('http://synthpop-data2.s3-website-us-west-1.amazonaws.com/modeldata/mpo27197000/nodes.csv').set_index('node_id')
edges = pd.read_csv('http://synthpop-data2.s3-website-us-west-1.amazonaws.com/modeldata/mpo27197000/edges.csv')

# Create network
net = pdna.Network(nodes["lon"], nodes["lat"], edges["from_id"], edges["to_id"],
                   edges[["distance"]])

# Identify low connectivity nodes
lcn = net.low_connectivity_nodes(10000, 10, imp_name='distance')

# Export cleaned network
net.save_hdf5('lcn_removed.h5', rm_nodes=lcn)


