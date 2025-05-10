-- To find crimes in the communities of Oakland, Armour Square, Edgewater and CHICAGO 
-- and list the associated community_area_numbers and the case_numbers.
SELECT CC.CASE_NUMBER,CC.CASE_NUMBER, CSE.COMMUNITY_AREA_NAME
FROM chicago_socioeconomic_data CSE RIGHT JOIN chicago_crime CC 
ON CSE.COMMUNITY_AREA_NUMBER = CC.COMMUNITY_AREA_NUMBER
WHERE CSE.COMMUNITY_AREA_NAME IN ('OAKLAND', 'ARMOUR SQUARE', 'EDGEWATER', 'CHICAGO')
ORDER BY CSE.COMMUNITY_AREA_NAME;
