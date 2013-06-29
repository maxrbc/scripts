#================================================================
#Author :  Max R. Berrios Cruz
#Date: Jun 28, 2013
#Email: max.berrios@upr.edu
#Version:
#================================================================


class filtering_otu_significance:

    def __init__(self, otu_table, otu_significance, P_value=0.05):
        
        #this variables just stores the location of the file
        
        self.__otu_table = otu_table
        self.__otu_significance = otu_significance
        self.__P_value = P_value


# Class getters

    def getOtuSignificance(self):
        return self.__otu_significance

    def getPValue(self):
        return self.__P_value

    def getOtuTableName(self):
        return self.__otu_table
    
    
    
    
# filtering method
# will compare the P_value of the significance determine if significant or not
# and will return in a list the signficant ones

    def compare(self, otu_significance):
        result = list()
        for i in range(1, len(otu_significance)):
            if eval(otu_significance[i][1]) <= self.getPValue() :
                result.append(otu_significance[i])
        return result
    
# from a list of id numbers wich are id.otu that are significant
# we will comapare it to the otu table that we have so the ones that
# are not statistically relevant are filtered from it


    
    def refine_Otu(self, otu_table_list, Id):
        result = list()
        Id_list = list()
        
        for i in Id:
            Id_list.append(i[0])
            
        result.append(otu_table_list[0])
        result.append(otu_table_list[1])
                      
        for i in range(2, len(otu_table_list)) :
            
            if (str(otu_table_list[i][0]) in Id_list):
                result.append(otu_table_list[i])
                      
        return result
