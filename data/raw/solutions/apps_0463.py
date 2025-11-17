import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWF4VmFsdWVBZnRlclJldmVyc2Uoc2VsZiwgbnVtczogTGlzdFtpbnRdKSAtPiBpbnQ6CiAgICAgICAgcmV0dXJuIHN1bShhYnMoYS1iKSBmb3IgYSxiIGluIHppcChudW1zLG51bXNbMTpdKSkgKyBtYXgobWF4KGFicyhudW1zWzBdLWIpLWFicyhhLWIpIGZvciBhLGIgaW4gemlwKG51bXMsbnVtc1sxOl0pKSxtYXgoYWJzKG51bXNbLTFdLWEpLWFicyhhLWIpIGZvciBhLGIgaW4gemlwKG51bXMsbnVtc1sxOl0pKSwyKihtYXgobWluKGEsYikgZm9yIGEsYiBpbiB6aXAobnVtcyxudW1zWzE6XSkpLW1pbihtYXgoYSxiKSBmb3IgYSxiIGluIHppcChudW1zLG51bXNbMTpdKSkpKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
