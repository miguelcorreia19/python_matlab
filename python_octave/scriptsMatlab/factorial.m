function [fact] = factorial(n)
  fact = 1; 
  for i = 1:n 
    fact = fact*i; 
  end
end