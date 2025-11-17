import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWluRGlmZmljdWx0eShzZWxmLCBqb2JEaWZmaWN1bHR5OiBMaXN0W2ludF0sIGQ6IGludCkgLT4gaW50OgogICAgICAgIE4gPSBsZW4oam9iRGlmZmljdWx0eSkKICAgICAgICBpZiBkID4gTjogcmV0dXJuIC0xCiAgICAgICAgbWVtbyA9IFtbZmxvYXQoJ2luZicpXSAqIChkICsgMSkgZm9yIF8gaW4gcmFuZ2UoTiArIDEpXQogICAgICAgIG1lbW9bMF1bMF0gPSAwCiAgICAgICAgZm9yIGkgaW4gcmFuZ2UoMSwgTiArIDEpOgogICAgICAgICAgICBmb3IgayBpbiByYW5nZSgxLCBtaW4oaSwgZCkgKyAxKToKICAgICAgICAgICAgICAgIG1lbW9baV1ba10gPSBtaW4obWVtb1tqXVtrIC0gMV0gKyBtYXgoam9iRGlmZmljdWx0eVtqOmldKSBmb3IgaiBpbiByYW5nZShpIC0gMSwgLTEsIC0xKSkKICAgICAgICByZXR1cm4gbWVtb1tOXVtkXQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
