import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIHdpZ2dsZU1heExlbmd0aChzZWxmLCBudW1zKToKICAgICAgICAgIiIiCiAgICAgICAgIDp0eXBlIG51bXM6IExpc3RbaW50XQogICAgICAgICA6cnR5cGU6IGludAogICAgICAgICAiIiIKICAgICAgICAgbiA9IGxlbihudW1zKQogICAgICAgICBpZiBuIDwgMjogcmV0dXJuIG4KICAgICAgICAgcHJldl9kaWZmID0gbnVtc1sxXSAtIG51bXNbMF0KICAgICAgICAgY291bnQgPSAyIGlmIHByZXZfZGlmZiAhPSAwIGVsc2UgMQogICAgICAgICBmb3IgaSBpbiByYW5nZSgyLCBuKToKICAgICAgICAgICAgIGRpZmYgPSBudW1zW2ldIC0gbnVtc1tpLTFdCiAgICAgICAgICAgICBpZiAoZGlmZiA+IDAgYW5kIHByZXZfZGlmZiA8PSAwKSBvciAoZGlmZiA8IDAgYW5kIHByZXZfZGlmZiA+PSAwKToKICAgICAgICAgICAgICAgICBjb3VudCArPSAxCiAgICAgICAgICAgICAgICAgcHJldl9kaWZmID0gZGlmZgogICAgICAgICByZXR1cm4gY291bnQ=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
