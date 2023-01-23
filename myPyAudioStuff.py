import pyaudio
import time
import math
import struct
import numpy.fft

WIDTH = 2
CHANNELS = 2
RATE = 44100

p = pyaudio.PyAudio()

def convertDataToListAmplitudes(data): #TODO - add type of data
    """takes in raw pyaudio data and returns the converted data in a 'list' (might be other ordered type)  where each element is amplitude ordered by time"""
    count = len(data)/2
    format = "%dh"%(count)
    shorts = struct.unpack( format, data )
    return shorts


def rms( data ): #TODO - add type of data
    """Converts the data from pyaudio to rms, can then convert to decibels"""
    count = len(data)/2
    shorts = convertDataToListAmplitudes(data)
    sum_squares = 0.0
    for sample in shorts:
        n = sample * (1.0/32768)
        sum_squares += n*n
    return math.sqrt( sum_squares / count )

def convertDataToPitch(data, return_all_data=False):
    """Converts the data from pyaudio to pitch (add unit in docstring)""" #TODO add unit in docstring
    shorts = convertDataToListAmplitudes(data)
    
    frequencyResponse = numpy.fft.rfft(shorts) #is a list of complex numbers (index reps frequency (no clue unit of frequency), value is amount of frequency received)
    listOfFourierOutputMagnitude = abs(frequencyResponse) #makes every complex number a real number 
    
    #New way that averages the frequencies received
    # myCounter = 0 #Reps the sum of all the values in listOfFourierOutputMagnitude to then use afterwards to make the mean of the values
    # weightedPitches = 0
    # for i in range(len(listOfFourierOutputMagnitude)):
    #     singleFrequencyAmount = listOfFourierOutputMagnitude[i] #So iterate over the list with both index and value
    #     myCounter += singleFrequencyAmount
    #     weightedPitches += singleFrequencyAmount*i #Instead of just using i, I'm weighting all the i's by the amount of received, then after dividing by the total so that it's a proper mean
    # currentPitch = weightedPitches/myCounter #So current pitch should still be a value from 1 to whatever the highest index is
    
    # Old way to calculate current pitch that just took frequency that received the most of. This sucked (not what we hear as pitch)
    highestLikelynessToBeCurrentPitch = max(listOfFourierOutputMagnitude)
    currentPitch = list(listOfFourierOutputMagnitude).index(highestLikelynessToBeCurrentPitch) #Grab the index of the pitch (higher index means higher pitch)
    # logarithmicpitch =
    
    if return_all_data:
        return currentPitch, listOfFourierOutputMagnitude
    return currentPitch #currently a value from 0 to the highest index of the list (seems to go to about 50)


stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                )

stream.start_stream()


