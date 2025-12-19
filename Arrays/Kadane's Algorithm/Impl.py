class Kadane:
    def __init__(self):
        # Fields for use:
        self.maxSum = None
        self.array = None
        self.maxSubArray = None
    
    def findMaxSum(self, arr):
        self.array = arr
        self.maxSum = arr[0]
        maxEnding = arr[0]
        
        # Track indices for the subarray
        start = 0
        end = 0
        tempStart = 0  # Temporary start for current subarray
        
        for i in range(1, len(arr)):
            if arr[i] > maxEnding + arr[i]:
                maxEnding = arr[i]
                tempStart = i
            else:
                maxEnding = maxEnding + arr[i]
            if maxEnding > self.maxSum:
                self.maxSum = maxEnding
                start = tempStart
                end = i
        self.maxSubArray = arr[start: end + 1]
        return self.maxSum
    
    def getResults(self):
        if self.maxSum is None:
            return "Error: Array not initialized yet."
        return f"Array: {self.array}\nMax Sum: {self.maxSum}\nSubarray: {self.maxSubArray}"
    
input_array = [6, 1, -25, 5, 45, -10]
algo = Kadane()
print(algo.getResults())