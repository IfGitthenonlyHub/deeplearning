import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgcGFsaW5kcm9tZVBhcnRpdGlvbihzZWxmLCBzOiBzdHIsIGs6IGludCkgLT4gaW50OgogICAgICAgIAogICAgICAgIEBscnVfY2FjaGUoTm9uZSkKICAgICAgICBkZWYgZGZzKHN1YnMsIGspOgogICAgICAgICAgICBpZiBrID09IGxlbihzdWJzKToKICAgICAgICAgICAgICAgIHJldHVybiAwCiAgICAgICAgICAgIGlmIGsgPT0gMToKICAgICAgICAgICAgICAgIHJldHVybiBzdW0oc3Vic1tpXSAhPSBzdWJzWy0xLWldIGZvciBpIGluIHJhbmdlKGxlbihzdWJzKS8vMikpCiAgICAgICAgICAgIHJlcyA9IGZsb2F0KCdpbmYnKQogICAgICAgICAgICBmb3IgaSBpbiByYW5nZSgxLCBsZW4oc3VicykgLSBrICsgMik6CiAgICAgICAgICAgICAgICByZXMgPSBtaW4ocmVzLCBkZnMoc3Vic1s6aV0sIDEpICsgZGZzKHN1YnNbaTpdLCBrIC0gMSkpCiAgICAgICAgICAgIHJldHVybiByZXMKICAgICAgICByZXR1cm4gZGZzKHMsIGsp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
