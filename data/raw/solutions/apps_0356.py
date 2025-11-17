import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIHNlYXJjaE1hdHJpeChzZWxmLCBtYXRyaXgsIHRhcmdldCk6CiAgICAgICAgICIiIgogICAgICAgICA6dHlwZSBtYXRyaXg6IExpc3RbTGlzdFtpbnRdXQogICAgICAgICA6dHlwZSB0YXJnZXQ6IGludAogICAgICAgICA6cnR5cGU6IGJvb2wKICAgICAgICAgIiIiCiAgICAgICAgIGlmIChub3QgbWF0cml4KSBvciAobm90IG1hdHJpeFswXSk6IHJldHVybiBGYWxzZQogICAgICAgICBpLCBqID0gMCwgbGVuKG1hdHJpeFswXSkgLSAxCiAgICAgICAgIHdoaWxlIChpIDwgbGVuKG1hdHJpeCkpIGFuZCAoaiA+PSAwKTogCiAgICAgICAgICAgICBpZiBtYXRyaXhbaV1bal0gPT0gdGFyZ2V0OiAKICAgICAgICAgICAgICAgICByZXR1cm4gVHJ1ZQogICAgICAgICAgICAgZWxpZiBtYXRyaXhbaV1bal0gPiB0YXJnZXQ6IAogICAgICAgICAgICAgICAgIGogLT0gMQogICAgICAgICAgICAgZWxzZTogCiAgICAgICAgICAgICAgICAgaSArPSAxCiAgICAgICAgIHJldHVybiBGYWxzZQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
