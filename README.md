# data_mapper
Access data across multiple files as if they were one file by wrapping them into one object with custom get and read functions

```python
from mapper import raw_data_obj

col_filepath = 'some_folder/'
raw_data = raw_data_obj(col_filepath)  # maps the folder, defaults to Pandas reader with memory map
print(raw_data)  # prints all files mapped, raw_data.keys() also returns all files
print(raw_data['some_file']['some_col'].describe())  # print description of column
````

## Advanced functionality

```python
from mapper import raw_data_obj
from functools import partial
import pandas as pd

# Create object
col_filepath = 'some_folder/'
raw_data = raw_data_obj(col_filepath)  # maps the folder, defaults to Pandas reader with memory map
# Set custom read function: partial allows assigning some keywords already
raw_data.set_read(partial(pd.read_csv(memory_map=Ture))
# Set custom concatenation function
raw_data.set_conc(partial(pd.concat, axis=1))
# Read data
print(raw_data)  # prints all files mapped, raw_data.keys() also returns all files
print(raw_data['some_file']['some_col'].describe())  # print description of column
```

## Future development

[ ] allow use of column directly (requires unique columns & pre-fetching to create mapping)
