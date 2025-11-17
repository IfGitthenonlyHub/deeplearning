import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgY2FuUmVvcmRlckRvdWJsZWQoc2VsZiwgQTogTGlzdFtpbnRdKSAtPiBib29sOgogICAgICAgIGMgPSBjb2xsZWN0aW9ucy5Db3VudGVyKEEpCiAgICAgICAgZm9yIHggaW4gc29ydGVkKGMsIGtleT1hYnMpOgogICAgICAgICAgICBpZiBjW3hdID4gY1syICogeF06CiAgICAgICAgICAgICAgICByZXR1cm4gRmFsc2UKICAgICAgICAgICAgY1syICogeF0gLT0gY1t4XQogICAgICAgIHJldHVybiBUcnVl").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
