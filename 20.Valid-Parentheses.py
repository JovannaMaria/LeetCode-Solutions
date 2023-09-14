class Solution(object):
    def isValid(self, s):
        stack=[0]
        for i in s:
            l=len(stack)
            if stack[l-1]=='[' and i==']':
                stack.pop()
            elif stack[l-1]=='{' and i=='}':
                stack.pop()
            elif stack[l-1]=='(' and i==')':
                stack.pop()
            else:
                stack.append(i)
        if stack[-1]==0:
            return True
        else:
            return False

# or

    def isValid(self, s):
        stack=[]
        map={']':'[','}':'{',')':'('}
        for i in s:
            if i not in map:
                stack.append(i)
                continue
            elif not stack or stack[-1]!=map[i]:
                return False
            stack.pop()
        return not stack

