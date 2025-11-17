import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("dD1pbnQoaW5wdXQoKSkNCmZvciBfIGluIHJhbmdlKHQpOg0KICAgIG49aW50KGlucHV0KCkpDQogICAgZm9yIGkgaW4gcmFuZ2Uobik6DQogICAgICAgIHByaW50KCIgIioobi1pLTEpKycqJyooMippKzEpKQ0KICAgICAgICBwcmludCgiICIqKG4taS0xKSsnKicqKDIqaSsxKSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
