# Usage 

## Purpose
Perform a search in the metadata catalogue http://data.jrc.ec.europa.eu/ and returns the IDs of the records associated.

## How to run it
In the console run:
```sh
$ python json4ckan.py
```
when prompted, insert the search parameters, then hit the enter button, example:
```sh
Enter search: fagus sylvatica
```
the IDs associated to the search are displayed in the console:
```sh
Retrieving http://data.jrc.ec.europa.eu/api/3/action/package_search?q="fagus+sylvatica"
ID 21012c45-0433-41d6-910e-24a2e72cf35a
ID 2a8983d8-53b6-45ad-8107-e617157e7ef7
ID cf0d4d2a-381f-4bba-b893-972acb9fbe36
ID bbce3f9f-7115-415c-83a9-db4363d37900
```
