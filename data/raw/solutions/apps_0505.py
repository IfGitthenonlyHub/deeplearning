import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWluUmVtb3ZlVG9NYWtlVmFsaWQoc2VsZiwgczogc3RyKSAtPiBzdHI6CiAgICAgICAgcmVzID0gJycKICAgICAgICBmb3IgYyBpbiBzOgogICAgICAgICAgICBpZiBjIT0nKSc6IHJlcyArPSBjCiAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICBpZiAnKCcgaW4gcmVzOgogICAgICAgICAgICAgICAgICAgIGlkeCA9IHJlcy5yZmluZCgnKCcpCiAgICAgICAgICAgICAgICAgICAgcmVzID0gcmVzWzppZHhdKydMJytyZXNbaWR4KzE6XQogICAgICAgICAgICAgICAgICAgIHJlcys9JyknCiAgICAgICAgcmVzID0gcmVzLnJlcGxhY2UoJygnLCAnJykKICAgICAgICByZXMgPSByZXMucmVwbGFjZSgnTCcsICcoJykKICAgICAgICByZXR1cm4gcmVz").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
