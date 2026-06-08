import statistics

data = [3, 7, 7, 1, 12, 12, 12, 2, 19, 4, 4, 18, 9, 9, 15]
data2 = [5, 40, 22, 80, 15, 90, 32, 120, 18, 60, 10, 95, 44, 70, 28]
grouped = [5, 5, 5, 12, 12, 18, 18, 18, 18, 27, 33, 33, 40]

print("mean:", statistics.mean(data))
print("geometric_mean:", statistics.geometric_mean([1, 3, 9]))
print("harmonic_mean:", statistics.harmonic_mean([1, 2, 4]))
print("median:", statistics.median(data))
print("median_low:", statistics.median_low(data))
print("median_high:", statistics.median_high(data))
print("median_grouped:", statistics.median_grouped(grouped, interval=10))
print("mode:", statistics.mode(data))
print("multimode:", statistics.multimode(data))
print("quantiles:", statistics.quantiles(data, n=4, method="inclusive"))
print("pstdev:", statistics.pstdev(data, mu=10))
print("pvariance:", statistics.pvariance(data, mu=10))
print("stdev:", statistics.stdev(data, xbar=statistics.mean(data)))
print("variance:", statistics.variance(data, xbar=statistics.mean(data)))
print("covariance:", statistics.covariance(data, data2))
print("correlation:", statistics.correlation(data, data2))
print(
    "linear_regression:", statistics.linear_regression(data, data2, proportional=False)
)
