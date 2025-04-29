# pm4py_process.py
# A simple process mining pipeline for student revision logs

import pm4py
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.visualization.petrinet import visualizer as pn_visualizer

# Load a sample event log (to be replaced with real Google Docs revision logs)
log = xes_importer.apply('data/sample_revision_log.xes')

# Discover a process model using Alpha Miner
net, initial_marking, final_marking = alpha_miner.apply(log)

# Visualize the discovered process model
gviz = pn_visualizer.apply(net, initial_marking, final_marking)
pn_visualizer.view(gviz)
