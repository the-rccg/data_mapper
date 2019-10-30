import pandas as pd
from functools import partial

class raw_data_obj(object):
    
    def __init__(self, col_path):
        ''' initialize by providing path'''
        self.path = col_path
        self.csvs = self._get_csvs(self.path)
        self.read = partial(pd.read_csv, memory_map=True)
        self.conc = partial(pd.concat, axis=1)
    
    def _get_csvs(self, col_path):
        ''' return all CSVs in path '''
        return [file for file in os.listdir(col_path) if file.split('.')[-1].lower() == 'csv']
    
    def set_path(self, path):
        ''' set path for the data '''
        self.path = path
        return True
    
    def set_csvs(self, csv_list):
        ''' set list of files to be used '''
        self.csvs = csv_list
        return True
    
    def set_read(self, read_func):
        ''' define the read function '''
        self.read = read_func
        return True
    
    def set_conc(self, concat_func):
        ''' define concatenation function '''
        self.conc = concat_func
        return True
    
    def _get_file(self, name):
        return self.path+name+'.csv'
    
    def __getitem__(self, col):
        ''' retrieve one column '''
        #return self.__dict__[key]
        if type(col) == str:
            ret_data = self.read(self._get_file(col))
            if len(ret_data.keys()) == 1:
                ret_data = ret_data[col]
            return ret_data
        elif type(col) == list:
            return self.conc((self.read(self._get_file(f)) for f in col))
        else:
            raise "Unrecognized type {}".format(type(col))
    
    def __repr__(self):
        ''' format for print '''
        #return repr(self.__dict__)
        return repr(self.csvs)
    
    def __len__(self):
        #return len(self.__dict__)
        return len(self.csvs)
    
    def __delitem__(self, key):
        return self.csvs.remove(key)
    
    def clear(self):
        return self.csvs.clear()

    def copy(self):
        return self.csvs.copy()

    def has_key(self, k):
        return k in self.csvs

    #def update(self, *args, **kwargs):
    #    return self.__dict__.update(*args, **kwargs)
    
    def keys(self):
        #return self.__dict__.keys()
        return self.csvs

    def values(self):
        #return self.__dict__.values()
        return [(self.read, csv) for csv in self.csvs]

    def items(self):
        #return self.__dict__.items()
        return [(csv, self.__getitem__(csv)) for csv in self.csvs]

    #def pop(self, *args):
    #    return self.__dict__.pop(*args)

    #def __cmp__(self, dict_):
    #    return self.__cmp__(self.__dict__, dict_)

    def __contains__(self, item):
        #return item in self.__dict__
        return item in self.csvs

    def __iter__(self):
        #return iter(self.__dict__)
        for csv in self.csvs:
            yield self.__getitem__(csv)

    #def __unicode__(self):
    #    return unicode(repr(self.__dict__))
