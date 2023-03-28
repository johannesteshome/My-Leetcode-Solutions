class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        def merge(left_half, right_half):

            p1 = p2 = 0

            while p1 < len(left_half):
                ans[left_half[p1][1]] += p2

                while p2 < len(right_half) and right_half[p2][0] < left_half[p1][0]:
                    ans[left_half[p1][1]] += 1
                    p2+=1
                
                p1+=1


            ptr1 = ptr2 = 0
            sortedList = []
            while ptr1 < len(left_half) and ptr2 < len(right_half):
                if left_half[ptr1][0] < right_half[ptr2][0]:
                    sortedList.append(left_half[ptr1])
                    ptr1 += 1
                else:
                    sortedList.append(right_half[ptr2])
                    ptr2 += 1

            if ptr1 < len(left_half):
                sortedList.extend(left_half[ptr1:])
            if ptr2 < len(right_half):
                sortedList.extend(right_half[ptr2:])

            return sortedList


        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]
            mid = left + (right - left) // 2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)

            return merge(left_half, right_half)

        ans = [0] * len(nums)
        arr = []

        for i in range(len(nums)):
            arr.append((nums[i], i))

        result = mergeSort(0, len(arr)-1, arr)
        print(result)
        return ans