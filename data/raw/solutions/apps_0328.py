import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGZpbmQxMzJwYXR0ZXJuKHNlbGYsIG51bXMpOgogICAgICAgICAiIiIKICAgICAgICAgOnR5cGUgbnVtczogTGlzdFtpbnRdCiAgICAgICAgIDpydHlwZTogYm9vbAogICAgICAgICAiIiIKICAgICAgICAgczMgPSAtIDIgKiogNjQgLSAxCiAgICAgICAgIG1heHNldCA9IFtdCiAgICAgICAgIGZvciBpIGluIHJldmVyc2VkKG51bXMpOgogICAgICAgICAgICAgaWYgaSA8IHMzOgogICAgICAgICAgICAgICAgIHJldHVybiBUcnVlCiAgICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgIHdoaWxlIGxlbihtYXhzZXQpID4gMCBhbmQgaSA+IG1heHNldFstMV06CiAgICAgICAgICAgICAgICAgICAgIHMzID0gbWF4c2V0LnBvcCgtMSkKICAgICAgICAgICAgIG1heHNldC5hcHBlbmQoaSkKICAgICAgICAgcmV0dXJuIEZhbHNl").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
