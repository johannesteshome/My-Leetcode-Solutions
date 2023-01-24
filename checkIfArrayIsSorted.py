class Solution:
       def arraySortedOrNot(self, arr, n):
           # two pointers on the same array aka Parallel pointers
           left, right = 0, 1
           while(right < n):
               if(arr[left] > arr[right]):
                   return False
               left+=1
               right+=1
           return True
