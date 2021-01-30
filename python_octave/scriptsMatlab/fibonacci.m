function [fib] = fibonacci(number)
  fib(1) = 1;
  fib(2) = 1;
  k=3 
  while k <= number
    fib(k) = fib(k-1) + fib(k-2);
    k=k+1;
  end
end