class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pre_sum = 0
        sub_arr = 0

        rem_cnt = defaultdict(int)
        rem_cnt[0] = 1

        for n in nums:
            pre_sum += n
            remain = pre_sum % k

            # if remain in rem_cnt:
            sub_arr += rem_cnt[remain]
            rem_cnt[remain] += 1

        return sub_arr
