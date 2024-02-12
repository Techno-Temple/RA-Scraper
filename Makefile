PROJECT_DIRECTORY = ra_scraper

build:
	docker build --tag codeaurelien/ra-scraper .

run:
	docker run --rm -it \
		--name ra-scraper \
		--volume ./data:/app/data \
		--volume ./config:/app/config \
		--env-file ./.env \
		codeaurelien/ra-scraper \
		--config-file /app/config/config_example.yaml

test:
	pytest --cov-report xml:coverage.xml --cov-report term --cov ${PROJECT_DIRECTORY} \
	--junitxml test_results.xml -vv tests/

clean: clean-build clean-pyc clean-test

clean-build:
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name 'spark-warehouse' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage*
	rm -fr htmlcov/
	rm -rf .pytest_cache/
	rm -rf tests/fake_data/
