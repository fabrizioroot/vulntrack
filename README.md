# vulntrack
An open source vulnerability/remediation tracker made with Python using Django.

![Python](https://img.shields.io/badge/Python-%2302569B.svg?style=flat&logo=python&logoColor=yellow)
![Django](https://img.shields.io/badge/Django-%2302569B.svg?style=flat&logo=django&logoColor=green)

## Requirements

- Python 3.14.8
- asgiref 3.13.0
- Django 6.1.2
- sqlparse 0.6.0

## Getting Started

To run the developer build:

First, generate the credentials manually or using the generate-env.sh utility:

```bash
$ chmod +x generate-env.sh
$ ./generate-env.sh
```

Then run the container:

```bash
$ docker compose -f compose-dev.yaml up --build
```
