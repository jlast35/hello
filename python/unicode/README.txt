Since windows command prompt can't realistically output unicode text...

(And if you run content group stuff in Cygwin, all the data files are on a Windows file system, so you have path translation issues...)

For compatibility with Windows:

1 If you ever use a print statement in Python, make sure it never outputs data that may be unicode.

2 Any unicode output that you MUST capture should be output to a log file, since there is no issue viewing unicode in Notepad++

3 If you must have console-output pacifier text to indicate what is currently processing, (or animate the fact that something currently IS still processing...) you either have to output {filename, line number} for text docs, or {filename, tab#, row, col) for spreadsheets.

maybe I could output to a gui instead...