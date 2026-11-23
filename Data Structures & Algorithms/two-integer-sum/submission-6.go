func twoSum(nums []int, target int) []int {
	m := map[int]int{}
	for i, num := range nums {
		y := target - num
		_, found := m[y]
		if found{
			return []int{m[y], i}
		}
		m[num] = i
	}
	return []int{}
}
