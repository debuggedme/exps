-- 找出那些 没有被 id = 2 的客户 推荐 的客户的姓名。

-- 输入： 
-- Customer 表:
-- +----+------+------------+
-- | id | name | referee_id |
-- +----+------+------------+
-- | 1  | Will | null       |
-- | 2  | Jane | null       |
-- | 3  | Alex | 2          |
-- | 4  | Bill | null       |
-- | 5  | Zack | 1          |
-- | 6  | Mark | 2          |
-- +----+------+------------+
-- 输出：
-- +------+
-- | name |
-- +------+
-- | Will |
-- | Jane |
-- | Bill |
-- | Zack |
-- +------+

-- https://leetcode.cn/problems/find-customer-referee/

select name
from Customer
where referee_id != 2 or referee_id is NULL