Utilities functions for dealing with [CSJ](https://kirit.com/Comma%20Separated%20JSON)


## How to use

### Read data from a CSJ file.

```shell
value = create_dict_from_csj_file('filename')
values = list(value)
```

### Create CSJ file

```shell
create_csj_file_from_dict('filename', values)
```