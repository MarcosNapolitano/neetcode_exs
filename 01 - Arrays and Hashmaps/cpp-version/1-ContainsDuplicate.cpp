#include <iostream>
#include <unordered_set>
#include <vector>
#include <map>

using namespace std;

int main(){

    class Solution {

        std::map<int, int> map;
        std::unordered_set<int> set;

        public:
        bool hasDuplicate(vector<int>& nums) {
            for (int i : nums) {

                if(map.find(i) != map.end()) return false;

                map[i] = 1;
            }

            return true;
        }

        bool containsDuplicate(vector<int>& nums){

            for(int i : nums) {

               if (set.count(i)) return true;

               set.insert(i);

            };

            return false;
        };

    };

    Solution a;
    vector<int> nums = { 1, 2, 3, 5 };

    cout << a.hasDuplicate(nums) << endl;
    cout << a.containsDuplicate(nums);

    return 0;

};
