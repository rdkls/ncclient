import unittest
from ncclient.devices.ericsson import *
import ncclient.transport
from mock import patch
import paramiko
import sys

class TestEricssonDevice(unittest.TestCase):

    def setUp(self):
        self.obj = EricssonDeviceHandler({'name': 'ericsson'})

    def test_perform_quality_check(self):
        self.assertFalse(self.obj.perform_qualify_check())

