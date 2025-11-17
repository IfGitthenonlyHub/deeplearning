import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGNhbk1lYXN1cmVXYXRlcihzZWxmLCB4LCB5LCB6KToKICAgICAgICAgIiIiCiAgICAgICAgIDp0eXBlIHg6IGludAogICAgICAgICA6dHlwZSB5OiBpbnQKICAgICAgICAgOnR5cGUgejogaW50CiAgICAgICAgIDpydHlwZTogYm9vbAogICAgICAgICAiIiIKICAgICAgICAgaWYgeCArIHkgPCB6OiByZXR1cm4gRmFsc2UKICAgICAgICAgZ2NkID0gbGFtYmRhIGEsIGI6IChnY2QoYiwgYSAlIGIpIGlmIGEgJSBiIGVsc2UgYikKICAgICAgICAgcmV0dXJuIHogPT0gMCBvciB6ICUgZ2NkKHgsIHkpID09IDA=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
