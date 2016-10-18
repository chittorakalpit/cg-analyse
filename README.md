# cg-analyse
=========================================================================================
Get the cg of last 5 years undergraduates and make a graphical analysis and a regression model.

### Data extraction
--------------------------------------------------------

Fork the repo and clone it, and run the script *test.py*. This will output the files department wise. In case of ConnectionError and the program closing unexpectedly, check the file *pointer* which gives the last student's roll number whose cg made into the data file successfully. Accordingly, edit the file *test.py* to start from the last roll number, change the loop counters, and edit the 2nd argument of ```open()``` from ```'w'``` to ```'a'```. This will append data to already existing file. Once the whole department is covered, commit the change and send a pull request.

Python3 is required. Run the script with ```python3 test.py```.
