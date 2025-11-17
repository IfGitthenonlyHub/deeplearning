import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("aW1wb3J0IHN5cwppbnB1dCA9IHN5cy5zdGRpbi5yZWFkbGluZQpUID0gaW50KGlucHV0KCkpCkFucyA9IFtdCmZvciBfIGluIHJhbmdlKFQpOgogICAgTiA9IGludChpbnB1dCgpKSAKICAgIEEgPSBsaXN0KG1hcChpbnQsIGlucHV0KCkuc3BsaXQoKSkpCiAgICBNID0gaW50KGlucHV0KCkpIAogICAgUFMgPSBbbGlzdChtYXAoaW50LCBpbnB1dCgpLnNwbGl0KCkpKSBmb3IgXyBpbiByYW5nZShNKV0KICAgIEwgPSBbMF0gKiAoTisxKQogICAgZm9yIHAsIHMgaW4gUFM6CiAgICAgICAgTFtzXSA9IG1heChMW3NdLCBwKQogICAgZm9yIGkgaW4gcmFuZ2UoTi0xLCAtMSwgLTEpOgogICAgICAgIExbaV0gPSBtYXgoTFtpXSwgTFtpKzFdKQogICAgYW5zID0gMQogICAgY250ID0gMQogICAgbWEgPSAwCiAgICBpZiBMWzFdIDwgbWF4KEEpOgogICAgICAgIEFucy5hcHBlbmQoLTEpCiAgICAgICAgY29udGludWUKICAgIGZvciBhIGluIEE6CiAgICAgICAgbWEgPSBtYXgobWEsIGEpCiAgICAgICAgaWYgTFtjbnRdIDwgbWE6CiAgICAgICAgICAgIGNudCA9IDEKICAgICAgICAgICAgYW5zICs9IDEKICAgICAgICAgICAgbWEgPSBhCiAgICAgICAgY250ICs9IDEKICAgIEFucy5hcHBlbmQoYW5zKQogCnByaW50KCJcbiIuam9pbihtYXAoc3RyLCBBbnMpKSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
