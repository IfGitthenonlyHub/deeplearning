import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Zm9yIHEgaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKIG4saz1saXN0KG1hcChpbnQsaW5wdXQoKS5zcGxpdCgpKSkKIHRlc3Q9W10KIHo9W10KIGY9MAogZm9yIGkgaW4gcmFuZ2Uobik6CiAgbD1baW50KGkpIGZvciBpIGluIGlucHV0KCkuc3BsaXQoKV0KICBsPWxbMTpdCiAgei5hcHBlbmQobCkKIGM9WzBdKihrKzEpCiBmb3IgaSBpbiByYW5nZShuKToKICBmb3IgaiBpbiB6W2ldOgogICBjW2pdKz0xCiBmb3IgaSBpbiByYW5nZSgxLGsrMSk6CiAgaWYgY1tpXT09MDoKICAgcHJpbnQoInNhZCIpCiAgIGY9MQogICBicmVhawogaWYgZj09MToKICBjb250aW51ZQogZm9yIGkgaW4gcmFuZ2Uobik6CiAgY250PTAKICBmb3IgaiBpbiB6W2ldOgogICBpZiBjW2pdIT0xOgogICAgY250Kz0xCiAgaWYgY250PT1sZW4oeltpXSk6CiAgIHByaW50KCJzb21lIikKICAgYnJlYWsKIGVsc2U6CiAgcHJpbnQoImFsbCIp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
