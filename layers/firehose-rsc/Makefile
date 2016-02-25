HUMILIS := .env/bin/humilis
PYTHON := .env/bin/python
STAGE := DEV
HUMILIS_ENV := firehose-rsc

# create virtual environment
.env:
	virtualenv .env -p python3

# install dev dependencies, create layers directory
develop: .env
	.env/bin/pip install -r requirements-dev.txt
	mkdir -p layers
	rm -f layers/firehose-rsc
	ln -fs ../ layers/firehose-rsc

# run test suite
test:
	.env/bin/tox

# remove virtualenv and layers dir
clean:
	rm -rf .env
	rm layers/firehose-rsc

create:
	$(HUMILIS) create --stage $(STAGE) $(HUMILIS_ENV).yaml


update:
	$(HUMILIS) update --stage $(STAGE) $(HUMILIS_ENV).yaml


delete:
	$(HUMILIS) delete --stage $(STAGE) $(HUMILIS_ENV).yaml
