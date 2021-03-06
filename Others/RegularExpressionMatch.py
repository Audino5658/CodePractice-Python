class Solution:
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])

    def match(self, text, pattern):
        if not pattern: return not text
        first_match = bool(text) and pattern[0] in {text[0], '.'}
        return first_match and self.match(text[1:], pattern[1:])  



def main():
    sol = Solution()
    res = sol.isMatch("aab", "c*a*b")

    #res = sol.match("aab", "a.b")
    #print(res)

    print(bool("test"))

if __name__ == "__main__":
    main()

