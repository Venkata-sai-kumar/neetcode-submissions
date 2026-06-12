func hasDuplicate(nums []int) bool {
    data := make(map[int]int)
    for _, num := range nums {
        _, found := data[num]
        if found {
            return true
        } else {
            data[num] = 1
        }
    }
    return false
}
