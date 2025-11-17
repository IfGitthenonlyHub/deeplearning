import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWluTWFsd2FyZVNwcmVhZChzZWxmLCBncmFwaCwgaW5pdGlhbCk6CiAgICAgICAgZGVmIGRmcyhpKToKICAgICAgICAgICAgbm9kZXMuYWRkKGkpCiAgICAgICAgICAgIGZvciBqIGluIHJhbmdlKGxlbihncmFwaFtpXSkpOgogICAgICAgICAgICAgICAgaWYgZ3JhcGhbaV1bal0gYW5kIGogbm90IGluIG5vZGVzOgogICAgICAgICAgICAgICAgICAgIGRmcyhqKQogICAgICAgIHJhbmssIGluaXRpYWwgPSBjb2xsZWN0aW9ucy5kZWZhdWx0ZGljdChsaXN0KSwgc2V0KGluaXRpYWwpCiAgICAgICAgZm9yIG5vZGUgaW4gc29ydGVkKGluaXRpYWwpOgogICAgICAgICAgICBub2RlcyA9IHNldCgpCiAgICAgICAgICAgIGRmcyhub2RlKQogICAgICAgICAgICBpZiBub2RlcyAmIGluaXRpYWwgPT0ge25vZGV9OgogICAgICAgICAgICAgICAgcmFua1tsZW4obm9kZXMpXS5hcHBlbmQobm9kZSkKICAgICAgICByZXR1cm4gcmFua1ttYXgocmFuayldWzBdIGlmIHJhbmsgZWxzZSBtaW4oaW5pdGlhbCk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
