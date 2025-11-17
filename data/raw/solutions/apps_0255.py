import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGp1bXAoc2VsZiwgbnVtcyk6CiAgICAgICAgICIiIgogICAgICAgICA6dHlwZSBudW1zOiBMaXN0W2ludF0KICAgICAgICAgOnJ0eXBlOiBpbnQKICAgICAgICAgIiIiCiAgICAgICAgIHAgPSBbMF0KICAgICAgICAgZm9yIGkgaW4gcmFuZ2UobGVuKG51bXMpIC0gMSk6CiAgICAgICAgICAgICB3aGlsZShpICsgbnVtc1tpXSA+PSBsZW4ocCkgYW5kIGxlbihwKSA8IGxlbihudW1zKSk6CiAgICAgICAgICAgICAgICAgcC5hcHBlbmQocFtpXSArIDEpCiAgICAgICAgIHJldHVybiBwWy0xXQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
