# AndroidNotifier
Python module to test Android implementation of Google Cloud Messaging locally

## Prerequisite
* Python 2.7.9+

## Installation
Clone repository:

    $ git clone https://github.com/steffenkarlsson/AndroidNotifier.git

## Usage
For one device:

    $ python gcm.py -t "Hello" -m "Foo Bar" <API KEY> <PHONE REGISTRATION ID>

For multiple devices:

    $ python gcm.py -t "Hello" -m "Foo Bar" <API KEY> <PHONE REGISTRATION ID 1>, ..., <PHONE REGISTRATION ID n> 

#### Linux based systems only
Export API KEY as local os environment variable to simplify the usage.

    export GCM_KEY=<API KEY>
    
Usage for a single device:

    $ python gcm.py -t "Hello" -m "Foo Bar" <PHONE REGISTRATION ID>

