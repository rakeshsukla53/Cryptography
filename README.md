# Cryptography


[Hard Core Predicate](#hard-core-predicate)

[Euclidean Algorithm](#euclidean-algorithm)

[One time Pad](#one-time-pad)
- - - 

## One Time Pad




## Euclidean Algorithm

In mathematics, the Euclidean algorithm[a], or Euclid's algorithm, is an efficient method for computing the greatest common divisor (GCD) of two numbers, the largest number that divides both of them without leaving a remainder

[Euclid Algorithm](https://github.com/rakeshsukla53/Cryptography/blob/master/images/Euclidean%20Algorithm/Selection_002.png)

Application of Euclid Algorithm 

The Euclidean algorithm has many theoretical and practical applications. It is used for reducing fractions to their simplest form and for performing division in modular arithmetic. Computations using this algorithm form part of the cryptographic protocols that are used to secure internet communications, and in methods for breaking these cryptosystems by factoring large composite numbers. The Euclidean algorithm may be used to solve Diophantine equations, such as finding numbers that satisfy multiple congruences according to the Chinese remainder theorem, to construct continued fractions, and to find accurate rational approximations to real numbers. Finally, it is a basic tool for proving theorems in number theory such as Lagrange's four-square theorem and the uniqueness of prime factorizations. The original algorithm was described only for natural numbers and geometric lengths (real numbers), but the algorithm was generalized in the 19th century to other types of numbers, such as Gaussian integers and polynomials of one variable. This led to modern abstract algebraic notions such as Euclidean domains.

  
## Hard Core Predicate 

In cryptography, a hard-core predicate of a one-way function f is a predicate b (i.e., a function whose output is a single bit) which is easy to compute given x but is hard to compute given f(x). In formal terms, there is no probabilistic polynomial-time algorithm that computes b(x) from f(x) with probability significantly greater than one half over random choice of x.

`RSA` is implemented on the same principal

![RSA](https://github.com/rakeshsukla53/Cryptography/blob/master/images/Hard_Core_Predicate/14.png)

`RSA` is also known as one way TRAP door function which means that there is no way to undue the encryption unless there you have the `private key`. 

![Easy to Predict](https://github.com/rakeshsukla53/Cryptography/blob/master/images/Hard_Core_Predicate/9.png)

![Hard to Predict](https://github.com/rakeshsukla53/Cryptography/blob/master/images/Hard_Core_Predicate/8.png)

`private key` is represented by `d` in the below images

`n` is the trap door here. Because of prime factorization it is extremely difficult to find n 

`number` which is greater than 1 can be represented exactly one way as the product of two prime numbers

`15 = 3*5`
 
`255 = 3*5*17`

`n` knowing the factors of n is the trapdoor function 

![Real Life Public Key](https://github.com/rakeshsukla53/Cryptography/blob/master/images/Hard_Core_Predicate/13.png)

[![RSA Video](https://github.com/rakeshsukla53/Cryptography/blob/master/images/Hard_Core_Predicate/1.png)](https://www.youtube.com/watch?v=Z8M2BTscoD4)

So hard core predicate is basically a boolean value which can tell whether the inverse of any function can be done or not in `True` or `False`

There is a difference between `One way function` and `Trap Door Function`. RSA is basically a `Trap Door Function` 

`Hard Core Bit` Predict `easy to compute` given x but `hard to guess` given f(x)








