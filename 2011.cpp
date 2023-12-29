#include <iostream>
#include <vector>

using namespace std;

// Function to solve the problem
class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int answer = 0;
        for(const auto& operation : operations) {
            if (operation == "--X" || operation == "X--" ){
                answer--;
            } else {
                answer++;
            }
        }
        return answer; // Add a semicolon after the return statement
    };
};

int main() {
    // Test the above Function
    Solution solution;
    vector<string> operations = {"--X","X++","X++"};
    cout << solution.finalValueAfterOperations(operations) << endl;
    return 0;
}


