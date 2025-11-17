import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGxlbmd0aE9mTG9uZ2VzdFN1YnN0cmluZyhzZWxmLCBzKToKICAgICAgICAgIiIiCiAgICAgICAgIDp0eXBlIHM6IHN0cgogICAgICAgICA6cnR5cGU6IGludAogICAgICAgICAiIiIKICAgICAgICAgTCwgcmVzLCBsYXN0ID0gLTEsIDAsIHt9CiAgICAgICAgIGZvciBSLCBjaGFyIGluIGVudW1lcmF0ZShzKToKICAgICAgICAgICAgIGlmIGNoYXIgaW4gbGFzdCBhbmQgbGFzdFtjaGFyXSA+IEw6CiAgICAgICAgICAgICAgICAgTCA9IGxhc3RbY2hhcl0KICAgICAgICAgICAgIGVsaWYgUi1MID4gcmVzOgogICAgICAgICAgICAgICAgIHJlcyA9IFItTAogICAgICAgICAgICAgbGFzdFtjaGFyXSA9IFIKICAgICAgICAgcmV0dXJuIHJlcw==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
