# this approach comes from: https://stackabuse.com/the-factory-method-design-pattern-in-python/
# create a function that accepts the metadata and returns a rawdata object of the correct class by calling the datafactory
def raw_data_creator(metadata_dictionary):
    data_factory = DataFactory()
    data_object = data_factory.create_raw(metadata_dictionary)
    return data_object

# create a different class for each data type/location
# we can make an INP class that this inherits from, then all processes can be done with one object
# see the inp class in pyce_tools.py file
class Bubbler:
    def __init__(self, metadata_dictionary):
        # actually should do this explicitly so that if the attr is not passed in the dictionary, it will give an explicit error upon instantiation
        self.__dict__.update(metadata_dictionary)
    
    # this will be_calculate_seawater() from below
    def calculate_raw(self):
        pass

class DataFactory:
    def create_raw(self, metadata_dictionary):
        if metadata_dictionary[type_] == 'bubbler':
            return Bubbler(metadata_dictionary)

# we can define a parent class of rawINP which forces all subsequent subclasses to have a'calculate raw' method
class RawINP(ABC):
    @abstractmethod
    def calculate_raw(self):
        pass

###################
# If we want to use a wrapper to ensure the correct values are being passed into the calculate seawater method
def check_seawater(func):
    def wrapper(self):
        #make sure all values in self have been given correctly
        return func
    return wrapper

class RawData2:
    def __init__(self, type_, location, **kwargs):
        self.type_ = type_
        self.location = location
        self.__dict__.update(kwargs)

    def calculate_raw(self):
        calculator = self._get_calculator()
        return calculator()
    
    # define this function as private using a single leading underscore. logic can be added here if new types are added
    def _get_calculator(self):
        if self.type_ == 'seawater':
            return self._calculate_seawater
        elif self.type_ == 'aerosol':
            if self.location == 'bubbler':
                return self._calculate_bubbler
            if self.location == 'coriolis':
                return self._calculate_coriolis
        else:
            raise ValueError(self.type_, self.location)
    
    @check_seawater
    def _calculate_seawater(self):
        # extract date and time from input parameters
        self.date = self.collection_date[:6]
        self.time = self.collection_date[9:11]+self.collection_date[12:]
        # use input parameters to build path to source file
        inpath = '..\\data\\raw\\IN\\' + self.type_ + '\\' + self.type_ + '_' + self.location + '_' + self.process + '_' + self.date + '_' + self.time + '.csv'
        # load analysis template
        template = pd.read_excel('..\\in_calculation_template.xlsx', skiprows=1)
        # read in the raw data csv
        raw = pd.read_csv(inpath, sep = ' ', header = None, parse_dates=False)
        
        # create a datetime df to split up the date and time into separate columns, then insert them
        datetime_col = raw[0].str.split(' ', expand=True)
        raw.insert(0, 'day',datetime_col[0])
        raw[0]=datetime_col[1]

        # drop the extra empty column at the end of every data file
        raw=raw.drop(columns=61)
        
        # set the column names so they match those in the template
        raw.columns = template.columns

        # create metadata dict 
        meta_dict = {
            'raw data source': inpath,
            'type':type_,
            'location':location,
            'process':process,
            'sample source name': sample_name,
            'sample collection date': collection_date,
            'sample analysis date': analysis_date,
            '# tubes': num_tubes,
            'ml/tube': vol_tube,
            'issues':issues,
            'sigma': 1.96
        }
                # insert the raw data into the template 
        template = load_workbook('..\\in_calculation_template.xlsx')
        template.remove(template["data.csv"])
        sheet = template.create_sheet('data.csv')
        for row in dataframe_to_rows(raw, index=False, header=True):
            sheet.append(row)
        sheet.insert_rows(idx=0)
        row = 0
        for key, value in meta_dict.items():
            template['summary_UF_UH']['z'][row].value = key
            template['summary_UF_UH']['aa'][row].value = value
            template['summary_UF_H']['z'][row].value = key
            template['summary_UF_H']['aa'][row].value = value
            row += 1
        # read and add blank data.
        blank_uf_uh = pd.read_excel(blank_source, sheet_name='summary_UF_UH')
        blank_uf_h = pd.read_excel(blank_source, sheet_name='summary_UF_H')
        row = 1
        for x in blank_uf_uh['N(frozen)']:
            template['summary_UF_UH']['f'][row].value = x
            row += 1
        row = 1
        for x in blank_uf_h['N(frozen)']:
            template['summary_UF_H']['f'][row].value = x
            row += 1
    
        template.save('..\\data\\interim\\IN\\calculated\\'+type_+'\\'+location+'\\'+type_ + '_' + location + '_' + process + '_' + date + '_' + time +'_calculated.xlsx')
        save_path = '..\\data\\interim\\IN\\calculated\\'+type_+'\\'+location+'\\'+type_ + '_' + location + '_' + process + '_' + date + '_' + time +'_calculated.xlsx'
        return print(f'...IN data calculated!\nCalculated report file saved to {save_path}.')
    def _calculate_bubbler(self):
        pass
    def _calculate_coriolis(self):
        pass

d = RawData2('seawater', 'bubbler', flow_rate=50, collection_date='042020', process='UF')

d.calculate_raw()
# blank_source, type_, location, process, sample_name, 
# collection_date, analysis_date, issues, num_tubes, vol_tube = 0.2, rinse_vol = 20, size = None,
# flow_start = None, flow_stop = None, sample_stop_time = None

#######################
