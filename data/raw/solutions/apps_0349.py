import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGRlbGV0ZUFuZEVhcm4oc2VsZiwgbnVtcyk6CiAgICAgICAgICIiIgogICAgICAgICA6dHlwZSBudW1zOiBMaXN0W2ludF0KICAgICAgICAgOnJ0eXBlOiBpbnQKICAgICAgICAgIiIiCiAgICAgICAgIGlmIGxlbihudW1zKSA9PSAwOiByZXR1cm4gMAogICAgICAgICB1cHBlciA9IG1heChudW1zKQogICAgICAgICBvcmRlcmVkID0gWzBdKih1cHBlcisxKQogICAgICAgICBmb3IgaSBpbiBudW1zOiBvcmRlcmVkW2ldKz1pCiAgICAgICAgICAgICAKICAgICAgICAgYW5zID0gWzBdKih1cHBlcisxKQogICAgICAgICBhbnNbMV0gPSBvcmRlcmVkWzFdICAgIAogICAgICAgICBmb3IgaSBpbiByYW5nZSAoMix1cHBlcisxKToKICAgICAgICAgICAgIGFuc1tpXSA9IG1heChhbnNbaS0xXSxhbnNbaS0yXStvcmRlcmVkW2ldKQogICAgICAgICAKICAgICAgICAgcmV0dXJuIGFuc1t1cHBlcl0=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
