import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZGlyID0gewogICAgJ04nOiAoMCwgMSksCiAgICAnRSc6ICgxLCAwKSwKICAgICdXJzogKC0xLCAwKSwKICAgICdTJzogKDAsIC0xKSwKfQoKZm9yIHRjIGluIHJhbmdlKGludChpbnB1dCgpKSk6CiAgICBjdXIsIGFucywgdmlzID0gKDAsIDApLCAwLCBzZXQoKQogICAgZm9yIGMgaW4gaW5wdXQoKToKICAgICAgICBueHQgPSAoY3VyWzBdICsgZGlyW2NdWzBdLCBjdXJbMV0gKyBkaXJbY11bMV0pCgogICAgICAgIGlmIChjdXIsIG54dCkgaW4gdmlzOgogICAgICAgICAgICBhbnMgKz0gMQogICAgICAgIGVsc2U6CiAgICAgICAgICAgIGFucyArPSA1CiAgICAgICAgICAgIHZpcy5hZGQoKGN1ciwgbnh0KSkKICAgICAgICAgICAgdmlzLmFkZCgobnh0LCBjdXIpKQogICAgICAgIGN1ciA9IG54dAoKICAgIHByaW50KGFucyk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
