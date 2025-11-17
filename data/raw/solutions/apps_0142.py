import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGZpbmRMVVNsZW5ndGgoc2VsZiwgc3Rycyk6CiAgICAgICAgICIiIgogICAgICAgICA6dHlwZSBzdHJzOiBMaXN0W3N0cl0KICAgICAgICAgOnJ0eXBlOiBpbnQKICAgICAgICAgIiIiCiAgICAgICAgIGRlZiBpc1N1YnNlcShzMSxzMik6CiAgICAgICAgICAgICBzMl9pdD1pdGVyKHMyKQogICAgICAgICAgICAgcmV0dXJuIGFsbChpIGluIHMyX2l0IGZvciBpIGluIHMxKQogICAgICAgICBmb3IgayBpbiBzb3J0ZWQoc3RycyxrZXk9bGVuLHJldmVyc2U9VHJ1ZSk6CiAgICAgICAgICAgICBpZiBzdW0oaXNTdWJzZXEoayxrMikgZm9yIGsyIGluIHN0cnMpPT0xOgogICAgICAgICAgICAgICAgIHJldHVybiBsZW4oaykKICAgICAgICAgcmV0dXJuIC0x").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
