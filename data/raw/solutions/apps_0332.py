import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGNvdW50U3Vic3RyaW5ncyhzZWxmLCBzKToKICAgICAgICAgIiIiCiAgICAgICAgIDp0eXBlIHM6IHN0cgogICAgICAgICA6cnR5cGU6IGludAogICAgICAgICAiIiIKICAgICAgICAgcz0nLCcrcysnLicKICAgICAgICAgYW5zPTAKICAgICAgICAgZm9yIGkgaW4gcmFuZ2UoMSxsZW4ocyktMSk6CiAgICAgICAgICAgICBqPTEKICAgICAgICAgICAgIHdoaWxlIHNbaStqXT09c1tpLWpdOgogICAgICAgICAgICAgICAgIGorPTEKICAgICAgICAgICAgIGFucys9agogICAgICAgICBmb3IgaSBpbiByYW5nZSgxLGxlbihzKS0xKToKICAgICAgICAgICAgIGo9MAogICAgICAgICAgICAgd2hpbGUgc1tpLWpdPT1zW2krMStqXToKICAgICAgICAgICAgICAgICBqKz0xCiAgICAgICAgICAgICBhbnMrPWoKICAgICAgICAgcmV0dXJuIGFucw==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
