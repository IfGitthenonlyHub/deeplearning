import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIG1heEFyZWEoc2VsZiwgaGVpZ2h0KToKICAgICAgICAgIiIiCiAgICAgICAgIDp0eXBlIGhlaWdodDogTGlzdFtpbnRdCiAgICAgICAgIDpydHlwZTogaW50CiAgICAgICAgICIiIgogICAgICAgICBpID0gMAogICAgICAgICBqID0gbGVuKGhlaWdodCktMQogICAgICAgICByZXMgPSAwCiAgICAgICAgIHdoaWxlIGkgPCBqOgogICAgICAgICAgICAgcmVzID0gbWF4KHJlcywoai1pKSptaW4oaGVpZ2h0W2ldLCBoZWlnaHRbal0pKQogICAgICAgICAgICAgaWYgaGVpZ2h0W2ldID4gaGVpZ2h0W2pdOgogICAgICAgICAgICAgICAgIGogLT0gMQogICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgICBpICs9IDEKICAgICAgICAgcmV0dXJuIHJlcw==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
