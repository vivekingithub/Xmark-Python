
                          Steps for running Xmark
-------------------------------------------------------------------------------
1. There are three components in our Xmark implementation
	.Embedder
	.Instrumentation
	.Retreiver

2. Embedding is performed in the XmarkMain.py script
	- The source program to be watermarked is the XmarkInput.py file
	- The generic Collatz code is present in the CollatzSource.py file
	- The watermarked source code is written into the XmarkOutput.py file

3. Instrumentation and Retreival logic are present in the RedMain.py file
	- The code to instrument is present in the RedInput.py file(Same as the XmarkOutput.py file with slight modifications to facilitate execution)
	- The RedMain.py script instruments the input and stores the output to RedOutput.py
	- After instrumentation RedMain.py also executes the RedOutput.py to retreive the watermark



                        Embedding                              Instrumentation                            Retreival
                     ___________________                    _____________________                   _____________________
  XmarkInput.py     |                   |                  |                     |                 |                     |
  ----------------->|                   | XmarkOutput.py   |                     | RedOutput.py    |                     |
                    |   XmarkMain.py    |----------------->|     RedMain.py      |---------------->|     RedMain.py      |---------->Watermark
  CollatzSource.py  |                   | RedInput.py      |                     |                 |                     |
  ----------------->|                   |                  |                     |                 |                     |
                    |___________________|                  |_____________________|                 |_____________________|     
