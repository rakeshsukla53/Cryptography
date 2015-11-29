# Cryptography

# 1 - Hard Core Predicate 

>> In cryptography, a hard-core predicate of a one-way function f is a predicate b (i.e., a function whose output is a single bit) which is easy to compute given x but is hard to compute given f(x). In formal terms, there is no probabilistic polynomial-time algorithm that computes b(x) from f(x) with probability significantly greater than one half over random choice of x.

`RSA` is implemented on the same principal

`RSA` is also known as one way TRAP door function which means that there is no way to undue the encryption unless there you have the `private key`. 

`private key` is represented by `d` in the below images

`n` is the trap door here. Because of prime factorization it is extremely difficult to find n 

`number` which is greater than 1 can be represented exactly one way as the product of two prime numbers

>> 15 = 3*5 
>> 255 = 3*5*17

`n` knowing the factors of n is the trapdoor function 



