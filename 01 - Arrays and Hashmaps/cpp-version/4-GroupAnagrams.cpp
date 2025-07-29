#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>

using std::string, std::vector, std::unordered_map, std::sort;

int main(){
    class Solution {

        unordered_map<string, vector<string>> map;
        vector<vector<string>> resVector;

        public:
            vector<vector<string>> groupAnagrams(vector<string>& strs) {

                for(string i : strs){
                    string key = i;
                    sort(key.begin(), key.end());

                    if (map.find(i) == map.end())
                        map[i] = {value};
                    else
                        map.find(i)->second.push_back(i);

                };
                for (auto it = map.begin(); it != map.end(); ++it)
                    resVector.push_back(it->second);

                return resVector;
            };
    };
    Solution a;
    vector<string> strs = {"eat","tea","tan","ate","nat","bat"};

    a.groupAnagrams(strs);

    return 0;
};
