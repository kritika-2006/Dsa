class Solution:
    def maxSumOfSquares(self, num: int, sum_val: int) -> str:
        # Agar required sum possible hi nahi hai (ya toh 0 se kam hai ya max 9 * num se zyada hai)
        if sum_val < 0 or sum_val > 9 * num:
            return ""
            
        digits = []
        for i in range(num):
            # Har position par zyada se zyada 9 rakh sakte hain, 
            # lekin yeh bhi ensure karna hai ki bache hue sum ke liye aage jagah bache
            d = min(9, sum_val)
            digits.append(d)
            sum_val -= d
            
        # Agar sum puri tarah distribute nahi hua
        if sum_val > 0:
            return ""
            
        # Bade digits ko pehle rakhna hai taaki number maximum bane, 
        # aur baki positions ke liye digits ko properly arrange karein
        # (Kyunki humne 9 se shuru kiya tha, digits already descending order ke paas hain, 
        # lekin hum ise properly sort ya adjust kar sakte hain)
        digits.sort(reverse=True)
        return "".join(map(str, digits))