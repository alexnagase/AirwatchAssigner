# AirwatchAssigner
Assign an enrolled Apple device to a user. After enrolling through DEP into Airwatch as DefaultStagingUser, there is no way to assign the device to an Organization User without the user having to login through thier Agent. AirwatchAssigner leverages the API to pair DefaultStagingUser devices to a created users (Or re-assign assigned devices).

## Instructions
Fill in login.csv with the Airwatch Console Server URL, generated API key, and admin username. Fill out data.csv with device serial number and username. AirwatchAssigner will default to using device_id and user_id but will use serial number and username if IDs are left blank. Run AirwatchAssigner.py and authenticate with Airwatch admin password. 

## Known Issues

* Get the data.csv inputs correct because theres no error reporting

## To do 

* Take user input to create user before assigning device
