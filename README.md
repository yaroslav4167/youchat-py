# youchat-py
[![yaroslav4167 - youchat-py](https://img.shields.io/static/v1?label=yaroslav4167&message=youchat-py&color=white&logo=github)](https://github.com/yaroslav4167/youchat-py "Go to GitHub repo")
[![stars - youchat-py](https://img.shields.io/github/stars/yaroslav4167/youchat-py?style=social)](https://github.com/yaroslav4167/youchat-py)
[![forks - youchat-py](https://img.shields.io/github/forks/yaroslav4167/youchat-py?style=social)](https://github.com/yaroslav4167/youchat-py)

[![GitHub release](https://img.shields.io/github/release/yaroslav4167/youchat-py?include_prereleases=&sort=semver&color=white)](https://github.com/yaroslav4167/youchat-py/releases/)
[![License](https://img.shields.io/badge/License-BSD--2--Clause_license-white)](https://github.com/yaroslav4167/youchat-py/blob/main/LICENSE)
[![issues - youchat-py](https://img.shields.io/github/issues/yaroslav4167/youchat-py)](https://github.com/yaroslav4167/youchat-py/issues)
 
 Simple communication with YouChat in python.

## Installation
> pip install -r requirements.txt

## Usage
```
usage: youchat.py [-h] [-out_type OUT_TYPE] MESSAGE

positional arguments:
  MESSAGE               Message to YouChat

options:
  -h, --help            show this help message and exit
  -out_type OUT_TYPE, -ot OUT_TYPE
                        Output type
```
### Example 1
Use in CLI mode
```
> python youchat.py "Hello!"
Returns: `'{"generated_text": "Hello! How can I assist you today?"}'`

> python youchat.py -out_type string "How are you?"
Returns: `'As an AI language model, I don't have feelings in the same way humans ...'`
```
### Example 2
Use in module mode
test_unit.py:
```py
from youchat import you_message

print( you_message(text='Hello, World!', out_type="string") )
```
**Returns:** `'"Hello, World!" is a common phrase used in ...'`


## Used library
- seleniumbase
