# CSVFilegen generates CSV file format of the results scrapped  every 3 minutes. Three different files are generated from the JSON  i.e. Alerts, Main routes and Sub Routes. CSV files are stored with following naming  pattern: Alerts are indicated
# with  AL, Main routes file is indicated by RT and sub routes are indicated by SR

import json
import datetime


def meter_per_second_2_mile_per_hour(input_meter_per_second):
	return input_meter_per_second * 2.23694


def csv_files_generator(input_datetime, input_string, target_directory):
	# get current time stamp
	current_time_string = input_datetime.strftime('%Y-%m-%d %H:%M:%S')
	file_name = input_datetime.strftime('%Y%m%d%H%M')

	real_json = json.loads(input_string)

	sub_route_header = ['Route Name', 'Time Stamp', 'From Street', 'To Street', 'Length (meters)',
	                    'Historical Travel Time (seconds)', 'Travel Time (seconds)', 'Historical Speed (mph)',
	                    'Speed (mph)', 'Jam Level']
	with open(target_directory + '\\' + 'SR_' + file_name + '.csv', 'a') as output_sub_routes_file:
		output_sub_routes_file.write(','.join(sub_route_header) + '\n')

	alert_header = ['Id', 'Report Time', 'Reported By', 'Alert Type', 'SubType', 'Street Name', 'City', 'Latitude',
	                'Longitude']
	with open(target_directory + '\\' + 'AL_' + file_name + '.csv', 'a') as output_alert_routes_file:
		output_alert_routes_file.write(','.join(alert_header) + '\n')

	route_header = ['Route Name', 'Time Stamp', 'Id', 'Length (meters)', 'Historical Travel Time (seconds)',
	                'Travel Time (seconds)', 'Historical Speed (mph)', 'Speed (mph)', 'Jam Level']
	with open(target_directory + '\\' + 'RT_' + file_name + '.csv', 'a') as output_routes_file:
		output_routes_file.write(','.join(route_header) + '\n')

	for route in real_json['routes']:
		output_list = [route['name'].lower(), current_time_string, str(route['id']), str(route['length']),
		               str(route['historicTime']), str(route['time']),
		               str(meter_per_second_2_mile_per_hour(route['length'] / route['historicTime'])),
		               str(meter_per_second_2_mile_per_hour(route['length'] / route['time'])), str(route['jamLevel'])]
		try:
			for subroute in route['subRoutes']:
				sub_route_list = [route['name'].lower(), current_time_string, subroute['fromName'].lower(),
				                  subroute['toName'].lower(), str(subroute['length']), str(subroute['historicTime']),
				                  str(subroute['time']),
				                  str(meter_per_second_2_mile_per_hour(subroute['length'] / subroute['historicTime'])),
				                  str(meter_per_second_2_mile_per_hour(subroute['length'] / subroute['time'])),
				                  str(subroute['jamLevel'])]
				with open(target_directory + '\\' + 'SR_' + file_name + '.csv', 'a') as output_sub_routes_file:
					output_sub_routes_file.write(','.join(sub_route_list) + '\n')

				if 'leadAlert' in subroute:
					alert_list = [subroute['leadAlert']['id'], datetime.datetime.fromtimestamp(
						int(subroute['leadAlert']['reportTime'] / 1000)).strftime('%Y-%m-%d %H:%M:%S'),
					              subroute['leadAlert']['reportByNickname'], subroute['leadAlert']['type'],
					              subroute['leadAlert']['subType'], subroute['leadAlert']['street'].lower(),
					              subroute['leadAlert']['city'].lower().replace(',', ' '),
					              subroute['leadAlert']['position'].split(' ')[0],
					              subroute['leadAlert']['position'].split(' ')[1]]

					with open(target_directory + '\\' + 'AL_' + file_name + '.csv', 'a') as output_alert_routes_file:
						output_alert_routes_file.write(','.join(alert_list) + '\n')

			with open(target_directory + '\\' + 'RT_' + file_name + '.csv', 'a') as output_routes_file:
				output_routes_file.write(','.join(output_list) + '\n')
		except KeyError, e:
			print e.message + ' === ' + route['name'].lower() + ' -- ' + str(route['id'])