class Solution:
    def countGoodSubstrings(self, s: str) -> int:
            res = 0
            i=0
            length = len(s)
            while(i<length):
                if i >= 2:
                    #print(substring)
                    if s[i] != s[i-1] and s[i] != s[i-2] and s[i-1] != s[i-2]:
                        res += 1
                i+=1
            return res

    def countGoodSubstrings_bad(self, s: str) -> int:

        substring = ""
        res = 0
        length = len(s)

        i = 0
        l = r = 0

        while(i<length):
            if i < 3:  
                substring += s[i]
                r+=1
            else:
                l+=1
                substring = s[l] + substring[2] + s[r]
                r+=1

            if i >= 2:
                #print(substring)
                if substring[0] != substring[1] and  substring[1] != substring[2] and substring[0] != substring[2]:
                    res += 1

            i+=1

        return res

    def test(self):
        s = "aababcabc"
        substring_table = {}
        substring_table[s[0]] += 1

        print(substring_table)


def main():
    input = "aababcabc"
    sol = Solution()
    print(sol.countGoodSubstrings(input))
    #sol.test()


if __name__ == "__main__":
    main()