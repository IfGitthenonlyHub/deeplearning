import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("dD1pbnQoaW5wdXQoKSkKZm9yIGkgaW4gcmFuZ2UodCk6CiAgICBuLGs9W2ludChpKSBmb3IgaSBpbiBpbnB1dCgpLnNwbGl0KCldCiAgICBhPVtpbnQoaSkgZm9yIGkgaW4gaW5wdXQoKS5zcGxpdCgpXQogICAgYS5zb3J0KHJldmVyc2U9VHJ1ZSkKICAgIHByaW50KHN1bShhWzprKzFdKSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
