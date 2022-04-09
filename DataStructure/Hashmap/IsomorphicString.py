# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        ns = len(s)
        nt = len(t)
        if ns != nt:
            return False

        s_map = {}
        for i, c in enumerate(s):
            if not c in s_map:
                s_map[c] = str(i)  
            else:
                s_map[c] += str(i)
        
        t_map = {}
        for i, c in enumerate(t):
            if not c in t_map:
                t_map[c] = str(i)  
            else:
                t_map[c] += str(i)
        
        for i in range(ns):
            if s_map[s[i]] != t_map[t[i]]:
                return False

        return True

    def isIsomorphic2(self, s: str, t: str) -> bool:

        ns = len(s)
        nt = len(t)
        if ns != nt:
            return False

        # Need to check 2 ways like s = "badc", t = "bada"
        s_map = {}
        t_map = {}  
        for i in range(ns):
            if not s[i] in s_map: 
                s_map[s[i]] = t[i]
            else:
                if s_map[s[i]] != t[i] :
                    return False
                    
            if  not t[i] in t_map:
                t_map[t[i]] = s[i]
            else:
                if t_map[t[i]] != s[i]:
                    return False
        
        return True
   

def main():
    s = "badc"
    t = "bada"
    sol = Solution()
    res = sol.isIsomorphic2(s, t)

    print(res)

if __name__ == '__main__':
    main()