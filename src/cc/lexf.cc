#include <iostream>
#include <string>
#include <vector>

using std::string;
using std::vector;
using std::cin;
using std::cout;
using std::endl;


void gen(
  const vector<char>& bs,
  const int n,
  vector<string>* ans,
  string* acc)
{
  if (n == 0) {
    ans->push_back(string(*acc));
    return;
  }

  for (const auto& b : bs) {
    acc->push_back(b);
    gen(bs, n-1, ans, acc);
    acc->pop_back();
  }
}

int main() {
  vector<char> xs;

  string b;
  while (std::getline(cin, b, ' ')) {
    xs.push_back(b[0]);
  }

  int n; cin >> n;

  vector<string> ans;
  string acc;
  gen(xs, n, &ans, &acc);

  for (const auto& s : ans) {
    cout << s << endl;
  }
}
