#Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/UC33e/config.py
from __future__ import absolute_import, print_function, unicode_literals
from .consts import *
TRANSPORT_CONTROLS = {u'STOP': GENERIC_STOP,
 u'PLAY': GENERIC_PLAY,
 u'REC': GENERIC_REC,
 u'LOOP': GENERIC_LOOP,
 u'RWD': GENERIC_RWD,
 u'FFWD': GENERIC_FFWD}
DEVICE_CONTROLS = ((GENERIC_ENC1, 0),
 (GENERIC_ENC2, 1),
 (GENERIC_ENC3, 2),
 (GENERIC_ENC4, 3),
 (GENERIC_ENC5, 4),
 (GENERIC_ENC6, 5),
 (GENERIC_ENC7, 6),
 (GENERIC_ENC8, 7))
VOLUME_CONTROLS = ((GENERIC_SLI1, 0),
 (GENERIC_SLI2, 1),
 (GENERIC_SLI3, 2),
 (GENERIC_SLI4, 3),
 (GENERIC_SLI5, 4),
 (GENERIC_SLI6, 5),
 (GENERIC_SLI7, 6),
 (GENERIC_SLI8, 7))
TRACKARM_CONTROLS = (GENERIC_BUT1,
 GENERIC_BUT2,
 GENERIC_BUT3,
 GENERIC_BUT4,
 GENERIC_BUT5,
 GENERIC_BUT6,
 GENERIC_BUT7,
 GENERIC_BUT8)
BANK_CONTROLS = {u'TOGGLELOCK': GENERIC_BUT9,
 u'BANKDIAL': -1,
 u'NEXTBANK': GENERIC_PAD5,
 u'PREVBANK': GENERIC_PAD1,
 u'BANK1': -1,
 u'BANK2': -1,
 u'BANK3': -1,
 u'BANK4': -1,
 u'BANK5': -1,
 u'BANK6': -1,
 u'BANK7': -1,
 u'BANK8': -1}
CONTROLLER_DESCRIPTIONS = {u'INPUTPORT': u'UC-33 USB MIDI Controller (Port 1)',
 u'OUTPUTPORT': u'UC-33 USB MIDI Controller (Port 1)',
 u'CHANNEL': 0}
MIXER_OPTIONS = {u'NUMSENDS': 2,
 u'SEND1': (-1, -1, -1, -1, -1, -1, -1, -1),
 u'SEND2': (-1, -1, -1, -1, -1, -1, -1, -1),
 u'MASTERVOLUME': 28}