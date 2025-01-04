class Solution:
    def pageFaults(self, N, C, pages):
        page_fault_count = 0
        q = []

        for pi in pages:
            if pi not in q:
                if len(q) >= C:
                    q.remove(q[0])
                page_fault_count+=1
                q.append(pi)

            else:
                q.remove(pi)
                q.append(pi)
        return page_fault_count
    
if __name__ == "__main__":
    s = Solution()
    pages = [5, 0, 1, 3, 2, 4, 1, 0, 5]
    N, C = len(pages), 4
    print(s.pageFaults(N, C, pages))
