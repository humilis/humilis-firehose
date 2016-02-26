HUMILIS := .env/bin/humilis
PYTHON := .env/bin/python
STAGE := DEV
HUMILIS_ENV := firehose

# create virtual environment
.env:
	virtualenv .env -p python3.5

# create symlinks
symlinks:
	mkdir -p layers
	rm -f layers/$(HUMILIS_ENV)
	ln -fs ../ layers/$(HUMILIS_ENV)

# install dev dependencies
develop: .env symlinks
	.env/bin/pip install -r requirements-dev.txt

# run test suite
test: develop
	.env/bin/tox

# remove virtualenv and layers dir
clean:
	rm -rf .env
	rm -f layers/$(HUMILIS_ENV)

create: develop
	$(HUMILIS) create \
	  --stage $(STAGE) \
	  --output $(HUMILIS_ENV)-$(STAGE).outputs.yaml $(HUMILIS_ENV).yaml

update: develop
	$(HUMILIS) update \
	  --stage $(STAGE) \
	  --output $(HUMILIS_ENV)-$(STAGE).outputs.yaml $(HUMILIS_ENV).yaml

delete: develop
	$(PYTHON) scripts/empty-bucket.py $(HUMILIS_ENV)-$(STAGE).outputs.yaml
	$(HUMILIS) delete --stage $(STAGE) $(HUMILIS_ENV).yaml
