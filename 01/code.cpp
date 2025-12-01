#include <iostream>
#include <string>
#include <vector>
#include <cstdint>
#include <cstdlib>
#include <cmath>

using namespace std;

void part1(vector<string> lines) {
  int64_t dial = 50;
  int64_t count = 0;

  for (int i = 0; i < lines.size(); i++) {
    dial += (lines[i][0] == 'L' ? -1 : 1) * stoi(lines[i].substr(1,lines[i].length()));
    dial %= 100;
    count += (dial == 0);
  }

  cout << count << endl;
}

void part2(vector<string> lines) {
  int64_t dial = 50;
  int64_t count = 0;

  for (int i = 0; i < lines.size(); i++) {
    int64_t turn = dial + (lines[i][0] == 'L' ? -1 : 1) * stoi(lines[i].substr(1,lines[i].length()));
    count += abs(turn) / 100 + (dial > 0 && turn <= 0);
    dial = (turn % 100 + 100) % 100;
  }

  cout << count << endl;
}

void both(vector<string> lines) {
  int64_t dial = 50;
  int64_t count1 = 0;
  int64_t count2 = 0;

  for (int i = 0; i < lines.size(); i++) {
    int64_t turn = dial + (lines[i][0] == 'L' ? -1 : 1) * stoll(lines[i].substr(1,lines[i].length()));
    count2 += llabs(turn) / 100 + (dial > 0 && turn <= 0);
    dial = (turn % 100 + 100) % 100;
    count1 += (dial == 0);
  }

  cout << count1 << endl << count2 << endl;
}

int main() {
  string input_line;
  vector<string> lines;
  while(cin) {
    getline(cin, input_line);
    lines.push_back(input_line);
  }
  lines.pop_back();

  // part1(lines);
  // part2(lines);
  both(lines);

  return 0;
}
