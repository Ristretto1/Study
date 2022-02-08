function pillars(num_pill, dist, width) {
    let sum = ((num_pill - 2) * width + dist * 100 * (num_pill - 1))
    if (sum > 0) {
        return sum
    } else {
        return 0
    }
}
