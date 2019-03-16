const adder = number => {
  return 10 + number;
};

const greetingsPrinter = name => {
  console.log(`Hello, ${name}!`);
};

const someObject = {
  adder,
  greetingsPrinter
};

someObject.adder = jest
  .fn()
  .mockImplementation(scalar => 100 + scalar)
  .mockName("add20");

global.console = {
  log: jest.fn()
};

it("should mock console.log behavior", () => {
  someObject.greetingsPrinter("Aidar");
  expect(global.console.log).toHaveBeenCalledWith("Hello, Aidar!");
});

it("should mock adder", () => {
    expect(someObject.adder(10)).toBe(110)
    expect(someObject.adder).toBeCalledTimes(1)
});