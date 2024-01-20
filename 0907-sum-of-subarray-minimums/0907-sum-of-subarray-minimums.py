class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        M = 1000000007
        s = 0
        n = len(arr)
        dp = [0]*(n)

        right = [i for i in range(n)]  
        stack = [0]

        for i in range(1,n,1):

            curr = arr[i]
            while(stack and curr < arr[stack[-1]]):

                idx = stack.pop()
                right[idx] = i

            stack.append(i)

        dp[-1] = arr[-1]

        for i in range(n-2,-1,-1):

            right_idx = right[i]     
            if right_idx == i:     # case 1

                curr = (n-i)*arr[i]
                dp[i] = curr

            else:   # case 2

                # sum upto next smaller rhs element
                upto_small = (right_idx-i)*(arr[i])   

                curr_sum = (upto_small + dp[right_idx])
                dp[i] = curr_sum
        for i in dp:
            s = int((s + i)%M)
        return s