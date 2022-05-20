import xmltodict

def main():
	#Read JSON data into the datastore variable
    with open("FlightData/2010/07-26/BER-LHR.txt", 'r') as f:
        data = xmltodict.parse(f.read())

    print(data)

if __name__ == "__main__":
    main()
