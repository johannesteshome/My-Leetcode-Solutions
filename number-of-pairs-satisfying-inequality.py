class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        def merge(left_half, right_half):
            nonlocal count

            cptr1 = len(left_half) - 1
            cptr2 = len(right_half) - 1

            # while cptr1 >= 0 and cptr2 >= 0:
            #     if left_half[cptr1] <= right_half[cptr2] + diff:
            #         count += 1
            #         cptr2 -= 1
            #     else:
            #         cptr1 -= 1
            #         count += (len(right_half) - cptr2 - 1)
            
            # if cptr1 > -1:
            #     for i in range(cptr1):
            #         count += len(right_half)

            while cptr1 >= 0:
                count += (len(right_half) - cptr2 - 1)

                while left_half[cptr1] - diff <= right_half[cptr2] and cptr2 >= 0:
                    cptr2-= 1
                    count +=1
                cptr1-=1


            ptr1 = ptr2 = 0
            sortedList = []
            while ptr1 < len(left_half) and ptr2 < len(right_half):
                if left_half[ptr1] < right_half[ptr2]:
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

        count = 0
        arr = []

        for i in range(len(nums1)):
            arr.append(nums1[i] - nums2[i])

        result = mergeSort(0, len(arr)-1, arr)
        print(result)
        return count