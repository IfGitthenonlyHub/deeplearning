import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbnVtRW5jbGF2ZXMoc2VsZiwgQTogTGlzdFtMaXN0W2ludF1dKSAtPiBpbnQ6CiAgICAgICAgZGVmIGRmcyhpLCBqKToKICAgICAgICAgICAgaWYgbm90ICgwPD1pPGxlbihBKSBhbmQgMDw9ajxsZW4oQVtpXSkpOgogICAgICAgICAgICAgICAgcmV0dXJuCiAgICAgICAgICAgIGlmIEFbaV1bal09PTA6CiAgICAgICAgICAgICAgICByZXR1cm4KICAgICAgICAgICAgQVtpXVtqXT0wCiAgICAgICAgICAgIGRmcyhpLTEsIGopCiAgICAgICAgICAgIGRmcyhpKzEsIGopCiAgICAgICAgICAgIGRmcyhpLCBqLTEpCiAgICAgICAgICAgIGRmcyhpLCBqKzEpCiAgICAgICAgZm9yIGkgaW4gcmFuZ2UobGVuKEEpKToKICAgICAgICAgICAgZm9yIGogaW4gcmFuZ2UobGVuKEFbaV0pKToKICAgICAgICAgICAgICAgIGlmIEFbaV1bal09PTA6CiAgICAgICAgICAgICAgICAgICAgY29udGludWUKICAgICAgICAgICAgICAgIGlmIChpPT0wIG9yIGo9PTAgb3IgaT09bGVuKEEpLTEgb3Igaj09bGVuKEFbaV0pLTEpOgogICAgICAgICAgICAgICAgICAgIGRmcyhpLCBqKQogICAgICAgIHJlcyA9IHN1bShbc3VtKHJvdykgZm9yIHJvdyBpbiBBXSkKICAgICAgICByZXR1cm4gcmVz").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
