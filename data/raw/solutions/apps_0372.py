import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGlzTWF0Y2goc2VsZiwgcywgcCk6CiAgICAgICAgICIiIgogICAgICAgICA6dHlwZSBzOiBzdHIKICAgICAgICAgOnR5cGUgcDogc3RyCiAgICAgICAgIDpydHlwZTogYm9vbAogICAgICAgICAiIiIKICAgICAgICAgaW1wb3J0IHJlCiAgICAgICAgIHBhdHRlcm4gPSByZS5jb21waWxlKHApCiAgICAgICAgIG1hdGNoID0gcGF0dGVybi5tYXRjaChzKQogICAgICAgICBpZiBtYXRjaDoKICAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgICByZXR1cm4gbWF0Y2guZ3JvdXAoKSA9PSBzCiAgICAgICAgICAgICBleGNlcHQ6CiAgICAgICAgICAgICAgICAgcmV0dXJuIEZhbHNlCiAgICAgICAgICAgICBmaW5hbGx5OgogICAgICAgICAgICAgICAgIHBhc3MKICAgICAgICAgZWxzZToKICAgICAgICAgICAgIHJldHVybiBGYWxzZQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
