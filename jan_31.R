require(tidyverse)
require(janitor)

mtcars

airquality %>%
  group_by(month) %>% 
  summarise(mn = mean(Temp, na.rm = TRUE))
