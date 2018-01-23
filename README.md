# Chevir
> a simple video encoder written in python

Chevir is a program that listens to a RabbitMQ queue and converts the
incoming video file paths with the given ffmpeg command arguments.

## Installing / Getting started

You can install and start using Chevir as follows:

```shell
git clone https://github.com/zafergurel/chevir.git
cd chevir/
mkdir log # default log folder in config.yaml
pip install -r requirements.txt # installs requirements
./main.py test <video file path> # adds a video file path.
./main.py start # start listening to rabbitmq for new tasks

# In Windows: 
# py -3 main.py test <video file path>
# py -3 main.py start <video file path>

# CTRL+C to quit
```
Chevir is a Python 3 application.
You need a RabbitMQ (http://www.rabbitmq.com/) server up and running.
Chevir listens to a channel named "video-encoding".
You can specify the RabbitMQ server information in config.yaml.

## Developing

To get the code, just run the following:

```shell
git clone https://github.com/zafergurel/chevir.git
cd chevir/
pip install -r requirements.txt
```

## Features

* Encodes videos using ffmpeg
* Listens to a RabbitMQ queue named video-encoding

## Configuration

All of the configuration is in config.yaml.

## Contributing

If you'd like to contribute, please fork the repository, use a feature
branch and send a pull request. Thank you :)!

## Licensing

The code is licensed under MIT license.
