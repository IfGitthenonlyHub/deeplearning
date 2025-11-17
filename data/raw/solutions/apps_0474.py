import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWF4U2NvcmVXb3JkcyhzZWxmLCB3b3JkczogTGlzdFtzdHJdLCBsZXR0ZXJzOiBMaXN0W3N0cl0sIHNjb3JlOiBMaXN0W2ludF0pIC0+IGludDoKICAgICAgICAjIFRpbWUgTygyXk4pCiAgICAgICAgIyBTcGFjZSBPKDEpCiAgICAgICAgCiAgICAgICAgZGVmIHNvbHZlKGlkeCwgY291bnRlcik6CiAgICAgICAgICAgIGlmIGlkeCA9PSBsZW4od29yZHMpOgogICAgICAgICAgICAgICAgcmV0dXJuIDAKCiAgICAgICAgICAgIHdjID0gY29sbGVjdGlvbnMuQ291bnRlcih3b3Jkc1tpZHhdKQogICAgICAgICAgICBpZiBhbGwoY291bnRlcltrZXldID49IHdjW2tleV0gZm9yIGtleSBpbiB3Yyk6CiAgICAgICAgICAgICAgICBhbnMgPSBtYXgoc3VtKHNjb3JlW29yZChjKS1vcmQoJ2EnKV0gZm9yIGMgaW4gd29yZHNbaWR4XSkgKyBzb2x2ZShpZHgrMSwgY291bnRlci13YyksIHNvbHZlKGlkeCsxLCBjb3VudGVyKSkKICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgIGFucyA9IHNvbHZlKGlkeCsxLCBjb3VudGVyKSAKICAgICAgICAgICAgICAgIAogICAgICAgICAgICByZXR1cm4gYW5zCiAgICAgICAgCiAgICAgICAgcmV0dXJuIHNvbHZlKDAsIGNvbGxlY3Rpb25zLkNvdW50ZXIobGV0dGVycykp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
