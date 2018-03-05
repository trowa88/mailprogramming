"""
정수 n이 주어지면, n개의 여는 괄호 "("와 n개의 닫는 괄호 ")"로 만들 수 있는 괄호 조합을 모두 구하시오. (시간 복잡도 제한 없습니다).

예제)
Input: 1
Output: ["()"]

Input: 2
Output: ["(())", "()()"]

Input: 3
Output: ["((()))", "(()())", "()(())", "(())()", "()()()"]

풀이
List<String> parenthesisPairs(int n) {
  List<String> ans = new ArrayList();
  recurse(ans, "", 0, 0, n);
  return ans;
}

void recurse(List<String> ans, String cur, int open, int close, int n){
  if (str.length() == n * 2) {
    ans.add(cur);
    return;
  }
  if (open < n) {
    recurse(ans, cur + "(", open + 1, close, n);
  }
  if (close < open) {
    recurse(ans, cur + ")", open, close + 1, n);
  }
}
"""


def parenthesis_pairs(n):
    result = []
    recurse(result, '', 0, 0, n)
    return result


def recurse(ans, cur, open_paren, close_paren, n):
    if len(cur) == n * 2:
        ans.append(cur)
        return
    if open_paren < n:
        recurse(ans, cur + '(', open_paren + 1, close_paren, n)
    if close_paren < open_paren:
        recurse(ans, cur + ')', open_paren, close_paren + 1, n)


if __name__ == '__main__':
    print(parenthesis_pairs(3))
