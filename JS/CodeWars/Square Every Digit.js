function squareDigits(num) {
    let arr = num.toString().split('');
    let str = '';
    for (let i = 0; i < arr.length; i++) {
        str += (arr[i] ** 2).toString();
    }
    return Number(str)
}