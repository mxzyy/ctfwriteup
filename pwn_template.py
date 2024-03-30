## Run local executable.
##   ./exploit.py LOCAL EXE=./executable
#
## Run remote (with local executable for addresses)
##   ./exploit.py HOST=example.com PORT=4141 EXE=/tmp/executable
#
## Run with GDB script.
##   ./exploit.py GDB
## --- (Edit GDB script if necessary) --------------------------------
gdbscript = """

""".format(
    **locals()
)
## -------------------------------------------------------------------

from pwn import *

## --- (do not edit) ---------------------------------------------------
exe = context.binary = ELF(args.EXE)

def start_local(argv=[], *a, **kw):
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def start_remote(argv=[], *a, **kw):
    host = args.HOST
    port = int(args.PORT)
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)

io = start()
## -----------------------------------------------------------------------

## EXPLOIT GOES HERE

