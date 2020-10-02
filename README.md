# Introduction

This is a sample project to showcase how API functional test automation can be performed with Python & Pytest framework.

The APIs defined for the functional tests are then reused to run performance & load tests using the locust framework.

This project uses https://jsonplaceholder.typicode.com/ as the application under test. Please note it is a free to use fake Online REST API for testing and prototyping.

For further information on pytest, take a look at https://docs.pytest.org/en/stable/

For further information on locust, take a look at https://locust.io/

# Project Setup

This project is build with `python 3.8.5`

It is recommended to use a python virtual environment to run python projects. You can set it up by following this: https://github.com/pyenv/pyenv-virtualenv

Once your python environment is setup, you need to install the required packages by running

```
pip install -r requirements.txt
```

## Functional Tests

To run functional tests run

```
pytest
```

This runs all of the test files configured in `setup.cgf`

The run also generates result artifacts under the `results` directory. These results can be viewed as an HTML page by running

```
allure serve results/
```

## Performance Tests

### In the GUI Mode

To run the performance tests run in the UI

```
locust -f perf_tests/post_perf_run.py
```

The above script brings up the locust server which can be accessed at http://localhost:8089

We need to provide the below mentioned inputs for the performance tests to begin:

`Number of total users to simulate 1`

`Spawn rate (users spawned/second) 1`

`Host https://jsonplaceholder.typicode.com/`

The test can be stopped using the stop button in the webpage.

### In Headless Mode

To run the performance run in a headless mode (mostly for CI execution) run

```
locust --config=locust_headless.conf
```

This runs the tests as defined in `locust_headless.conf` config file

The results will be generated in a csv format `perf_result_*.csv`

## Framework Organization

```
├── README.md
├── actions
│   ├── base_actions.py     - Base API actions for all other actions file
│   └── post_actions.py     - API actions related to posts feature
├── configs
│   ├── config.py           - Environment configs
├── e2e_tests
│   ├── post_crud_tests.py  - e2e functional test file
├── locust_headless.conf    - locust headless execution configs
├── perf_tests
│   ├── post_perf_run.py    - Performance test file
├── requirements.txt        - Required python libraries
├── results                 - e2e results directory
└── setup.cfg               - Pytest config
```
