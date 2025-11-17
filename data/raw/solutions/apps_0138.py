import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgZ2V0TWF4TGVuKHNlbGYsIG51bXM6IExpc3RbaW50XSkgLT4gaW50OgogICAgICAgIGFucyA9IHBvcyA9IG5lZyA9IDAKICAgICAgICBmb3IgeCBpbiBudW1zOiAKICAgICAgICAgICAgaWYgeCA+IDA6IHBvcywgbmVnID0gMSArIHBvcywgMSArIG5lZyBpZiBuZWcgZWxzZSAwCiAgICAgICAgICAgIGVsaWYgeCA8IDA6IHBvcywgbmVnID0gMSArIG5lZyBpZiBuZWcgZWxzZSAwLCAxICsgcG9zCiAgICAgICAgICAgIGVsc2U6IHBvcyA9IG5lZyA9IDAgIyByZXNldCAKICAgICAgICAgICAgYW5zID0gbWF4KGFucywgcG9zKQogICAgICAgIHJldHVybiBhbnM=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
