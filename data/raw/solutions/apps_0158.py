import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBAbHJ1X2NhY2hlKE5vbmUpCiAgICBkZWYga1NpbWlsYXJpdHkoc2VsZiwgQTogc3RyLCBCOiBzdHIpIC0+IGludDoKICAgICAgICBpZiBsZW4oQSkgPT0gMDogcmV0dXJuIDAKICAgICAgICBpZiBBWzBdPT1CWzBdOiByZXR1cm4gc2VsZi5rU2ltaWxhcml0eShBWzE6XSxCWzE6XSkKICAgICAgICBhbnMgPSBtYXRoLmluZgogICAgICAgIGZvciBpIGluIHJhbmdlKDEsbGVuKEIpKTogCiAgICAgICAgICAgIGlmIEJbaV09PUFbMF06IGFucyA9IG1pbihhbnMsIDErc2VsZi5rU2ltaWxhcml0eShBWzE6XSxCWzE6aV0rQlswXStCW2krMTpdKSkKICAgICAgICByZXR1cm4gYW5z").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
