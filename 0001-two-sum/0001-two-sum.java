class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int[] answer = new int[2];
        int index = 0;
        int length = nums.length;
        
        map.put(nums[0], 0);
        
       for(int i=1; i<length; i++){
           if(map.containsKey(target - nums[i])){
               answer[0] = map.get(target - nums[i]);
               answer[1] = i;
               break;
           }
           else{
               map.put(nums[i], i);
           }
       }
        return answer;
    }
}