import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Zm9yIGhhYWdoZmogaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKICAgIG4gPSBpbnQoaW5wdXQoKSkKICAgIGEgPSBsaXN0KG1hcChpbnQsaW5wdXQoKS5zcGxpdCgpKSkKICAgIGRwID0gW1sxMDAwMDAwMDAwMDAwMDBdICogMiBmb3IgaSBpbiByYW5nZShuICsgMildCiAgICBkcFswXVswXSA9IDAKICAgIGZvciBpIGluIHJhbmdlKDEsIG4gKyAxKToKICAgICAgICBkcFtpXVswXSA9IG1pbihkcFtpIC0xXVsxXSwgZHBbaSAtIDJdWzFdKQogICAgICAgIGRwW2ldWzFdID0gbWluKGRwW2kgLTFdWzBdICArIGFbaSAtIDFdLCBkcFtpIC0gMl1bMF0gICsgYVtpIC0gMV0gKyBhW2kgLSAyXSkKICAgIHByaW50KG1pbihkcFtuXSkp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
