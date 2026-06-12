func hasDuplicate(nums []int) bool {
    data := make(map[int]int)
    for _, num := range nums {
        _, found := data[num]
        if found {
            data[num] += 1
        } else {
            data[num] = 1
        }
    }
    for _, value := range data {
        if value > 1{
            return true
        }
    }
    return false
}
