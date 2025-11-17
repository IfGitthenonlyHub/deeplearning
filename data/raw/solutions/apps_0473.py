import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgY291bnRUcmlwbGV0cyhzZWxmLCBhcnI6IExpc3RbaW50XSkgLT4gaW50OgogICAgICAgIGQgPSBkZWZhdWx0ZGljdChzZXQpCiAgICAgICAgcyA9IDAKICAgICAgICBkWzBdLmFkZCgtMSkKICAgICAgICBmb3IgaSx4IGluIGVudW1lcmF0ZShhcnIpOgogICAgICAgICAgICBzIF49IHgKICAgICAgICAgICAgZFtzXS5hZGQoaSkKCiAgICAgICAgcmV0dXJuIHN1bShbYWJzKGEtYiktMSBmb3IgayBpbiBkIGZvciBhLGIgaW4gY29tYmluYXRpb25zKGRba10sMildKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
