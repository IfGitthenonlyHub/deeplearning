import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgY291bnRWb3dlbFBlcm11dGF0aW9uKHNlbGYsIG46IGludCkgLT4gaW50OgogICAgICAgIGEsZSxpLG8sdSA9IDEsMSwxLDEsMQogICAgICAgIGZvciBfIGluIHJhbmdlKG4tMSk6CiAgICAgICAgICAgIGEsZSxpLG8sdSA9IGUsIGEraSwgYStlK28rdSwgaSt1LCBhCiAgICAgICAgcmV0dXJuKGErZStpK28rdSklKDEwKio5Kzcp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
