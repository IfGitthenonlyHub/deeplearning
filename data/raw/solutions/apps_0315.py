import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWluaW11bVN3YXAoc2VsZiwgczE6IHN0ciwgczI6IHN0cikgLT4gaW50OgogICAgICAgIHh4ID0gW10KICAgICAgICBmb3IgaSBpbiByYW5nZShsZW4oczEpKToKICAgICAgICAgICAgaWYgczFbaV0gIT0gczJbaV06CiAgICAgICAgICAgICAgICB4eC5hcHBlbmQoczFbaV0pCgogICAgICAgIGlmIGxlbih4eCklMiA9PSAxOgogICAgICAgICAgICByZXR1cm4gLTEKICAgICAgICByZXMgPSBsZW4oeHgpLy8yCiAgICAgICAgaWYgeHguY291bnQoJ3gnKSUyID09IDE6CiAgICAgICAgICAgIHJlcyArPSAxCiAgICAgICAgcmV0dXJuIHJlcw==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
