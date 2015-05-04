#!/usr/bin/python
#For unscaling MACPRF output
import sys
import csv
import os

def unscaleCSV(file,factor):
	with open(file,'r') as orig:
		with open(os.path.splitext(file)[0]+'_unscaled'+os.path.splitext(file)[1],'w') as new:
			reader = csv.reader(orig,delimiter='\t')
			writer = csv.writer(new,delimiter='\t')
			for line in reader:
				writer.writerow(line)
				if len(line) > 1:
					if 'Position' in line[0] and 'MS_PolSys' in line[1]:
						i = 1
						line = reader.next()
						while len(line) > 0:
							for k in range(i,i+factor):
								line[0] = k
								writer.writerow(line)
							i += factor
							line = reader.next()

if __name__ == "__main__":
	unscaleCSV(sys.argv[1],int(sys.argv[2]))
