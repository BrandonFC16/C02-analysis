#Author: Brandon Fook Chong
#Student ID: 260989601


class Country:
    '''
    Represents a country
    
    Instance Attributes: iso_code (str), name (str), continents (list),
                         co2_emissions (dict), population (dict)
                         
    Class Attributes: min_year_recorded (int), max_year_recorded (int)
    '''
    #set the mininum year recorded as a huge number so we are sure
    #that the next min year given is smaller no matter what
    min_year_recorded = 100000000000
    
    #the first max year will always at least be bigger than 0
    max_year_recorded = 0
    
    def __init__(self, code, name, continents, year, emissions, population):
        '''
        (Country, str, str, list, int, dict, dict) -> void
        
        Initializes our Instance Attributes and our Class Attributes.
        Also checks if the given information is available and updates
        the max_year and min_year_recorded if need be
        
        >>> r = Country("SEN", "Senegal", ["AFRICA"], 1991, 16.1, 142623)
        >>> r.iso_code
        'SEN'
        
        >>> r = Country("DNK", "Denmark", ["EUROPE"], 1906, 0, 160000)
        >>> r.year
        1906
        
        >>> r = Country("CMR", "Cameroon", ["AFRICA"], 1908, 4560, 78090)
        >>> r.name
        'Cameroon'
        '''
        #create our instance attributes
        #check if the iso code given is valid
        if len(code) == 3 or code == 'OWID_KOS':
            self.iso_code = code
        
        self.name = name
        self.continents = continents
        self.year = year
        self.co2_emissions = {}
        self.population = {}
        
        #check if the population and the emissions are not equal to -1
        #cause -1 would mean no info is available
        if population != -1:
            
            #add the population for the given year to our dictionary of population
            self.population[year] = population
            
        if emissions != -1:
            self.co2_emissions[year] = emissions

        #check if the year is now bigger than the previous max year
        if self.year > Country.max_year_recorded:
            
                #update the max year if the given year is bigger 
                Country.max_year_recorded = self.year
                
        if self.year < Country.min_year_recorded:
                Country.min_year_recorded = self.year
                
        
    def __str__(self):
        '''
        (Country) -> str
        
        Returns a string made up of the desired instance attributes
        
        >>> r = Country("CMR", "Cameroon", ["AFRICA"], 1908, 4560, 78090)
        >>> str(r)
        'Cameroon\\tAFRICA\\t{1908: 4560}\\t{1908: 78090}'
        
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> str(r)
        'Russia\\tASIA,EUROPE\\t{2007: 1604.778}\\t{2007: 14266000}'
        
        >>> r = Country("DNK", "Denmark", ["EUROPE"], 1906, 0, 160000)
        >>> str(r)
        'Denmark\\tEUROPE\\t{1906: 0}\\t{1906: 160000}'
        '''
        #using our instance attributes, we delimit them with a tab
        #and also return a string which represents all this data
        return (self.name + '\t' + ','.join(self.continents) + '\t' + str(self.co2_emissions) +
                '\t' + str(self.population))
    
    
    def add_yearly_data(self, data):
        '''
        (Country, str) -> void
        
        Adds new data points to the dicts of emissions and population for our object
        with the year given as input to become the new key
        
        >>> r = Country("DNK", "Denmark", ["EUROPE"], 1906, 0, 160000)
        >>> r.add_yearly_data("2001\\t19.2\\t4543345")
        >>> str(r)
        'Denmark\\tEUROPE\\t{1906: 0, 2001: 19.2}\\t{1906: 160000, 2001: 4543345}'
        
        >>> a = Country("AFG", "Afghnistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> a.co2_emissions == {1949: 0.015, 2018: 9.439}
        True
        >>> a.population == {1949: 7663783, 2018: 37122000}
        True
        
        >>> r = Country("CMR", "Cameroon", ["AFRICA"], 1908, 4560, 78090)
        >>> r.add_yearly_data("2000\\t567.2\\t926265")
        >>> str(r)
        'Cameroon\\tAFRICA\\t{1908: 4560, 2000: 567.2}\\t{1908: 78090, 2000: 926265}'
        '''
        #transform the string into a list so that we can work
        #with each element that represent an info
        data = data.split('\t')
    
        #check if the population (found a the second index)
        #was given and it is not am empty string/column
        if data[2] != -1 and data[2] != '':
            
            #add the pop to our dictionary since the info is there
            #with the given year as key
            self.population[int(data[0])] = int(data[2])
            
        if data[1] != -1 and data[1] != '':
            self.co2_emissions[int(data[0])] = float(data[1])
        
        
    def get_co2_emissions_by_year(self, year):
        '''
        (Country, int) -> float
        
        Returns the co2 emission for the specific year given as input
        
        >>> a = Country("AFG", "Afghnistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> a.get_co2_emissions_by_year(1949)
        0.015
        >>> a.get_co2_emissions_by_year(2000)
        0.0
        
        >>> r = Country("CMR", "Cameroon", ["AFRICA"], 1908, 4560, 78090)
        >>> r.add_yearly_data("2000\\t567.2\\t926265")
        >>> r.get_co2_emissions_by_year(2000)
        567.2
        
        >>> r = Country("DNK", "Denmark", ["EUROPE"], 1906, -1, 160000)
        >>> r.add_yearly_data("2001\\t19.2\\t4543345")
        >>> r.get_co2_emissions_by_year(1906)
        0.0
        '''
        #check for each key in our dict
        for key in self.co2_emissions:
            
            #if it matches the key given as argument we return the emissions for that year
            if key == year:
                return self.co2_emissions[key]
        
        #if the year is not present then we return the float 0.0
        return 0.0
            
            
    def get_co2_per_capita_by_year(self, year):    
        '''
        (Country, int) -> float
        
        Returns the co2 a person produced for a given year in a certain country
        
        >>> a = Country("AFG", "Afghnistan", ["ASIA"], 1949, -1, 7663783)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> round(a.get_co2_per_capita_by_year(2018), 5)
        0.25427
        >>> print(a.get_co2_per_capita_by_year(1949))
        None
        
        >>> r = Country("CMR", "Cameroon", ["AFRICA"], 1908, 4560, 78090)
        >>> r.add_yearly_data("2000\\t567.2\\t926265")
        >>> r.get_co2_per_capita_by_year(1908)
        58394.16058394161
        
        >>> r = Country("DNK", "Denmark", ["EUROPE"], 1906, 0, 160000)
        >>> r.add_yearly_data("2001\\t19.2\\t4543345")
        >>> print(r.get_co2_per_capita_by_year(1906))
        None
        '''
        #using the previous function we get the co2 produced for a year
        co2_emissions_by_year = Country.get_co2_emissions_by_year(self, year)
        
        #check if the info was available
        if co2_emissions_by_year != 0.0:
            
            #since we want the co2 tonnes and that it used to be in millions of tonnes
            #we multiply it by 1 million to get the co2 in tonnes
            co2_emissions_by_year_in_tonnes = co2_emissions_by_year * 1000000
            
            #finally we divide by the total population to get the co2 per person 
            return co2_emissions_by_year_in_tonnes / self.population[year]
            
        #if the info is not there we return None
        else:
            return None
        
       
    def get_historical_co2(self, year):
        '''
        (Country, int) -> float
        
        Returns the historical co2 of a Country, so the co2 this country produced up until
        the year given as argument
        
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2007, 62.899, 1218000)
        >>> q.add_yearly_data("1993\\t30.985\\t501000")
        >>> q.add_yearly_data("1989\\t14.292\\t462000")
        >>> q.get_historical_co2(2000)
        45.277
        >>> q.get_historical_co2(2005)
        45.277
        >>> q.get_historical_co2(2007)
        108.176
        
        >>> r = Country("CMR", "Cameroon", ["AFRICA"], 1908, 4560, 78090)
        >>> r.add_yearly_data("2000\\t567.2\\t926265")
        >>> r.get_historical_co2(2000)
        5127.2
        
        >>> r = Country("DNK", "Denmark", ["EUROPE"], 1906, 0, 160000)
        >>> r.add_yearly_data("2001\\t19.2\\t4543345")
        >>> r.get_historical_co2(1906)
        0.0
        '''
        total_historical_co2 = 0.0
        
        #iterate through our dict of emissions
        for key in self.co2_emissions:
            
            #check if the key is smaller than the given year
            if key <= year:
                
                #we then add it to our total historical emissions
                #since the year is stil smaller than the given year
                #and we want all emission up until that givne year
                total_historical_co2 += self.co2_emissions[key] 
                
        return total_historical_co2
    
    @classmethod
    def get_country_from_data(cls, data):
        '''
        (type, str) -> Country
        
        Creates a new object of type Country given a string with
        the data separated with tabs
        
        >>> a = Country.get_country_from_data("ALB\\tAlbania\\tEUROPE\\t1991\\t4.283\\t3280000")
        >>> a.__str__()
        'Albania\\tEUROPE\\t{1991: 4.283}\\t{1991: 3280000}'
        
        >>> r = Country("DNK", "Denmark", ["EUROPE"], 1906, 0, 160000)
        >>> r.__str__()
        'Denmark\\tEUROPE\\t{1906: 0}\\t{1906: 160000}'
        
        >>> r = Country("CMR", "Cameroon", ["AFRICA"], 1908, 4560, 78090)
        >>> r.__str__()
        'Cameroon\\tAFRICA\\t{1908: 4560}\\t{1908: 78090}'
        '''
        #create a list from the given string of data
        data = data.split('\t')
        
        #each information we want will now be an element in the list
        #which we can easily access using indices
        ISO_code = data[0]
        name = data[1]
        
        #account for the fact that sometimes countries will be in
        #2 continents, which we thus split by comma
        if "," in data[2]:
            continents = data[2].split(',')
        
        #if it is only one then we just add transform it into a list
        else:
            continents = [data[2]]
            
        year = int(data[3])
        
        #check if the co2 emission is given or not
        if data[4] != '':
            co2_emissions = float(data[4])
        else:
            co2_emissions = -1
        
        #since the population is the last info, it could be a new line
        #in our files
        if data[5] != '\n':
            population = int(data[5])
        
        #if it is a new line then the information is not provided
        #and we set it equal to 1
        else:
            population = -1
        
        return cls(ISO_code, name, continents, year, co2_emissions, population)
    
    
    @staticmethod
    def get_countries_by_continent(countries):
        '''
        (list) -> dict
        
        Returns a dictionary mapping continents to a list of countries of type Country,
        which are all part of this continent
        
        >>> a = Country("AFG", "Afghanistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> c = [a, b, r]
        >>> d = Country.get_countries_by_continent(c)
        >>> str(d['ASIA'][1])
        'Russia\\tASIA,EUROPE\\t{2007: 1604.778}\\t{2007: 14266000}'
        
        >>> a = Country("AFG", "Afghanistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> r = Country("DNK", "Denmark", ["EUROPE"], 1906, 0, 160000)
        >>> c = [a, r]
        >>> d = Country.get_countries_by_continent(c)
        >>> str(d['ASIA'][0])
        'Afghanistan\\tASIA\\t{1949: 0.015}\\t{1949: 7663783}'
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("CMR", "Cameroon", ["AFRICA"], 1908, 4560, 78090)
        >>> c = [b, r]
        >>> d = Country.get_countries_by_continent(c)
        >>> str(d['EUROPE'][0])
        'Albania\\tEUROPE\\t{2007: 3.924}\\t{2007: 3034000}'
        '''
        my_dict = {}
        
        #itreate to the given countries
        for country in countries:
            
            #iterate through the continents for each country
            for continent in country.continents:
                
                #check if the continent is already in our dict
                if continent not in my_dict:
                    
                    #we create a list for this country to store all countries part of this continent
                    my_list = [country]
                    
                    #create a new key with this list of countries belonging to this key
                    #which represents a continent
                    my_dict[continent] = my_list
                    
                #if the continent was already created, then we just append the country to our list
                #and then add it to the desired key (continent)
                else:
                    my_dict[continent].append(country)
        
        return my_dict
        
        
    @staticmethod
    def get_total_historical_co2_emissions(countries, year):
        '''
        (list, int) -> float
        
        Returns the total historical co2 emissions of the given countries, which the co2 emissions
        up until the given year
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2007, 62.899, 1218000)
        >>> b.add_yearly_data("1991\\t4.283\\t3280000")
        >>> q.add_yearly_data("1993\\t30.985\\t501000")
        >>> q.add_yearly_data("1989\\t14.292\\t462000")
        >>> c = [b, r, q]
        >>> Country.get_total_historical_co2_emissions(c,2007)
        1721.161
        >>> Country.get_total_historical_co2_emissions(c,2000)
        49.56
        
        >>> a = Country("AFG", "Afghanistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> r = Country("DNK", "Denmark", ["EUROPE"], 1906, 0, 160000)
        >>> c = [a, r]
        >>> Country.get_total_historical_co2_emissions(c,2000)
        0.015
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("CMR", "Cameroon", ["AFRICA"], 1908, 4560, 78090)
        >>> c = [b, r]
        >>> Country.get_total_historical_co2_emissions(c,1500)
        0.0
        '''
        total_emissions = 0
        
        #iterate through every country
        for country in countries:
            
            #using the previous function to get the historical co2 of a certain country
            #up until a certain year, we do it for every country and add it to our total emissions
            total_emissions += country.get_historical_co2(year)
        
        return total_emissions
        
        
    @staticmethod
    def get_total_co2_emissions_per_capita_by_year(countries, year):
        '''
        (list, int) -> float
        
        Returns a float representing the total emissions per capita in a given year
        for the list of given countries, which we can get by adding all these emissions
        together that we can each find using a previous function
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> c = [b, r]
        >>> round(Country.get_total_co2_emissions_per_capita_by_year(c,2007), 5)
        92.98855
        
        >>> a = Country("AFG", "Afghanistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> r = Country("DNK", "Denmark", ["EUROPE"], 1906, 0, 160000)
        >>> c = [a, r]
        >>> round(Country.get_total_co2_emissions_per_capita_by_year(c,1949), 5)
        0.00196
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("CMR", "Cameroon", ["AFRICA"], 1908, 4560, 78090)
        >>> c = [b, r]
        >>> round(Country.get_total_co2_emissions_per_capita_by_year(c,1500), 5)
        0.0
        '''
        emissions_total = 0
        population_total = 0
        
        for country in countries:
            
            #check if we have both the information for the population and the emissions
            if year not in country.co2_emissions or year not in country.population:
                continue
            
            #check if the year is in our dict
            if year in country.co2_emissions:
                
                #add the emissions for the country in this certain year to our total
                emissions_total += country.co2_emissions[year]
                
            #check if the year is in our dict of population 
            if year in country.population:
                
                #add population for the country to our population 
                population_total += country.population[year]
        
        #to not divide by 0 we check if the population is not given (thus 0)
        if population_total == 0:
            return 0.0
        
        #first transform the emissions in millions of tonnes into tonnes
        #then divide by the number of people to get the total co2 per capita
        #in a given year
        return emissions_total * 1000000 / population_total
    
    
    @staticmethod
    def get_co2_emissions_per_capita_by_year(countries, year):
        '''
        (list, int) -> dict
        
        Returns a dictionary mapping the given countries to their co2 emissions per capita
        in a given year
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> b.add_yearly_data("1991\\t4.283\\t3280000")
        >>> c = [b, r]
        >>> d1 = Country.get_co2_emissions_per_capita_by_year(c,2007)
        >>> len(d1)
        2
        >>> round(d1[r], 5)
        112.4897
        
        >>> a = Country("AFG", "Afghanistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> r = Country("DNK", "Denmark", ["EUROPE"], 1906, 0, 160000)
        >>> c = [a, r]
        >>> d1 = Country.get_co2_emissions_per_capita_by_year(c,1906)
        >>> print(d1[r])
        None
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("CMR", "Cameroon", ["AFRICA"], 1908, 4560, 78090)
        >>> c = [b, r]
        >>> d1 = Country.get_co2_emissions_per_capita_by_year(c,2007)
        >>> round(d1[b], 3)
        1.293
        '''
        my_dict = {}
        
        #iterate through every country in our list of countries
        for country in countries:
            
            #get the co2 per capita for the country using a previous function 
            co2_per_capita_by_year = country.get_co2_per_capita_by_year(year)
            
            #add it to our dictionary with the object of type Country as the key
            #and the emissions per capita by year as the value
            my_dict[country] = co2_per_capita_by_year
            
        return my_dict
    
    
    @staticmethod
    def get_historical_co2_emissions(countries, year):
        '''
        (list, int) -> dict
        
        Returns a a dictionary mapping the given countries to their historical co2 emissions
        in a given year
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2007, 62.899, 1218000)
        >>> b.add_yearly_data("1991\\t4.283\\t3280000")
        >>> q.add_yearly_data("1993\\t30.985\\t501000")
        >>> q.add_yearly_data("1989\\t14.292\\t462000")
        >>> c = [b, r, q]
        >>> d1 = Country.get_historical_co2_emissions(c,2007)
        >>> len(d1)
        3
        >>> round(d1[q], 5)
        108.176
        
        >>> a = Country("AFG", "Afghanistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> r = Country("DNK", "Denmark", ["EUROPE"], 1906, 0, 160000)
        >>> c = [a, r]
        >>> d1 = Country.get_historical_co2_emissions(c,1906)
        >>> print(d1[r])
        0.0
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("CMR", "Cameroon", ["AFRICA"], 1908, 4560, 78090)
        >>> c = [b, r]
        >>> d1 = Country.get_historical_co2_emissions(c,1907)
        >>> round(d1[r], 3)
        0.0
        '''
        my_dict = {}
        
        for country in countries:
            
            #get the historical co2 emissions for the country using a previous function
            historical_co2_emissions = country.get_historical_co2(year)
            
            #add it to our dictionary with the object of type Country as the key
            #and the historical co2 emissions as the value
            my_dict[country] = historical_co2_emissions
            
        return my_dict
    
    
    @staticmethod
    def get_top_n(countries, n):
        '''
        (dict, int) -> list
        
        Returns a list of tuples with one of the elements representing the ISO code of
        the country and the number associated to it, given a dictionary of Countries and
        an integer which tells us the top n values that should appear in the list. Also,
        the tuples must be in a descending order, with alphebetical order settling countries
        associated to the same number
        
        >>> a = Country("ALB", "Albania", [], 0, 0.0, 0)
        >>> b = Country("AUT", "Austria", [], 0, 0.0, 0)
        >>> c = Country("BEL", "Belgium", [], 0, 0.0, 0)
        >>> d = Country("BOL", "Bolivia", [], 0, 0.0, 0)
        >>> e = Country("BRA", "Brazil", [], 0, 0.0, 0)
        >>> f = Country("IRL", "Ireland", [], 0, 0.0, 0)
        >>> g = Country("MAR", "Marocco", [], 0, 0.0, 0)
        >>> h = Country("NZL", "New Zealand", [], 0, 0.0, 0)
        >>> i = Country("PRY", "Paraguay", [], 0, 0.0, 0)
        >>> j = Country("PER", "Peru", [], 0, 0.0, 0)
        >>> k = Country("SEN", "Senegal", [], 0, 0.0, 0)
        >>> l = Country("THA", "Thailand", [], 0, 0.0, 0)
        >>> d = {a: 5, b: 5, c: 3, d: 10, e: 3, f: 9, g: 7, h: 8, i: 7, j: 4, k: 6, l: 0}
        >>> t = Country.get_top_n(d, 10)
        >>> t[:5]
        [('BOL', 10), ('IRL', 9), ('NZL', 8), ('MAR', 7), ('PRY', 7)]
        >>> t[5:]
        [('SEN', 6), ('ALB', 5), ('AUT', 5), ('PER', 4), ('BEL', 3)]
        
        >>> a = Country("SEN", "Senegal", [], 0, 0.0, 0)
        >>> b = Country("DNK", "Denmark", [], 0, 0.0, 0)
        >>> c = Country("MLI", "Mali", [], 0, 0.0, 0)
        >>> d = {a: 5, b: 5, c: 3}
        >>> t = Country.get_top_n(d, 10)
        >>> t[:2]
        [('DNK', 5), ('SEN', 5)]
        >>> t[5:]
        []
        
        >>> h = Country("NZL", "New Zealand", [], 0, 0.0, 0)
        >>> i = Country("PRY", "Paraguay", [], 0, 0.0, 0)
        >>> j = Country("PER", "Peru", [], 0, 0.0, 0)
        >>> k = Country("SEN", "Senegal", [], 0, 0.0, 0)
        >>> l = Country("THA", "Thailand", [], 0, 0.0, 0)
        >>> d = {h: 0, i: 0, j: 0, k: 0, l: 0}
        >>> t = Country.get_top_n(d, 10)
        >>> t
        [('NZL', 0), ('PER', 0), ('PRY', 0), ('SEN', 0), ('THA', 0)]
        '''
        my_dict = {}
        
        for country in countries:
            
            #check if the object is already in our dict
            if countries[country] in my_dict:
                
                #we thus just append the code to our already existing list 
                my_dict[countries[country]].append(country.iso_code)
            
            #if the object is not in our dict then we must create a new key and a list of iso codes
            else:
                
                #our list of codes
                iso_codes = [country.iso_code]
                
                #add the list to our dict 
                my_dict[countries[country]] = iso_codes
    
        my_list = []
        
        #get a list of all keys, which are iso codes, using key()
        my_keys = list(my_dict.keys())
        
        #sort the keys but in desceding order
        my_keys.sort(reverse = True)
        
        #iterate through all the codes
        for key in my_keys:
            
            #the list of iso codes that were keys
            iso_codes = my_dict[key]
            
            #sort the keys in alphabetical order
            iso_codes.sort()
            
            #append every code to our empty list as tuples
            #with the code and the number as the two elements
            for iso_code in iso_codes:
                my_list.append((iso_code, key))
        
        #return our list of tuple from up to the desired value
        return my_list[:n]
    
    
def get_countries_from_file(file):
    '''
    (str) -> dict
    
    Given a file with the same exact format the output file we get from
    our previous function add_continents_to_data, returns a dictionary that
    maps iso codes to objects of type Country.
    
    >>> d1 = get_countries_from_file("small_co2_data.tsv")
    >>> len(d1)
    9
    >>> str(d1['ALB'])
    'Albania\\tEUROPE\\t{2002: 3.748}\\t{2002: 3126000}'
    
    >>> d2 = get_countries_from_file("smaller_co2_data.tsv")
    >>> len(d2)
    34
    
    >>> d3 = get_countries_from_file("even_smaller_co2_data.tsv")
    >>> str(d3['CMR'])
    'Cameroon\\tAFRICA\\t{1908: 4560}\\t{1908: 78090}'
    
    '''
    fobj = open(file, "r", encoding="utf-8")
    
    my_dict = {}
    
    #iterate through every line
    for line in fobj:
        
        my_list = line.strip('\n').split('\t')
        
        if my_list[0] not in my_dict:
            #using a previous function we format every line
            #and get the countries as objects of type Country
            a = Country.get_country_from_data(line)
        
            #we then add the iso code of this object as the a key in our dict and
            #finally map it to the object of type Country which is our value
            my_dict[a.iso_code] = a
        
        #if country already exists then we just add the data
        #to our existing dicts using a previous function
        else:
            my_dict[my_list[0]].add_yearly_data('\t'.join(my_list[3:]))
            
    return my_dict
    
    