function demo() {
    console.log("Function called!!")
    return Promise.resolve("Success");
    // or
    // return Promise.reject("Failure");
}
demo().then(
    (message) => {
        console.log("Then success:" + message);
    },
    (message) => {
        console.log("Then failure:" + message);
    }
)
console.log(message);