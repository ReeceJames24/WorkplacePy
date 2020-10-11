# program to copy order time and order completion time

import re, pyperclip

#TO DO: Regex for the timestamps
timeRegex = re.compile(r'\d\d:\d\d:\d\d')

#TO DO: Paste raw data to this program
rawData = pyperclip.paste()

#TO DO: Extract matches from raw data
extractedTime = timeRegex.findall(rawData)

#TO DO: Copy extracted data to clipboard
results = '\n'.join(extractedTime)
pyperclip.copy(results)
print('Extracted Timestamps have been copied to your clipboard')
