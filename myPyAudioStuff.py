import pyaudio
import time
import math
import struct

WIDTH = 2
CHANNELS = 2
RATE = 44100

p = pyaudio.PyAudio()


# Not using this any more, looks like I shouldn't use callback
# def callback(in_data, frame_count, time_info, status):
#     global counter
#     print(len(in_data))
#     print("/n")
#     counter += 1
#     print(counter)
#     return (in_data, pyaudio.paContinue)

def rms( data ):
    """Converts the data from pyaudio to rms, can then convert to decibels"""
    count = len(data)/2
    format = "%dh"%(count)
    shorts = struct.unpack( format, data )
    sum_squares = 0.0
    for sample in shorts:
        n = sample * (1.0/32768)
        sum_squares += n*n
    return math.sqrt( sum_squares / count )



stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                )

stream.start_stream()


