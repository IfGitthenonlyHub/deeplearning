import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgIyBAcmV0dXJuIGEgc3RyaW5nCiAgICAgZGVmIGxvbmdlc3RQYWxpbmRyb21lKHNlbGYsIHMpOgogICAgICAgICBpZiBsZW4ocyk9PTA6CiAgICAgICAgIAlyZXR1cm4gMAogICAgICAgICBtYXhMZW49MQogICAgICAgICBzdGFydD0wCiAgICAgICAgIGZvciBpIGluIHJhbmdlKGxlbihzKSk6CiAgICAgICAgIAlpZiBpLW1heExlbiA+PTEgYW5kIHNbaS1tYXhMZW4tMTppKzFdPT1zW2ktbWF4TGVuLTE6aSsxXVs6Oi0xXToKICAgICAgICAgCQlzdGFydD1pLW1heExlbi0xCiAgICAgICAgIAkJbWF4TGVuKz0yCiAgICAgICAgIAkJY29udGludWUKIAogICAgICAgICAJaWYgaS1tYXhMZW4gPj0wIGFuZCBzW2ktbWF4TGVuOmkrMV09PXNbaS1tYXhMZW46aSsxXVs6Oi0xXToKICAgICAgICAgCQlzdGFydD1pLW1heExlbgogICAgICAgICAJCW1heExlbis9MQogICAgICAgICByZXR1cm4gc1tzdGFydDpzdGFydCttYXhMZW5d").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
