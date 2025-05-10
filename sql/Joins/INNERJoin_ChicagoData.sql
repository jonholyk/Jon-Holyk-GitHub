-- To create a list of the case number, type of crime and community area 
-- for all crimes in community area number 18.
SELECT CC.CASE_NUMBER, CC.PRIMARY_TYPE, CSE.COMMUNITY_AREA_NAME
FROM chicago_socioeconomic_data CSE INNER JOIN chicago_crime CC 
WHERE CSE.COMMUNITY_AREA_NUMBER = 18