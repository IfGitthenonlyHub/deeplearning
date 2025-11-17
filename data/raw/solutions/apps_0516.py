import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Zm9yIGkgaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKICAgIG4saz1tYXAoaW50LGlucHV0KCkuc3BsaXQoKSkKICAgIHMsYSxsID0gMCwwLGxpc3QobWFwKGludCxpbnB1dCgpLnNwbGl0KCkpKQogICAgbDI9MipsCiAgICBmb3IgaSBpbiByYW5nZShuLTEpOgogICAgICAgIGZvciBqIGluIHJhbmdlKGkrMSxuKToKICAgICAgICAgICAgaWYobFtpXT5sW2pdKTphKz0xCiAgICBmb3IgaSBpbiByYW5nZShuKToKICAgICAgICBmb3IgaiBpbiByYW5nZShuLDIqbik6CiAgICAgICAgICAgIGlmKGwyW2ldPmwyW2pdKTpzKz0xCiAgICBwcmludCgoKGsqKGstMSkpLy8yKSpzK2sqYSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
