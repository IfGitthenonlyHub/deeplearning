import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgcHVzaERvbWlub2VzKHNlbGYsIGRvbWlub2VzOiBzdHIpIC0+IHN0cjoKICAgICAgICBuID0gbGVuKGRvbWlub2VzKQogICAgICAgIGZvcmNlID0gWzBdICogbgogICAgICAgIGYgPSAwCiAgICAgICAgZm9yIGkgaW4gcmFuZ2Uobik6CiAgICAgICAgICAgIGlmIGRvbWlub2VzW2ldID09ICdSJzoKICAgICAgICAgICAgICAgIGYgPSBuCiAgICAgICAgICAgIGVsaWYgZG9taW5vZXNbaV0gPT0gJ0wnOgogICAgICAgICAgICAgICAgZiA9IDAKICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgIGYgPSBtYXgoZi0xLCAwKQogICAgICAgICAgICBmb3JjZVtpXSArPSBmCiAgICAgICAgZm9yIGkgaW4gcmFuZ2Uobi0xLCAtMSwgLTEpOgogICAgICAgICAgICBpZiBkb21pbm9lc1tpXSA9PSAnTCc6CiAgICAgICAgICAgICAgICBmID0gbgogICAgICAgICAgICBlbGlmIGRvbWlub2VzW2ldID09ICdSJzoKICAgICAgICAgICAgICAgIGYgPSAwCiAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICBmID0gbWF4KGYtMSwgMCkKICAgICAgICAgICAgZm9yY2VbaV0gLT0gZgogICAgICAgIHJldHVybiAnJy5qb2luKCcuJyBpZiBmPT0wIGVsc2UgJ1InIGlmIGYgPiAwIGVsc2UgJ0wnIGZvciBmIGluIGZvcmNlKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
