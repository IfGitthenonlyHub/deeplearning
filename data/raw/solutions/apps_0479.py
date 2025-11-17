import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGxlYXN0QnJpY2tzKHNlbGYsIHdhbGwpOgogICAgICAgICAiIiIKICAgICAgICAgOnR5cGUgd2FsbDogTGlzdFtMaXN0W2ludF1dCiAgICAgICAgIDpydHlwZTogaW50CiAgICAgICAgICIiIgogICAgICAgICBkID0ge30KICAgICAgICAgZm9yIGkgaW4gd2FsbDoKICAgICAgICAgICAgIHN1bWEgPSAwCiAgICAgICAgICAgICBmb3IgaiBpbiByYW5nZShsZW4oaSktMSk6CiAgICAgICAgICAgICAgICAgc3VtYSArPSBpW2pdCiAgICAgICAgICAgICAgICAgaWYgc3VtYSBpbiBkOgogICAgICAgICAgICAgICAgICAgICBkW3N1bWFdICs9IDEKICAgICAgICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgICAgICBkW3N1bWFdID0gMQogICAgICAgICBpZiBsZW4oZCkgPT0gMDoKICAgICAgICAgICAgIHJldHVybiBsZW4od2FsbCkKICAgICAgICAgcmV0dXJuIGxlbih3YWxsKSAtIG1heChkLnZhbHVlcygpKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
