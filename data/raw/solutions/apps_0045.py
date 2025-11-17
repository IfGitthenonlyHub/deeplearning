import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Zm9yIF8gaW4gWzBdKmludChpbnB1dCgpKToKIG49aW50KGlucHV0KCkpO289MDtjPTEKIHdoaWxlIG4gPj0gMDoKICBuLT1jKihjKzEpLy8yO28rPTE7Yz0yKmMrMQogcHJpbnQoby0xKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
