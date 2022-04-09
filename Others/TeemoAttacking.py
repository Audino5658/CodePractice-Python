class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        
        left = timeSeries[0]
        right = timeSeries[0] + duration - 1
        totalTime = right - left + 1

        for ATKtime in timeSeries[1::] :
            if ATKtime <= right:
                totalTime += (ATKtime + duration - 1) - right
                right = ATKtime + duration - 1              
            else:
                totalTime += duration
                left = ATKtime
                right = ATKtime + duration - 1

        return totalTime



    def findPoisonedDuration_bad(self, timeSeries: list[int], duration: int) -> int:
        
        intervalList = []
        for atkTime in timeSeries:
            intervalList.append([atkTime, atkTime+duration-1])

        left = intervalList[0][0]
        right = intervalList[0][1]
        totalTime = right - left + 1

        for interval in intervalList[1::] :
            if interval[0] <= right:
                totalTime += interval[1] - right
                right = interval[1]
            else:
                totalTime += interval[1] - interval[0] + 1
                right = interval[1]
                left = interval[0]

        return totalTime
            
        




def main():
    timeSeries = [1,2]
    duration = 2

    sol = Solution()
    res = sol.findPoisonedDuration(timeSeries, duration)
    print(res)

    

if __name__ == "__main__":
    main()