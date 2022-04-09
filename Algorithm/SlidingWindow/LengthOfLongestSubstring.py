# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        
        if n == 0:
            return 0

        max_len = 1

        for i in range(n-1):
            cur_str = s[i]
            cur_len = 1
            for j in range(i+1, n):
                if(not s[j] in cur_str) :
                    cur_len +=1
                    cur_str += s[j]
                else:
                    break
            max_len = max(cur_len , max_len)

        return max_len

    def lengthOfLongestSubstring2(self, s: str) -> int:
        char = []*128
        left = right = 0

        res = 0
        while res < len(s):
            r = s[right]
            char[ord(r)] += 1

            while char[ord(r)] > 1:
                l = s[left]
                char[ord(l)] -= 1
                left +=1

            res = max( res, right-left+1)
            right +=1

        return res

def main():

    sol = Solution()
    res = sol.lengthOfLongestSubstring("abcabcbb")
    print(res)

    

if __name__ == "__main__":
    main()