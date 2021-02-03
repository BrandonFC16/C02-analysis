#Author: Brandon Fook Chong
#Student ID: 260989601

import matplotlib.pyplot as plt

#import the previous modules to obtain
#and then plot our data
from build_countries import *
from data_cleanup import *
from add_continents import *

def get_bar_co2_pc_by_continent(d, year):
    '''
    (dict, int) -> list
    
    Creates a barplot that groups all co2 emissions per capita
    of countries that are part of the same continent together
    and returns a list of these emissions
    
    >>> d2 = get_countries_from_file("large_co2_data.tsv")
    >>> data = get_bar_co2_pc_by_continent(d2, 2000)
    >>> len(data)
    6
    >>> data[0] # AFRICA
    1.0975340644568221
    >>> data[3] # N. AMERICA
    14.739682155717826
    >>> round(data[4], 5) # OCEANIA
    12.66302
    
    >>> d1 = get_countries_from_file("smaller_co2_data.tsv")
    >>> data = get_bar_co2_pc_by_continent(d1, 1999)
    >>> len(data)
    4
    
    >>> d3 = get_countries_from_file("even_smaller_co2_data.tsv")
    >>> data = get_bar_co2_pc_by_continent(d3, 1900)
    >>> data[0]
    0.00234534
    '''
    #create a dictionary with the countries separated by continent
    my_dict = Country.get_countries_by_continent(d.values())
    
    #iterate through every continent
    for continent in my_dict:
        
        #get the total co2 emissions per capita by year using a previous function
        #for a continent in a given year
        my_dict[continent] = Country.get_total_co2_emissions_per_capita_by_year\
                             (my_dict[continent], year)
    
    #get the items from our dict and transform it into a list
    my_list = list(my_dict.items())
    
    #sort the dictionary in alphabetical order
    my_list.sort()
    
    #list to store our x and y values
    x_values = []
    y_values = []
    
    #unpack our list of tuples and add them to their
    #respective x or y list
    for name, co2 in my_list:
        x_values.append(name)
        y_values.append(co2)
        
    #create the label and title for our plot
    plt.ylabel('co2 (in tonnes)')
    plt.title('CO2 emissions per capita in '+ str(year) + ' by brandon.fookchong@mail.mcgill.ca')
    
    #using our two previous list, create our graph
    plt.bar(x_values, y_values)
    
    #save our graph as an image with a specific file name
    plt.savefig('co2_pc_by_continent_' + str(year) + '.png')
    
    #return the list of emissions
    return y_values


def get_bar_historical_co2_by_continent(d, year):
    '''
    (dict, int) -> list
    
    Creates a barplot that groups all historical co2 emissions up to the given year
    of countries that are part of the same continent together
    and returns a list of these emissions
    
    >>> d2 = get_countries_from_file("large_co2_data.tsv")
    >>> data = get_bar_historical_co2_by_continent(d2, 1990)
    >>> len(data)
    6
    >>> round(data[2],4) # EUROPE
    334210.701
    >>> round(data[4],4) # OCEANIA
    8488.463
    
    >>> d2 = get_countries_from_file("large_co2_data.tsv")
    >>> data = get_bar_historical_co2_by_continent(d2, 2000)
    >>> len(data)
    6
    >>> round(data[1], 5) # ASIA
    280013.276
    >>> round(data[4], 5) # OCEANIA
    11935.639
    
    >>> d2 = get_countries_from_file("large_co2_data.tsv")
    >>> data = get_bar_historical_co2_by_continent(d2, 1800)
    >>> len(data)
    6
    >>> round(data[1], 5) # ASIA
    0.0
    >>> round(data[4], 5) # OCEANIA
    0.0
    '''
    #this function is almost exactly the same as the previous one
    my_dict = Country.get_countries_by_continent(d.values())
    
    for continent in my_dict:
        
        #the only difference is pretty much to get the historical co2 emissions
        #instead of the emissions per capita
        my_dict[continent] = Country.get_total_historical_co2_emissions(my_dict[continent], year)
    
    my_list = list(my_dict.items())
    
    my_list.sort()
    
    x_values = []
    y_values = []
    
    for name, co2 in my_list:
        x_values.append(name)
        y_values.append(co2)
    
    plt.ylabel('co2 (in millions of tonnes)')
    plt.title('Historical CO2 emissions up to '+ str(year) +
              ' by brandon.fookchong@mail.mcgill.ca')
    
    plt.bar(x_values, y_values)
    plt.savefig('hist_co2_by_continent_' + str(year) + '.png')
    
    return y_values


def get_bar_co2_pc_top_ten(d, year):
    '''
    (dict, int) -> list
    
    Creates a barplot that represents the top 10 countries
    with biggest co2 emissions per capita for the given year
    and returns a list of these emissions
    
    >>> d1 = get_countries_from_file("small_co2_data.tsv")
    >>> data = get_bar_co2_pc_top_ten(d1, 2001)
    >>> len(data)
    5
    >>> data[2]
    6.168578993821712
    >>> data[3]
    1.4196063588190764
    
    >>> d2 = get_countries_from_file("large_co2_data.tsv")
    >>> data = get_bar_co2_pc_top_ten(d2, 2000)
    >>> len(data)
    10
    >>> data[1] # ARE
    35.669432035737074
    >>> data[3] # KWT
    26.104645476772617
    >>> data[8] # AUS
    18.44005055026065
    
    >>> d2 = get_countries_from_file("large_co2_data.tsv")
    >>> data = get_bar_co2_pc_top_ten(d2, 1999)
    >>> len(data)
    10
    >>> data[1] 
    28.23861852433281
    >>> data[3] 
    26.143964935940662
    >>> data[8] 
    17.78243670886076
    '''
    #create a dictionary that maps countries to their co2 emissions
    #per capita in the desired year
    my_dict = Country.get_co2_emissions_per_capita_by_year(d.values(), year)
    
    new_dict = {}
    
    for key in my_dict:
        
        #check if the value exists
        if my_dict[key] != None:
            
            #add the value to our new dict
            new_dict[key] = my_dict[key]
            
    #create a 2D list of tuples with iso codes and their emissions
    #which is ordered based on the biggest emissions and alphabetical
    #order in case of a tie
    my_list = Country.get_top_n(new_dict, 10)
    
    x_values = []
    y_values = []
    
    #unpack our list of tuples into two distinct lists that
    #we will use as our x and y values
    for code, co2 in my_list:
        x_values.append(code)
        y_values.append(co2)
    
    #label our axis and title
    plt.ylabel('co2 (in tonnes)')
    plt.title('Top 10 countries for CO2 emissions pc in '+ str(year) +
              ' by brandon.fookchong@mail.mcgill.ca')
    
    #create the plot using our lists of values for the x and y axis
    plt.bar(x_values, y_values)
    
    #save the graph as a picture in a specific filename
    plt.savefig('top_10_co2_pc_' + str(year) + '.png')
    
    #return the list of emissions
    return y_values


def get_bar_top_ten_historical_co2(d, year):
    '''
    (dict, int) -> list
    
    Creates a barplot that represents the top 10 countries
    with biggest historical co2 emissions up to the given year
    and returns a list of these emissions
    
    >>> d1 = get_countries_from_file("small_co2_data.tsv")
    >>> get_bar_top_ten_historical_co2(d1, 2015)
    [306.696, 166.33, 149.34300000000002, 48.923, 41.215, 3.748, 3.324, 1.553, 0.0]
    
    >>> d2 = get_countries_from_file("large_co2_data.tsv")
    >>> data = get_bar_top_ten_historical_co2(d2, 2018)
    >>> len(data)
    10
    >>> round(data[3],4) 
    91300.314
    >>> round(data[4],4) 
    77448.896
    >>> round(data[9],4) 
    27232.403
    
    >>> d2 = get_countries_from_file("large_co2_data.tsv")
    >>> data = get_bar_top_ten_historical_co2(d2, 2000)
    >>> len(data)
    10
    >>> round(data[3],4) 
    71940.957
    >>> round(data[4],4) 
    68459.444
    >>> round(data[9],4) 
    20727.115
    '''
    #this function is almost exactly the same as the previous one,
    #the only difference is that we find the historical emissions
    #instead of the emissions per capita
    my_dict = Country.get_historical_co2_emissions(d.values(), year)
    
    new_dict = {}
    for key in my_dict:
        
        if my_dict[key] != None:
            
            new_dict[key] = my_dict[key]
            
    my_list = Country.get_top_n(new_dict, 10)
    
    x_values = []
    y_values = []
    
    for code, co2 in my_list:
        x_values.append(code)
        y_values.append(co2)
        
    plt.ylabel('co2 (in millions of tonnes)')
    plt.title('Top 10 countries for historical CO2 emissions up to ' + str(year) +
              ' by brandon.fookchong@mail.mcgill.ca')
    
    plt.bar(x_values, y_values)
    plt.savefig('top_10_hist_co2_' + str(year) + '.png')
    
    return y_values

def get_plot_co2_emissions(d, iso_codes, min_year, max_year):
    '''
    (dict, list, int, int) -> list
    
    Creates a plot that shows the evolution of the co2 emissions
    by giving these emissions from a given year to another given
    year, where each line represents a country that were given in a list
    
    >>> d2 = get_countries_from_file("large_co2_data.tsv")                                
    >>> data = get_plot_co2_emissions(d2, ["USA", "CHN", "RUS", "DEU", "GBR"], 1990, 2000)
    >>> len(data)
    5
    >>> len(data[2]) 
    11
    >>> data[2][:5]
    [2525.501, 2396.186, 1957.863, 1859.648, 1641.541]
    
    >>> d2 = get_countries_from_file("large_co2_data.tsv")
    >>> data = get_plot_co2_emissions(d2, ["USA", "CHN", "RUS", "DEU", "GBR"], 1800, 2000)
    >>> len(data[0]) # USA
    201
    >>> data[2][4] # RUS
    0.0
    >>> data[4][190] # GBR
    600.773
    >>> data[3][200] # DEU
    900.376
    
    >>> d2 = get_countries_from_file("large_co2_data.tsv")
    >>> data = get_plot_co2_emissions(d2, ["USA", "CHN", "RUS", "DEU", "GBR"], 1900, 2000)
    >>> len(data[0]) # USA
    101
    >>> data[2][4] 
    0.0
    >>> data[4][43] 
    454.849
    >>> data[3][50] 
    510.732
    '''
    #calculate the step to not have too much points
    step = int(round((max_year + 1) - min_year) / 10)
    
    #use range to get all the years
    all_years = range(min_year, max_year + 1)
    
    #get the x values for the step years only
    #since these will be the only points we graph
    #to not saturate the graph
    x_values = range(min_year, max_year + 1, step)
    
    #empty list that we return at the end as it will contain
    #the co2 emissions for all the years
    final_list = []
    
    #get the iso code of each country
    for iso_code in iso_codes:
        
        #list that resets at every iteration
        my_list = []
        
        #iterate through all the years between
        #min anx max years
        for year in all_years:
             
            #add the co2 emissions for that year to our temporary list
            my_list.append(Country.get_co2_emissions_by_year(d[iso_code], year))
        
        #add the temporary list to our final list before it resets
        #so that it contains all of the emissions for all the
        #desired years
        final_list.append(my_list)
    
    #create a list that will hold our years that we want to plot
    step_list = []
    
    #iterate through all the sublists in final_list
    #that each represent the emissions for a country
    for sublist in final_list:
        
        #list that will hold the years to we will plot
        #for a specific country that will reset at every iteration
        sub_step_list = []
        
        #get the years that we want to plot using the
        #step we calculated earlier
        for i in range(0, len(sublist), step):
            
            #add these emissions for these years to our sub_step_list
            sub_step_list.append(sublist[i])
        
        #add all of these sub_step_lists to our step_list after
        #every iteration to finally get the a list with
        #only the years we want to plot and not all of them
        step_list.append(sub_step_list)
    
    #create the label for the axis and the title
    plt.ylabel('co2 (in millions of tonnes)')
    plt.title('CO2 emissions between ' + str(min_year) + ' and ' + str(max_year) +
              ' by brandon.fookchong@mail.mcgill.ca')
    
    #format each lines for the plots differently
    plt.plot(x_values, step_list[0], 'o-g')
    
    #we must how many countries were given
    #and we know that it can variate from 1 to 5 countries given to plot
    if len(step_list) > 1:
        plt.plot(x_values, step_list[1], 'v-.b')
    if len(step_list) > 2 :
        plt.plot(x_values, step_list[2], '.--y')
    if len(step_list) > 3:
        plt.plot(x_values, step_list[3], ',:c')
    if len(step_list) > 4 :
        plt.plot(x_values, step_list[4], 'v--r')
    
    #create a legend that shows what country is what line
    plt.legend(iso_codes)
    
    #save our plot as a picture
    plt.savefig('co2_emissions_' + str(min_year) + '_' + str(max_year) + '.png')
    
    #return the list of all the co2 emissions for all the countries
    #and not the one with only the years we plotted
    return final_list

