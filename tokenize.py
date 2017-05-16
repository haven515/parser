
import sys
from classes.Parser import Parser

def main():
    # Check that only one argument was passed
    if len(sys.argv) != 2:
        print("Tokenize takes one text file as an argument.")
        return
    
    # pass the text file to the Tokenizer
    parser = Parser(sys.argv[1])
    
    # run the Tokenizer
    parser.run()
    
    # print the results
    parser.print_results_sorted()
    
    return
    

if __name__ == '__main__':
    main()
    