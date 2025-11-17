import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("aW5wdXQ9X19pbXBvcnRfXygnc3lzJykuc3RkaW4ucmVhZGxpbmUKZm9yIF8gaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKCW49aW50KGlucHV0KCkpCglzPWxpc3QobWFwKGludCxpbnB1dCgpLnNwbGl0KCkpKQoJZz1bWy0xXWZvciBfIGluIHJhbmdlKG4rMSldCglmb3IgaSBpbiByYW5nZShuKToKCQlnW3NbaV1dLmFwcGVuZChpKQoJaW5mPTEwKioxMAoJYW5zPVstMV0qbgoJbHN0dW51c2VkPW4KCWZvciBpIGluIHJhbmdlKDEsbisxKToKCQlnW2ldLmFwcGVuZChuKQoJCW14PTAKCQlmb3IgaiBpbiByYW5nZSgxLGxlbihnW2ldKSk6CgkJCW14PW1heChteCxnW2ldW2pdLWdbaV1bai0xXS0xKQoJCWZvciBqIGluIHJhbmdlKG14LGxzdHVudXNlZCk6CgkJCWFuc1tqXT1pCgkJbHN0dW51c2VkPW1pbihsc3R1bnVzZWQsbXgpCglwcmludCgqYW5zKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
