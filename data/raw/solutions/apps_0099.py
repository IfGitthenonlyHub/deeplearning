import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Zm9yIG50IGluIHJhbmdlKGludChpbnB1dCgpKSk6CgluID0gaW50KGlucHV0KCkpCglzID0gaW5wdXQoKQoJaWYgIjEiIG5vdCBpbiBzOgoJCXByaW50IChzKQoJCWNvbnRpbnVlCglhbnMgPSAiIgoJZm9yIGkgaW4gcmFuZ2Uobik6CgkJaWYgc1tpXT09IjAiOgoJCQlhbnMgKz0gc1tpXQoJCWVsc2U6CgkJCWluZCA9IGkKCQkJYnJlYWsKCXRlbXAgPSAiIgoJZm9yIGkgaW4gcmFuZ2Uobi0xLGluZC0xLC0xKToKCQlpZiBzW2ldPT0iMCI6CgkJCWFucyArPSAiMCIKCQkJYnJlYWsKCQllbHNlOgoJCQl0ZW1wICs9ICIxIgoJYW5zICs9IHRlbXAKCXByaW50IChhbnMp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
