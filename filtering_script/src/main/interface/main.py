#================================================================
#Author :  Max R. Berrios Cruz
#Date: Jun 28, 2013
#Email: max.berrios@upr.edu
#Version:
#================================================================


from src.operation.filtering_significance import filtering_otu_significance
from src.parser.input_output import i_o


class main:
    
    def __init__(self,values):
        
        print("Running the main")       
        self.filter =  filtering_otu_significance(values["-i"],values["-s"],values["-p"])
        self.output_name = values["-o"]
        
    def workflow(self):
        
        print(self.filter.getOtuSignificance())
        otu = i_o().inputReading(self.filter.getOtuTableName())
        print(self.filter.getOtuSignificance())
        significant = i_o().inputReading(self.filter.getOtuSignificance())
        
        comp_sig = self.filter.compare(significant)
        refine_otu = self.filter.refine_Otu(otu, comp_sig)
        
        i_o().toConsole(refine_otu)
        i_o().toOutput(refine_otu,self.output_name)
        

        

