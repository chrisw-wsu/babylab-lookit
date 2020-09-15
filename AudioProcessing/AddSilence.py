#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 10:32:25 2020

@author: chris
"""
from pydub import AudioSegment
from glob import iglob
import glob
import os
import fnmatch
import json
import time


def addSilence(PATH_in, PATH_out, ToProcess): 

    mp3List = PATH_out + '/' + ToProcess + '.txt'

    mp3FileList = fnmatch.filter(os.listdir(PATH_in), "*.wav")

    for each_mp3 in mp3FileList:


        each_mp3_fullDir = PATH_in + "/" + each_mp3

        word = AudioSegment.from_mp3(each_mp3_fullDir)

        #word = AudioSegment.from_wav(each_mp3_fullDir)

        silence_733ms = AudioSegment.silent(duration = 733)

        word_with_silence = silence_733ms + word

        exp_album = each_mp3[0:9]

        output = each_mp3[0:-4]+"_s.mp3"

        mp3_out = os.path.join(PATH_out, output)

        word_with_silence = word_with_silence.set_frame_rate(44100)

        word_with_silence = word_with_silence.set_sample_width(2)

        word_with_silence = word_with_silence.set_channels(1)

        word_with_silence.export(mp3_out, format="mp3", bitrate="192k", parameters=['-codec:a', 'libmp3lame'], tags={'artist': 'MARCS_BabyLab', 'genre': exp_album, 'album':'OPAL','comments': 'lookit'})
            
        localtime = time.asctime( time.localtime(time.time()) )

        with open(mp3List, 'a') as f:
            f.write(localtime+ ',' +  output + ',' + exp_album + ',' + str(word_with_silence.channels) + ',' + str(word_with_silence.sample_width) + ',' + str(len(word_with_silence)) + ',' + str(word_with_silence.frame_rate) +'\n')





