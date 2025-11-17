import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Zm9yIG4gaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKCWEsYj1tYXAoaW50LGlucHV0KCkuc3BsaXQoKSkKCWMsZD1tYXAoaW50LGlucHV0KCkuc3BsaXQoKSkKCW0xPW1heChhLGIpCgluMT1taW4oYSxiKQoJbTI9bWF4KGMsZCkKCW4yPW1pbihjLGQpCglpZiBtMT09bTIgYW5kIG4xK24yPT1tMToKCQlwcmludCgnWWVzJykKCWVsc2U6CgkJcHJpbnQoJ05vJyk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
