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
# 
#   Writes the coverage data to a quicklooks file
#   NOTE: will overwrite if the data exists
#         
#   
#   
#   
#   
#
#




import sys      #for exit command and maxint
import argparse #to get command line args 
                #needed to install argparse module because using python 2.6
                #and argparse comes with python 2.7
                #  sudo easy_install argparse
import os       #to run system commands

import toolbox #import my toolbox with defs


print "Script started ..."


#create an argument parser object
#description will be printed when help is used
parser = argparse.ArgumentParser(description='A script to write the coverage data to a quicklooks file')

#add the available arguments -h and --help are aqdded by default
#if the input file does not exist then program will exit
#if output file does not exit it will be created
# args.input is the input file Note: cant write to this file because read only
# args.output is the output file
# args.m is the minimum seq length
parser.add_argument('-q', '--ql_file', type=argparse.FileType('rU'), help='protein fasta file',required=True)
parser.add_argument('-c', '--contig_cov_file', type=argparse.FileType('rU'), help='protein fasta file',required=True)
parser.add_argument('-o', '--output_file', type=argparse.FileType('w'), help='output file',required=True)


#get the args
args = parser.parse_args()



#Test print the args
#print args

cov_lines = 0
ql_lines = 0
scaffolds_not_in_cov = 0
lines_with_data = 0

scaffolds = []
reads = []
length = []
gc = []
coverage = []



#read the contig cov file into the list
line = args.contig_cov_file.readline()

while line:
	cov_lines += 1
	line = line.strip() #remove endline

	cols = line.split("\t")

	if len(cols) != 5:
		print "Error ... contig data file not 5 colums seperated by tabs"
		sys.exit(1)

	
	scaffolds.append(cols[0])
	reads.append(cols[1])
	length.append(cols[2])
	gc.append(cols[3])
	coverage.append(cols[4])
	
	line = args.contig_cov_file.readline()

args.contig_cov_file.close()


#read quicklooks file
line = args.ql_file.readline() #first line
ql_lines += 1

args.output_file.write(line)


line = args.ql_file.readline()

while line:
	ql_lines += 1
	
	line = line.strip()

	#get the id note there is a prefix on the id
	#
	cols = line.split("\t")

	if len(cols) < 6:
		print "ERROR ... quicklooks file needs to have at least 6 columns"
		sys.exit(1)
 
	id = cols[0].split("_")[-2] + "_" + cols[0].split("_")[-1] #scaffold_0

	if cols[2] != "NA" or cols[3] != "NA" or cols[4] != "NA" or cols[5] != "NA":
		lines_with_data == 1


	if id in scaffolds:
		index = scaffolds.index(id)
		
		line = cols[0] + "\t" + cols[1] + "\t" + reads[index] + "\t" + length[index] + "\t" + gc[index] + "\t" + coverage[index]
		i = 6
		while i < len(cols):
			line = line + "\t" + cols[i]
			i += 1

	else:
		scaffolds_not_in_cov += 1
		

	args.output_file.write(line + "\n")

	line = args.ql_file.readline()


args.ql_file.close()
args.output_file.close

print "Print lines read from coverage file = ",cov_lines
print "Print lines read from quicklooks file  = ",ql_lines
print ""
print "Number of items in contig_cov = ",len(scaffolds)
print ""
print "Number of scaffolds not found in contig coverage file = ",scaffolds_not_in_cov
print ""
print"Lines that already had data and were overwritten = ",lines_with_data
print ""

print "Script finished..."
