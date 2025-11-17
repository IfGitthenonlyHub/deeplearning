import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("dmFscyA9IFswXQpmb3IgXyBpbiByYW5nZSgyMCk6CiAgICB2YWxzICs9IFsxXSArIFsxLXggZm9yIHggaW4gcmV2ZXJzZWQodmFscyldCiAgICAKCmNsYXNzIFNvbHV0aW9uOgogICAgZGVmIGZpbmRLdGhCaXQoc2VsZiwgbjogaW50LCBrOiBpbnQpIC0+IHN0cjoKICAgICAgICByZXR1cm4gc3RyKHZhbHNbay0xXSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
