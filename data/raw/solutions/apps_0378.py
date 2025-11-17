import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGNhblBhcnRpdGlvbihzZWxmLCBudW1zKToKICAgICAgICAgIiIiCiAgICAgICAgIDp0eXBlIG51bXM6IExpc3RbaW50XQogICAgICAgICA6cnR5cGU6IGJvb2wKICAgICAgICAgIiIiCiAgICAgICAgIHMgPSAwCiAgICAgICAgIGJpdHMgPSAxCiAKICAgICAgICAgZm9yIG51bSBpbiBudW1zOgogICAgICAgICAgICAgcyArPSBudW0KICAgICAgICAgICAgIGJpdHMgfD0gYml0cyA8PCBudW0KIAogICAgICAgICByZXR1cm4gbm90IChzICYgMSkgYW5kICgoYml0cyA+PiAocyA+PiAxKSkgJiAxKSA9PSAx").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
