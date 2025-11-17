import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("IyBjb29rIHlvdXIgZGlzaCBoZXJlCnN0ID0gc3RyKGlucHV0KCkpCgpkZWYgY2hlY2twYWwoaSxqLGssbCk6CiAKIGE9aQogYj1sCiB3aGlsZShhPGIpOgogIGlmIHN0W2FdICE9IHN0W2JdOgogICAKICAgcmV0dXJuIC0xCiAgCiAgaWYoYT09aik6CiAgIGEgPSBrLTEKICBpZihiPT1rKToKICAgYiA9IGorMQoKICBhKz0xCiAgYi09MSAKICMgcHJpbnQoaSxqLGssbCkKICMgcHJpbnQoInllcyIpCiByZXR1cm4gMQoKbCA9IGxlbihzdCkKY291bnQgPSAwCmZvciBpIGluIHJhbmdlKGwpOgogZm9yIGogaW4gcmFuZ2UoaSxsKToKICBmb3IgayBpbiByYW5nZShqKzEsbCk6CiAgIGZvciBtIGluIHJhbmdlKGssbCk6CiAgICBpZiBjaGVja3BhbChpLGosayxtKSA9PSAxOiAKICAgICBjb3VudCArPSAxCiAgIApwcmludChjb3VudCk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
