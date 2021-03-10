# Calculation Board

1. The app is developed using Flask and socketio.
2. Socket programming has been used to keep all the clients updated with the latest calculations.

### To run the flask server.

1. pip3 install -r requirements.txt
2. python3 main.py

	To access the UI, go to: http://localhost:5000

To test if client syncing is working good we could use ngrok to test the system on multiple systems.
Download ngrok.

Sample command: ./ngrok http 5000