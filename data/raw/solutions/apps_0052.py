import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("bj1pbnQoaW5wdXQoKSkKYT1zb3J0ZWQoaW50KGlucHV0KCkpIGZvciBfIGluIHJhbmdlKG4pKQpwcmludChzdW0oYVtpXSphWy1pLTFdIGZvciBpIGluIHJhbmdlKG4pKSUxMDAwNyk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
