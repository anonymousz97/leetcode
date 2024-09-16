​1. Count how many bits in a | b need to be flipped to a 1.
2. Count how many bits in a need to be flipped to a 0.
3. Count how many bits in b need to be flipped to a 0.

Formula for each section

1. (((a | b) & c) ^ c).bit_count()
First, we calculate a | b. Then, we use c as a bitmask to extract only the bits in a | b that are set to 1 in c. Finally, we use an xor to calculate how many of the set bits in c are 0 in a | b. This works because the bits that are 1s in both c and a | b will become 0s, while the bits that are 1s in c and 0s in a | b will become 1s. And, since we used c as a bitmask, we don't have to worry about bit that are 1s in a | b but 0s in c. Finally, we count the number of these set bits to give us the total number of bits in a | b that need to be flipped from 0s to 1s.

2+3 We follow a similar approach to step 1. First, we use a bitmask. The main difference from step one is that now, we use the bitmask on c. Specifically, we extract all the bits in c that are 1s in a (or 1s in b for step 3). Then, we xor with a to calculate how many of the set bits in a (or b for step 3) are 0s in c. Finally, we count how many of those bits there are to give us the total number of bits in a (or b for step 3) that need to be flipped from 1s to 0s.
