#================================================================
#Author :  Max R. Berrios Cruz
#Date: Jun 28, 2013
#Email: max.berrios@upr.edu
#Version:
#================================================================

import sys

class i_o:
    
        
#Reading method. Should read the input file and assign it to a
#list which will be returned

    def inputReading(self,filename):
        filename = open(filename,"r")
        doc = list()
        for line in filename:
            doc.append(line.split("\t"))
        filename.close()
        return doc

# print to console ... debug method

    def toConsole(self, otu_table_list):
        Word = ""
        lineNum = otu_table_list.__len__()  
        for line in range(0, lineNum):
            wordNum = otu_table_list[line].__len__()
            for word in range(0, wordNum - 1):
                Word += (str(otu_table_list[line][word]) + "\t")
            Word += (str(otu_table_list[line][wordNum - 1]))
        print(Word)
        print("done!")  




# print to out put file
                      
    def toOutput(self, otu_table_list,output_name):

        doc = open(output_name+".txt", "w")
        
        lineNum = otu_table_list.__len__()  
        for line in range(0, lineNum):
            wordNum = otu_table_list[line].__len__()
            for word in range(0, wordNum - 1):
                doc.write(str(otu_table_list[line][word]) + "\t")
            doc.write(str(otu_table_list[line][wordNum - 1]))
            
        doc.close()
        print("Done!")
        
    def Help(self):
        print("\n\t\t\tProgrammer help!\n")
        print("\t[categories_significance_otu_filter.py -h]\n")                                        
        print("\n[categories_significance_otu_filter.py filters the Otu table by the most        \n\
significants otu presents in each sample as determined by an ANOVA test in the              \n\
otu_category_significance.py script.These are printed out to a new otu_table that           \n\
contains only those determined significant by the p value selected by the user.             \n\n\
Note: Both the input and output otu tables and the category_significance must be            \n\
in .txt format and Tab delimited, to convert the otu_table.biom use the convert_biom.py script]")
 
        print("\n\tRequiered Inputs:\n")
 
        print("\t\t-i Otu_table\n")
        print("\t\t-s Otu_categorie_significance\n")
    
        print("\tAnother optional inputs:\n")

        print("\t\t-h help \n")
        print("\t\t-p Probabilty threshold { DEFAULT == 95% => 0.05 THRESHOLD}\n")
        print("Example using default p_value\n\
categories_significance_otu_filter.py -i Otu_table.txt -s Otu_significance.txt \n")
        print("Example setting p_value:\n\
categories_significance_otu_filter.py -i Otu_table.txt -s Otu_significance.txt -p 0.05 \n")
    
        sys.exit()
    
