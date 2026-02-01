#include <iostream>
#include <vector>
#include <unordered_map>

// Two Sum: return indices of two numbers that add up to target.
// Time complexity: O(n) using a hash map.
std::vector<int> twoSum(const std::vector<int>& nums, int target) {
    std::unordered_map<int, int> index_map; // value -> index
    for (int i = 0; i < (int)nums.size(); ++i) {
        int complement = target - nums[i];
        auto it = index_map.find(complement);
        if (it != index_map.end()) {
            // Found the pair: indices are (it->second, i)
            return {it->second, i};
        }
        // Store value -> index for future complements
        index_map[nums[i]] = i;
    }
    return {}; // no pair found
}

int main() {
    std::vector<int> nums = {2, 7, 11, 15};
    int target = 9;

    auto result = twoSum(nums, target);
    if (!result.empty()) {
        std::cout << "Indices: " << result[0] << ", " << result[1] << "\n";
        std::cout << "Values: " << nums[result[0]] << " + " << nums[result[1]] << " = " << target << "\n";
    } else {
        std::cout << "No two numbers add up to the target." << std::endl;
    }

    return 0;
}
