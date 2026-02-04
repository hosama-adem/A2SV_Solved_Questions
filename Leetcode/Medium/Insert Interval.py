class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        sorted_intervals=sorted(intervals)
        result=[]
        left,right=0,1
        result.append(sorted_intervals[left])

        while right<len(intervals):
            if result[left][1]>=sorted_intervals[right][0] and result[left][1]<=sorted_intervals[right][1]:
                temp = result.pop()
                print(temp)
                result.append([temp[0],sorted_intervals[right][1]])
                right+=1

                
            elif result[left][1]>=sorted_intervals[right][0] and result[left][1]>=sorted_intervals[right][1]:
               
                right+=1

            
            else:
                result.append(sorted_intervals[right])
                right+=1
                left+=1
            
        return result


