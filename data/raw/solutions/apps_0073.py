import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZGVmIHNvbHZlKCk6CiAgICBuID0gaW50KGlucHV0KCkpCiAgICBhID0gbGlzdChtYXAoaW50LCBpbnB1dCgpLnNwbGl0KCkpKQogICAgYyA9IFswXSAqIChuICsgMSkKICAgIGRlZiBpbmMoKToKICAgICAgICBmb3IgaSBpbiByYW5nZShuIC0gMSk6CiAgICAgICAgICAgIGlmIGFbaV0gPiBhW2kgKyAxXToKICAgICAgICAgICAgICAgIHJldHVybiBGYWxzZQogICAgICAgIHJldHVybiBUcnVlCiAgICBkZWYgY2FsYygpOgogICAgICAgIGZvciBpIGluIHJhbmdlKG4gKyAxKToKICAgICAgICAgICAgY1tpXSA9IDAKICAgICAgICBmb3IgaSBpbiBhOgogICAgICAgICAgICBjW2ldICs9IDEKICAgICAgICBmb3IgaSBpbiByYW5nZShuICsgMSk6CiAgICAgICAgICAgIGlmIG5vdCBjW2ldOgogICAgICAgICAgICAgICAgcmV0dXJuIGkKICAgICAgICByZXR1cm4gbiArIDEKICAgIGFucyA9IFtdCiAgICB3aGlsZSBub3QgaW5jKCk6CiAgICAgICAgeCA9IGNhbGMoKQogICAgICAgIGlmIHggPj0gbjoKICAgICAgICAgICAgeSA9IDAKICAgICAgICAgICAgd2hpbGUgeSA8IG4gYW5kIGFbeV0gPT0geToKICAgICAgICAgICAgICAgIHkgKz0gMQogICAgICAgICAgICBhW3ldID0geAogICAgICAgICAgICBhbnMuYXBwZW5kKHkpCiAgICAgICAgZWxzZToKICAgICAgICAgICAgYVt4XSA9IHgKICAgICAgICAgICAgYW5zLmFwcGVuZCh4KQogICAgcHJpbnQobGVuKGFucykpCiAgICBwcmludCgqbWFwKGxhbWJkYSB4OiB4ICsgMSwgYW5zKSkKCnQgPSBpbnQoaW5wdXQoKSkKZm9yIF8gaW4gcmFuZ2UodCk6CiAgICBzb2x2ZSgp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
