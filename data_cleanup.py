#Author: Brandon Fook Chong
#Student ID: 260989601

#helper function which replaces the .isalpha() function
def alphabet(s):
    '''
    (str) -> bool
    
    Check if the given string is only made up of letters
    from the alphabet
    
    >>> alphabet('potato%')
    False

    >>>  alphabet('potato')
    True
    
    >>> alphabet('123')
    False
    '''
    for letter in s:
        #account for all the possible characters for the name of our countries
        if letter.lower() not in "abcdefghijklmnopqrstuvwxyz-' ":
            return False
        
    return True


def find_delim(sen):
    """
    (str) -> str
    
    Returns the most common delimiter found in the given string
    
    >>> find_delim("0 1 2 3,4")
    ' '
    
    >>> find_delim("potatoes\\tapples pie\\tfish-cakes")
    '\\t'
    
    >>> find_delim("cat.dog.bat.crab.cod")
    '.'
    """
    #counters for our delimiters
    my_list = [0,0,0,0]
    
    #delimiters
    delims = ['\t', ' ', ',', '-']
    
    #iterate through our sentence
    for char in sen:
        
        #check for each delimiter
        if char == '\t':
            #if it is in our sentence then we add one to our counter
            my_list[0] += 1
        
        elif char == ' ':
            my_list[1] += 1
        
        elif char == ',':
            my_list[2] += 1
            
        elif char == '-':
            my_list[3] += 1
    
    #find the highest value which represents the most used delimiter
    #using the max function
    index_max_val = my_list.index(max(my_list))
    
    #return the delimiter that appeared the most 
    return delims[index_max_val]


def clean_one(input_filename, output_filename):
    '''
    (str, str) -> int
    
    Using the previous function, checks every line in the given filename
    and finds the most common delimiter, which is then replaced by a tab and
    this new line is written in the given output file, the function returns
    the number of line written
    
    >>> clean_one('small_raw_co2_data.txt', 'small_tab_sep_co2_data.tsv')
    10
    
    >>> clean_one('smaller_raw_co2_data.txt', 'smaller_tab_sep_co2_data.tsv')
    6
    
    >>> clean_one('even_smaller_raw_co2_data.txt', 'even_smaller_tab_sep_co2_data.tsv')
    4
    '''
    #open both files, the first one where we will read the lines
    #while we write in the second one
    fobj1 = open(input_filename, "r", encoding="utf-8")
    fobj2 = open(output_filename, "w", encoding="utf-8")
    
    line_counter = 0
    
    #iterate through our file
    for line in fobj1:
        
        #add one to our counter every time we have a line
        line_counter += 1
        
        #find the most common delimiter
        delim = find_delim(line)
        
        #depending on what the most common delimiter is,
        #we replace it by a tab and write this line in the output file
        if delim == ',':
            line = line.replace(',', '\t')
            fobj2.write(line)
        
        elif delim == ' ':
            line = line.replace(' ', '\t')
            fobj2.write(line)
            
        elif delim == '-':
            line = line.replace('-', '\t')
            fobj2.write(line)
        
        elif delim == '\t':
            fobj2.write(line)
    
    #close the files once we are done working with it
    fobj1.close()
    fobj2.close()
    
    return line_counter


def final_clean(input_filename, output_filename):
    '''
    (str, str) -> int
    
    Given a tab separated file, which we got in the previous function,
    we account for the possible fallouts of replacing every delimiter by
    a tab. Indeed, some decimal numbers were written with commas and some countries
    have names compsoed of more than 1 word
    
    >>> final_clean('small_tab_sep_co2_data.tsv', 'small_clean_co2_data.tsv')
    10
    
    >>> final_clean('smaller_tab_sep_co2_data.tsv', 'smaller_clean_co2_data.tsv')
    6

    >>> final_clean('even_smaller_tab_sep_co2_data.tsv', 'even_smaller_clean_co2_data.tsv')
    4
    '''
    fobj1 = open(input_filename, "r", encoding="utf-8")
    
    #open the file using the write mode since we will add the
    #modified lines to it
    fobj2 = open(output_filename, "w", encoding="utf-8")
    
    line_counter = 0
    
    for line in fobj1:
        
        #create a list to work with, we will use the indices of this list
        array = line.split('\t')
        
        #the ISO_code is the first item in the list
        #so we pop it and store it for later
        ISO_code = array.pop(0)
        
        #empty string to hold the country name
        country = ''
        
        #add one to our line counter after every iteration
        line_counter += 1
        
        #the while loop checks if we have a letter
        while(alphabet(array[0])):
            
            #we add the letter to our country variable
            #which will eventually become the full country name
            #as long as it is made up of letters
            country += array.pop(0) + ' '
            
        #just like the ISO code we store it for later
        year = array.pop(0)
        
        #remove the extra spaces to only have a tab in between columns
        country = country.strip()
        
        #the population is the last variable, we store it again
        population = array.pop(len(array)-1)
        
        #finally, we have the co2 emissions, which sometimes will
        #use commas instead of dots, which is why we replace them with dots
        co2 = ','.join(array)
        co2 = co2.replace(',', '.')
        
        #using all of the variables we stored, we recreate the line
        #but this time separated by tabs only and with exactly 5 columns
        #for our 5 variables
        newline = '\t'.join([ISO_code, country, year, co2, population])
        fobj2.write(newline)       
        
    fobj1.close()
    fobj2.close()
    
    return line_counter
            
            