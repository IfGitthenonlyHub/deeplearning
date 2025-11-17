import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIG11bHRpcGx5KHNlbGYsbnVtMSwgbnVtMik6CiAgICAgICAgIGE9WycwJywnMScsJzInLCczJywnNCcsJzUnLCc2JywnNycsJzgnLCc5J10KICAgICAgICAgej0wCiAgICAgICAgIHg9MAogICAgICAgICBmb3IgaSxlbGVtZW50IGluIGVudW1lcmF0ZShudW0xKToKICAgICAgICAgICAgIGZvciBqIGluIHJhbmdlKDEwKToKICAgICAgICAgICAgICAgICBpZiBlbGVtZW50PT1hW2pdOgogICAgICAgICAgICAgICAgICAgICB6Kz1qKigxMCoqKGxlbihudW0xKS1pLTEpKQogICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgZm9yIGMsYiBpbiBlbnVtZXJhdGUobnVtMik6CiAgICAgICAgICAgICBmb3IgayBpbiByYW5nZSgxMCk6CiAgICAgICAgICAgICAgICAgaWYgYj09YVtrXToKICAgICAgICAgICAgICAgICAgICAgeCs9ayooMTAqKihsZW4obnVtMiktYy0xKSkKICAgICAgICAgbXVsPXoqeAogICAgICAgICByZXR1cm4oJycuam9pbignJWQnJW11bCkp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
