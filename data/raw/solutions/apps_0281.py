import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgY2FuQ29udmVydFN0cmluZyhzZWxmLCBzOiBzdHIsIHQ6IHN0ciwgazogaW50KSAtPiBib29sOgogICAgICAgIGlmIGxlbihzKSAhPSBsZW4odCk6CiAgICAgICAgICAgIHJldHVybiBGYWxzZQogICAgICAgIAogICAgICAgIGMgPSBDb3VudGVyKChvcmQoYzIpIC0gb3JkKGMxKSkgJSAyNiBmb3IgYzEsIGMyIGluIHppcChzLCB0KSkKICAgICAgICByZXR1cm4gayA+PSBtYXgoKG0gKyAyNiAqIChjb3VudCAtIDEpIGZvciBtLCBjb3VudCBpbiBsaXN0KGMuaXRlbXMoKSkgaWYgbSksCiAgICAgICAgICAgICAgICAgICAgICAgIGRlZmF1bHQgPSAwKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
