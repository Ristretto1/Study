var isSquare = function (arr) {
    if (arr.length){
        for (let i = 0; i < arr.length; i++) {
            if (!(Number.isInteger(Math.sqrt(arr[i])))) {
                return false
            } else {
                continue
            }
        }
        return true
    } else {
        return undefined
    }
}

console.log(isSquare([]))