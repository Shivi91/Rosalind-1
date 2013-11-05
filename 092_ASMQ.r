# A solution to a ROSALIND bioinformatics problem.
# 
# Problem Title: Assessing Assembly Quality with N50 and N75
# Rosalind ID: ASMQ
# Rosalind #: 092
# URL: http://rosalind.info/problems/asmq/

# I'm learning R, and this is a straightforward problem, so I'll try it in R!
contigs <- scan('data/rosalind_asmq.txt', what='character')
lengths <- nchar(contigs)
L <- seq(max(lengths),min(lengths), -1)

N <- vector(mode='numeric', length=length(L))
N[1] = L[1]*length(lengths[lengths==L[1]])
for(i in 2:length(L) ){
  N[i] = L[i]*length(lengths[lengths==L[i]]) + N[i-1]
}

minL <- c(ceiling(0.5*sum(lengths)),ceiling(0.75*sum(lengths)))
N_values <- vector(mode='numeric', length=2)
for (i in 1:2){
    N_values[i] = L[match(min(N[N>minL[i]]),N)]
}

cat(as.character(N_values), file='output/092_ASMQ.txt', sep=' ')
