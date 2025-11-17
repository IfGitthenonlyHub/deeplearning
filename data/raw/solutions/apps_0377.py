import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbnRoTWFnaWNhbE51bWJlcihzZWxmLCBOOiBpbnQsIEE6IGludCwgQjogaW50KSAtPiBpbnQ6CiAgICAgICAgZnJvbSBmcmFjdGlvbnMgaW1wb3J0IGdjZAogICAgICAgIE1PRCA9IDEwKio5KzcKICAgICAgICBMID0gQS9nY2QoQSxCKSpCCiAgICAgICAgCiAgICAgICAgZGVmIG1heF91bmlxdWVfbnVtcyh4KToKICAgICAgICAgICAgcmV0dXJuIHgvL0EreC8vQi14Ly9MCiAgICAgICAgCiAgICAgICAgbG8gPSAwCiAgICAgICAgaGkgPSBOKm1pbihBLEIpCiAgICAgICAgd2hpbGUgbG88aGk6CiAgICAgICAgICAgIG1pZCA9IChsbytoaSkvLzIKICAgICAgICAgICAgaWYgbWF4X3VuaXF1ZV9udW1zKG1pZCk8TjoKICAgICAgICAgICAgICAgIGxvID0gIG1pZCArIDEKICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgIGhpID0gbWlkCiAgICAgICAgcmV0dXJuIGxvJU1PRA==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
