import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGNvdW50QmF0dGxlc2hpcHMoc2VsZiwgYm9hcmQpOgogICAgICAgICAiIiIKICAgICAgICAgOnR5cGUgYm9hcmQ6IExpc3RbTGlzdFtzdHJdXQogICAgICAgICA6cnR5cGU6IGludAogICAgICAgICAiIiIKICAgICAgICAgYW5zID0gMAogICAgICAgICBmb3Igciwgcm93IGluIGVudW1lcmF0ZShib2FyZCk6CiAgICAgICAgICAgICBmb3IgYywgdmFsIGluIGVudW1lcmF0ZShyb3cpOgogICAgICAgICAgICAgICAgIGlmIHZhbCA9PSAnWCc6CiAgICAgICAgICAgICAgICAgICAgIGFucyArPSAxCiAgICAgICAgICAgICAgICAgICAgIGlmIHIgYW5kIGJvYXJkW3ItMV1bY10gPT0gJ1gnOgogICAgICAgICAgICAgICAgICAgICAgICAgYW5zIC09IDEKICAgICAgICAgICAgICAgICAgICAgZWxpZiBjIGFuZCBib2FyZFtyXVtjLTFdID09ICdYJzoKICAgICAgICAgICAgICAgICAgICAgICAgIGFucyAtPSAxCiAgICAgICAgIHJldHVybiBhbnM=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
