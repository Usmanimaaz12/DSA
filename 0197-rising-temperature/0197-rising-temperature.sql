select w1.id
from weather AS w1,weather AS w2
where w1.temperature > w2.temperature AND datediff(w1.recordDate,w2.recordDate)=1



