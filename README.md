# Software Catalog

This is a repository stores the description of the software using the eFlows4HPC methodology. 

## Repository structure

Software descriptions have to be included inside this repository according to the following structure

```
software-catalog
  |- packages
  |    |- software_1
  |    |    |- package.py		Installation description following the Spack package format
  |    |    |- invokation.json          Description of the software invocation
  |    |       ...
  |    |- software_2    
  |          ....
  |- cfg				Spack configuration used by the Image Creation Service	
  |    
  |- repo.yaml				Spack description of for this repository  

```  

## Including new software

To include a new create a fork of the repository including a the new software and invocation description and a create pull request with the newly added software.

