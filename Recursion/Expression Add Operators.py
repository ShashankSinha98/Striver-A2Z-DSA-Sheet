from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []

        def _solve(idx: int, curr_str: str, curr_res: int, prev: int):
            if idx >= len(num):
                if curr_res == target:
                    res.append(curr_str)
                return

            for i in range(idx, len(num)):
                sub_str = num[idx: i+1]


                sub_num = int(sub_str)
                if idx == 0:
                    _solve(i+1, sub_str, sub_num, sub_num)
                else:
                    _solve(i+1, curr_str+"+"+sub_str, curr_res+sub_num, sub_num)
                    _solve(i+1, curr_str+"-"+sub_str, curr_res-sub_num, -sub_num)
                    _solve(i+1, curr_str+"*"+sub_str, curr_res-prev+(prev*sub_num), prev*sub_num)
                
                if num[idx] == '0':
                    break


        
        _solve(0, "", 0, 0)
        return res
    

if __name__ == "__main__":
    s = Solution()
    num, target = "105", 5
    print(s.addOperators(num, target))