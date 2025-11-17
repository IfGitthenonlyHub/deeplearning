import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbGFyZ2VzdE92ZXJsYXAoc2VsZiwgaW1nMTogTGlzdFtMaXN0W2ludF1dLCBpbWcyOiBMaXN0W0xpc3RbaW50XV0pIC0+IGludDoKICAgICAgICBBID0gWyhpLCBqKSBmb3IgaSwgcm93IGluIGVudW1lcmF0ZShpbWcxKSBmb3IgaiwgaXRlbSBpbiBlbnVtZXJhdGUocm93KSBpZiBpdGVtXQogICAgICAgIEIgPSBbKGksIGopIGZvciBpLCByb3cgaW4gZW51bWVyYXRlKGltZzIpIGZvciBqLCBpdGVtIGluIGVudW1lcmF0ZShyb3cpIGlmIGl0ZW1dCiAgICAgICAgY291bnQgPSBjb2xsZWN0aW9ucy5Db3VudGVyKChheC1ieCwgYXktYnkpIGZvciBheCwgYXkgaW4gQSBmb3IgYngsIGJ5IGluIEIpCiAgICAgICAgcmV0dXJuIG1heChsaXN0KGNvdW50LnZhbHVlcygpKSBvciBbMF0p").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
