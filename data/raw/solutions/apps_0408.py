import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgZmluZEJlc3RWYWx1ZShzZWxmLCBhcnI6IExpc3RbaW50XSwgdGFyZ2V0OiBpbnQpIC0+IGludDoKICAgICAgICBhcnIuc29ydCgpCiAgICAgICAgbiA9IGxlbihhcnIpCiAgICAgICAgZm9yIGkgaW4gcmFuZ2Uobik6CiAgICAgICAgICAgIHNvbCA9IHJvdW5kKHRhcmdldCAvIG4pCiAgICAgICAgICAgIGlmIGFycltpXSA+PSBzb2w6CiAgICAgICAgICAgICAgICByZXR1cm4gc29sCiAgICAgICAgICAgIHRhcmdldCAtPSBhcnJbaV0KICAgICAgICAgICAgbiAtPSAxCiAgICAgICAgcmV0dXJuIGFyclstMV0=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
