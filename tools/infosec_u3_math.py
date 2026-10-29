"""Bounded, transparent textbook RSA arithmetic. NEVER production encryption.
Published small primes/private exponents are classroom data, not real secrets.
"""
import math

def _int(value,label):
    if type(value) is not int:
        raise TypeError(label+' must be an integer')
    return value

def small_prime(n):
    _int(n,'Prime candidate')
    if not 3<=n<=65535 or n%2==0:
        return False
    return all(n%d for d in range(3,math.isqrt(n)+1,2))

def toy_keypair(p,q,e):
    for value,label in [(p,'p'),(q,'q'),(e,'e')]:
        _int(value,label)
    if p==q or not small_prime(p) or not small_prime(q):
        raise ValueError('Use distinct odd primes from 3 through 65535')
    phi=(p-1)*(q-1)
    if not 1<e<phi or math.gcd(e,phi)!=1:
        raise ValueError('Require 1<e<phi and gcd(e,phi)=1')
    return {'p':p,'q':q,'n':p*q,'phi':phi,'e':e,'d':pow(e,-1,phi),
            'lambda_n':math.lcm(p-1,q-1)}

def representative(value,modulus):
    _int(value,'Representative');_int(modulus,'Modulus')
    if modulus<2 or not 0<=value<modulus:
        raise ValueError('Require 0 <= representative < modulus')
    return value

def rsa_encrypt(message,pair):
    return pow(representative(message,pair['n']),pair['e'],pair['n'])

def rsa_decrypt(cipher,pair):
    return pow(representative(cipher,pair['n']),pair['d'],pair['n'])

def power_trace(base,exponent,modulus):
    representative(base,modulus);_int(exponent,'Exponent')
    if exponent<0 or exponent.bit_length()>64:
        raise ValueError('Teaching exponent must be nonnegative and at most 64 bits')
    acc=1;factor=base;remaining=exponent;rows=[]
    while remaining:
        bit=remaining&1
        if bit:
            acc=acc*factor%modulus
        rows.append({'bit':bit,'power':factor,'accumulator':acc})
        factor=factor*factor%modulus;remaining>>=1
    return acc,rows
