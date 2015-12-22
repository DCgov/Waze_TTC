# Waze_TTC

The program developed scrapes through the Waze website ( provided by Citizen connect program ) and extracts the information and stores them in CSV format.  The program generatres three CSV files every 3 minutes from website. The data is extracted and stored in three different files. 

## How to use this code

The results of this program are 3 csv files: Waze alerts records, Waze traffic jam routes, and the sub routes for the traffic jam routes. 

## File Format 

RT file shows the data stored from the major routes. Data includes travel time, length of the routes and speeds are calculated accordingly in miph
SR file shows the subroutes extracted from above main routes 
AL indicates alerts shown along the routes 

## Dependencies

[Python Requests](http://www.python-requests.org/en/latest/) Module is required while the script program is running.

## Credential File Format

Credential file is the place, user has to put in the URL link, username and password for the program to read.

## Comments and Questions 

Please let us know your feedback [here](http://inganire.com/t/open-source-waze-citizens-connect-travel-time-page/17)

## Waze Traffic Jam Levels

	* level 0: Free flow
	* level 1: Light traffic
	* level 2: Moderate traffic
	* level 3: Heavy traffic
	* level 4: Bumper to bumper