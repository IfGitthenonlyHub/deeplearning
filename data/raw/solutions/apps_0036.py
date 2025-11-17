import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("bj1pbnQoaW5wdXQoKSkKYT1saXN0KG1hcChpbnQsaW5wdXQoKS5zcGxpdCgpKSkgCm09aW50KGlucHV0KCkpIApxPWxpc3QobWFwKGludCxpbnB1dCgpLnNwbGl0KCkpKQoKYj1bXQpmb3IgaSBpbiByYW5nZShuKToKICAgIGIrPVtpKzFdKmFbaV0KIAoKZm9yIGkgaW4gcToKICAgIHByaW50KGJbaS0xXSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
