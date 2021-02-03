#Author: Brandon Fook Chong
#Student ID: 260989601

def get_iso_codes_by_continent(filename):
    '''
    (str) -> dict
    
    Using a file containing the ISO codes of countries and their respective continents,
    this function returns a dictionary with keys as the continents and associated to them
    a list of ISO codes each representing a country that belongs that to continent
    
    >>> d = get_iso_codes_by_continent("iso_codes_by_continent.tsv")
    >>> d['ASIA'][34]
    'KWT'
    >>> d['ASIA'][35]
    'MYS'
    >>> len(d['EUROPE'])
    48
    >>> d['EUROPE'][22]
    'SWE'
    
    >>> d = get_iso_codes_by_continent("small_iso_codes_by_continent.tsv")
    >>> len(d['EUROPE'])
    9
    >>> d['ASIA'][4]
    'MDV'
    
    >>> d = get_iso_codes_by_continent("even_smaller_iso_codes_by_continent.tsv")
    >>> len(d['EUROPE'])
    2
    >>> d['ASIA'][2]
    'LAO'
    '''
    #dict where we will store our countries mapped to ISO codes
    new_dict = {}
    
    #open to file in read mode to extract our countries and their codes
    fobj = open(filename, "r", encoding="utf-8")
    
    #list where we will store the ISO codes for each continent
    Asia = []
    South_America = []
    Africa = []
    North_America = []
    Oceania = []
    Europe = []
    
    #empty string to temporarily hold our ISO codes
    iso_code = ''
    
    #iterate through each line in the file
    for line in fobj:
        
        #look at each character in the line
        for char in line:
            
            #when there is not a tab, it is our ISO code
            if char != '\t':
                
                #we thus add it to our empty string
                iso_code += char
    
            #if it is a tab then we have our code and we must add it
            #to our list 
            else:
                
                #check for each continent in the line
                if "Asia" in line:
                    
                    #if it is a certain continent, like in this case, Asia,
                    #we add the ISO code to our list for Asia
                    Asia.append(iso_code)
                
                #do the same thing for the other continents
                #but this time add them their respective lists
                #each representing a continent
                elif "South America" in line:
                    South_America.append(iso_code)
                    
                elif "Africa" in line:
                    Africa.append(iso_code)
                    
                elif "North America" in line:
                    North_America.append(iso_code)
                    
                elif "Oceania" in line:
                    Oceania.append(iso_code)
                    
                elif "Europe" in line:
                    Europe.append(iso_code)
                
                #reset the iso code variable to an empty string
                #to store the next one
                iso_code = ''
                
                #once we are done with adding the ISO code to our list,
                #we can move on to the next line and exit the for loop
                #for the characters in line
                break
            
    #once we added all the iso codes to our lists, we add them
    #to our dictionaries with their respective continents as keys
    new_dict['AFRICA'] = Africa
    new_dict['ASIA'] = Asia
    new_dict['OCEANIA'] = Oceania
    new_dict['SOUTH AMERICA'] = South_America
    new_dict['NORTH AMERICA'] = North_America
    new_dict['EUROPE'] = Europe
    
    return new_dict


def add_continents_to_data(input_filename, continents_filename, output_filename):
    '''
    (str, str, str) -> int
    
    Adds a third column to the lines we formatted before which represents the continent
    the country belongs to, we also must take into account that some countries will
    be in 2 continents
    
    >>> add_continents_to_data("small_clean_co2_data.tsv", "iso_codes_by_continent.tsv",
    "small_co2_data.tsv")
    10
    
    >>> add_continents_to_data("smaller_clean_co2_data.tsv", "iso_codes_by_continent.tsv",
    "smaller_co2_data.tsv")
    6
    
    >>> add_continents_to_data("even_smaller_clean_co2_data.tsv", "iso_codes_by_continent.tsv",
    "even_smaller_co2_data.tsv")
    4
    '''
    #create a dictionary with keys as the continents and
    #every ISO codes associated to the continents
    my_dict = get_iso_codes_by_continent(continents_filename)
    
    fobj1 = open(input_filename, "r", encoding="utf-8")
    fobj2 = open(output_filename, "w", encoding="utf-8")
    
    line_counter = 0
    
    for line in fobj1:
        
        #empty list to store our continents
        continent_list = []
        line_counter += 1
        
        #create a list with the line that we split based on tabs
        line = line.split('\t')
        
        #iterate through our dict
        for key in my_dict:
            
            #check if the iso code is in our dict 
            if line[0] in my_dict[key]:
                
                #then we add it to our list of continents
                continent_list.append(key)
                
        #transform our list of continent into a string
        continents = ','.join(continent_list)
        
        #insert the continents to our line
        line.insert(2, continents)
        
        #transform the our line back into a string
        line = '\t'.join(line)
        fobj2.write(line)
        
    fobj1.close()
    fobj2.close()
    
    return line_counter
    
    
