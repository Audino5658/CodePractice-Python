class Solution:

    def countCharacters(self, words: list[str], chars: str) -> int:

        res_sum = 0
        char_found = False
        for word in words:            
            for wc in word:
                if (word.count(wc) > chars.count(wc)):
                    char_found = False
                    break
                else:
                    char_found = True

            if char_found:
                res_sum += len(word)
        
        return res_sum

    def countCharacters_old(self, words: list[str], chars: str) -> int:
        res_sum = 0
        for word in words:
            count = 0
            tmp_chars = list(chars)
            for i, wc in enumerate(word):
                for c in tmp_chars:                              
                    if c == wc:
                        count+=1  
                        tmp_chars.pop(tmp_chars.index(c))
                        #tmp_chars = tmp_chars[0 : i : ] + tmp_chars[i + 1 : :]
                        break 
                        

                if i == len(word) -1:
                    if  count == len(word):
                        res_sum += count
        
        return res_sum

    def test(self, chars: str):
        for i, c in enumerate(chars):
            print(i)
            if(c=="e"):
                chars = chars[0 : i : ] + chars[i + 1 : :]
            


def main():
    #s = "iloveleetcode"
    #words =["i","love","leetcode","apples"]
    words = ["hello","world","leetcode"]
    chars = "welldonehoneyr"
    sol = Solution()
    #sol.test(chars)
    res = sol.countCharacters(words, chars)
    print(res)

    

if __name__ == "__main__":
    main()