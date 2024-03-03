function passwordValidator(password) {
    let result = [];
    let digitsInPassword = 0;
    let notValidCharacter = 0;

    if (password.length < 6 && password.length < 11) {
        result.push("Password must be between 6 and 10 characters")
    }

    for (const char of password) {
        if (/\d/g.test(char)) {
            digitsInPassword ++;
        } else if (!(/[a-zA-Z]/g.test(char))) {
            notValidCharacter ++;
        }
    }

    if (notValidCharacter > 0) {
        result.push("Password must consist only of letters and digits")
    }

    if (digitsInPassword < 2) {
        result.push("Password must have at least 2 digits")
    }

    if (result.length !== 0) {
        console.log(result.join("\n"));
    } else console.log("Password is valid");
}


passwordValidator('logIn');
passwordValidator('MyPass123');
passwordValidator('Pa$s$s');