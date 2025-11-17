import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWluQ29zdChzZWxmLCBuOiBpbnQsIGN1dHM6IExpc3RbaW50XSkgLT4gaW50OgogICAgICAgIAogICAgICAgIEBscnVfY2FjaGUoTm9uZSkKICAgICAgICBkZWYgZHAobCwgcik6CiAgICAgICAgICAgIGlmIGFueShsIDwgYyA8IHIgZm9yIGMgaW4gY3V0cyk6CiAgICAgICAgICAgICAgICBhbnMgPSByIC0gbCArIG1pbihbZHAobCwgYykgKyBkcChjLCByKSBmb3IgYyBpbiBjdXRzIGlmIGwgPCBjIDwgcl0sIGRlZmF1bHQ9MCkKICAgICAgICAgICAgICAgIHJldHVybiBhbnMKICAgICAgICAgICAgcmV0dXJuIDAKICAgICAgICByZXR1cm4gZHAoMCwgbik=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
