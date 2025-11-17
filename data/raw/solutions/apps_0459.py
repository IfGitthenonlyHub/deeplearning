import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGNoYXJhY3RlclJlcGxhY2VtZW50KHNlbGYsIHMsIGspOgogICAgICAgICAiIiIKICAgICAgICAgOnR5cGUgczogc3RyCiAgICAgICAgIDp0eXBlIGs6IGludAogICAgICAgICA6cnR5cGU6IGludAogICAgICAgICAiIiIKICAgICAgICAgc3RhcnQgPSBlbmQgID0gbWF4biA9IDAKICAgICAgICAgYWxwaGFfZGljdCA9IGNvbGxlY3Rpb25zLmRlZmF1bHRkaWN0KGludCkKICAgICAgICAgZm9yIGVuZCBpbiByYW5nZSgxLGxlbihzKSsxKToKICAgICAgICAgICAgIGFscGhhX2RpY3Rbc1tlbmQtMV1dICs9IDEKICAgICAgICAgICAgIG1heG4gPSBtYXgobWF4biwgYWxwaGFfZGljdFtzW2VuZC0xXV0pCiAgICAgICAgICAgICBpZiBlbmQtc3RhcnQgPiBrK21heG46CiAgICAgICAgICAgICAgICAgYWxwaGFfZGljdFtzW3N0YXJ0XV0gLT0gMQogICAgICAgICAgICAgICAgIHN0YXJ0ICs9IDEKICAgICAgICAgcmV0dXJuIGVuZC1zdGFydA==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
