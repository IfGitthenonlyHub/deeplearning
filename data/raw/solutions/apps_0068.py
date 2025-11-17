import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Zm9yIF8gaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKCW4gPSBpbnQoaW5wdXQoKSkKCglzID0gbGlzdChpbnB1dCgpKQoKCWdyb3VwcyA9IFtdCglsYXN0ID0gJycKCWNudCA9IDAKCWZvciBjIGluIHM6CgkJaWYgYyAhPSBsYXN0OgoJCQlpZiBjbnQ6IGdyb3Vwcy5hcHBlbmQoY250KQoJCQljbnQgPSAxCgkJZWxzZToKCQkJY250ICs9IDEKCQlsYXN0ID0gYwoKCWlmIGNudDogZ3JvdXBzLmFwcGVuZChjbnQpCgoJbSA9IGxlbihncm91cHMpCglpID0gMAoJaiA9IDAKCglvcHMgPSAwCgl3aGlsZSBpIDwgbToKCQlvcHMgKz0gMQoKCQl3aGlsZSBqIDwgaSBvciAoaiA8IG0gYW5kIGdyb3Vwc1tqXSA9PSAxKTogaiArPSAxCgoJCWlmIGogPCBtOiBncm91cHNbal0gLT0gMQoJCWVsc2U6IGkgKz0gMQoJCWkgKz0gMQoKCXByaW50KG9wcyk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
