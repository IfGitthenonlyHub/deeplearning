import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIHVuaXF1ZVBhdGhzKHNlbGYsIG0sIG4pOgogICAgICAgICAiIiIKICAgICAgICAgOnR5cGUgbTogaW50CiAgICAgICAgIDp0eXBlIG46IGludAogICAgICAgICA6cnR5cGU6IGludAogICAgICAgICAiIiIKICAgICAgICAgYWxsPW0tMStuLTEKICAgICAgICAgeD0xCiAgICAgICAgIHk9MQogICAgICAgICBmb3IgaSBpbiByYW5nZShtLTEpOgogICAgICAgICAgICAgeD14KihhbGwtaSkKICAgICAgICAgICAgIHk9eSooaSsxKQogICAgICAgICByZXR1cm4geC8veQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
