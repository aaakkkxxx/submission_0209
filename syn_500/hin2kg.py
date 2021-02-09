# -*- coding: utf-8 -*-

from collections import Counter
import random
import numpy as np 

_graph_size = 500

a_list = np.array(["A"+str(i) for i in range(int(_graph_size*0.3))])
b_list = np.array(["B"+str(i) for i in range(int(_graph_size*0.3))])
c_list = np.array(["C"+str(i) for i in range(int(_graph_size*0.4))])

_random_edge_number_a = random.randint(3*len(a_list), 5*len(a_list))
aa_list = []
edge_type = [0, 1]
for n in np.random.choice(a_list, replace=False, size=len(a_list)):
    aa_list.append((str(n), str(random.choice(a_list)), random.choices(edge_type, [0.7, 0.3])[-1]))
for n in np.random.choice(a_list, size=_random_edge_number_a):
    aa_list.append((str(n), str(random.choice(a_list)), random.choices(edge_type, [0.7, 0.3])[-1]))

_random_edge_number_b = random.randint(2*len(b_list), 3*len(b_list))
ba_list = []
for n in np.random.choice(b_list, replace=False, size=len(b_list)):
    ba_list.append((str(n), str(random.choice(a_list)), 2))
for n in np.random.choice(b_list, size=_random_edge_number_b):
    ba_list.append((str(n), str(random.choice(a_list)), 2))

_random_edge_number_b = random.randint(len(b_list), 2*len(b_list))
bb_list = []
edge_type = [3, 4]
for n in np.random.choice(b_list, replace=False, size=len(b_list)):
    bb_list.append((str(n), str(random.choice(b_list)), random.choices(edge_type, [0.55, 0.45])[-1]))
for n in np.random.choice(b_list, size=_random_edge_number_b):
    bb_list.append((str(n), str(random.choice(b_list)), random.choices(edge_type, [0.55, 0.45])[-1]))

_random_edge_number_c = random.randint(2*len(c_list), 4*len(c_list))
ca_list = []
for n in np.random.choice(c_list, replace=False, size=len(c_list)):
    ca_list.append((str(n), str(random.choice(a_list)), 5))
for n in np.random.choice(c_list, size=_random_edge_number_c):
    ca_list.append((str(n), str(random.choice(a_list)), 5))
    

ent_list = []
ent_list.extend(a_list)
ent_list.extend(b_list)
ent_list.extend(c_list)
ent2id = dict()
for ent in ent_list:
    ent2id[str(ent)] = len(ent2id)

node_type_dict = {"A":"0", "B":"1", "C":"2"}
with open("syn_node_{}.dat".format(_graph_size), 'w') as out:
    for i in list(ent2id.keys()):
        out.write(' '.join([str(ent2id[i]), i[:1], node_type_dict[i[:1]]])+'\n')
      
links = []
links.extend(aa_list)
links.extend(ba_list)
links.extend(bb_list)
links.extend(ca_list)

with open("syn_link_{}.dat".format(_graph_size), 'w') as out:
    for i in links:
        out.write(' '.join([str(ent2id[i[0]]), str(ent2id[i[1]]), str(i[2])]))
        out.write('\n')
