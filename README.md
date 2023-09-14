# youchat-py
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
**Command:**
> python youchat.py "Hello!"

**Returns:** `'{"generated_text": "Hello! How can I assist you today?"}'`

**Command:**
> python youchat.py -out_type string "How are you?"

**Returns:** `'As an AI language model, I don't have feelings in the same way humans ...'`

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
