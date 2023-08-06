'''
You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done on that day.

You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.
'''

def minDifficulty(jobDifficulty, d): #naive greedy
    jobs = jobDifficulty
    if len(jobs) < d:
        return -1
    tot = 0
    hi = 0
    for i in range(len(jobs)):
        if (len(jobs) - i <= d -1 ):
            tot += jobs[i]
        else:
            if jobs[i] > hi:
                hi = jobs[i]
    return tot + hi

    
    

print(minDifficulty([11,111,22,222,33,333,44,444], 6))
