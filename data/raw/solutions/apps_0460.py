import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGFycmF5TmVzdGluZyhzZWxmLCBudW1zKToKICAgICAgICAgIiIiCiAgICAgICAgIDp0eXBlIG51bXM6IExpc3RbaW50XQogICAgICAgICA6cnR5cGU6IGludAogICAgICAgICAiIiIKICAgICAgICAgYW5zLCBzdGVwLCBuID0gMCwgMCwgbGVuKG51bXMpCiAgICAgICAgIHNpZ25hbCA9IFtGYWxzZV0gKiBuCiAgICAgICAgIGZvciBpIGluIHJhbmdlKG4pOgogICAgICAgICAgICAgd2hpbGUgbm90IHNpZ25hbFtpXToKICAgICAgICAgICAgICAgICBzaWduYWxbaV0gPSBUcnVlCiAgICAgICAgICAgICAgICAgc3RlcCArPSAxCiAgICAgICAgICAgICAgICAgaSA9IG51bXNbaV0KICAgICAgICAgICAgICAgICBhbnMgPSBtYXgoYW5zLCBzdGVwKQogICAgICAgICAgICAgc3RlcCA9IDAKICAgICAgICAgcmV0dXJuIGFucw==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
