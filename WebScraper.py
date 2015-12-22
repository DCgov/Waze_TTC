# The program developed by Washington DC department of transportation and is used to collect traffic time details from Waze citizen connect web portal.
# The program is shared for informational purpose only. Please understand that DDOT does not guarantee the accuracy and workability of the program.
__author__ = 'DDOT'

from requests.auth import HTTPBasicAuth
import requests
import re
import time
import datetime
from CSVFileGen import csv_files_generator


if __name__ == '__main__':
    while True:
        with open('credentials.csv', 'r') as crdts:
            oneline = crdts.readline()
            link = oneline.split(',')[0]
            user = oneline.split(',')[1]
            pwd = oneline.split(',')[2]
            FileLocation = oneline.split(',')[3]

        r = requests.get(link, auth=HTTPBasicAuth(user, pwd))

        # remove Lines showing the path of the route
        json_text_no_lines = re.sub(r'("Line":\[|)\{"x":-\d+.\d+,"y":\d+.\d+\}(,|)(\],|)', '', r.text, flags=re.IGNORECASE)

        # remove bboxes from JSON file
        json_text_no_lines = re.sub(r'"bbox":\{"minY":\d+.\d+,"minX":-\d+.\d+,"maxY":\d+.\d+,"maxX":-\d+.\d+\}(,|)', '',
                                 json_text_no_lines, flags=re.IGNORECASE)

        # get current time stamp
        current_time = datetime.datetime.now()
        current_time_string = current_time.strftime('%Y-%m-%d %H:%M:%S')

        csv_files_generator(current_time, json_text_no_lines, FileLocation)

        print current_time_string + ' Data Operated. '

        time.sleep(3 * 60)