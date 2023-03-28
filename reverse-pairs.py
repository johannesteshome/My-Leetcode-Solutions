class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0
        def merge(left_half, right_half):
            nonlocal count

            p1 = p2 = 0

            # while p1 < len(left_half) and p2 < len(right_half):
            #     if left_half[p1] > right_half[p2] * 2:
            #         count += 1
            #         p2 += 1
            #     else:
            #         p1 += 1
            #         if p1 < len(left_half):
            #             count += p2
            
            # if p1 < len(left_half) and p2 < len(right_half):
            #     for i in range(p1, len(left_half)):
            #         count += len(right_half)


            while p1 < len(left_half):
                count += p2

                while p2 < len(right_half) and left_half[p1] > right_half[p2] * 2:
                    count += 1
                    p2 += 1
                
                p1 += 1


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

        result = mergeSort(0, len(nums)-1, nums)
        print(result)
        return count