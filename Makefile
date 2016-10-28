HUMILIS := .env/bin/humilis
PIP := .env/bin/pip
PYTHON := .env/bin/python
TOX := .env/bin/tox
STAGE := DEV
HUMILIS_ENV := tests/integration/humilis-firehose

# create virtual environment
.env:
	virtualenv .env -p python3

# install dev dependencies, create layers directory
develop: .env
	.env/bin/pip install -r requirements-test.txt

# run integration tests
test: .env
	$(PIP) install tox
	$(TOX)

# remove .tox and .env dirs
clean:
	rm -rf .env .tox

# configure humilis
configure:
	$(HUMILIS) configure --local

# deploy the test environment
create: develop
	$(HUMILIS) create \
		--stage $(STAGE) \
		--output $(HUMILIS_ENV)-$(STAGE).outputs.yaml \
		$(HUMILIS_ENV).yaml

# update the test deployment
update: develop
	$(HUMILIS) update \
		--stage $(STAGE) \
		--output $(HUMILIS_ENV)-$(STAGE).outputs.yaml \
		$(HUMILIS_ENV).yaml

# delete the test deployment
delete: develop
	$(PYTHON) ./scripts/empty-bucket.py $(HUMILIS_ENV)-$(STAGE).outputs.yaml
	$(HUMILIS) delete --stage $(STAGE) $(HUMILIS_ENV).yaml

# upload to Pypi
pypi: develop
	$(PYTHON) setup.py sdist upload
