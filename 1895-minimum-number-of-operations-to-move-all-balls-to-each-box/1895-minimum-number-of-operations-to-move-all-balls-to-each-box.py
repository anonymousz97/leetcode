class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        left_sum = 0
        right_sum = 0
        left_count = 0
        right_count = 0
        for idx, i in enumerate(boxes):
            if i == '1':
                right_sum += idx
                right_count += 1
        # print(left_sum, right_sum, left_count, right_count)
        res = []
        # start looping left right
        for i in range(len(boxes)):
            res.append(left_sum + right_sum)
            if boxes[i] == '1':
                right_count -= 1
                left_count += 1
            left_sum = left_sum + left_count
            right_sum = right_sum - right_count
        return res
        