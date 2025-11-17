import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGNoZWNrSW5jbHVzaW9uKHNlbGYsIHMxLCBzMik6CiAgICAgICAgICIiIgogICAgICAgICA6dHlwZSBzMTogc3RyCiAgICAgICAgIDp0eXBlIHMyOiBzdHIKICAgICAgICAgOnJ0eXBlOiBib29sCiAgICAgICAgICIiIgogICAgICAgICBsMSwgbDIgPSBsZW4oczEpLCBsZW4oczIpCiAgICAgICAgIGMxID0gWzBdICogMTI4CiAgICAgICAgIG4gPSAwCiAgICAgICAgIGZvciBpIGluIHMxOgogICAgICAgICAgICAgYyA9IG9yZChpKQogICAgICAgICAgICAgaWYgYzFbY10gPT0gMDogbiArPSAxCiAgICAgICAgICAgICBjMVtjXSArPSAxCiAgICAgICAgIGZvciBpIGluIHJhbmdlKGwyKToKICAgICAgICAgICAgIGogPSBpIC0gbDEKICAgICAgICAgICAgIGlmIGogPj0gMDoKICAgICAgICAgICAgICAgICBjID0gb3JkKHMyW2pdKQogICAgICAgICAgICAgICAgIGlmIG5vdCBjMVtjXTogbiArPSAxCiAgICAgICAgICAgICAgICAgYzFbY10gKz0gMQogICAgICAgICAgICAgYyA9IG9yZChzMltpXSkKICAgICAgICAgICAgIGMxW2NdIC09IDEKICAgICAgICAgICAgIGlmIG5vdCBjMVtjXToKICAgICAgICAgICAgICAgICBuIC09IDEKICAgICAgICAgICAgICAgICBpZiBub3QgbjogcmV0dXJuIFRydWUKICAgICAgICAgcmV0dXJuIEZhbHNl").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
