

def getnumber():
    seq0, seq1 = raw_input().split(' ')
    count = 0
    for i in xrange(len(seq0)):
        # if (seq0[i] == 'A' and seq1[i] != 'T') or (seq0[i] == 'T' and seq1[i] != 'A') \
        #         or (seq0[i] == 'C' and seq1[i] != 'G') or (seq0[i] == 'G' and seq1[i] != 'C'):
        if ''.join(seq0[i] + seq1[i]) not in ['AT', 'TA', 'GC', 'CG']:
            count += 1
    print count

getnumber()