# logic.py
def next_greater(nums) :
	ans = [-1]*len(nums)
	stack = []
	for i in range(len(nums)) :
		while stack and nums[i] > stack[-1] :
			ans[len(stack)] = nums[i]
			stack.pop()
		stack.append(arr[i])
	return ans

def daily_temperatures(temps) :
	ans = [0]*len(temps)
	stack = []
	for i in range(len(temps)) :
		while stack and temps[i] > temps[stack[-1]] :
			ans[stack[-1]] = i - stack[-1]
		stack.append(i)
	return ans

def largest_rectangle(heights) :
	area = 0
	for i in range(len(heights)) :
		left = right = i
		while left >= 0 and heights[left] >= heights[i] :
			left -= 1
		left += 1
		while right < n and heights[right] >= heights[i] :
			right += 1
		right -= 1
		width = right - left + 1
		area = max(area,heights[i]*width)
	return area

def max_sliding_window(arr,k) :
	from collections import deque
	q = deque()
	ans = []
	for i in range(len(arr)) :
		while q[0] < i-k+1 :
			q.popleft()
		while q and arr[i] >= q[-1] :
			q.pop()
		q.append(i)
		if q[0] >= k-1 :
			ans.append(q[0])
	return ans