#!/usr/bin/env python

import rtmidi, atomac, atomac.AXKeyboard

MIDI_CHANNEL = 1
TEXT_CONTROLLER = 0
BG_CONTROLLER = 1
PREV_CONTROLLER = 43
NEXT_CONTROLLER = 44
BLANK_CONTROLLER = 45

def print_message(midi, textSlider, bgSlider, app):
  try:
    if midi.isController():
      if midi.getControllerNumber() == TEXT_CONTROLLER:
        newSpeed = round(((midi.getControllerValue() / 127.0) * 5), 1)
        #print newSpeed
        textSlider.AXValue = newSpeed
      elif midi.getControllerNumber() == BG_CONTROLLER:
        newSpeed = round(((midi.getControllerValue() / 127.0) * 5), 1)
        #print newSpeed
        bgSlider.AXValue = newSpeed
      elif midi.getControllerNumber() == PREV_CONTROLLER and midi.getControllerValue() == 127:
        app.sendKey(atomac.AXKeyboard.LEFT)
      elif midi.getControllerNumber() == NEXT_CONTROLLER and midi.getControllerValue() == 127:
        app.sendKey(atomac.AXKeyboard.RIGHT)
      else:
        print 'CONTROLLER', midi.getControllerNumber(), midi.getControllerValue()
  except atomac._a11y.ErrorInvalidUIElement:
    pass

def main():
  # Assume ProPresenter is running; get the accessibility object for our slider
  print "Getting transition sliders..."
  pp = atomac.getAppRefByBundleId("com.renewedvision.ProPresenter4")
  textSlider = pp.findFirstR(AXRole="AXSlider", AXHelp="Slide transition time")
  bgSlider = pp.findFirstR(AXRole="AXSlider", AXHelp="Image/Video transition time")
  
  # Now start receiving MIDI messages
  print "Getting available MIDI controllers..."
  midiin = rtmidi.RtMidiIn()
  ports = range(midiin.getPortCount())
  if ports:
    for i in ports:
      print i, midiin.getPortName(i)
    midiin.openPort(0)
    print "Listening for MIDI..."
    while True:
      m = midiin.getMessage(250) # some timeout in ms
      if m != None:
        print_message(m, textSlider, bgSlider, pp)
        # hack around pyrtmidi bug; if messages are queued, midiin.getMessage
        # blocks until the timeout elapses if a timeout is specified
        m = midiin.getMessage()
        m1 = m
        while m1 != None: #flush queue and get the last "real" message
          m1 = midiin.getMessage()
          if m1 != None:
            m = m1
        if m != None:
          print_message(m, textSlider, bgSlider, pp)
          
  else:
    print 'NO MIDI INPUT PORTS!'

if __name__ == "__main__":
  main()
