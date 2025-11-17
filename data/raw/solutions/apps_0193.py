import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWluU2V0U2l6ZShzZWxmLCBhcnI6IExpc3RbaW50XSkgLT4gaW50OgogICAgICAgIGMgPSBDb3VudGVyKGFycikKICAgICAgICBsID0gbGVuKGFycikKICAgICAgICB0dXAgPSBjLm1vc3RfY29tbW9uKGxlbihjKSkKICAgICAgICBpID0gMAogICAgICAgIHdoaWxlIGwgPiBsZW4oYXJyKS8yOgogICAgICAgICAgICBsIC09IHR1cFtpXVsxXQogICAgICAgICAgICBpICs9IDEKICAgICAgICAgICAgCiAgICAgICAgcmV0dXJuIGk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
