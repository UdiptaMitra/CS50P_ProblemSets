import math

# sample lists
seq = [3, 7, 7, 1, 12, 12, 12, 2, 19, 4, 4, 18]
seq2 = [1, 3, 5, 7, 9]

# inverse trig + trig + hyperbolic trig
print("acos:", math.acos(1))
print("acosh:", math.acosh(2))
print("asin:", math.asin(0.5))
print("asinh:", math.asinh(2))
print("atan:", math.atan(1))
print("atan2:", math.atan2(3, 4))
print("atanh:", math.atanh(0.5))
print("cos:", math.cos(1))
print("cosh:", math.cosh(1))
print("sin:", math.sin(1))
print("sinh:", math.sinh(1))
print("tan:", math.tan(1))
print("tanh:", math.tanh(1))

# rounding and integer-related
print("ceil:", math.ceil(4.2))
print("floor:", math.floor(4.8))
print("trunc:", math.trunc(4.9))
print("isfinite:", math.isfinite(5))
print("isinf:", math.isinf(math.inf))
print("isnan:", math.isnan(math.nan))
print("isqrt:", math.isqrt(27))

# combinatorics
print("comb:", math.comb(5, 2))
print("perm:", math.perm(5, 2))
print("factorial:", math.factorial(5))

# sign, remainder, gcd, copysign
print("copysign:", math.copysign(8, -3))
print("fmod:", math.fmod(17, 5))
print("remainder:", math.remainder(17, 5))
print("gcd:", math.gcd(84, 36))

# logs, powers, exp
print("exp:", math.exp(2))
print("log:", math.log(8, 2))
print("log10:", math.log10(1000))
print("log1p:", math.log1p(5))
print("log2:", math.log2(32))
print("pow:", math.pow(3, 4))

# products, sums
print("fsum:", math.fsum(seq))
print("prod:", math.prod(seq2))

# distances, norms, angles
print("dist:", math.dist([3, 4], [0, 0]))
print("hypot:", math.hypot(3, 4))
print("degrees:", math.degrees(math.pi / 2))
print("radians:", math.radians(180))

# roots
print("sqrt:", math.sqrt(81))

# constants
print("e:", math.e)
print("inf:", math.inf)
print("nan:", math.nan)
print("pi:", math.pi)
print("tau:", math.tau)
