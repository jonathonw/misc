SongConverter.py
================

Converts MediaShout text files to a format more conducive to use
with Renewed Vision's ProPresenter, preserving slide order and
(where possible) slide names.

Usage
-----

    SongConverter.py song-file.txt
    
where `song-file.txt` is a text file containing one or more songs
exported from MediaShout.

The converted songs will be placed in individual text files in
an 'output' subfolder of the current folder.  These files can
be directly imported by ProPresenter.

Known Issues
------------

* Slides labeled "Ending *n*" will not be labeled correctly in
  ProPresenter, and the label "Ending *n*" will appear in the
  text of the converted slide.
* If multiple copies of a song exist in the same text file,
  only the last copy will be converted and remain in the output
  directory.
* MediaShout text files must be correctly formed for this converter
  to be able to work with them.  Incorrectly formatted files
  (due to hand-editing or other reasons) may cause the converter
  to fail.
  
Notes
-----

Tested with MediaShout 2.5.5 and ProPresenter 4.2.6.
