import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Zm9yIHQgaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKIG4gPSBpbnQoaW5wdXQoKSkKIGEgPSBsaXN0KG1hcChpbnQsIGlucHV0KCkuc3BsaXQoKSkpCiBjID0gMgogbSA9IDAKIGZvciBpIGluIHJhbmdlKDIsbik6CiAgaWYgKGFbaV0gPT0gYVtpLTFdK2FbaS0yXSk6CiAgIGMrPTEKICBlbHNlOgogICBtID0gbWF4KGMsbSkKICAgYyA9IDIKIG0gPSBtYXgoYyxtKQogcHJpbnQobSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
