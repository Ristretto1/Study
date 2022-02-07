"1 sheep...2 sheep...3 sheep..."

var countSheep = function (num) {
    let text = ''
    for (let i = 1; i <= num; i++) {
        text +=  (i +' sheep...')
    }
    return text
}