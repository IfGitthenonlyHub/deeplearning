import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgIGRlZiBmaW5kTWluTW92ZXMoc2VsZixtYWNoaW5lcyk6CiAgICAgcyA9IHN1bShtYWNoaW5lcykKICAgICBsID0gbGVuKG1hY2hpbmVzKQogICAgIGlmIHMlbDogcmV0dXJuIC0xCiAgICAgYSwgYywgYW5zID0gaW50KHMvbCksIDAsIDAKICAgICBmb3IgeCBpbiBtYWNoaW5lczoKICAgICAgIHkgPSB4IC0gYQogICAgICAgYyArPSB5CiAgICAgICBhbnMgPSBtYXgoYW5zLCB5LCBhYnMoYykpCiAgICAgcmV0dXJuIGFucwogICAgICIiIgogICAgIDp0eXBlIG1hY2hpbmVzOiBMaXN0W2ludF0KICAgICA6cnR5cGU6IGludAogICAgICIiIg==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
