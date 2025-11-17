import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbnVtT2ZTdWJhcnJheXMoc2VsZiwgYTogTGlzdFtpbnRdLCBrOiBpbnQsIHRocmVzaG9sZDogaW50KSAtPiBpbnQ6CiAgICAgICAgcHJlZml4U3VtID0gWzBdCiAgICAgICAgZm9yIGkgaW4gYToKICAgICAgICAgICAgcHJlZml4U3VtLmFwcGVuZChpICsgcHJlZml4U3VtWy0xXSkKICAgICAgICByZXR1cm4gc3VtKHByZWZpeFN1bVtpICsga10gLSBwcmVmaXhTdW1baV0gPj0gayAqIHRocmVzaG9sZCBmb3IgaSBpbiByYW5nZShsZW4oYSkgLSBrICsgMSkp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
