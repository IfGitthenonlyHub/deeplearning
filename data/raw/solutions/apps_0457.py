import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb24ob2JqZWN0KToKICAgIGRlZiBjb2luQ2hhbmdlKHNlbGYsIGNvaW5zLCBhbW91bnQpOgogICAgICAgIE1BWCA9IGZsb2F0KCdpbmYnKQogICAgICAgIGRwID0gWzBdICsgW01BWF0gKiBhbW91bnQKCiAgICAgICAgZm9yIGkgaW4gcmFuZ2UoMSwgYW1vdW50ICsgMSk6CiAgICAgICAgICAgIGRwW2ldID0gbWluKFtkcFtpIC0gY10gaWYgaSAtIGMgPj0gMCBlbHNlIE1BWCBmb3IgYyBpbiBjb2luc10pICsgMQoKICAgICAgICByZXR1cm4gW2RwW2Ftb3VudF0sIC0xXVtkcFthbW91bnRdID09IE1BWF0=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
