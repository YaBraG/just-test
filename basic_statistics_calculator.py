class BasicStatisticsCalculator:
    def mean(self, data):
        if not data:
            return 0
        return sum(data) / len(data)
    
    def variance(self, data):
        if len(data) < 2:
            return 0
        mean_value = self.mean(data)
        return sum((x - mean_value) ** 2 for x in data) / (len(data) - 1)
    
    def deviation(self, data):
        return self.variance(data) ** 0.5
    
data = [10, 20, 30, 40, 50]

calculator = BasicStatisticsCalculator()

mean_value = calculator.mean(data)
variance_value = calculator.variance(data)
deviation_value = calculator.deviation(data)

print(f"Mean: {mean_value}")
print(f"Variance: {variance_value}")
print(f"Standard Deviation: {deviation_value}")
