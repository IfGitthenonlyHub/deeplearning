import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgdGFsbGVzdEJpbGxib2FyZChzZWxmLCByb2RzOiBMaXN0W2ludF0pIC0+IGludDoKICAgICAgICBkcCA9IHswOiAwfQogICAgICAgIGZvciByIGluIHJvZHM6CiAgICAgICAgICAgIGZvciBkLCB0IGluIGxpc3QoZHAuaXRlbXMoKSk6CiAgICAgICAgICAgICAgICBkcFtyK2RdID0gbWF4KGRwLmdldChyK2QsIDApLCB0KQogICAgICAgICAgICAgICAgZHBbYWJzKHItZCldID0gbWF4KGRwLmdldChhYnMoci1kKSwgMCksIHQgKyBtaW4ociwgZCkpCiAgICAgICAgcmV0dXJuIGRwWzBd").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
