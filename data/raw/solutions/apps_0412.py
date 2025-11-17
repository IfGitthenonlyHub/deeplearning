import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbnVtUm9sbHNUb1RhcmdldChzZWxmLCBkLCBmLCB0YXJnZXQpOgogICAgICAgIGRwID0gWzFdICsgWzBdKnRhcmdldAogICAgICAgIGZvciBpIGluIHJhbmdlKGQpOgogICAgICAgICAgICBmb3IgaiBpbiByYW5nZSh0YXJnZXQsIC0xLCAtMSk6CiAgICAgICAgICAgICAgICBkcFtqXSA9IHN1bShbZHBbai1rXSBmb3IgayBpbiByYW5nZSgxLCAxK21pbihmLCBqKSldIG9yIFswXSkKICAgICAgICByZXR1cm4gZHBbdGFyZ2V0XSAlICgxMCoqOSArIDcp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
