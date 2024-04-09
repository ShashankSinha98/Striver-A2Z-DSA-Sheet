class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        tmp = s + s

        i, j = 0, 0
        while i < len(tmp):
            if tmp[i] == goal[j]:
                old_pos = i
                while i < len(tmp) and j < len(goal) and tmp[i]==goal[j]:
                    i += 1
                    j += 1
                
                if j == len(goal):
                    return True
                else:
                    i = old_pos + 1
                    j = 0
            else:
                i+=1
        return False


if __name__ == "__main__":
    s = "abcde"
    goal = "abced"
    print(Solution().rotateString(s, goal))
                