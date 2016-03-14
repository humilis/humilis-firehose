Firehose delivery layer for humilis
===================================

[![PyPI](https://img.shields.io/pypi/v/humilis-firehose.svg?style=flat)](https://pypi.python.org/pypi/humilis-firehose)

A [humilis][humilis] plug-in layer that deploys one ore more 
[Firehose delivery streams][firehose] to deliver events to [S3][s3] and 
[Redshift][redshift].

[firehose]: http://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html
[humilis]: https://github.com/InnovativeTravel/humilis
[redshift]: https://aws.amazon.com/documentation/redshift/
[s3]: https://aws.amazon.com/documentation/s3/


## Installation

To install the latest stable release:

```
pip install humilis-firehose
```


Install the development version:

```
pip install git+https://github.com/InnovativeTravel/humilis-firehose
```


## Development

Assuming you have [virtualenv][venv] installed:

[venv]: https://virtualenv.readthedocs.org/en/latest/

```
make develop
```

Configure humilis:

```
.env/bin/humilis configure --local
```


## Testing

There is no logic in this layer beyond the deployment of AWS resources so 
there is no unit test suite. You can test the deployment of the Firehose
delivery streams with:

```bash
make create
```

Then you can run integration tests using:

```
make test
```

Don't forget to delete the deployment after you are done:

```bash
make delete
```


## More information

See [humilis][humilis] documentation.

[humilis]: https://github.com/InnovativeTravel/humilis/blob/master/README.md


## Who do I ask?

Ask [German](mailto:german@innovativetravel.eu).
