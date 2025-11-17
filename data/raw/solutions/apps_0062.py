import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Zm9yIF8gaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKICAgIHE9aW5wdXQoKQogICAgYW5zPXFbMF0KICAgIHRlc3Q9WzBdKjI2CiAgICBqPTAKICAgIGMgPSAxCiAgICBmb3IgaSBpbiBxWzE6XToKICAgICAgICBpZiBqPjAgYW5kIGFuc1tqLTFdPT1pOgogICAgICAgICAgICBqLT0xCiAgICAgICAgICAgIGNvbnRpbnVlCiAgICAgICAgaWYgajxsZW4oYW5zKS0xIGFuZCBhbnNbaisxXT09aToKICAgICAgICAgICAgais9MQogICAgICAgICAgICBjb250aW51ZQogICAgICAgIGlmIGo9PTA6CiAgICAgICAgICAgIGFucz1pK2FucwogICAgICAgICAgICBjb250aW51ZQogICAgICAgIGlmIGo9PWxlbihhbnMpLTE6CiAgICAgICAgICAgIGFucys9aQogICAgICAgICAgICBqKz0xCiAgICAgICAgICAgIGNvbnRpbnVlCiAgICAgICAgYz0wCiAgICBmb3IgaSBpbiBhbnM6dGVzdFtvcmQoaSktOTddKz0xCiAgICBmb3IgaSBpbiByYW5nZSgyNik6CiAgICAgICAgaWYgdGVzdFtpXT4xOmM9MAogICAgICAgIGlmIHRlc3RbaV09PTA6YW5zKz1jaHIoaSs5NykKICAgIGlmIGM6CiAgICAgICAgcHJpbnQoJ1lFUycpCiAgICAgICAgcHJpbnQoYW5zKQogICAgZWxzZToKICAgICAgICBwcmludCgnTk8nKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
