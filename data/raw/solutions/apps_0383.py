import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgZGZzKHNlbGYsIGksIHZpc2l0ZWQsIGdyYXBoKToKICAgICAgICBpZiBpIGluIHZpc2l0ZWQ6CiAgICAgICAgICAgIHJldHVybgogICAgICAgIHZpc2l0ZWQuYWRkKGkpCiAgICAgICAgZm9yIHgsIGVkZ2UgaW4gZW51bWVyYXRlKGdyYXBoW2ldKToKICAgICAgICAgICAgaWYgZWRnZToKICAgICAgICAgICAgICAgIHNlbGYuZGZzKHgsIHZpc2l0ZWQsIGdyYXBoKQogICAgCiAgICBkZWYgbWluTWFsd2FyZVNwcmVhZChzZWxmLCBncmFwaDogTGlzdFtMaXN0W2ludF1dLCBpbml0aWFsOiBMaXN0W2ludF0pIC0+IGludDoKICAgICAgICBudW1JbmZlY3RlZCA9IGZsb2F0KCdpbmYnKQogICAgICAgIG1pblZhbCA9IE5vbmUKICAgICAgICBpbml0aWFsLnNvcnQoKQogICAgICAgIGZvciBpIGluIGluaXRpYWw6CiAgICAgICAgICAgIHZpc2l0ZWQgPSBzZXQoW2ldKQogICAgICAgICAgICBmb3IgaiBpbiBpbml0aWFsOgogICAgICAgICAgICAgICAgc2VsZi5kZnMoaiwgdmlzaXRlZCwgZ3JhcGgpCiAgICAgICAgICAgIGlmIGxlbih2aXNpdGVkKSA8IG51bUluZmVjdGVkOgogICAgICAgICAgICAgICAgbnVtSW5mZWN0ZWQgPSBsZW4odmlzaXRlZCkKICAgICAgICAgICAgICAgIG1pblZhbCA9IGkKICAgICAgICAKICAgICAgICByZXR1cm4gbWluVmFs").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
