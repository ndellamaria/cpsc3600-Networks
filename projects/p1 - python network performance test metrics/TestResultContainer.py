import statistics 
import json

class TestResultContainer:
	"""
	This is a class for holding test results and calculating statistics
	on the values

	Attributes:
		results (dictionaty): holds input values with key as type of input and
		value as list of values 
		avgMeans (dictionary): holds calculated mean statstic for variables
		avgStDevs (dictionary): holds calculated standard deviation for variables 
	"""

	def __init__(self):
		"""
		Initalizes instance of class

		Attributes: 
		results (dictionaty): holds input values with key as type of input and
		value as list of values 
		avgMeans (dictionary): holds calculated mean statstic for variables
		avgStDevs (dictionary): holds calculated standard deviation for variables 
		"""

		self.results = {"Throughput": [], "RTT": [], "ConnectionStatus": []}

		self.avgMeans = {"Throughput": 0, "RTT": 0, "ConnectionStatus": 0}

		self.avgStDevs = {"Throughput": 0, "RTT": 0, "ConnectionStatus": 0}

	def addThroughput(self, inputThroughput):
		"""
		Adds throughput value to dictionary 

		Parameters: 
			inputThroughput: value for throughput entered by user for test case
		"""
		self.results["Throughput"].append(inputThroughput)

	def addRTT(self, inputRTT):
		"""
		Adds RTT value to dictionary 

		Parameters: 
			inputRTT: value for RTT entered by user for test case
		"""
		self.results["RTT"].append(inputRTT)
 
	def addConnectionStatus(self, inputConnectionStatus):
		"""
		Adds connection status value to dictionary 

		Parameters: 
			inputConnectionStatus: value for connection status entered by user for test case
		"""
		self.results["ConnectionStatus"].append(inputConnectionStatus)

	def calcAvg(self):
		"""
		calculate average of the three values and add to dictionary
		round to 3 decimal places
		"""
		self.avgMeans["Throughput"] = round(statistics.mean(self.results["Throughput"]), 3)
		self.avgMeans["RTT"] = round(statistics.mean(self.results["RTT"]), 3)
		self.avgMeans["ConnectionStatus"] = round(statistics.mean(self.results["ConnectionStatus"]), 3)

	def calcStDev(self):
		"""
		calculate standard deviation of the three values and add to dictionary
		round to 3 decimal places 
		"""
		self.avgStDevs["Throughput"] = round(statistics.stdev(self.results["Throughput"]), 3)
		self.avgStDevs["RTT"] = round(statistics.stdev(self.results["RTT"]), 3)
		self.avgStDevs["ConnectionStatus"] = round(statistics.stdev(self.results["ConnectionStatus"]), 3)

	def write_to_json(self):
		"""
		write results dictionary to json file 
		"""
		with open('results.json', 'w') as fp:
			json.dump(self.results, fp)
