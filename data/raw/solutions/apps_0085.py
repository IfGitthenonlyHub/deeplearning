import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Zm9yIHQgaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKICAgIHMgPSBbaW50KGMgPT0gIjEiKSBmb3IgYyBpbiBpbnB1dCgpXQogICAgeCA9IGludChpbnB1dCgpKQogICAgbiA9IGxlbihzKQoKICAgIHNhdCA9IGxhbWJkYSBpOiAoc1tpXSBpZiBpIGluIHJhbmdlKG4pIGVsc2UgMSkKCiAgICB3ID0gWyhzYXQoaSAtIHgpICYgc2F0KGkgKyB4KSkgZm9yIGkgaW4gcmFuZ2UobildCgogICAgd2F0ID0gbGFtYmRhIGk6ICh3W2ldIGlmIGkgaW4gcmFuZ2UobikgZWxzZSAwKQoKICAgIHNfcmVmID0gWyh3YXQoaSAtIHgpIHwgd2F0KGkgKyB4KSkgZm9yIGkgaW4gcmFuZ2UobildCiAgICAKICAgIGlmIHMgIT0gc19yZWY6CiAgICAgICAgcHJpbnQoLTEpCiAgICBlbHNlOgogICAgICAgIHByaW50KCIiLmpvaW4obWFwKHN0ciwgdykpKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
