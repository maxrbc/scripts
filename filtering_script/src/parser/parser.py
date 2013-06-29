#================================================================
#Author :  Max R. Berrios Cruz
#Date: Jun 28, 2013
#Email: max.berrios@upr.edu
#Version:
#================================================================


from input_output import i_o

class parser:
    
    
    
    def __init__(self):
        print("alive!")
        self.otu = ""
        self.significance = ""
        self.p_value = 0.05
        self.output = "filtered_otuput"
        self.__values = {
                    '-i':self.otu,
                    "-s":self.significance,
                    '-p':self.p_value,
                    '-o':self.output,
                    '-h':"help"
                    }


    def get_values(self):
        return self.__values

                    
    
    
    
    def optionsListener(self,options):
        print("Listener!")
        
        while len(options)>0:
            
            target = options.pop()
            
            if target in self.__values and target != "-h":
                self.__values[target] = options.pop()
                
            else:
                i_o().Help() 
    
            