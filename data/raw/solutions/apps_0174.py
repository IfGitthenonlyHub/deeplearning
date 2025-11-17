import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGxlbmd0aExvbmdlc3RQYXRoKHNlbGYsIGlucCk6CiAgICAgICAgICIiIgogICAgICAgICA6dHlwZSBpbnB1dDogc3RyCiAgICAgICAgIDpydHlwZTogaW50CiAgICAgICAgICIiIgogICAgICAgICBtLCBsID0gMCwgey0xOiAtMX0KICAgICAgICAgZm9yIHMgaW4gaW5wLnNwbGl0KCdcbicpOgogICAgICAgICAgICAgZCA9IHMuY291bnQoJ1x0JykKICAgICAgICAgICAgIGxbZF0gPSAxICsgbFtkLTFdICsgbGVuKHMpIC0gZAogICAgICAgICAgICAgaWYgJy4nIGluIHM6IAogICAgICAgICAgICAgICAgIG0gPSBtYXgobSwgbFtkXSkKICAgICAgICAgcmV0dXJuIG0=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
