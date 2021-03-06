import wave
import struct
import sys
from struct import pack
import math

def copy(data):
    output = []
    for index,value in enumerate(data):
        output.append(value)
    return output

#aumenta ou diminui o volume da sample
def volume_control(data, fator):
    output = []
    for index,value in enumerate(data):
        output.append(value*fator)
    return output

#inverte o som
def reverse(data):
    output = []
    for index in range(len(data)-1, -1, -1):
        output.append(value)
    return output

def mask(data, index1, index2):
    output = []
    for index,value in enumerate(data):
        if index > index1 and index < index2:
            output.append(2*math.sin((2*math.pi*sample_rate*index)/rate)) 
        else:
            output.append(value)
    return output

def main(argv):
    stream = wave.open(argv[1], "rb")
    sample_rate = stream.getframerate()
    num_frames = stream.getnframes()
    raw_data = stream.readframes( num_frames )
    stream.close()
    data = struct.unpack("%dh" % num_frames, raw_data) # "B" para ficheiros 8bits
    # Aplica efeito sobre data, para output_data
    i = 2
    output_data = []
    while i < len(argv):
        if argv[i] == "copy":
            output_data = copy(data)
        elif argv[i] == "foo":
            param = int(argv[i+1])
            output_data = foo(data, param)
            i += 1
        elif... #Outros filtros
            i += 1
    wvData = b""
    for v in output_data:
    wvData += pack("h", int(v))

    stream = wave.open("out-"+argv[1], "wb")
    stream.setnchannels(1)
    stream.setsampwidth(2)
    stream.setframerate(sample_rate)
    stream.setnframes(len(wvData))
    stream.writeframes(bytearray(wvData))
    stream.close()
if len(sys.argv) < 3:
    print("Usage: %s wave-file filter1 <params> filter2 <params> ..." % sys.argv[0])
else:
main(sys.argv)