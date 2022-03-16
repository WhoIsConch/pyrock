# Pyrock

A wrapper for Mr. Conos's [Rock API](https://github.com/Mr-Conos/Rock-API) in Python. Supports both asynchronous and synchronous applications.

**WARNING**: This project is very young and probably does not work.

## Installation

To install Pyrock, simply run the following pip command:
`pip install pyrock`

If you want the versions straight from the master branch of GitHub, however, you can run the following pip command:
`pip install git+https://github.com/ConchDev/pyrock.git`

## Using Pyrock
```py
import pyrock

client = pyrock.Client()

rock = client.get_rock("bedrock")

print(rock.description)
```

Using Pyrock is very simple. All you need to do is create a Pyrock `Client` instance and then get to it! 

To use Pyrock with aio applications, simply change `import pyrock` to `import pyrock.aio`. Then be sure to `await` any methods marked as async.
```py
import pyrock.aio as pyrock
``` 