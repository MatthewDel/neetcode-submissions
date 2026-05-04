class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        print(arr)
        stack = []
        for path in arr:
            if path != '' and path != '.' and path != '..':
                stack.append(path)
            elif stack and path == '..':
                stack.pop()
        return "/" + "/".join(stack)
      
