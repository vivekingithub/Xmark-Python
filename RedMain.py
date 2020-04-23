
#Execute this file to perform instrumentation and to retreive the watermark

import subprocess
import sys

from redbaron import RedBaron

count = 0
binStream = []
streamOpen = "stream = open('RedStream.py','w')"
streamClose = "stream.close()"

with open("RedInput.py", "r") as source:
    red = RedBaron(source.read())

# Instrument
for i in red("while_")("else"):
    red.root.insert(0, 'a' + str(count) + ' = list()')
    red.root.append('print(str(a' + str(count) + '), file = stream)')
    i.append('a' + str(count) + '.append(0)')
    i.parent.find("if_").insert(0, 'a' + str(count) + '.append(1)')
    count += 1

red.root.insert(0, streamOpen)
red.root.append(streamClose)

with open('RedOutput.py', 'w') as dest:
    dest.write(red.dumps())

# Execute the instrumented instance
streamOutput = subprocess.check_output([sys.executable, "RedOutput.py", '1', '24'])


# Reverses given binary stream list
def reverse(a):
    list.reverse(a)
    watermark = 1
    for item in a:
        if item:
            watermark = (watermark - 1) // 3
        else:
            watermark = watermark * 2
    return watermark


# Read binary streams
with open("RedStream.py", 'r') as out:
    for line in out:
        binList = RedBaron(line)[0].to_python()
        binStream.append(binList)


# Finds the first duplicate
def retrieve(list):
    stream_set = set()
    for x in list:
        if x in stream_set:
            return x
        else:
            stream_set.add(x)
    return None


# Cleans empty streams and retrieves watermark
reversedBinStreams = [reverse(x) for x in binStream if x != []]
waterMark = retrieve(reversedBinStreams)
print(waterMark)
