import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgZGVmIG1heGltdW1TdW0oc2VsZiwgYXJyOiBMaXN0W2ludF0pIC0+IGludDoKICAgIG1heDAsIG1heDEsIHJlc3VsdCA9IGFyclswXSwgYXJyWzBdLCBhcnJbMF0KICAgIGZvciBuIGluIGFyclsxOl06CiAgICAgIG1heDEgPSBtYXgobWF4MSArIG4sIG1heDAsIG4pCiAgICAgIG1heDAgPSBtYXgobWF4MCArIG4sIG4pCiAgICAgIHJlc3VsdCA9IG1heChyZXN1bHQsIG1heDEpCiAgICByZXR1cm4gcmVzdWx0").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
