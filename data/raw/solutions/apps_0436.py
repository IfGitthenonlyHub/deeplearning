import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("aW1wb3J0IGZ1bmN0b29scwpjbGFzcyBTb2x1dGlvbjoKICAgIEBmdW5jdG9vbHMubHJ1X2NhY2hlKCkKICAgIGRlZiBtaW5EYXlzKHNlbGYsIG46IGludCkgLT4gaW50OgogICAgICAgIGlmIG4gPD0gMToKICAgICAgICAgICAgcmV0dXJuIG4KICAgICAgICAKICAgICAgICByZXR1cm4gMSArIG1pbihuJTIgKyBzZWxmLm1pbkRheXMobi8vMiksIG4lMyArIHNlbGYubWluRGF5cyhuLy8zKSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
