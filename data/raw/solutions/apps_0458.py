import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWluU3ViYXJyYXkoc2VsZiwgbnVtczogTGlzdFtpbnRdLCBwOiBpbnQpIC0+IGludDoKICAgICAgICB0PXN1bShudW1zKSVwCiAgICAgICAgaWYgbm90IHQ6IHJldHVybiAwCiAgICAgICAgZCxzLGE9ezA6LTF9LDAsbGVuKG51bXMpCiAgICAgICAgZm9yIGkseCBpbiBlbnVtZXJhdGUobnVtcyk6CiAgICAgICAgICAgIHM9KHMreCklcAogICAgICAgICAgICB0dD0ocy10KSVwCiAgICAgICAgICAgIGlmIHR0IGluIGQ6IGE9bWluKGEsaS1kW3R0XSkKICAgICAgICAgICAgZFtzXT1pCiAgICAgICAgcmV0dXJuIC0xIGlmIGE9PWxlbihudW1zKSBlbHNlIGE=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
