class Kadane:
    def __init__(self, array):
        # Fields for use:
        self.maxSum = None
        self.array = array
        self.maxSubArray = None
    
    def findMaxSum(self):
        self.maxSum = self.array[0]
        maxEnding = self.array[0]
        
        # Track indices for the subarray
        start = 0
        end = 0
        tempStart = 0  # Temporary start for current subarray
        
        for i in range(1, len(self.array)):
            
            # If it is better to start a new sequence
            if self.array[i] > maxEnding + self.array[i]:
                maxEnding = self.array[i]
                tempStart = i # Also track the start of the new sequence
            # Else continue adding to the current sequence
            else:
                maxEnding = maxEnding + self.array[i]
            
            # If sum was increased
            if maxEnding > self.maxSum:
                self.maxSum = maxEnding # then update max sum
                start = tempStart # track the latest starting index
                end = i # end index is current i value since this value must have been added to current sequence to increase max sum.
        self.maxSubArray = self.array[start: end + 1]
        return self.maxSum
    
    def getResults(self):
        if self.maxSum is None:
            return "Error: Array not initialized yet."
        return f"Array: {self.array}\nMax Sum: {self.maxSum}\nSubarray producing max sum: {self.maxSubArray}"
    
input_array = [6, 1, -25, 5, 45, -10]
algo = Kadane(input_array)
algo.findMaxSum()
print(algo.getResults())