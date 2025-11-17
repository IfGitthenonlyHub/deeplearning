import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWF4U3VtVHdvTm9PdmVybGFwKHNlbGYsIEE6IExpc3RbaW50XSwgTDogaW50LCBNOiBpbnQpIC0+IGludDoKICAgICAgICBOID0gbGVuKEEpCiAgICAgICAgCiAgICAgICAgcmVzID0gMAogICAgICAgIGZvciBpIGluIHJhbmdlKE4gLSBMICsgMSk6CiAgICAgICAgICAgIGxfc3VtID0gc3VtKEFbaTppICsgTF0pCiAgICAgICAgICAgIGZvciBqIGluIGxpc3QocmFuZ2UoaS1NKzEpKSArIGxpc3QocmFuZ2UoaStMLCBOLU0rMSkpOgogICAgICAgICAgICAgICAgcmVzID0gbWF4KHJlcywgbF9zdW0gKyBzdW0oQVtqOmogKyBNXSkpCiAgICAgICAgcmV0dXJuIHJlcw==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
