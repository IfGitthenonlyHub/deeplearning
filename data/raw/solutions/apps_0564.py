import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Zm9yIF8gaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKIG4saz1saXN0KG1hcChpbnQsaW5wdXQoKS5zcGxpdCgpKSkKIGM9bGlzdChtYXAoaW50LGlucHV0KCkuc3BsaXQoKSkpCiBjb3VudD0xCiBmb3IgaSBpbiByYW5nZShuKToKICBpZiBpKzE8bjoKICAgaWYgY1tpXS1jW2krMV0+PWsgb3IgY1tpKzFdLWNbaV0+PWs6CiAgICBjb250aW51ZQogICBlbHNlOgogICAgY291bnQrPTEKICAgIGNbaV0sY1tpKzFdPWNbaSsxXSxjW2ldCiBwcmludChjb3VudCk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
