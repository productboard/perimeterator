![Perimeterator](./docs/images/Perimeterator.png?raw=true)


## Usage

```shell
pip3 install .
aws-vault exec <account>
python3 src/enumerator.py
cat list.csv
```


## Description
Perimeterator is a small project intended to allow for continuous auditing
of internet facing AWS services. It can be quickly deployed into AWS and will
periodically enumerate internet-facing IP addresses for a number of commonly
misconfigured AWS resources.

The results from this enumeration process are pushed into a work queue for
scanning by external scanner 'workers' in order to locate open network
services. Scanner 'workers' can be deployed anywhere, and are intended to be
deployed into non-trusted networks in order to provide a representation of
access to services from the "general internet".

Currently, the following AWS resource types are supported:

* EC2
* ELB
* ELBv2
* RDS
* ES
* NAT
