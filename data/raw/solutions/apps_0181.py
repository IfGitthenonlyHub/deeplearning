import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIG1heFByb2ZpdChzZWxmLCBwcmljZXMpOgogICAgICAgICAiIiIKICAgICAgICAgOnR5cGUgcHJpY2VzOiBMaXN0W2ludF0KICAgICAgICAgOnJ0eXBlOiBpbnQKICAgICAgICAgIiIiCiAgICAgICAgIGZyZWU9MAogICAgICAgICBoYXZlLGNvb2w9ZmxvYXQoJy1pbmYnKSxmbG9hdCgnLWluZicpCiAgICAgICAgIGZvciBwIGluIHByaWNlczoKICAgICAgICAgICAgIGZyZWUsaGF2ZSxjb29sPW1heChmcmVlLGNvb2wpLG1heChmcmVlLXAsaGF2ZSksaGF2ZStwCiAgICAgICAgIHJldHVybiBtYXgoZnJlZSxjb29sKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
