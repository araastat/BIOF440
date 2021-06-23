## 2021 Spring grading
##
library(tidyverse)
grades <- read_csv('~/Downloads/2021-05-09T1412_Grades-BIOF440_Data_Visualization_with_Python.csv')

grades <- grades %>% slice(-1) %>%
  select(Student, ID, `SIS Login ID`:`Discussions (7216)`)

names(grades) <- str_replace(names(grades), ' \\(\\d{4}\\)','')
grades <- grades %>% rename(HW1="Good and Bad")

hw_full <- c(20,90,40,25,25,25)
hws <- grades %>% select(starts_with('HW')) %>%
  scale(center=F, scale = hw_full) %>%
  as_tibble()

cuts = c(-1, 70, 80,90,95, 100)

gradesheet <- cbind(Student=grades$Student, hws) %>%
  pivot_longer(cols = -Student, names_to = 'hw', values_to = 'scores') %>%
  group_by(Student) %>%
  slice_max(n = 2, order_by = scores, with_ties=FALSE) %>%
  summarise(scores = median(scores, na.rm=T) * 50) %>%
  left_join(grades %>% select(Student,`Discussions`,`Final Project`)) %>%
  rowwise() %>%
  mutate(total = sum(c_across(scores:`Final Project`), na.rm=T)) %>%
  ungroup() %>%
  mutate(total = pmin(total,100)) %>%
  mutate(grade = cut(total, cuts))

levels(gradesheet$grade) <- c('F','C','B','A','A+')

openxlsx::write.xlsx(gradesheet, here::here('Personal/Spring2021grades.xlsx'))
