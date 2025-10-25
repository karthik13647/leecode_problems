select w2.id
from weather w1 
cross join weather w2
where DATEDIFF(w2.recordDate,w1.recordDate) = 1 and 
w1.temperature<w2.temperature;