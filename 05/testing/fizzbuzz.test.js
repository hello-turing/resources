/*
    TDD - Test Driven Development is a programming methodology, test-first approach.
    1. Write a failing test (Red)
    2. Make the test pass (Green)
    3. Refactor the implementation (Refactor)
*/

const fizzBuzz = require('./fizzbuzz');

describe("Testing FizzBuzz function", () => {
/*
    it("should process array of integers", () => {
        const integers = [1, 2, 3, 5, 6, 10, 15, 30];

        const processedIntegers = fizzBuzz.processIntegers(integers);

        expect(processedIntegers).toEqual([1, 2, "Fizz", "Buzz", "Fizz", "Buzz", "FizzBuzz", "FizzBuzz"]);
    });
*/
    it("should process each integer separately", () => {
        expect(fizzBuzz.processInteger(1)).toBe(1);
        expect(fizzBuzz.processInteger(2)).toBe(2);
        expect(fizzBuzz.processInteger(3)).toBe("Fizz");
        expect(fizzBuzz.processInteger(5)).toBe("Buzz");
    });

});