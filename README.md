Humilis plug-in to deploy Firehose delivery streams
===================================================

[![PyPI](https://img.shields.io/pypi/v/humilis-firehose.svg?style=flat)](https://pypi.python.org/pypi/humilis-firehose)
[![Build Status](https://travis-ci.org/humilis/humilis-firehose.svg?branch=master)](https://travis-ci.org/humilis/humilis-firehose)

A [humilis][humilis] plug-in layer that deploys
[Firehose delivery streams][firehose].

[firehose]: http://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html
[humilis]: https://github.com/InnovativeTravel/humilis
[redshift]: https://aws.amazon.com/documentation/redshift/
[s3]: https://aws.amazon.com/documentation/s3/


## Installation


```
pip install humilis-firehose
```


To install the development version:

```
pip install git+https://github.com/humilis/humilis-firehose
```


## Development

Assuming you have [virtualenv][venv] installed:

[venv]: https://virtualenv.readthedocs.org/en/latest/

```
make develop
```

Configure humilis:

```
make configure
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

[humilis]: https://github.com//humilis/blob/master/README.md


## Contact

If you have questions, bug reports, suggestions, etc. please create an issue on
the [GitHub project page][github].

[github]: http://github.com/humilis/humilis-firehose


## License

This software is licensed under the [MIT license][mit].

[mit]: http://en.wikipedia.org/wiki/MIT_License

See [License file][LICENSE].

[LICENSE]: https://github.com/humilis/humilis-firehose/blob/master/LICENSE.txt


© 2016 German Gomez-Herrero, [Find Hotel][fh] and others.

[fh]: http://company.findhotel.net
