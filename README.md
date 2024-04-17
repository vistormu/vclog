# VCLog: Minimal and Simple Console Logging

[![pypi version](https://img.shields.io/pypi/v/vclog?logo=pypi)](https://pypi.org/project/vclog/)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](http://choosealicense.com/licenses/mit/)
[![docs](https://badgen.net/badge/readthedocs/documentation/blue)](https://vclog.readthedocs.io/en/latest/)

Vistor's Console Logger (VCLog) offers a minimal and colorful console logging. Single-script. No dependencies.

## Features

As every logger in the world, there are four levels of logging: `info`, `debug`, `warning`, and `error`.
```python
from vclog import Logger

Logger.info("info")
>> |I| info

Logger.debug("debug")
>> |D| debug

Logger.warning("warning")
>> |W| warning

Logger.error("error")
>> |E| error
```

It also has a `plain` method in which color, background color, and style can be specified.
```python
Logger.plain("plain text with format", color="blue", bg_color="green", style="bold")
```

The logger can also be disabled by setting the `disable` attribute to `True`. This only works for the instantiated logger.
```python
logger = Logger("instance", disable=True)
logger.info("this message will not be displayed")
```

The package also offers a `format` method to get the formatted string directly.
```python
from vclog import format

message: str = format("Hello, World!", color="red")
```

The main feature of VCLog is that the `Logger` can be used as a static class or it can be instantiated. When instantiated, you can provide a name to be displayed.
```python
Logger.info("as a static method")
>> |I| as a static method

logger = Logger("instance")
logger.info("as an instance")
>> |I| [instance] as an instance
```

## Installation

Follow the next steps for installing the simulation on your device.

**Requierements:**
- Python 3.10.0 or higher

> **Note**: VCLog works on Linux, Windows and Mac.

### Install from pip
VCLog is available as a pip package. For installing it just use:
```
pip install vclog
```

### Install from source
You can either clone the repository
```bash
git clone https://github.com/vistormu/vclog.git
```

or just copy and paste the `logger.py` file.

## Documentation
The official documentation of the package is available on [Read the Docs](https://vclog.readthedocs.io/en/latest/). Here you will find the [installation instructions](https://vclog.readthedocs.io/en/latest/src/installation.html), the [API reference](https://vclog.readthedocs.io/en/latest/src/api_reference.html) and some [minimal working examples](https://vclog.readthedocs.io/en/latest/src/examples.html).
