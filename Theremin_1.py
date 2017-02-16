import ctypes
from ctypes import wintypes
import time
import serial
from statistics import mode

user32 = ctypes.WinDLL('user32', use_last_error=True)
VK_TAB  = 0x09
VK_MENU = 0x12
VK_CONTROL = 0X11
VK_UP = 0X26
VK_DOWN = 0X28
VK_A = 0x41
VK_B = 0x42
VK_C = 0x43
VK_D = 0x44
VK_E = 0x45
VK_F = 0x46
VK_G = 0x47
vK_M = 0x4D
VK_N = 0x4E
VK_Q = 0x51
VK_W = 0x57
VK_E = 0x45
VK_R = 0x52
VK_T = 0x54
VK_X = 0x58
VK_Y = 0x59
VK_U = 0x55
VK_V = 0x56
VK_Z = 0x5A
VK_I = 0x49
VK_KEY_2 = 0x32 
VK_KEY_3 = 0x33
VK_KEY_4 = 0x34
VK_KEY_5 = 0x35
VK_KEY_6 = 0x36
VK_KEY_7 = 0x37
#dict={'a':0x32,'c':0x33,'e':0x52,'f':0x35,'h':0x36,'j':0x37,'l':0x49,'z':0x41}
ser = serial.Serial('COM3',9600)

INPUT_MOUSE    = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
KEYEVENTF_SCANCODE    = 0x0008

MAPVK_VK_TO_VSC = 0

#msdn.microsoft.com/en-us/library/dd375731

# C struct definitions

wintypes.ULONG_PTR = wintypes.WPARAM

class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx",          wintypes.LONG),
                ("dy",          wintypes.LONG),
                ("mouseData",   wintypes.DWORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

class KEYBDINPUT(ctypes.Structure):
    _fields_ = (("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

    def __init__(self, *args, **kwds):
        super(KEYBDINPUT, self).__init__(*args, **kwds)
        # some programs use the scan code even if KEYEVENTF_SCANCODE
        # isn't set in dwFflags, so attempt to map the correct code.
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk,
                                                 MAPVK_VK_TO_VSC, 0)

class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))

class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT))
    _anonymous_ = ("_input",)
    _fields_ = (("type",   wintypes.DWORD),
                ("_input", _INPUT))

LPINPUT = ctypes.POINTER(INPUT)

def _check_count(result, func, args):
    if result == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    return args

user32.SendInput.errcheck = _check_count
user32.SendInput.argtypes = (wintypes.UINT, # nInputs
                             LPINPUT,       # pInputs
                             ctypes.c_int)  # cbSize

# Functions

def PressKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode,
                            dwFlags=KEYEVENTF_KEYUP))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))


def Upkey():
	
	PressKey(VK_UP)
	time.sleep(2)
	ReleaseKey(VK_UP)

def Downkey():
	
	PressKey(VK_DOWN)
	time.sleep(2)
	ReleaseKey(VK_UP)

def akey():
	
	PressKey(VK_A)
	time.sleep(2)
	ReleaseKey(VK_A)

def bkey():
	
	PressKey(VK_B)
	#time.sleep(1)
	ReleaseKey(VK_B)
def ckey():
	
	PressKey(VK_C)
	#time.sleep(1)
	ReleaseKey(VK_C)
def bckey():
	
	PressKey(VK_B)
	PressKey(VK_C)
	time.sleep(2)
	ReleaseKey(VK_B)
	ReleaseKey(VK_C)
def gkey():
	
	PressKey(VK_G)
	#time.sleep(1)
	ReleaseKey(VK_G)
def wkey():
	
	PressKey(VK_W)
	#time.sleep(1)
	ReleaseKey(VK_W)
def zkey():
	
	PressKey(VK_Z)
	#time.sleep(1)
	ReleaseKey(VK_Z)
def xkey():
	
	PressKey(VK_X)
	#time.sleep(1)
	ReleaseKey(VK_X)
def ckey():
	
	PressKey(VK_C)
	#time.sleep(1)
	ReleaseKey(VK_C)
def vkey():
	
	PressKey(VK_V)
	#time.sleep(1)
	ReleaseKey(VK_V)
def nkey():
	
	PressKey(VK_N)
	#time.sleep(1)
	ReleaseKey(VK_N)
def mkey():
		
	PressKey(VK_M)
	#time.sleep(1)
	ReleaseKey(VK_M)
def key2():
	
	PressKey(VK_2)
	#time.sleep(1)
	ReleaseKey(VK_2)
def key3():
	
	PressKey(VK_3)
	#time.sleep(1)
	ReleaseKey(VK_3)
def key5():
	
	PressKey(VK_5)
	#time.sleep(1)
	ReleaseKey(VK_5)
def key6():
	
	PressKey(VK_6)
	#time.sleep(1)
	ReleaseKey(VK_6)
def key7():
	
	PressKey(VK_7)
	#time.sleep(1)
	ReleaseKey(VK_7)

import ctypes
from ctypes import wintypes
import comtypes
import time
import serial
from statistics import mode

from ctypes import (
    POINTER as _POINTER,
    HRESULT as _HRESULT,
    c_float as _c_float,
)

from ctypes.wintypes import (
    BOOL as _BOOL,
    DWORD as _DWORD,
)

from comtypes import (
    GUID as _GUID,
    COMMETHOD as _COMMETHOD,
    STDMETHOD as _STDMETHOD,
)


MMDeviceApiLib = _GUID(
    '{2FDAAFA3-7523-4F66-9957-9D5E7FE698F6}')

IID_IAudioEndpointVolume = _GUID(
    '{5CDF2C82-841E-4546-9722-0CF74078229A}')
IID_IMMDevice = _GUID(
    '{D666063F-1587-4E43-81F1-B948E807363F}')
IID_IMMDeviceCollection = _GUID(
    '{0BD7A1BE-7A1A-44DB-8397-CC5392387B5E}')
IID_IMMDeviceEnumerator = _GUID(
    '{A95664D2-9614-4F35-A746-DE8DB63617E6}')

CLSID_MMDeviceEnumerator = _GUID(
    '{BCDE0395-E52F-467C-8E3D-C4579291692E}')

class IAudioEndpointVolume(comtypes.IUnknown):
    _iid_ = IID_IAudioEndpointVolume
    _methods_ = (
        _STDMETHOD(_HRESULT,
            'RegisterControlChangeNotify', []),
        _STDMETHOD(_HRESULT,
            'UnregisterControlChangeNotify', []),
        _STDMETHOD(_HRESULT,
            'GetChannelCount', []),
        _COMMETHOD([], _HRESULT,
            'SetMasterVolumeLevel',
            (['in'], _c_float, 'fLevelDB'),
            (['in'], _POINTER(_GUID), 'pguidEventContext')),
        _COMMETHOD([], _HRESULT,
            'SetMasterVolumeLevelScalar',
            (['in'], _c_float, 'fLevelDB'),
            (['in'], _POINTER(_GUID), 'pguidEventContext')),
        _COMMETHOD([], _HRESULT,
            'GetMasterVolumeLevel',
            (['out','retval'], _POINTER(ctypes.c_float), 'pfLevelDB')),
        _COMMETHOD([], _HRESULT,
            'GetMasterVolumeLevelScalar',
            (['out','retval'], _POINTER(_c_float), 'pfLevelDB')),
        _COMMETHOD([], _HRESULT,
            'SetChannelVolumeLevel',
            (['in'], _DWORD, 'nChannel'),
            (['in'], _c_float, 'fLevelDB'),
            (['in'], _POINTER(_GUID), 'pguidEventContext')),
        _COMMETHOD([], _HRESULT,
            'SetChannelVolumeLevelScalar',
            (['in'], _DWORD, 'nChannel'),
            (['in'], _c_float, 'fLevelDB'),
            (['in'], _POINTER(_GUID), 'pguidEventContext')),
        _COMMETHOD([], _HRESULT,
            'GetChannelVolumeLevel',
            (['in'], _DWORD, 'nChannel'),
            (['out','retval'], _POINTER(_c_float), 'pfLevelDB')),
        _COMMETHOD([], _HRESULT,
            'GetChannelVolumeLevelScalar',
            (['in'], _DWORD, 'nChannel'),
            (['out','retval'], _POINTER(_c_float), 'pfLevelDB')),
        _COMMETHOD([], _HRESULT,
            'SetMute',
            (['in'], _BOOL, 'bMute'),
            (['in'], _POINTER(_GUID), 'pguidEventContext')),
        _COMMETHOD([], _HRESULT,
            'GetMute',
            (['out','retval'], _POINTER(_BOOL), 'pbMute')),
        _COMMETHOD([], _HRESULT,
            'GetVolumeStepInfo',
            (['out','retval'], _POINTER(_c_float), 'pnStep'),
            (['out','retval'], _POINTER(_c_float), 'pnStepCount')),
        _COMMETHOD([], _HRESULT,
            'VolumeStepUp',
            (['in'], _POINTER(_GUID), 'pguidEventContext')),
        _COMMETHOD([], _HRESULT,
            'VolumeStepDown',
            (['in'], _POINTER(_GUID), 'pguidEventContext')),
        _COMMETHOD([], _HRESULT,
            'QueryHardwareSupport',
            (['out','retval'], _POINTER(_DWORD), 'pdwHardwareSupportMask')),
        _COMMETHOD([], _HRESULT,
            'GetVolumeRange',
            (['out','retval'], _POINTER(_c_float), 'pfMin'),
            (['out','retval'], _POINTER(_c_float), 'pfMax'),
            (['out','retval'], _POINTER(_c_float), 'pfIncr')))

class IMMDevice(comtypes.IUnknown):
    _iid_ = IID_IMMDevice
    _methods_ = (
        _COMMETHOD([], _HRESULT,
            'Activate',
            (['in'], _POINTER(_GUID), 'iid'),
            (['in'], _DWORD, 'dwClsCtx'),
            (['in'], _POINTER(_DWORD), 'pActivationParams'),
            (['out','retval'],
             _POINTER(_POINTER(IAudioEndpointVolume)), 'ppInterface')),
        _STDMETHOD(_HRESULT,
            'OpenPropertyStore', []),
        _STDMETHOD(_HRESULT,
            'GetId', []),
        _STDMETHOD(_HRESULT,
            'GetState', []))

class IMMDeviceCollection(comtypes.IUnknown):
    _iid_ = IID_IMMDeviceCollection

class IMMDeviceEnumerator(comtypes.IUnknown):
    _iid_ = IID_IMMDeviceEnumerator
    _methods_ = (
        _COMMETHOD([], _HRESULT,
            'EnumAudioEndpoints',
            (['in'], _DWORD, 'dataFlow'),
            (['in'], _DWORD, 'dwStateMask'),
            (['out','retval'],
             _POINTER(_POINTER(IMMDeviceCollection)), 'ppDevices')),
        _COMMETHOD([], _HRESULT,
            'GetDefaultAudioEndpoint',
            (['in'], _DWORD, 'dataFlow'),
            (['in'], _DWORD, 'role'),
            (['out','retval'],
             _POINTER(_POINTER(IMMDevice)), 'ppDevices')))


def _get_default_endpoint_volume():
    enumerator = comtypes.CoCreateInstance(
                    CLSID_MMDeviceEnumerator,
                    IMMDeviceEnumerator,
                    comtypes.CLSCTX_INPROC_SERVER)
    endpoint = enumerator.GetDefaultAudioEndpoint(0, 1)
    return endpoint.Activate(IID_IAudioEndpointVolume,
                             comtypes.CLSCTX_INPROC_SERVER,
                             None)

def get_volume_range():
    comtypes.CoInitialize()
    try:
        endpoint_volume = _get_default_endpoint_volume()
        return endpoint_volume.GetVolumeRange()
    finally:
        comtypes.CoUninitialize()

def get_master_volume_level():
    comtypes.CoInitialize()
    try:
        endpoint_volume = _get_default_endpoint_volume()
        return endpoint_volume.GetMasterVolumeLevel()
    finally:
        comtypes.CoUninitialize()

def set_master_volume_level(level_db):
    comtypes.CoInitialize()
    try:
        endpoint_volume = _get_default_endpoint_volume()
        endpoint_volume.SetMasterVolumeLevel(level_db, None)
    finally:
        comtypes.CoUninitialize()

	
p1='d'
phex1=0X41
phex2=0x34
phex3=0x31
PressKey(0x31)
PressKey(0x34)
PressKey(0X41)
if __name__ == "__main__":
	while True:
		data=ser.read()
		data1=data.decode('ascii')
		ser.flushInput()
		data=ser.read()
		data2=data.decode('ascii')
		ser.flushInput()
		print(data1,data2)
		#print(data)
		#print('pvalue=',pvalue)
		'''pvalue=data
        if (data!=pvalue):
        	ReleaseKey(int(dict(pvalue.decode('ascii')),16))

        	PressKey(int(dict(data.decode('ascii')),16))
        	PressKey(VK_I)
        	time.sleep(1)
        	ReleaseKey(VK_I)
        	print('world')
        else:	
        	print('Hello')
        rvalue=data
        print('rvalue=',rvalue)'''
		
#dict={'a':0x32,'c':0x33,'e':0x52,'f':0x35,'h':0x36,'j':0x37,'l':0x49,'z':0x41}
		
		if data1 == 'a':
			PressKey(VK_Z)
			PressKey(VK_X)
			PressKey(VK_C)
			phex1=VK_Z
			phex2=VK_X
			phex3=VK_C
		if data1 == 'b':
			PressKey(VK_B)
			PressKey(VK_C)
			PressKey(0x31)
			
			phex1=VK_B
			phex2=VK_C
			phex3=0x31 
		if data1 == 'c':
			PressKey(VK_Q)
			PressKey(VK_W)
			PressKey(VK_E)
			
			phex1=VK_Q
			phex2=VK_W
			phex3=VK_E
		if data1 == 'd':
			PressKey(0x31)
			PressKey(0x34)
			PressKey(0X41)
			phex1=0x31
			phex2=0x34
			phex3=0x41
		if data1!=p1:
			ReleaseKey(phex1)
			ReleaseKey(phex2)
			ReleaseKey(phex3)
		
		if data2 == 'k':
			set_master_volume_level(-95)
		if data2 == 'l':
			set_master_volume_level(-80)
		if data2 == 'm':
			set_master_volume_level(-70)
		if data2 == 'n':
			set_master_volume_level(-60)
		if data2 == 'o':
			set_master_volume_level(-50)
		if data2 == 'p':
			set_master_volume_level(-40)
		if data2 == 'q':
			set_master_volume_level(-30)
		if data2 == 'r':
			set_master_volume_level(-20)
		if data2 == 's':
			set_master_volume_level(-10)
		if data2 == 't':
			set_master_volume_level(0)
		if data2 == 'z':
		    set_master_volume_level(-5)

		p1=data1
		p2=data2
	

        
