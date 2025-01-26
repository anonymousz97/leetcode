class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        value_index_pairs = [(value, idx) for idx, value in enumerate(nums)]
        value_index_pairs.sort()
        grouped_pairs = [[value_index_pairs[0]]]
        for i in range(1, len(value_index_pairs)):
            if value_index_pairs[i][0] - value_index_pairs[i - 1][0] <= limit:
                grouped_pairs[-1].append(value_index_pairs[i])
            else:
                grouped_pairs.append([value_index_pairs[i]])

        for group in grouped_pairs:
            indices = [index for _, index in group]
            indices.sort()
            for i, index in enumerate(indices):
                nums[index] = group[i][0]

        return nums