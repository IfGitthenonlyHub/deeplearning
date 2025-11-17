import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgcmFua1RlYW1zKHNlbGYsIHZvdGVzOiBMaXN0W3N0cl0pIC0+IHN0cjoKICAgICAgICB0ZWFtcyA9IGxpc3Qodm90ZXNbMF0pCiAgICAgICAgcmFua3MgPSB7fQogICAgICAgIGZvciB0IGluIHRlYW1zOgogICAgICAgICAgICByYW5rc1t0XSA9IFswXSAqIGxlbih0ZWFtcykKICAgICAgICAgICAgZm9yIHYgaW4gdm90ZXM6CiAgICAgICAgICAgICAgICByYW5rc1t0XVt2LmluZGV4KHQpXSAtPSAxCiAgICAgICAgcmV0dXJuICcnLmpvaW4odCBmb3IgXywgdCBpbiBzb3J0ZWQoKCh2LCB0KSBmb3IgdCwgdiBpbiBsaXN0KHJhbmtzLml0ZW1zKCkpKSkp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
