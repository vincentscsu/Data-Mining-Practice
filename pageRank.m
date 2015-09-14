% PageRank algorithm with mechanism that deals with dead-ends and spider traps
% M: adjacency matrix
% r: rank
% rSum: sum of your rank scores
% beta: taxation probability parameter - %teleport
% epsilon: a range to check whether r has converged

M = [0, 0, 1; 0.5, 0, 0; 0.5, 1, 0];
N = rows(M);
rSum = 1;
beta = 0.7;
const = ones(N, 1) * ((1 - beta) / N);

r = ones(N, 1) / N;

epsilon = 0.000000001;

do
	r_pre = r;
	r = M * r;
	r = beta * M * r + const;
	s = sum(r);
	if (s < rSum)
		r = r + (rSum - s) / N;
	endif
	
	eps = abs(r - r_pre);

until (eps < epsilon)
r