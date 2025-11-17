import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZnJvbSAgbWF0aCBpbXBvcnQgZ2NkCgpmb3IgXyBpbiByYW5nZShpbnQoaW5wdXQoKSkpOgogICAgbSxkLHc9bGlzdChtYXAoaW50LGlucHV0KCkuc3BsaXQoKSkpCiAgICBNPW1pbihtLGQpCiAgICBXPXcvL2djZCh3LGQtMSkKICAgIFE9TS8vVwogICAgUj1NJVcKICAgIGFucz0oVy1SKSooUSooUS0xKS8vMikrUiooUSooUSsxKS8vMikKICAgIHByaW50KGFucyk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
