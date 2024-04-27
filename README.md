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
  sqlite> CREATE TABLE activitybasic(id INTEGER PRIMARY KEY AUTOINCREMENT, startdate DATE, starttime TIME, enddate DATE, endtime TIME, steps INT);
  sqlite> COMMIT;
  ```

  * DB is ready. Exit with:
  ```
  sqlite> .quit
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

  * Push the SenseHat joy stick in to start recording:

  * If successful, the following should appear on `ssh` terminal
  ```
  Activity Started.
  ```

  * WHen you are finished recording, you may end the call, or press pound for more options :P