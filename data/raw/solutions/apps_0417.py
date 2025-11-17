import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGZpbmRNZWRpYW5Tb3J0ZWRBcnJheXMoc2VsZiwgbnVtczEsIG51bXMyKToKICAgICAgICAgIiIiCiAgICAgICAgIDp0eXBlIG51bXMxOiBMaXN0W2ludF0KICAgICAgICAgOnR5cGUgbnVtczI6IExpc3RbaW50XQogICAgICAgICA6cnR5cGU6IGZsb2F0CiAgICAgICAgICIiIgogICAgICAgICBudW1zID0gc29ydGVkKG51bXMxICsgbnVtczIpCiAgICAgICAgIG4gPSBsZW4obnVtcykKICAgICAgICAgcmV0dXJuIG51bXNbaW50KG4vMildIGlmIG4lMj09MSBlbHNlIChudW1zW2ludChuLzIpXStudW1zW2ludChuLzIpLTFdKS8yLjA=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
