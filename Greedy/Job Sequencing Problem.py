class Job:
    # Job class which stores profit and deadline.
    def __init__(self,id,deadline=0, profit=0):
        self.profit = profit
        self.deadline = deadline
        self.id = id

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,jobs: list[Job],n):
        jobs.sort(key=lambda x: x.profit, reverse=True)
        max_deadline = 0
        for i in range(len(jobs)):
            max_deadline = max(max_deadline, jobs[i].deadline)
        
        jobs_tracker = [-1]*(max_deadline+1)
        max_profit = 0
        cnt=0

        for i in range(len(jobs)):
            id, d, p = jobs[i].id, jobs[i].deadline, jobs[i].profit
            t = d
            while t > 0:
                if jobs_tracker[t]==-1:
                    jobs_tracker[t] = id
                    max_profit+=p
                    cnt+=1
                    break
                t-=1

        return [cnt, max_profit]
    

    def mapToJobs(self, jobs: list[tuple]) -> list[Job]:
        res = []
        for ji in jobs:
            id, d, p = ji
            res.append(Job(id, d, p))
        return res

#For Input: 
# 11
# 1 11 321 2 2 62 3 5 456 4 8 394 5 11 424 6 10 22 7 1 393 8 6 87 9 3 118 10 8 384 11 10 83
#
if __name__ == "__main__":
    s = Solution()
    jobs = [(6,2,80),(3,6,70),(4,6,65),(2,5,60),(5,4,25),(8,2,22),(1,4,20),(7,2,10)]
    n = len(jobs)
    print(s.JobScheduling(s.mapToJobs(jobs), len(jobs)))
