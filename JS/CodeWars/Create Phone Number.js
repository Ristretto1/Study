let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

function createPhoneNumber(numbers){
    let str = numbers.join('');
    let phone = '(' + str.substring(0,3) + ') ' + str.substring(3,6) + '-' + str.substring(6,10)
  
    return phone
  }

