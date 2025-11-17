import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWluQWRkVG9NYWtlVmFsaWQoc2VsZiwgUzogc3RyKSAtPiBpbnQ6CiAgICAgICAgcmVzLG5lZWQ9MCwwCiAgICAgICAgZm9yIGkgaW4gcmFuZ2UobGVuKFMpKToKICAgICAgICAgICAgaWYgU1tpXT09JygnOgogICAgICAgICAgICAgICAgbmVlZCs9MQogICAgICAgICAgICBpZiBTW2ldPT0nKSc6CiAgICAgICAgICAgICAgICBuZWVkLT0xCiAgICAgICAgICAgICAgICBpZiBuZWVkPT0tMToKICAgICAgICAgICAgICAgICAgICBuZWVkPTAKICAgICAgICAgICAgICAgICAgICByZXMrPTEKICAgICAgICByZXR1cm4gcmVzK25lZWQ=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
