func hasDuplicate(nums []int) bool {
    a := map[int]int{}
	for i,val := range nums{
		_, found := a[val]
		if found{
			return true
		}
		a[val] = i
	}
	return false
}
