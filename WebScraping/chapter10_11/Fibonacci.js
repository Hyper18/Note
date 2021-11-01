function fibonacci(a, b){
    var nextNum = a + b;
    console.log("Next num is" + nextNum)
    if(nextNum < 100){
        fibonacci(n, nextNum)
    }
}

fibonacci(1, 1)