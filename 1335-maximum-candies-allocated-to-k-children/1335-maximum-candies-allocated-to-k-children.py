class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if k == 0:
            return 0

        left, right = 1, max(candies)
        best = 0

        while left <= right:
            mid = (left + right) // 2
            count = sum(c // mid for c in candies)  # Tổng số phần có thể tạo ra

            if count >= k:
                best = mid  # Lưu kết quả tốt nhất hiện tại
                left = mid + 1  # Tăng giá trị để tìm số lượng lớn hơn
            else:
                right = mid - 1  # Giảm giá trị vì không đủ phần

        return best
            