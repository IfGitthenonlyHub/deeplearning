import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbG9uZ2VzdERlY29tcG9zaXRpb24oc2VsZiwgdGV4dDogc3RyKSAtPiBpbnQ6CiAgICAgIGlmIG5vdCB0ZXh0OiByZXR1cm4gMAogICAgICBpLCBqLCByZXN1bHQgPSAwLCBsZW4odGV4dCkgLSAxLCAwCiAgICAgIHdoaWxlIGkgPCBqOgogICAgICAgIGlmIHRleHRbOmkrMV0gPT0gdGV4dFtqOl06CiAgICAgICAgICByZXR1cm4gc2VsZi5sb25nZXN0RGVjb21wb3NpdGlvbih0ZXh0W2krMTogal0pICsgMgogICAgICAgIGVsc2U6CiAgICAgICAgICBpLCBqID0gaSArIDEsIGogLSAxCiAgICAgIHJldHVybiAx").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
