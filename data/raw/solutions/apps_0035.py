import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("aW1wb3J0IHN5cwppbnB1dCA9IHN5cy5zdGRpbi5yZWFkbGluZQp0ID0gaW50KGlucHV0KCkpCmZvciBfIGluIHJhbmdlKHQpOgogIG4gPSBpbnQoaW5wdXQoKSkKICBhID0gbGlzdChtYXAoaW50LGlucHV0KCkuc3BsaXQoKSkpCiAgYS5zb3J0KCkKICBhbnMgPSAwCiAgc2VwYSA9IC0xCiAgZm9yIGkgaW4gcmFuZ2Uobik6CiAgICBpZiBpLXNlcGEgPj0gYVtpXToKICAgICAgc2VwYSA9IGkKICAgICAgYW5zICs9IDEKICBwcmludChhbnMp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
