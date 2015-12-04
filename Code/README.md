Files:

benchRunner.sh
	Runs PyBench a number of times and puts the output into a folder named with a timestamp. Each run is numbered 0 through <end>.

AutoConvert.py
	Goes into the folder structure of the Results folder, takes each instance of a PyBench output file, runs it through PyBench, and then puts every text file output into the same file (one output after another in one file).
	
pull.py
	Takes the above file and pulls out only the average values. It then puts all of them into a .csv file for analysis.