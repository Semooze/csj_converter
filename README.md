Utilities functions for dealing with [CSJ](https://kirit.com/Comma%20Separated%20JSON)

## How to use

### Read data from a CSJ file.

```python
from csj_converter.csj_converter import create_dict_from_csj_file

values = create_dict_from_csj_file('filename')
list_of_values = list(values)

print(list_of_values)
'''
[
    {'slug': 't1', 'title': 'Terminator', 'released': '1984-10-26', 'length_minutes': None, 'created': '2016-06-11 08:54:09.006744+00', 'tags': ['adventure', 'action', 'dystopian', 'robots', 'time-travel', 'sci-fi'], 'watched__last': '2016-06-11 08:55:31.54614+00', 'watched__times': 6},
    {'slug': 't2', 'title': 'Terminator 2: Judgement Day', 'released': '1991-07-01', 'length_minutes': 94, 'created': '2016-06-11 08:54:12.895416+00', 'tags': ['adventure', 'action', 'dystopian', 'robots', 'time-travel', 'sci-fi'], 'watched__last': None, 'watched__times': None}
]
'''
```

### Create a CSJ file.

```python
from csj_converter.csj_converter import create_csj_file_from_dict

list_of_values = [
    {'slug': 't1', 'title': 'Terminator', 'released': '1984-10-26', 'length_minutes': None, 'created': '2016-06-11 08:54:09.006744+00', 'tags': ['adventure', 'action', 'dystopian', 'robots', 'time-travel', 'sci-fi'], 'watched__last': '2016-06-11 08:55:31.54614+00', 'watched__times': 6},
    {'slug': 't2', 'title': 'Terminator 2: Judgement Day', 'released': '1991-07-01', 'length_minutes': 94, 'created': '2016-06-11 08:54:12.895416+00', 'tags': ['adventure', 'action', 'dystopian', 'robots', 'time-travel', 'sci-fi'], 'watched__last': None, 'watched__times': None}
]
create_csj_file_from_dict('filename', list_of_values)
```

After running the program will create file named 'filename' which content data in CSV format
```csv
"slug", "title", "released", "length_minutes", "created", "tags", "watched__last", "watched__times"
"t1", "Terminator", "1984-10-26", null, "2016-06-11 08:54:09.006744+00", ["adventure", "action", "dystopian", "robots", "time-travel", "sci-fi"], "2016-06-11 08:55:31.54614+00", 6
"t2", "Terminator 2: Judgement Day", "1991-07-01", 94, "2016-06-11 08:54:12.895416+00", ["adventure", "action", "dystopian", "robots", "time-travel", "sci-fi"], null, null
```