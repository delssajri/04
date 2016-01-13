# Automatic build: 
- run `sudo make install` in your terminal to  build and install payserver images 

# Server start and stop
- run `sudo ./start.sh` in your terminal to launch server. It will start couchdb and websocket server.
- run `sudo ./stop.sh` in your terminal to stop server.
- run `./tests/place_order.py` to test server operation. It will respond with 200 OK if server is correctly configured and running.


