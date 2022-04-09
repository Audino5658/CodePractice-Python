class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        sentence = ""
        for sub_str in words:
            sentence += sub_str
            if sentence == s:
                return True

        return False
        

        

def main():
    #s = "iloveleetcode"
    #words =["i","love","leetcode","apples"]
    s = "a"
    words =["aa","aaaa","banana"]
    sol = Solution()
    res = sol.isPrefixString(s,words)
    print(res)

    

if __name__ == "__main__":
    main()