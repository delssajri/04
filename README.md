# Expected system configuration:
Repository is configured and was tested for use under following host system configuration:
- Ubuntu 14.04 LTS
- ruby 1.9.3
- python 2.7
- curl 7.35
- Docker 1.6.2 (default for Ubuntu 14.04, with old networking)
- GNU Make >= 3.81
- openjdk-7-jdk installed with deb
- Android SDK installed to `$HOME/Android/Sdk (default setting)
- calabash-android 0.6.0

# Server build and run:
## Automatic build: 
- run `sudo make server` in your terminal to  build and install payserver images 

## Server start and stop
- run `sudo ./start.sh` in your terminal to launch server. It will start couchdb and websocket server.
- run `./tests/place_order.py` to test server operation. It will respond with 200 OK if server is correctly configured and running.
- run `sudo ./stop.sh` in your terminal to stop server.

# CreditCard Application build and test:
## Makefile based build:
- run `source ./env` to set environment variables: ANDROID_HOME, JAVA_HOME and update PATH for Android binaries. Edit ./env if your Android SDK and JDK binaries have different location. Be sure you are running it as ordinary user.
- run `make app` in your terminal to  build CreditCard application
Application apk file will be located in ./debug/ directory. File isn't signed, sign it with your signature if neccessary. 

## Manual build:
- run `source ./env` to set environment variables: ANDROID_HOME, JAVA_HOME and update PATH for Android binaries. Edit ./env if your Android SDK and JDK binaries have different location.
- cd to CreditCard directory
- run `bash gradlew assembleDebug` to build apk. Resulting apk will be located in `CreditCard/app/build/outputs/apk` directory

## Test:
- configure hostname for host running tests as `farm`. Configure either your DNS server or set host alias to this name. Be sure host responds for `farm`. For example you can try to ping it. CreditCard application sends its request to farm.
- launch your prefered Android Device via Android Virtual Device Manager
- run `sudo bash` to become root user. Please don't use `su` and its forms because you need to preserv your $HOME env.
- run `source ./env` to set environment variables: ANDROID_HOME, JAVA_HOME and update PATH for Android binaries. Edit ./env if your Android SDK and JDK binaries have different location.
- run `make test` to launch calabash tests. Make will successfully exit on tests pass or fail if tests were failed. Mention server will be restarted during tests and database content will be dropped.

