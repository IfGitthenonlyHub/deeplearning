import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGZpbmRNYXhpbXVtWE9SKHNlbGYsIG51bXMpOgogICAgICAgICAiIiIKICAgICAgICAgOnR5cGUgbnVtczogTGlzdFtpbnRdCiAgICAgICAgIDpydHlwZTogaW50CiAgICAgICAgICIiIgogICAgICAgICBhbnMgPSAwCiAgICAgICAgIGZvciBiaXQgaW4gcmFuZ2UoMzEsIC0xLCAtMSkgOgogICAgICAgICAgICAgYW5zID0gKGFucyA8PCAxKSArIDEKICAgICAgICAgICAgIHByZSA9IHNldCgpCiAgICAgICAgICAgICBmb3IgbiBpbiBudW1zIDoKICAgICAgICAgICAgICAgICBwID0gKG4gPj4gYml0KSAmIGFucwogICAgICAgICAgICAgICAgIGlmIHAgaW4gcHJlIDoKICAgICAgICAgICAgICAgICAgICAgYnJlYWsKICAgICAgICAgICAgICAgICBwcmUuYWRkKGFucyAtIHApCiAgICAgICAgICAgICBlbHNlIDoKICAgICAgICAgICAgICAgICBhbnMgLT0gMQogICAgICAgICByZXR1cm4gYW5z").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
