import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("dD1pbnQoaW5wdXQoKSkKZm9yIF8gaW4gcmFuZ2UodCk6CiAgbix4PW1hcChpbnQsaW5wdXQoKS5zcGxpdCgpKQogIGE9bGlzdChtYXAoaW50LGlucHV0KCkuc3BsaXQoKSkpCiAgYS5zb3J0KCkKICBhLnJldmVyc2UoKQogIGNvdW50PTAKICBhbnM9MAogIGZvciBpIGluIHJhbmdlKG4pOgogICAgY291bnQrPTEKICAgIGlmIGNvdW50KmFbaV0+PXg6CiAgICAgIGFucys9MQogICAgICBjb3VudD0wCiAgcHJpbnQoYW5zKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
