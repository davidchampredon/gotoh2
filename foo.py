from gotoh2 import Aligner, map_coordinates

g1 = Aligner(gop=10)  # default gop=10
g2 = Aligner(gop=8)   

ref   = 'TACGTA'
query = 'TACTA'  # G removed
a1 = g1.align(ref, query)
a2 = g2.align(ref, query)
print(a1)
print(a2)
