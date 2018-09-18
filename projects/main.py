# main file to read in user input vaules for test cases
# calculates the mean and standard deviation of the following:
# throughput, RTT, and connection status

from TestResultContainer import TestResultContainer
import sys

# variable to hold what number test case is being entered
testNumber = 0

# instance of TestResultContainer class to hold input
trc = TestResultContainer()

# loop until ctrl+C
while(True):
	

	print("Enter results for test {}".format(testNumber+1))
	
	# get throughput value 
	valid = False	
	try:
		while valid == False:
			inVal = input("Enter throughuput: ")

			# validate float
			try:
				inVal = float(inVal)
				# check if input is a float and non-negative
				if isinstance(inVal, float) and inVal >= 0:
					valid = True

					# add value to dictionary 
					trc.addThroughput(inVal)
					testNumber+=1
				else:
					print("Invalid input. Try again.")
			except:
				print("Invalid input. Try again.")

		# get RTT value 
		valid = False	
		while valid == False:
			inVal = input("Enter RTT: ")

			# validate float
			try:
				inVal = float(inVal)
				# check if input is a float and non-negative
				if isinstance(inVal, float) and inVal >= 0:
					valid = True

					# add value to dictionary 
					trc.addRTT(inVal)
				else:
					print("Invalid input. Try again.")
			except:
				print("Invalid input. Try again.")

		# get connection status value 
		valid = False
		while valid == False:
			inVal = input("Enter connection status: ")

			# validate float
			try:
				inVal = float(inVal)
				# check if input is a float and non-negative
				if isinstance(inVal, float) and inVal >= 0:
					valid = True

					# add value to dictionary 
					trc.addConnectionStatus(inVal)
				else:
					print("Invalid input. Try again.")
			except:
				print("Invalid input. Try again.")

	# catch ctrl+c interrupt and exit loop 
	except KeyboardInterrupt:
		print("You have entered {} test results".format(testNumber))
		break

# calculate mean and standard deviation statistics
trc.calcAvg()
trc.calcStDev()

# print results
print("The average and standard deviation of Throughput are {} and {}.".format(trc.avgMeans["Throughput"], trc.avgStDevs["Throughput"]))
print("The average and standard deviation of RTT are {} and {}.".format(trc.avgMeans["RTT"], trc.avgStDevs["RTT"]))
print("The average and standard deviation of Connection Status are {} and {}.".format(trc.avgMeans["ConnectionStatus"], trc.avgStDevs["ConnectionStatus"]))
	
# write results to json file	
trc.write_to_json()