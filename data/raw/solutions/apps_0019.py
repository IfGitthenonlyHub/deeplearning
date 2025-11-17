import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Zm9yIF8gaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKICAgIG4sIGssIGQgPSBsaXN0KG1hcChpbnQsIGlucHV0KCkuc3BsaXQoKSkpCiAgICBhID0gbGlzdChtYXAoaW50LCBpbnB1dCgpLnNwbGl0KCkpKQogICAgcyA9IHt9CiAgICBmb3IgcSBpbiByYW5nZShkKToKICAgICAgICBzW2FbcV1dID0gcy5nZXQoYVtxXSwgMCkrMQogICAgYW5zID0gbGVuKHMpCiAgICBmb3IgcSBpbiByYW5nZShkLCBuKToKICAgICAgICBpZiBzW2FbcS1kXV0gPT0gMToKICAgICAgICAgICAgZGVsIHNbYVtxLWRdXQogICAgICAgIGVsc2U6CiAgICAgICAgICAgIHNbYVtxLWRdXSAtPSAxCiAgICAgICAgc1thW3FdXSA9IHMuZ2V0KGFbcV0sIDApKzEKICAgICAgICBhbnMgPSBtaW4oYW5zLCBsZW4ocykpCiAgICBwcmludChhbnMp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
