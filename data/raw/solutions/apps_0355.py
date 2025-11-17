import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGZpbmRLdGhOdW1iZXIoc2VsZiwgbiwgayk6CiAgICAgICAgICIiIgogICAgICAgICA6dHlwZSBuOiBpbnQKICAgICAgICAgOnR5cGUgazogaW50CiAgICAgICAgIDpydHlwZTogaW50CiAgICAgICAgICIiIgogICAgICAgICBjdXIgPSAxCiAgICAgICAgIGstPTEKICAgICAgICAgd2hpbGUgaz4wOgogICAgICAgICAgICAgc3RlcHMgPSBzZWxmLmNhbFN0ZXBzKG4sIGN1ciwgY3VyKzEpCiAgICAgICAgICAgICBpZiBzdGVwczw9azoKICAgICAgICAgICAgICAgICBjdXIrPTEKICAgICAgICAgICAgICAgICBrLT1zdGVwcwogICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgICBjdXIqPTEwCiAgICAgICAgICAgICAgICAgay09MQogICAgICAgICAKICAgICAgICAgcmV0dXJuIGN1cgogCiAgICAgZGVmIGNhbFN0ZXBzKHNlbGYsIG4sIG4xLCBuMik6CiAgICAgICAgIHN0ZXBzID0gMAogICAgICAgICB3aGlsZSBuMTw9bjoKICAgICAgICAgICAgIHN0ZXBzICs9IG1pbihuKzEsIG4yKS1uMQogICAgICAgICAgICAgbjEqPTEwCiAgICAgICAgICAgICBuMio9MTAKIAogICAgICAgICByZXR1cm4gc3RlcHM=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
