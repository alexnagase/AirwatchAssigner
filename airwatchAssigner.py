#!/usr/bin/python
 
import requests
import getpass
import base64
import csv
import json

with open('login.csv') as g:
    login = list(csv.reader(g))

password = getpass.getpass("Password for Airwatch admin " + login[2][1] + ": ")

airwatch_server = "https://" + str(login[0][1])
aw_tenant_code = str(login[1][1])
username = str(login[2][1])
b64auth = base64.b64encode(username + ':' + password)

headers = {
    'Accept': 'application/json',
    'Authorization': 'Basic ' + b64auth,
    'aw-tenant-code': aw_tenant_code,
}

with open('data.csv') as f:
    data = csv.DictReader(f)
    for row in data:
        if str(row['\xef\xbb\xbfdevice_id']) == "":

            devParams = (
                ('searchBy', 'Serialnumber'),
                ('id', str(row['serial_number'])),
            )

            response = requests.get('https://as888.awmdm.com/API/mdm/devices', headers=headers, params=devParams)
            json_data = json.loads(response.text)

            deviceID = str(json_data['Id']['Value'])

        else:
            deviceID = str(row['\xef\xbb\xbfdevice_id'])

        if str(row['user_id']) == "":

            params = (
                ('username', str(row['username'])),
            )

            response = requests.get(airwatch_server + '/API/system/users/search', headers=headers, params=params)
            json_data = json.loads(response.text)

            enrollmentUserID = str((json_data['Users'])[0]['Id']['Value'])


        else:
            enrollmentUserID = str(row['user_id'])

        print deviceID
        print enrollmentUserID

        request_url = airwatch_server + '/API/mdm/devices/' + str(deviceID) + '/enrollmentuser/' + str(enrollmentUserID)


        r = requests.patch(request_url, data=None, headers=headers)
        if r.status_code == 200:
            print "Response Code 200, Success"
        else:
            print "Response Code " + str(r.status_code) + ", Failed"




