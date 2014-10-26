#Import csv module from standard library
import csv

#Create global constanst to store source csv file
MY_FILE = "../data/sample_sfpd_incident_all.csv"


def parse(raw_file, delimiter):
	"""Parses raw CSV file into a JSON format"""

	#Open CSV file
	opened_file = open(raw_file)
	#Read CSV file
	csv_data = csv.reader(opened_file, delimiter=delimiter)
	#Build data structure to hold parsed data
	parsed_data = []
	#Get column headers from first row of CSV
	fields = csv_data.next()
	#Loop over remaining rows and map field values to headers
	for row in csv_data:
		parsed_data.append(dict(zip(fields,row)))
	#Close CSV file
	opened_file.close()

	return parsed_data

def main():
	new_data = parse(MY_FILE, ",")

	print new_data

if __name__ == "__main__":
	main()