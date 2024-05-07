class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack

    def place_sorted(self, st: list, n):
    
        if len(st) == 0:
            st.append(n)
            return
        
        elem = st[-1]
    
        if elem > n:
            st.pop()
            self.place_sorted(st, n)
            st.append(elem)
        else:
            st.append(n)


    def Sorted(self, st):
        if len(st) <= 1:
            return
    
        elem = st.pop()
        self.Sorted(st)
        self.place_sorted(st, elem)

if __name__ == "__main__":
    st = [1, 0, 0, 2]
    s = Solution()
    s.Sorted(st)
    print(st)
