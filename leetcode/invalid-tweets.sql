-- 查询所有无效推文的编号（ID）。当推文内容中的字符数严格大于 15 时，该推文是无效的。

-- 输入：
-- Tweets 表：
-- +----------+----------------------------------+
-- | tweet_id | content                          |
-- +----------+----------------------------------+
-- | 1        | Vote for Biden                   |
-- | 2        | Let us make America great again! |
-- +----------+----------------------------------+

-- 输出：
-- +----------+
-- | tweet_id |
-- +----------+
-- | 2        |
-- +----------+
-- 解释：
-- 推文 1 的长度 length = 14。该推文是有效的。
-- 推文 2 的长度 length = 32。该推文是无效的。

-- https://leetcode.cn/problems/invalid-tweets/

select tweet_id
from Tweets
where LENGTH(content) > 15  