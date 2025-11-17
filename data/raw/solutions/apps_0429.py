import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb24ob2JqZWN0KToKICAgICBkZWYgZ2V0SGludChzZWxmLCBzZWNyZXQsIGd1ZXNzKToKICAgICAgICAgIiIiCiAgICAgICAgIDp0eXBlIHNlY3JldDogc3RyCiAgICAgICAgIDp0eXBlIGd1ZXNzOiBzdHIKICAgICAgICAgOnJ0eXBlOiBzdHIKICAgICAgICAgICAgICAgICAiIiIKICAgICAgICAgZCA9IHt9CiAgICAgICAgIGJ1bGwsIGNvdyA9IDAsMAogCiAgICAgICAgIGZvciBpbmRleCxzIGluIGVudW1lcmF0ZShzZWNyZXQpOgogICAgICAgICAgICAgaWYgZ3Vlc3NbaW5kZXhdID09IHM6CiAgICAgICAgICAgICAgICAgYnVsbCArPSAxCiAgICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgIGRbc10gPSBkLmdldChzLDApICsgMQogCiAgICAgICAgIGZvciBpbmRleCxzIGluIGVudW1lcmF0ZShzZWNyZXQpOgogICAgICAgICAgICAgaWYgKGd1ZXNzW2luZGV4XSAhPSBzKSAmIChkLmdldChndWVzc1tpbmRleF0sMCkgIT0gMCk6CiAgICAgICAgIAkgICAgY293ICs9IDEKICAgICAgICAgCSAgICBkW2d1ZXNzW2luZGV4XV0gLT0gMQogICAgICAgICAJICAgIAogICAgICAgICByZXR1cm4gc3RyKGJ1bGwpICsgIkEiICsgc3RyKGNvdykgKyAiQiI=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
