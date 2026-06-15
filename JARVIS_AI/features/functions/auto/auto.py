import os
import main.features.functions.auto.auto as auto
import sys
import configparser as parser
import sysconfig as config
import syslog as log
import logger
import logging
import pathlib as plib

from organizer import *

class Auto(Exception):
    def __init__(self, *args):
        return super().__init__(*args)


Auto()
