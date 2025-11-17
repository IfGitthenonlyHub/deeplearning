import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGhJbmRleChzZWxmLCBjaXRhdGlvbnMpOgogICAgICAgICAiIiIKICAgICAgICAgOnR5cGUgY2l0YXRpb25zOiBMaXN0W2ludF0KICAgICAgICAgOnJ0eXBlOiBpbnQKICAgICAgICAgIiIiCiAgICAgICAgIGggPSAwCiAgICAgICAgIGNvdW50ID0gMAogICAgICAgICBmb3IgYyBpbiBjaXRhdGlvbnNbOjotMV06CiAgICAgICAgICAgICBpZiBjIDw9IGNvdW50OgogICAgICAgICAgICAgICAgIHJldHVybiBjb3VudAogICAgICAgICAgICAgY291bnQgKz0gMQogICAgICAgICByZXR1cm4gY291bnQ=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
