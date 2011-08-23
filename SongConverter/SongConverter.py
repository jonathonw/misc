#!/usr/bin/env python

import codecs
import sys

if len(sys.argv) != 2:
  print "Usage:", sys.argv[0], "mediashout-export-file"
  exit(-1)

f = codecs.open(sys.argv[1], "r", "windows-1253")

verseOrder = None
verses = {}
currentVerse = ""
currentTitle = ""
verseText = ""
for line in f:
  line = line.strip()
  if line.startswith("Title: "):
    if currentVerse != "":
      verses[currentVerse] = verseText.strip()
      print "Stored verse", currentVerse
      print "Text:", verseText
      print "Got a whole song..."
      print "=============================="
      print "Title:", currentTitle
      print ""
      print verses
      #for key, value in verses.iteritems():
      #  print key
      #  print value
      #  print ""
      outputFile = codecs.open("output/" + currentTitle + ".txt", "w", "utf-8")
      outputFile.write(u"\n\n")
      for verseName in verseOrder:
        outputFile.write(verseName + u"\n")
        outputFile.write(verses[verseName] + u"\n")
        outputFile.write(u"\n")
      outputFile.write(u"\n\n")
      outputFile.close()
      currentVerse = ""
      verseText = ""
      verses = {}
    currentTitle = line.replace("Title: ", "", 1).strip()
    print "Found title:", currentTitle
  elif line.startswith("PlayOrder: "):
    verseOrderString = line.replace("PlayOrder: ", "", 1).strip()
    verseOrderString = verseOrderString.replace(" ", "")
    verseOrderString = verseOrderString.replace("Verse", "Verse ")
    verseOrderString = verseOrderString.replace("Chorus", "Chorus ")
    verseOrderString = verseOrderString.replace("Bridge", "Bridge ")
    verseOrderString = verseOrderString.replace("Ending", "Ending ")
    verseOrder = verseOrderString.split(",")
    print "Got verse order: ", verseOrder
  elif (line.startswith("Verse ") or line.startswith("Chorus ") or line.startswith("Bridge ") or line.startswith("Ending ")) and line.endswith(":"):
    if currentVerse != "":
      verses[currentVerse] = verseText.strip()
      print "Stored verse", currentVerse
      print "Text:", verseText
    currentVerse = line.replace(":", "")
    verseText = ""
  else:
    if currentVerse != "":
      verseText = verseText + line + "\n"

verses[currentVerse] = verseText.strip()
print "Stored verse", currentVerse
print "Text:", verseText
print "Got a whole song..."
print "=============================="
print "Title:", currentTitle
print ""
print verses
#for key, value in verses.iteritems():
#  print key
#  print value
#  print ""
outputFile = codecs.open("output/" + currentTitle + ".txt", "w", "utf-8")
outputFile.write(u"\n\n")
for verseName in verseOrder:
  outputFile.write(verseName + u"\n")
  outputFile.write(verses[verseName] + u"\n")
  outputFile.write(u"\n")
outputFile.write(u"\n\n")
outputFile.close()
currentVerse = ""
verseText = ""
verses = {}
