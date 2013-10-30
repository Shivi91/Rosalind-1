# A solution to a ROSALIND bioinformatics problem.
# 
# Problem Title: Wright-Fisher's Expected Behavior
# Rosalind ID: EBIN
# Rosalind #: 094
# URL: http://rosalind.info/problems/ebin/

# This problem is more mathematics than programming.
#
# It is well established that the expected value of a binomial random variable X given by
# X~Bin(n,p) has expected value E(X)=n*p.
#
# Learning R, so might as well use it for a simple problem like this!

n <- scan("data/rosalind_ebin.txt",nlines = 1)
p <- scan("data/rosalind_ebin.txt", skip = 1)
E <- n*p
cat(as.character(E), file='output/094_EBIN.txt', sep=' ')
