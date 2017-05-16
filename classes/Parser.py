from string import maketrans


# The number of bytes that Parser will read from the file at once.
FILE_CHUNK_SIZE = 1000

class Parser():
    '''
    Reads all the text in a text file and add them to a dictionary.
    The dictionary contains the number of times each token appears
    in the document.
    '''


    def __init__(self, file_name):
        '''
        Constructor
        Opens the specified file and initializes the dictionary
        Creates the translation table for punctuation and upper/lower case
        
        WARNING: opening the file can throw a IOError
        '''
        self.file = open(file_name, 'r')
        # token_dict will store key = String, value = int
        self.token_dict = {}
        self.translation_table = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()~`-_=+{}[]|;:/?.>,<\\\n\t\'\"', \
            'abcdefghijklmnopqrstuvwxyz                                  ')
        self.complete = False
    
    
    def run(self):
        '''
        Primary function of the class
        Reads chunks of text from the file equivalent to FILE_CHUNK_SIZE
        Splits the read text along empty spaces
        Add all the tokens into the token_dict
        Stops when the EOF is reached and read() returns empty string
        '''
        # read first chunk
        line = self.file.read(FILE_CHUNK_SIZE)
        leftover = ''
        # while there are more chunks to parse
        while line:
            # change upper-case to lower-case, replace punctuation with space, change 
            line = line.translate(self.translation_table)
            # split the chunk into tokens
            tokens = line.split(' ')
            # after EOF has been reached, treat last element as a token
            # while EOF has not been reached, the last element can potentially
            #    be part of a token. Thus, pop and store it and append to next read.
            if not self.complete:
                leftover = tokens.pop()
            # add each token to the dictionary as the key; increment the value
            for token in tokens:
                if token != '':
                    self.token_dict[token] = self.token_dict.get(token, 0) + 1
            # end loop after EOF has been reached and all tokens inserted
            if self.complete:
                break
            # read and append next chunk to the last element
            line = leftover + self.file.read(FILE_CHUNK_SIZE)
            # this will return True and set self.complete to True when self.file reaches EOF
            if line == leftover:
                self.complete = True
    
    
    def compare(self, other):
        '''
        Compares the tokens in token_dict in self and other.
        Prints and returns the number of tokens that are the same.
        Use this function after run() has been called by self and other.
        '''
        counter = 0
        for token in self.token_dict.iterkeys():
            if token in other.token_dict:
                counter += 1
        print "shared tokens: {}".format(counter)
        return counter
    
    def print_results(self):
        '''
        Prints all the items in the token_dict to the console
        '''
        for pair in self.token_dict.iteritems():
            print "{}: {}".format(pair[0], pair[1])    
    
    
    def print_results_sorted(self):
        '''
        Prints all the items in the token_dict to the console.
        Uses sorted to sort the items.
        Sorting priority:
            value (desc) -> token (asc)
        '''
        for pair in sorted(self.token_dict.iteritems(), key=lambda x: (-x[1], x[0]), reverse=False):
            print "{}: {}".format(pair[0], pair[1])
    

# for testing purposes
'''
if __name__ == '__main__':
    parser = Parser('test.txt')
    parser.run()
    parser.print_results_sorted()
    
'''