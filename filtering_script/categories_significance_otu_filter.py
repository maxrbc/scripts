#================================================================
#Author :  Max R. Berrios Cruz
#Date: Jun 28, 2013
#Email: max.berrios@upr.edu
#Version:
#================================================================


import sys

from src.parser.input_output import i_o
from src.main.interface.main import main 
from src.parser.parser import parser




def Start(values):
    
    Main = main(values)
    Main.workflow()
    
def readTerminal():
    
    try:
        options = []
        
        for i in sys.argv[1:]:
            print(i)
            options.append(i)
            
        options.reverse()
        
            
        optionsParser = parser()
        optionsParser.optionsListener(options)
       
        Start(optionsParser.get_values())
        
            
            
    except:
        i_o().Help()

if __name__ == "__main__":
    readTerminal()
















       