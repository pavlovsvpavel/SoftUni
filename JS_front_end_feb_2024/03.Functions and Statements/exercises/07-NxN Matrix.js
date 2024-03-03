function martrixCreation(n) {
    let matrix = [];

    for (let i = 0; i < n; i++) {
        matrix[i] = [];
        for (let j = 0; j < n; j++) {
            matrix[i][j] = n;
            
        } 
    }

    console.log(matrix.map((row) => row.join(" ")).join("\n"));
}

martrixCreation(7);