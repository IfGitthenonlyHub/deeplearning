import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("aW5wdXQ9X19pbXBvcnRfXygnc3lzJykuc3RkaW4ucmVhZGxpbmUKZm9yIF8gaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKCW4sVD1tYXAoaW50LGlucHV0KCkuc3BsaXQoKSkKCXM9bGlzdChtYXAoaW50LGlucHV0KCkuc3BsaXQoKSkpCglhbnM9WzBdKm4KCWc9e30gIyBsYXN0IGluZCB3aXRoIHN1bSB4Cglmb3IgaSBpbiByYW5nZShuKToKCQlpZiBULXNbaV0gaW4gZzoKCQkJYW5zW2ldPTEtYW5zW2dbVC1zW2ldXV0KCQlnW3NbaV1dPWkKCXByaW50KCphbnMp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
