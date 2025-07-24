#include <iostream>
#include <unordered_map>

using namespace std;

int main(){

    class Solution {

        std::unordered_map<char, int> map;

        public:
        bool isAnagram(string s, string t) {

            for (char i : s) {

                if(map.find(i) != map.end()){

                    map[i] += 1;
                    continue;

                };;

                map[i] = 1;
            };

            for (char i : t) {

                if(map.find(i) == map.end()) return false;

                map[i] -= 1;
            };

            for (auto& p : map)
                if (p.second > 0) return false;

            return true;
        };
    };
    
    Solution a;
    const string str1 = "ram";
    const string str2 = "mra";

    cout << a.isAnagram(str1, str2)<< endl;
    cout << "testing" << endl;

    return 0;

};

