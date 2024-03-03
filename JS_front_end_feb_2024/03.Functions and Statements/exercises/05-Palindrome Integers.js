

function palindromeCheck(arrayOfNumbers) {
    for (const number of arrayOfNumbers) {
        if (reverseNumber(number) === number) {
            console.log("true");
        } else console.log("false");
    }

    function reverseNumber(num) {
        return Number(num.toString().split('').reverse().join(''));
      }
}

palindromeCheck([123,323,421,121]);
palindromeCheck([32,2,232,1010]);