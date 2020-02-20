![Cisco Meraki][logo]


# meraki-electronic-shelf-label-cli

This is a command line tool for configuring a [meraki](https://meraki.cisco.com/) dashboard network with support for [Imagotag](https://www.ses-imagotag.com/en/) electronic shelf labels.

## Prerequisites

1. Your organization/network must be part of meraki's closed beta for integration with Imagotag.
1. Python 3.3+
1. pip3

## Installation

1. Clone this repository
1. Open a terminal window to the `meraki-electronic-shelf-label-cli` directory
1. Create your virtual environment with `pip3 install -r requirements.txt`
1. Run the script with python3 `python3 meraki_esl_configuration.py`

## Usage

This command line tool is a combination of 5 different command line utilities.  The main tool is called with python like so:

```sh
$ python3 meraki_esl_configuration.py
Usage: meraki_esl_configuration.py [OPTIONS] COMMAND [ARGS]...

Options:
  --api_key TEXT   Your Meraki API key  [required]
  --base_url TEXT  The base URL for your requests (https://api.meraki.com)
                   [required]
  --help           Show this message and exit.

Commands:
  edit-device-settings
  edit-network-settings
  get-device-settings
  get-network-settings
  list-eligible-devices
```

### edit-device-settings

```sh
$ python3 meraki_esl_configuration.py --base_url https://api.meraki.com --api_key <valid-api-key> edit-device-settings --help
Usage: meraki_esl_configuration.py edit-device-settings [OPTIONS]

Options:
  --serial TEXT   This is your meraki device serial number  [required]
  --enabled TEXT  This is enabled/disabled  [required]
  --channel TEXT  This is the channel  [required]
  --help          Show this message and exit.
```

### edit-network-settings

```sh
$ python3 meraki_esl_configuration.py --base_url https://api.meraki.com --api_key <valid-api-key> edit-network-settings --help
Usage: meraki_esl_configuration.py edit-network-settings [OPTIONS]

Options:
  --network_id TEXT  This is your meraki network_id  [required]
  --enabled TEXT     This is enabled/disabled  [required]
  --host_name TEXT   This is the host name  [required]
  --help             Show this message and exit.
```

### get-device-settings

```sh
$ python3 meraki_esl_configuration.py --base_url https://api.meraki.com --api_key <valid-api-key> get-device-settings --help  
Usage: meraki_esl_configuration.py get-device-settings [OPTIONS]

Options:
  --serial TEXT  This is your meraki device serial number  [required]
  --help         Show this message and exit.
```

### get-network-settings

```sh
$ python3 meraki_esl_configuration.py --base_url https://api.meraki.com --api_key <valid-api-key> get-network-settings --help
Usage: meraki_esl_configuration.py get-network-settings [OPTIONS]

Options:
  --network_id TEXT  This is your meraki network_id  [required]
  --help             Show this message and exit.
```

### list-eligible-devices

```sh
$ python3 meraki_esl_configuration.py --base_url https://api.meraki.com --api_key <valid-api-key> list-eligible-devices --help
Usage: meraki_esl_configuration.py list-eligible-devices [OPTIONS]

Options:
  --network_id TEXT  This is your meraki network_id  [required]
  --help             Show this message and exit.
```

## Help

Please submit an issue if you thing that you have found a bug in this piece of software. For questions regarding ESL or signing up for our beta, please contact your Meraki representative.

[logo]: https://github.com/meraki/meraki-electronic-shelf-label-cli/raw/master/resources/cisco_meraki.png "Cisco Meraki"
