const FIZZ = "Fizz";
const BUZZ = "Buzz";

const processIntegers = integers => {
  return integers.map(integer => processInteger(integer));
};

const processInteger = integer => {
    if(integer%3==0){
        integer = "Fizz";
    }else if(integer%5==0)
        integer = "Buzz";
  return integer;
};



module.exports = { processIntegers, processInteger };
