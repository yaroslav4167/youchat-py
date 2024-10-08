# youchat-py
[![yaroslav4167 - youchat-py](https://img.shields.io/static/v1?label=yaroslav4167&message=youchat-py&color=white&logo=github)](https://github.com/yaroslav4167/youchat-py "Go to GitHub repo")
[![stars - youchat-py](https://img.shields.io/github/stars/yaroslav4167/youchat-py?style=social)](https://github.com/yaroslav4167/youchat-py)
[![forks - youchat-py](https://img.shields.io/github/forks/yaroslav4167/youchat-py?style=social)](https://github.com/yaroslav4167/youchat-py)

[![GitHub release](https://img.shields.io/github/release/yaroslav4167/youchat-py?include_prereleases=&sort=semver&color=white)](https://github.com/yaroslav4167/youchat-py/releases/)
[![License](https://img.shields.io/badge/License-BSD--2--Clause_license-white)](https://github.com/yaroslav4167/youchat-py/blob/main/LICENSE)
[![issues - youchat-py](https://img.shields.io/github/issues/yaroslav4167/youchat-py)](https://github.com/yaroslav4167/youchat-py/issues)
 
 Simple communication with YouChat (GPT-4) in python and CLI.

## Installation
> pip install youchat-py

If you use CLI - don't forget to install xvfb.
> apt install xvfb

## Usage
```
usage: youchat [-h] [-out_type OUT_TYPE] [-timeout TIMEOUT] MESSAGE

positional arguments:
  MESSAGE               Message to YouChat

options:
  -h, --help            show this help message and exit
  -out_type OUT_TYPE, -ot OUT_TYPE
                        Output type (json/string)
  -timeout TIMEOUT, -t TIMEOUT
                        Timeout to wait response
```
### Example 1
Use in CLI mode
```
youchat hello!
```
Returns: `{"generated_text": "Hello! How can I assist you today?"}`
```
youchat -out_type string "who are you"
```
Returns: `I am YouBot, a large language model developed by You.com. ...`

> **Note**
> on **zsh** - you must use single quotes `youchat 'who are you?'`


### Example 2
Use in module mode
test_unit.py:
```py
from youchat import you_message

print( you_message(text='Hello, World!', out_type="string") )
```
**Returns:** `"Hello, World!" is a common phrase used in ...`

## Problems and solutions
If you often cannot get youchat response - try to update seleniumbase library `pip install -U seleniumbase`

## Used library
- seleniumbase
