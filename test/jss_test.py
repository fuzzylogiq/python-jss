#!/usr/bin/env python
"""Tests for jss wrapper.
For test to succeed, you need to set up a preferences file at:
~/Library/Preferences/org.da.jss_helper.plist

Create a plist file with the API username and password like so:
defaults write org.da.jss_helper jss_user <username>
defaults write org.da.jss_helper jss_pass <password>
defaults write org.da.jss_helper jss_url <URL to JSS>

"""

import subprocess
import base64

from nose.tools import *

from jss import *


def std_jss():
    jp = JSSPrefs()
    j = JSS(jss_prefs=jp)
    return j


def test_jssprefs():
    jp = JSSPrefs()
    result = subprocess.check_output(['defaults', 'read', 'org.da.jss_helper', 'jss_user'])
    assert_in(jp.user, result)
    result = subprocess.check_output(['defaults', 'read', 'org.da.jss_helper', 'jss_pass'])
    assert_in(jp.password, result)
    result = subprocess.check_output(['defaults', 'read', 'org.da.jss_helper', 'jss_url'])
    assert_in(jp.url, result)


def test_jssprefs_missing_key_error():
    assert_raises(JSSPrefsMissingKeyError, JSSPrefs, '/nonexistent_path')


def test_jss_with_jss_prefs():
    jp = JSSPrefs()
    j = JSS(jss_prefs=jp)
    assert_is_instance(j, JSS)


def test_jss_with_args():
    authUser = subprocess.check_output(['defaults', 'read', 'org.da.jss_helper', 'jss_user'])
    authPass = subprocess.check_output(['defaults', 'read', 'org.da.jss_helper', 'jss_pass'])
    repoUrl = subprocess.check_output(['defaults', 'read', 'org.da.jss_helper', 'jss_url'])
    j = JSS(url=repoUrl, user=authUser, password=authPass)
    assert_is_instance(j, JSS)


def test_jss_auth_error():
    j = std_jss()
    j.password = 'DonkeyTacos'
    assert_raises(JSSAuthenticationError, j.raw_get, '/policies')


def test_jss_raw_get_error():
    j = std_jss()
    assert_raises(JSSGetError, j.raw_get, '/donkey-tacos')


#JSSObject Tests###############################################################


def test_jss_computer():
    j = std_jss()
    computers = j.Computer()
    print(computers)
    assert_is_instance(computers, list)
    assert_greater(len(computers), 0)
    id_ = computers[0].xml.find('id').text
    computer = j.Computer(id_)
    assert_is_instance(computer, Computer)
    computer.pprint()


def test_jss_computergroup():
    j = std_jss()
    computergroups = j.ComputerGroup()
    print(computergroups)
    assert_is_instance(computergroups, list)
    assert_greater(len(computergroups), 0)
    id_ = computergroups[0].xml.find('id').text
    computergroup = j.ComputerGroup(id_)
    assert_is_instance(computergroup, ComputerGroup)
    computergroup.pprint()


def test_jss_policy():
    j = std_jss()
    policies = j.Policy()
    print(policies)
    assert_is_instance(policies, list)
    assert_greater(len(policies), 0)
    id_ = policies[0].xml.find('id').text
    policy = j.Policy(id_)
    assert_is_instance(policy, Policy)
    policy.pprint()

def test_jss_mobiledevice():
    j = std_jss()
    mobiledevices = j.MobileDevice()
    print(mobiledevices)
    assert_is_instance(mobiledevices, list)
    assert_greater(len(mobiledevices), 0)
    id_ = mobiledevices[0].xml.find('id').text
    mobiledevice = j.MobileDevice(id_)
    assert_is_instance(mobiledevice, MobileDevice)
    mobiledevice.pprint()

def test_jss_mobiledeviceconfigurationprofile():
    j = std_jss()
    mobiledeviceconfigps = j.MobileDeviceConfigurationProfile()
    print(mobiledeviceconfigps)
    assert_is_instance(mobiledeviceconfigps, list)
    assert_greater(len(mobiledeviceconfigps), 0)
    id_ = mobiledeviceconfigps[0].xml.find('id').text
    mobiledeviceconfigp = j.MobileDeviceConfigurationProfile(id_)
    assert_is_instance(mobiledeviceconfigp, MobileDeviceConfigurationProfile)
    mobiledeviceconfigp.pprint()

def test_jss_mobiledevicegroups():
    j = std_jss()
    mobiledevicegroups = j.MobileDeviceGroup()
    print(mobiledevicegroups)
    assert_is_instance(mobiledevicegroups, list)
    assert_greater(len(mobiledevicegroups), 0)
    id_ = mobiledevicegroups[0].xml.find('id').text
    mobiledevicegroup = j.MobileDeviceGroup(id_)
    assert_is_instance(mobiledevicegroup, MobileDeviceGroup)
    mobiledevicegroup.pprint()

