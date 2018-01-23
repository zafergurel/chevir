# Chevir
> a simple video encoder written in python

Chevir is a program that listens to a RabbitMQ queue and converts the
incoming video file paths with the given ffmpeg command arguments.

## Installing / Getting started

You can install Chevir as follows:

```shell
git clone https://github.com/zafergurel/chevir.git
python setup.py install
chevir test <video file path> # adds a video file path
chevir start # start listening to rabbitmq for new tasks
```

You need a RabbitMQ server up and running.
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

* What's the main functionality
* You can also do another thing
* If you get really randy, you can even do this

## Configuration

All of the configuration is in config.yaml.

## Contributing

If you'd like to contribute, please fork the repository, use a feature
branch and send a pull request. Thank you :)!

## Licensing

The code is licensed under MIT license.
