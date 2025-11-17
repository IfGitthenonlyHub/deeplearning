import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbnVtYmVyT2ZTdWJhcnJheXMoc2VsZiwgbnVtczogTGlzdFtpbnRdLCBrOiBpbnQpIC0+IGludDoKICAgICAgICBsID0gWzBdKihsZW4obnVtcykrMSkKICAgICAgICBmb3IgaSxuIGluIGVudW1lcmF0ZShudW1zKToKICAgICAgICAgICAgbFtpKzFdPWxbaV0rbiUyCiAgICAgICAgYyA9IENvdW50ZXIobCkKICAgICAgICAjcHJpbnQobCkKICAgICAgICByZXR1cm4gc3VtKGNbeC1rXSpjW3hdIGZvciB4IGluIGMp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
