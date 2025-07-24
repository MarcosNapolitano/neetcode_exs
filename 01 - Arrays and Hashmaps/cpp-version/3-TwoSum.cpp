#include <unordered_map>
#include <iostream>
#include <vector>

using namespace std;

int main(){
    class Solution {

        unordered_map<int, int> map;
        vector<int> res;

        public:
            vector<int> twoSum(vector<int>& nums, int target) {

                for (int i = 0; i < nums.size() ; ++i) {
                    int t = target - nums[i];

                    if (map.find(t) != map.end()) {

                        if (map.find(t)->second != i) {
                            res.insert(res.begin(), {map.find(t)->second, i});
                            break;
                        };
                    };

                    map[nums[i]] = i;
                };
                return res;
            };
    };

    Solution a;
    vector<int> nums = {3, 2, 4};

    a.twoSum(nums, 6);

    return 0;
};
