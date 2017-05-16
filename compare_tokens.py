
import sys
from classes.Parser import Parser

def main():
    # Check that only one argument was passed
    if len(sys.argv) != 3:
        print("Tokenize takes two text files as an argument.")
        return
    
    # pass the text file to the Parser
    parser1 = Parser(sys.argv[1])
    parser2 = Parser(sys.argv[2])
    
    # run the Parsers
    parser1.run()
    parser2.run()
    
    # print the number of shared tokens
    parser1.compare(parser2)
    
    return
    

if __name__ == '__main__':
    main()
    