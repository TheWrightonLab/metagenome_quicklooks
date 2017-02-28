#!/usr/bin/python

#PYTHON SCRIPT 
#written by: Richard Wolfe
#
#to run type: python longest_sequence.py -i <inputfile> 
#         or: ./longest_sequence.py -i <inputfile> 
#
#   if error: /usr/bin/python^M: bad interpreter: No such file or directory
#      -there is a windows endl after shebang
#      -open in vi 
#         once in vi type:
#           :set ff=unix<return>
#           :x<return>
#
#
#
# 
#       The id is in the first column Ex: OPENtoOpen31_contig-100_0
#       the scasffold is the last _0
#       put a space here like: OPENtoOpen31_contig-100 0
#
#   
#       -i input file
#       -o output file





import sys      #for exit command and maxint
import argparse #to get command line args 
                #needed to install argparse module because using python 2.6
                #and argparse comes with python 2.7
                #  sudo easy_install argparse
import os       #to run system commands




#create an argument parser object
#description will be printed when help is used
parser = argparse.ArgumentParser(description='A script to extract sequences from a fasta file')

#add the available arguments -h and --help are aqdded by default
#if the input file does not exist then program will exit
#if output file does not exit it will be created
# args.input is the input file Note: cant write to this file because read only
# args.output is the output file
# args.m is the minimum seq length
parser.add_argument('-i', '--input_file', type=argparse.FileType('rU'), help='Input file name',required=True)
parser.add_argument('-o', '--output_file', type=argparse.FileType('w'), help='Output file name',required=True)



#get the args
args = parser.parse_args()



input_lines = 0
output_lines = 0


 

#read first line 
line = args.input_file.readline()


#if the file is not empty keep reading one at a time
while line:
	input_lines += 1
	line = line.rstrip() #remove endline

	columns = line.split("\t")  #split on tabs

	cols_id = columns[0].split("_")
	new_id = cols_id[0]
	i = 1
	while i < len(cols_id) - 1:
		new_id = new_id + "_" + cols_id[i]
		i += 1

	new_id = new_id + " " + cols_id[-1]

	columns[0] = new_id

	args.output_file.write("\t".join(columns))
	args.output_file.write("\n")
	output_lines += 1
	
	
	line = args.input_file.readline()	

#close the file
args.input_file.close()
args.output_file.close()



print "Lines read from input file = ", input_lines

print "Lines wrote to output file = ", output_lines

print "Script finished..."
