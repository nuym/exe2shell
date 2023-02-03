import sys, os

if len(sys.argv) < 2:
    print('usage: ' + sys.argv[0] + ' file.exe\n')
    sys.exit(0)

shellcode = ''
bytes = 0

with open(sys.argv[1], 'rb') as f:
    for b in f.read():
        shellcode += '\\x' + hex(b)[2:].zfill(2)
        bytes += 1

print('Number of bytes for file ' + sys.argv[1] + ': ' + str(bytes) + '\n')

with open("shell.txt", "w") as fp:
    fp.write(shellcode)

print("Done!")
