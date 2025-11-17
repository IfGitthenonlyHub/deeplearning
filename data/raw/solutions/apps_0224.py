import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIG51bURpc3RpbmN0KHNlbGYsIHMsIHQpOgogICAgICAgICAiIiIKICAgICAgICAgOnR5cGUgczogc3RyCiAgICAgICAgIDp0eXBlIHQ6IHN0cgogICAgICAgICA6cnR5cGU6IGludAogICAgICAgICAiIiIKICAgICAgICAgcmVzdWx0ID0gKGxlbih0KSArIDEpICogWzBdCiAgICAgICAgIHJlc3VsdFswXSA9IDEKICAgICAgICAgZm9yIGogaW4gcmFuZ2UobGVuKHMpKToKICAgICAgICAgICAgIGZvciBpIGluIHJldmVyc2VkKHJhbmdlKGxlbih0KSkpOgogICAgICAgICAgICAgICAgIGlmIHNbal0gPT0gdFtpXToKICAgICAgICAgICAgICAgICAgICAgcmVzdWx0W2kgKyAxXSArPSByZXN1bHRbaV0KICAgICAgICAgcmV0dXJuIHJlc3VsdFstMV0=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
