
#================================================================
#Author :  Max R. Berrios Cruz
#Date: Jun 28, 2013
#Email: max.berrios@upr.edu
#Version:
#================================================================


import unittest
from src.parser.parser import parser
from src.parser.input_output import i_o

class Test(unittest.TestCase):
    
        otu = ""
        significance = ""
        p_value = 0.05
        output = "filtered_otuput"
        values = { '-i':otu,
                  "-s":significance,
                  '-p':p_value,
                  '-o':output,
                  '-h':"help"
                  }
        test_values = {'-i':"otu",
                  "-s":"significance",
                  '-p':"p_value",
                  '-o':"output",
                  '-h':"help"
                       }

        def testParser(self):
            
            L = ["-i","otu","-s","significance","-p","p_value","-o","output","-h","help"]
            L.reverse()
            
            options = parser()
            options.optionsListener(L)
            
            self.assertEqual(self.test_values, options.get_values(), "testing the parser")

        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()