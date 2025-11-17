import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIG51bWJlck9mQXJpdGhtZXRpY1NsaWNlcyhzZWxmLCBBKToKICAgICAgICAgY3Vyciwgc3VtID0gMCwgMAogICAgICAgICBmb3IgaSBpbiByYW5nZSgyLCBsZW4oQSkpOgogICAgICAgICAgICAgaWYgQVtpXSAtIEFbaSAtIDFdID09IEFbaSAtIDFdIC0gQVtpIC0gMl06CiAgICAgICAgICAgICAgICAgY3VyciArPSAxCiAgICAgICAgICAgICAgICAgc3VtICs9IGN1cnIKICAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICAgY3VyciA9IDAKICAgICAgICAgcmV0dXJuIHN1bQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
