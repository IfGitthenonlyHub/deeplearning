import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWluY29zdFRpY2tldHMoc2VsZiwgZGF5czogTGlzdFtpbnRdLCBjb3N0czogTGlzdFtpbnRdKSAtPiBpbnQ6CiAgICAgICAgZHAgPSBbMF0gKiAoZGF5c1stMV0gKyAxKQogICAgICAgIGZvciBkYXkgaW4gcmFuZ2UoMCwgZGF5c1stMV0gKyAxKToKICAgICAgICAgICAgaWYgZGF5IG5vdCBpbiBkYXlzOgogICAgICAgICAgICAgICAgZHBbZGF5XSA9IGRwW21heCgwLCBkYXkgLSAxKV0KICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgIGRwW2RheV0gPSBtaW4oZHBbbWF4KDAsIGRheSAtIDEpXSArIGNvc3RzWzBdLCBkcFttYXgoMCwgZGF5IC0gNyldICsgY29zdHNbMV0sIGRwW21heCgwLCBkYXkgLSAzMCldICsgY29zdHNbMl0pCgogICAgICAgIHJldHVybiBkcFstMV0=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
