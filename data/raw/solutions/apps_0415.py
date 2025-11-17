import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWluU3dhcChzZWxmLCBBOiBMaXN0W2ludF0sIEI6IExpc3RbaW50XSkgLT4gaW50OgogICAgICAgIAogICAgICAgIG5vLCB5ZXMsIG4gPSAwLCAxLCBsZW4oQSkKICAgICAgICBmb3IgaSBpbiByYW5nZSgxLCBuKToKICAgICAgICAgICAgbm9fdSwgeWVzX3UgPSBuLCBuCiAgICAgICAgICAgIGlmIEFbaS0xXSA8IEFbaV0gYW5kIEJbaS0xXSA8IEJbaV06CiAgICAgICAgICAgICAgICBub191LCB5ZXNfdSA9IG5vLCB5ZXMgKyAxCiAgICAgICAgICAgIGlmIEFbaS0xXSA8IEJbaV0gYW5kIEJbaS0xXSA8IEFbaV06CiAgICAgICAgICAgICAgICBub191ID0gbWluKG5vX3UsIHllcykKICAgICAgICAgICAgICAgIHllc191ID0gbWluKHllc191LCBubysxKSAgCiAgICAgICAgICAgIAogICAgICAgICAgICBubywgeWVzID0gbm9fdSwgeWVzX3UKICAgICAgICByZXR1cm4gbWluKG5vLCB5ZXMp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
