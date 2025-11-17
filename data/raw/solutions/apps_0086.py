import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Zm9yIF8gaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKICAgIG4gPSBpbnQoaW5wdXQoKSkKICAgIGwgPSBsaXN0KG1hcChpbnQsaW5wdXQoKS5zcGxpdCgpKSkKICAgIG9uZSA9IGwuY291bnQoMSkKICAgIHplcm8gPSBuLW9uZQogICAgaWYgemVybz49bi8vMjoKICAgICAgICBwcmludCh6ZXJvKQogICAgICAgIHByaW50KCpbMF0qemVybykKICAgIGVsc2U6CiAgICAgICAgb25lIC09IG9uZSUyCiAgICAgICAgcHJpbnQob25lKQogICAgICAgIHByaW50KCpbMV0qb25lKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
