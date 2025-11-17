import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbW92ZXNUb01ha2VaaWd6YWcoc2VsZiwgbnVtczogTGlzdFtpbnRdKSAtPiBpbnQ6CiAgICAgICAgcmVzID0gWzAsIDBdCiAgICAgICAgCiAgICAgICAgZm9yIGkgaW4gcmFuZ2UobGVuKG51bXMpKToKICAgICAgICAgICAgcmVzW2klMl0gKz0gbWF4KG51bXNbaV0gKyAxIC0gbWluKG51bXNbaS0xXSBpZiBpIGVsc2UgZmxvYXQoJ2luZicpLCBudW1zW2krMV0gaWYgaSA8IGxlbihudW1zKSAtIDEgZWxzZSBmbG9hdCgnaW5mJykpLCAwKQogICAgICAgIAogICAgICAgIHJldHVybiBtaW4ocmVzKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
