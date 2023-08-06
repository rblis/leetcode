nums = [2,0,2,1,1,0]
cols = [0,0,0]
for num in nums:
    if num == 0:
        cols[0] += 1
    if num == 1:
        cols[1] += 1 
    if num == 2:
        cols[2] += 1
print( [0]*cols[0] + [1]*cols[1] + [2]*cols[2] )