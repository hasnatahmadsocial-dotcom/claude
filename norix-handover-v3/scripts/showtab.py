import sys
exec(open('scripts/cmp2.py').read().split('A=load')[0])
A=load(sys.argv[1])
for tid in sys.argv[2:]:
    t,L=A[tid]; print('#####',t)
    for l in L: print(l)
