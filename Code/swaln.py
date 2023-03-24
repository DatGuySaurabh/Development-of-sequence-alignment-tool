import sys


# open the file
#Human_Genome = open("Humanch1.fasta")

# read the contents
#seq1 = Human_Genome.read()
#print ("Enter the first sequence. ")
#seq1=sys.stdin.readline()
#seq1=seq1.replace("\n","")
#print ("Enter the second sequence. ")
#seq2=sys.stdin.readline()
#seq2=seq2.replace("\n","")


#valid = 'ATCG'
#if any(i not in valid for i in seq1 + seq2):
#    print ('Please provide 2 valid DNA sequences as input.\n', 'Exit!\n')
#    sys.exit()


match    =  2
mismatch = -2
gap      = -1


def s_w(seqA, seqB):
   
    cols      = len(seqA)
    rows      = len(seqB)
    matrix    = [[0 for row in range(rows+1)] for col in range(cols+1)]
    paths     = [[0 for row in range(rows+1)] for col in range(cols+1)]
    max_score = 0
    s1, s2 = [], []
   
    for i in range(cols):
        for j in range(rows):
            if seqA[i] == seqB[j]:
                diag = matrix[i][j] + match
            else:
                diag = matrix[i][j] + mismatch
            up    = matrix[i + 1][j] + gap
            left  = matrix[i][j + 1] + gap
            score = max(0,diag, up, left)
            matrix[i+1][j+1] = score
            if score > max_score:
                max_score = score
                start_pos = [i+1, j+1]
   
            if matrix[i+1][j+1]   == diag and matrix[i+1][j+1] != 0:
                paths[i+1][j+1] = 'diag'
            elif matrix[i+1][j+1] == up   and matrix[i+1][j+1] != 0:
                paths[i+1][j+1] = 'up'
            elif matrix[i+1][j+1] == left and matrix[i+1][j+1] != 0:
                paths[i+1][j+1] = 'left'
   
    i, j = start_pos
    start_path = paths[i][j]
    while start_path != 0:
        if start_path == 'diag':
            s1.append(seqA[i-1])
            s2.append(seqB[j-1])
            i, j = i-1, j-1
        elif start_path == 'up':
            s1.append('-')
            s2.append(seqB[j-1])
            j = j-1
        else:
            s1.append(seqA[i-1])
            s2.append('-')
            i = i-1
        start_path = paths[i][j]
        
        print(s1,s2)
    #s1.reverse()
    #s2.reverse()
    seq1 = "".join(s1)
    seq2 = ''.join(s2)
    print("Score for the alignment is = " ,max_score)
    print (' Alignment\n', seq1, '\n', seq2, '\n')

    
    
#aln1, aln2 = s_w(seqA, seqB)
#print("Score for the alignment is = " ,max_score)
#print (' Alignment\n', seqA, '\n', seqB, '\n')