# ActivityTracker

Implementation of an activity tracking software using RaspberryPi's and a 9-degree IMU.

## Requirements:
* RaspberryPi, running Bookworm OS. (Developed and tested on bookworm).
* RaspberryPi SenseHAT V1
* Python 3.11

## Setup:
* Setup Pi:
  * Using the Raspberry Pi Imager, flash your SD card with Raspbian OS. For this project, we are using:
    * Bookworm
    * Raspberry Pi 4
    * 32gb SD card

* Boot up your Pi
  * `Python 3.11` should be installed. If not, install it

* Setup `ssh`, so you can access your Pi and start the script.

* Install `sqlite3`:
  * We followed https://www.raspberrypi.com/software/

* Setup the DB on your Pi:
  * Create the DB:
  ```
  sqlite3 Activity.db
  ```

  * This should take you inside the DB, via `sqlite3` shell. Create the tables with:
  ```
  sqlite> BEGIN;
  sqlite> CREATE TABLE activity(id INTEGER PRIMARY KEY AUTOINCREMENT, startdate DATE, starttime TIME, enddate DATE, endtime TIME, steps INT, duration TEXT);
  sqlite> COMMIT;
  ```

  * DB is ready. Exit with:
  ```
  sqlite> .quit
  ```

* Install other dependencies:

  * Install Scipy: 
  ```
  sudo apt-get install python3-scipy
  ```

## Run:

* First, Complete [Setup](#setup)

* `ssh` into your PI

* Run:

  * Run the script:
  ```
  cd ~/ActivityTracker
  python main.py
  ```

  * Push the SenseHat joy stick inwards to start recording:

  * If successful, the following should appear on `ssh` terminal
  ```
  Activity Started.
  ```

  * Re-push the SenseHat joy stick inwards to terminate the active recording. Steps and duration should be logged to the termianl, and to the LED screen:
  ```
  (2, '00:02')
  ```

  * Push the joy stick up to view the history of recorded activities. The first thing logged to LED screen and terminal will be the id of the latest activity.
  ```
  View Mode: On
  Id: 12
  ```

  * Use the joy stick to toggle left and right through the different metrics recorded for each activity. Toggle right until you see:
  ```
  Steps: 2
  ```

  * Use the joy stick to toggle up and down through different activities
  ```
  Id: 12
  ```

  * Push the joy stick inwards to terminate view mode. Once out of view mode, you can restart activity recording.
  ```
  View Mode: Off
  ```