import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIG1heFByb2R1Y3Qoc2VsZiwgbnVtcyk6CiAgICAgICAgICIiIgogICAgICAgICA6dHlwZSBudW1zOiBMaXN0W2ludF0KICAgICAgICAgOnJ0eXBlOiBpbnQKICAgICAgICAgIiIiCiAgICAgICAgIGlmIGxlbihudW1zKSA9PSAxOgogICAgICAgICAgICAgcmV0dXJuIG51bXNbMF0KIAogICAgICAgICBlbHNlOgogICAgICAgICAgICAgcmVzdWx0ID0gYmlnID0gc21hbGwgPSBudW1zWzBdCiAgICAgICAgIGZvciBpIGluIG51bXNbMTpdOgogICAgICAgICAgICAgYmlnLCBzbWFsbCA9IG1heChpLCBpKmJpZywgaSpzbWFsbCksIG1pbiAoaSxpKnNtYWxsLCBpKmJpZykKICAgICAgICAgICAgIHJlc3VsdCA9IG1heChyZXN1bHQsIGJpZykKICAgICAgICAgcmV0dXJuIHJlc3VsdA==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
