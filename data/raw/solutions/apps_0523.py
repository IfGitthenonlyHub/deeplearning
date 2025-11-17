import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("TU9EPTEwKio5KzcKcD0xMDAwMDAwCmZhY3Q9WzBdKnAgCmZhY3RbMF09MSAKZm9yIGkgaW4gcmFuZ2UoMSxwKToKIGZhY3RbaV09KGZhY3RbaS0xXSppKSVNT0QKZGVmIE1JKGEsTU9EKToKIHJldHVybiBwb3coYSxNT0QtMixNT0QpCmRlZiBuY2sobiwgayk6CiBpZiBuPT1rIG9yIGs9PTA6CiAgcmV0dXJuIDEgCiBpZiBuPGs6CiAgcmV0dXJuIDAgCiByZXR1cm4gZmFjdFtuXSpNSShmYWN0W2tdLE1PRCkqTUkoZmFjdFtuLWtdLE1PRCklTU9ECmZvciBfIGluIHJhbmdlKGludChpbnB1dCgpKSk6CiBuLGs9bWFwKGludCxpbnB1dCgpLnNwbGl0KCkpCiBwcm9kPTEKIGw9W2ludChpKSBmb3IgaSBpbiBpbnB1dCgpLnNwbGl0KCldCiBsLnNvcnQoKQogZm9yIGkgaW4gcmFuZ2Uobik6CiAgdG90PW5jayhuLTEsay0xKQogIHg9bi1pCiAgYXNtaW49bmNrKHgtMSxrLTEpCiAgeT1pKzEKICBhc21heD1uY2soeS0xLGstMSkKICByZXE9dG90LWFzbWluLWFzbWF4CiAgcHJvZCo9cG93KGxbaV0scmVxLE1PRCkKIHByaW50KHByb2QlTU9EKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
