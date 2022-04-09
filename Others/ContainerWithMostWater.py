
class Solution:
    def maxArea(self, height) -> int:
        max_area = 0
        n = len(height)

        if n < 1:
            return 0

        for i in range(n-1):
            for j in range(1, n):
                water_h = height[i] if height[i] < height[j] else height[j]
                area = water_h * (j-i)
                max_area = area if area > max_area else max_area

        return max_area

    def maxArea2(self, height) -> int:
        max_area = 0
        n = len(height)

        if n < 1:
            return 0

        r=n-1
        l=0
        for i in range(n-1):
            
            water_h = 0
            if height[l] < height[r] :
                water_h = height[l] 
                l+=1
            else :
                water_h = height[r]
                r-=1

            area = water_h * (n-i-1)    
            print(water_h , " ", (n-i-1)  )       
            max_area = area if area > max_area else max_area

        return max_area

def main():
    sol = Solution()
    res = sol.maxArea2([1,8,6,2,5,4,8,3,7])
    print(res)  
    pass

if __name__ == "__main__":
    main()