import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZGVmIGcoIGEgLCBiICk6CiAgICBjdXIgPSAxCiAgICByZXMgPSAwCiAgICB6ZSA9IDAKICAgIHdoaWxlIGN1ciA8PSBiOgogICAgICAgIGlmIGIgJiBjdXI6CiAgICAgICAgICAgIGIgXj0gY3VyCiAgICAgICAgICAgIGlmIGEgJiBiID09IDA6CiAgICAgICAgICAgICAgICByZXMgKz0gKCAxIDw8IHplICkKICAgICAgICBpZiBhICYgY3VyID09IDA6CiAgICAgICAgICAgIHplID0gemUgKyAxCiAgICAgICAgY3VyIDw8PSAxCiAgICByZXR1cm4gcmVzCgpkZWYgZiggYSAsIGIgKToKICAgIHJlcyA9IDAKICAgIGlmIGEgPT0gYjoKICAgICAgICByZXR1cm4gMAogICAgaWYgYSA9PSAwOgogICAgICAgIHJldHVybiAyICogYiAtIDEgKyBmKCAxICwgYiApCiAgICBpZiBhICYgMToKICAgICAgICByZXMgPSByZXMgKyAyICogKCBnKCBhICwgYiApIC0gZyggYSAsIGEgKSApCiAgICAgICAgYSA9IGEgKyAxCiAgICBpZiBiICYgMToKICAgICAgICByZXMgPSByZXMgKyAyICogKCBnKCBiIC0gMSAsIGIgKSAtIGcoIGIgLSAxICwgYSApICkKICAgIHJldHVybiAzICogZiggYSA+PiAxICwgYiA+PiAxICkgKyByZXMKCnQgPSBpbnQoaW5wdXQoKSkKCndoaWxlIHQgPiAwOgogICAgdCA9IHQgLSAxCiAgICBsICwgciA9IG1hcChpbnQgLCBpbnB1dCgpLnNwbGl0KCkpCiAgICBwcmludCggZiggbCAsIHIgKyAxICkgKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
