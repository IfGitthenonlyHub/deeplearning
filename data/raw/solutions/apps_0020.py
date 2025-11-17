import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Zm9yIF8gaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKCW4sbT1tYXAoaW50LGlucHV0KCkuc3BsaXQoKSkKCWxtPWhtPW0KCXB0PTAKCWFucz0iWUVTIgoJZm9yIGkgaW4gcmFuZ2Uobik6CgkJdCxsLGg9bWFwKGludCxpbnB1dCgpLnNwbGl0KCkpCgkJbG0tPSh0LXB0KQoJCWhtKz0odC1wdCkKCQlwdD10CgkJaG09bWluKGgsaG0pCgkJbG09bWF4KGwsbG0pCgkJaWYgaG08bG06CgkJCWFucz0iTk8iCglwcmludChhbnMp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
