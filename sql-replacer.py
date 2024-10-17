def replace_question_marks(text, replacements):
  """
  将多行字符串中的问号替换为字符串数组中的对应字符串。

  Args:
    text: 包含多个问号的多行字符串
    replacements: 包含对应字符串的数组

  Returns:
    替换后的字符串
  """
  if len(replacements) != text.count("?"):
    raise ValueError("问号数量与替换字符串数量不匹配")

  i = 0
  result = text
  for replacement in replacements:
    result = result.replace("?", str(replacement), 1)
    i += 1
  return result

# --------------------- 下面可以修改要处理的SQL语句和要替换的信息

sql_string = """select 
	aa.*,
	aa.noCompleteHouseNumberZ - IFNULL(cc.repeatNoCompleteHouseNumber, 0) as noCompleteHouseNumber,
	aa.unitNumberZ - IFNULL(cc.repeatUnitNumber, 0) as unitNumber,
	aa.noElevatorUnitNumberZ - IFNULL(cc.repeatNoElevatorUnitNumber, 0) as noElevatorUnitNumber,
	aa.planHouseCountZ - IFNULL(cc.repeatHouseCount, 0) as planHouseCount,
	aa.planConsAreaZ - IFNULL(cc.repeatConsArea, 0) as planConsArea,
	aa.planBuildCountZ - IFNULL(cc.repeatBuildCount, 0) as planBuildCount,
	aa.evolveHouseCountZ1  as evolveHouseCount1,
	aa.evolveConsAreaZ1  as evolveConsArea1,
	aa.evolveBuildCountZ1  as evolveBuildCount1,
	aa.evolveHouseCountZ2  as evolveHouseCount2,
	aa.evolveConsAreaZ2  as evolveConsArea2,
	aa.evolveBuildCountZ2  as evolveBuildCount2,
	aa.evolveHouseCountZ3  as evolveHouseCount3,
	aa.evolveConsAreaZ3  as evolveConsArea3,
	aa.evolveBuildCountZ3  as evolveBuildCount3,
	bb.communityNumber,
	bb.communityNumber1,
	bb.communityNumber2,
	bb.communityNumber3
FROM
(
select '3' as type,
			e.county_code,
			count(distinct(e.id)) as projectNumber,
			IFNULL(sum(e.plan_house_count),0) as planHouseCountZ,
			IFNULL(sum(e.plan_cons_area),0) as planConsAreaZ,
			IFNULL(sum(e.plan_build_count),0) as planBuildCountZ,
			IFNULL(sum(e.no_complete_house),0) as noCompleteHouseNumberZ,
			IFNULL(sum(e.unit_number),0) as unitNumberZ,
			IFNULL(sum(e.no_elevator_unit_number),0) as noElevatorUnitNumberZ,
			count(
				distinct(case e.evolveStage when 1 then e.id else null end)
			)  as projectNumber1,
			IFNULL(sum(
				case e.evolveStage when 1 then e.evolve_house_count else 0 end
			),0) as evolveHouseCountZ1,
			IFNULL(sum(
				case e.evolveStage when 1 then e.evolve_cons_area else 0 end
			),0) as evolveConsAreaZ1,
			IFNULL(sum(
				case e.evolveStage when 1 then e.evolve_build_count else 0 end
			),0) as evolveBuildCountZ1,
			count(
				distinct(case e.evolveStage when 2 then e.id else null end)
			)  as projectNumber2,
			IFNULL(sum(
				case e.evolveStage when 2 then e.evolve_house_count else 0 end
			),0) as evolveHouseCountZ2,
			IFNULL(sum(
				case e.evolveStage when 2 then e.evolve_cons_area else 0 end
			),0) as evolveConsAreaZ2,
			IFNULL(sum(
				case e.evolveStage when 2 then e.evolve_build_count else 0 end
			),0) as evolveBuildCountZ2,
			count(
				distinct(case e.evolveStage when 3 then e.id else null end)
			)  as projectNumber3,
			IFNULL(sum(
				case e.evolveStage when 3 then e.evolve_house_count else 0 end
			),0) as evolveHouseCountZ3,
			IFNULL(sum(	
				case e.evolveStage when 3 then e.evolve_cons_area else 0 end
			),0) as evolveConsAreaZ3,
			IFNULL(sum(
				case e.evolveStage when 3 then e.evolve_build_count else 0 end
			),0) as evolveBuildCountZ3,
			IFNULL(sum(e.ic_total_amount),0) as icTotalAmount,
			IFNULL(sum(e.zcTotalAmount),0) as zcTotalAmount,
			IFNULL(sum(e.xd_fd_country + e.xd_fd_social + e.xd_fd_resident + e.xd_fd_other),0) as xdTotalAmount,
			IFNULL(sum(e.xd_fd_country),0) as fdCountry,
			IFNULL(sum(e.xd_fd_central_budget + e.xd_fd_central_finance),0) as fdCentral,
			IFNULL(sum(e.xd_fd_central_budget),0) as fdCentralBudget,
			IFNULL(sum(e.xd_fd_central_finance),0) as fd_central_finance,
			IFNULL(sum(e.xd_fd_province_finance),0) as fd_province_finance,
			IFNULL(sum(e.xd_fd_city_finance + e.xd_fd_county_finance + e.xd_fd_county_below_finance),0) as fd_city_finance,
			IFNULL(sum(e.xd_fd_special_bond),0) as fd_special_bond,
			IFNULL(sum(e.xd_fd_social),0) as fd_social,
			IFNULL(sum(e.xd_fd_operating_subject),0) as fd_operating_subject,
			IFNULL(sum(e.xd_fd_business_unit),0) as fd_business_unit,
			IFNULL(sum(e.xd_fd_electric_power_enterprises),0) as fd_electric_power_enterprises,
			IFNULL(sum(e.xd_fd_communication_enterprises),0) as fd_communication_enterprises,
			IFNULL(sum(e.xd_fd_drainage_enterprise),0) as fd_drainage_enterprise,
			IFNULL(sum(e.xd_fd_heating_enterprises),0) as fd_heating_enterprises,
			IFNULL(sum(e.xd_fd_gas_enterprises),0) as fd_gas_enterprises,
			IFNULL(sum(e.xd_fd_property_unit),0) as fd_property_unit,
			IFNULL(sum(e.xd_fd_other_social),0) as fd_other_social,
			IFNULL(sum(e.xd_fd_financial_institution),0) as fd_financial_institution,
			IFNULL(sum(e.xd_fd_resident),0) as fd_resident,
			IFNULL(sum(e.xd_fd_other),0) as fd_other
from (
select 
	aa.*,d.plan_house_count,d.plan_cons_area,d.plan_build_count,max(e.evolve_stage) as evolveStage,f.community_id,
	e.evolve_house_count,e.evolve_cons_area,e.evolve_build_count
from (select a.*,a.zc_fd_country + a.zc_fd_social + a.zc_fd_resident + a.zc_fd_other as 'zcTotalAmount',
	sum(c.no_complete_house) as no_complete_house,
	sum(c.unit_number) as unit_number,
	sum(c.no_elevator_unit_number) as no_elevator_unit_number
	from gdszzj.base_project a 
	left join gdszzj.base_annual_plan c on c.project_id = a.id
	where 1=1 
	and a.county_code like concat(?,'%')
	AND a.period = ? 
group by a.county_code,a.id
) aa 
INNER join gdszzj.base_annual_plan d on aa.id = d.project_id  AND  (d.community_id IS NULL OR d.community_id ='')
INNER join gdszzj.base_progress_situation e on d.id = e.plan_id
LEFT JOIN gdszzj.project_community f on aa.id = f.project_id
WHERE (d.plan_year = ? && (e.fill_month = ? || (e.evolve_stage = 3 && e.fill_month < ?)) ||
(d.plan_year < ? && e.evolve_stage = 3))
GROUP BY aa.id,d.community_id HAVING MAX(d.plan_house_count)  
) e
) aa
left join (
SELECT
	'3' as type,
	count( DISTINCT a.community_id ) as communityNumber,
	count(DISTINCT case when a.evolve_stage = 1 then a.community_id else null end) as communityNumber1,
	count(DISTINCT case when a.evolve_stage = 2 then a.community_id else null end) as communityNumber2,
	count(DISTINCT case when a.evolve_stage = 3 then a.community_id else null end) as communityNumber3
FROM
	(
SELECT
	d.community_id,
	max(c.evolve_stage) AS evolve_stage 
FROM
	gdszzj.base_project a
	INNER JOIN gdszzj.base_annual_plan b ON a.id = b.project_id
	INNER JOIN gdszzj.base_progress_situation c ON b.id = c.plan_id
	LEFT JOIN gdszzj.project_community d ON a.id = d.project_id
WHERE
	a.county_code like concat(?,'%')
	and a.period = ? 
	AND (b.plan_year = ? && (c.fill_month = ? || (c.evolve_stage = 3 && c.fill_month < ?)) ||
(b.plan_year < ? && c.evolve_stage = 3))
GROUP BY
	d.community_id
	) a
) bb on aa.type = bb.type
left join(
	SELECT
'3' as type,
sum(a.no_complete_house) as repeatNoCompleteHouseNumber,
sum(a.unit_number) as repeatUnitNumber,
sum(a.no_elevator_unit_number) as repeatNoElevatorUnitNumber,
sum(a.community_cons_area) as repeatConsArea,
sum(a.community_house_count) as repeatHouseCount,
sum(a.community_build_count) as repeatBuildCount,
sum(a.community_cons_area1) as repeatConsArea1,
sum(a.community_house_count1) as repeatHouseCount1,
sum(a.community_build_count1) as repeatBuildCount1,
sum(a.community_cons_area2) as repeatConsArea2,
sum(a.community_house_count2) as repeatHouseCount2,
sum(a.community_build_count2) as repeatBuildCount2,
sum(a.community_cons_area3) as repeatConsArea3,
sum(a.community_house_count3) as repeatHouseCount3,
sum(a.community_build_count3) as repeatBuildCount3
FROM
(
SELECT 
	*	
FROM
(
SELECT
	a.county_code,
	a.city_code,
	c.community_id,
	e.community_cons_area,
	e.community_house_count,
	e.community_build_count,
	e.no_complete_house,
	e.unit_number,
	e.no_elevator_unit_number,
	case when max(c.evolve_stage) = 1 then e.community_cons_area else 0 end as 'community_cons_area1',
	case when max(c.evolve_stage) = 1 then e.community_house_count else 0 end as 'community_house_count1',
	case when max(c.evolve_stage) = 1 then e.community_build_count else 0 end as 'community_build_count1',
	case when max(c.evolve_stage) = 2 then e.community_cons_area else 0 end as 'community_cons_area2',
	case when max(c.evolve_stage) = 2 then e.community_house_count else 0 end as 'community_house_count2',
	case when max(c.evolve_stage) = 2 then e.community_build_count else 0 end as 'community_build_count2',
	case when max(c.evolve_stage) = 3 then e.community_cons_area else 0 end as 'community_cons_area3',
	case when max(c.evolve_stage) = 3 then e.community_house_count else 0 end as 'community_house_count3',
	case when max(c.evolve_stage) = 3 then e.community_build_count else 0 end as 'community_build_count3'
FROM
	gdszzj.base_project a
	INNER JOIN gdszzj.base_annual_plan b ON a.id = b.project_id
	INNER JOIN gdszzj.base_progress_situation c ON b.id = c.plan_id 
	LEFT JOIN gdszzj.base_community e on c.community_id = e.id
WHERE
	a.county_code LIKE concat( ?, '%' ) 
	AND a.plan_means = 1
	AND a.period = ? 
	AND (b.plan_year = ? && (c.fill_month = ? || (c.evolve_stage = 3 && c.fill_month < ?)) ||
(b.plan_year < ? && c.evolve_stage = 3))
	GROUP BY a.id,c.community_id
	union all
	SELECT
	a.county_code,
	a.city_code,
	d.community_id,
	e.community_cons_area,
	e.community_house_count,
	e.community_build_count,
	e.no_complete_house,
	e.unit_number,
	e.no_elevator_unit_number,
	case when max(c.evolve_stage) = 1 then e.community_cons_area else 0 end as 'community_cons_area1',
	case when max(c.evolve_stage) = 1 then e.community_house_count else 0 end as 'community_house_count1',
	case when max(c.evolve_stage) = 1 then e.community_build_count else 0 end as 'community_build_count1',
	case when max(c.evolve_stage) = 2 then e.community_cons_area else 0 end as 'community_cons_area2',
	case when max(c.evolve_stage) = 2 then e.community_house_count else 0 end as 'community_house_count2',
	case when max(c.evolve_stage) = 2 then e.community_build_count else 0 end as 'community_build_count2',
	case when max(c.evolve_stage) = 3 then e.community_cons_area else 0 end as 'community_cons_area3',
	case when max(c.evolve_stage) = 3 then e.community_house_count else 0 end as 'community_house_count3',
	case when max(c.evolve_stage) = 3 then e.community_build_count else 0 end as 'community_build_count3'
FROM
	gdszzj.base_project a
	INNER JOIN gdszzj.base_annual_plan b ON a.id = b.project_id
	INNER JOIN gdszzj.base_progress_situation c ON b.id = c.plan_id 
	INNER JOIN gdszzj.project_community d ON a.id = d.project_id 
	LEFT JOIN gdszzj.base_community e on d.community_id = e.id
WHERE
	a.county_code LIKE concat( ?, '%' ) 
	AND a.plan_means = 2
	AND a.period = ? 
	AND (b.plan_year = ? && (c.fill_month = ? || (c.evolve_stage = 3 && c.fill_month < ?)) ||
(b.plan_year < ? && c.evolve_stage = 3))
	GROUP BY a.id,d.community_id
) a GROUP BY a.community_id HAVING count(*) > 1
)a 
) cc on aa.type = cc.type union 
select 
	aa.*,
	aa.noCompleteHouseNumberZ - IFNULL(cc.repeatNoCompleteHouseNumber, 0) as noCompleteHouseNumber,
	aa.unitNumberZ - IFNULL(cc.repeatUnitNumber, 0) as unitNumber,
	aa.noElevatorUnitNumberZ - IFNULL(cc.repeatNoElevatorUnitNumber, 0) as noElevatorUnitNumber,
	aa.planHouseCountZ - IFNULL(cc.repeatHouseCount, 0) as planHouseCount,
	aa.planConsAreaZ - IFNULL(cc.repeatConsArea, 0) as planConsArea,
	aa.planBuildCountZ - IFNULL(cc.repeatBuildCount, 0) as planBuildCount,
	aa.evolveHouseCountZ1  as evolveHouseCount1,
	aa.evolveConsAreaZ1  as evolveConsArea1,
	aa.evolveBuildCountZ1  as evolveBuildCount1,
	aa.evolveHouseCountZ2  as evolveHouseCount2,
	aa.evolveConsAreaZ2  as evolveConsArea2,
	aa.evolveBuildCountZ2  as evolveBuildCount2,
	aa.evolveHouseCountZ3  as evolveHouseCount3,
	aa.evolveConsAreaZ3  as evolveConsArea3,
	aa.evolveBuildCountZ3  as evolveBuildCount3,
	bb.communityNumber,
	bb.communityNumber1,
	bb.communityNumber2,
	bb.communityNumber3
FROM
(
select '4' as type,
			e.county_code,
			count(distinct(e.id)) as projectNumber,
			IFNULL(sum(e.plan_house_count),0) as planHouseCountZ,
			IFNULL(sum(e.plan_cons_area),0) as planConsAreaZ,
			IFNULL(sum(e.plan_build_count),0) as planBuildCountZ,
			IFNULL(sum(e.no_complete_house),0) as noCompleteHouseNumberZ,
			IFNULL(sum(e.unit_number),0) as unitNumberZ,
			IFNULL(sum(e.no_elevator_unit_number),0) as noElevatorUnitNumberZ,
			count(
				distinct(case e.evolveStage when 1 then e.id else null end)
			)  as projectNumber1,
			IFNULL(sum(
				case e.evolveStage when 1 then e.evolve_house_count else 0 end
			),0) as evolveHouseCountZ1,
			IFNULL(sum(
				case e.evolveStage when 1 then e.evolve_cons_area else 0 end
			),0) as evolveConsAreaZ1,
			IFNULL(sum(
				case e.evolveStage when 1 then e.evolve_build_count else 0 end
			),0) as evolveBuildCountZ1,
			count(
				distinct(case e.evolveStage when 2 then e.id else null end)
			)  as projectNumber2,
			IFNULL(sum(
				case e.evolveStage when 2 then e.evolve_house_count else 0 end
			),0) as evolveHouseCountZ2,
			IFNULL(sum(
				case e.evolveStage when 2 then e.evolve_cons_area else 0 end
			),0) as evolveConsAreaZ2,
			IFNULL(sum(
				case e.evolveStage when 2 then e.evolve_build_count else 0 end
			),0) as evolveBuildCountZ2,
			count(
				distinct(case e.evolveStage when 3 then e.id else null end)
			)  as projectNumber3,
			IFNULL(sum(
				case e.evolveStage when 3 then e.evolve_house_count else 0 end
			),0) as evolveHouseCountZ3,
			IFNULL(sum(	
				case e.evolveStage when 3 then e.evolve_cons_area else 0 end
			),0) as evolveConsAreaZ3,
			IFNULL(sum(
				case e.evolveStage when 3 then e.evolve_build_count else 0 end
			),0) as evolveBuildCountZ3,
			IFNULL(sum(e.ic_total_amount),0) as icTotalAmount,
			IFNULL(sum(e.zcTotalAmount),0) as zcTotalAmount,
			IFNULL(sum(e.fdcountry2 + e.xd_fd_social + e.xd_fd_resident + e.xd_fd_other),0) as xdTotalAmount,
			IFNULL(sum(e.fdcountry2),0) as fdCountry,
			IFNULL(sum(e.xd_fd_central_budget + e.fd_central_finance2),0) as fdCentral,
			IFNULL(sum(e.xd_fd_central_budget),0) as fdCentralBudget,
			IFNULL(sum(e.fd_central_finance2),0) as fd_central_finance,
			IFNULL(sum(e.xd_fd_province_finance),0) as fd_province_finance,
			IFNULL(sum(e.xd_fd_city_finance + e.xd_fd_county_finance + e.xd_fd_county_below_finance),0) as fd_city_finance,
			IFNULL(sum(e.xd_fd_special_bond),0) as fd_special_bond,
			IFNULL(sum(e.xd_fd_social),0) as fd_social,
			IFNULL(sum(e.xd_fd_operating_subject),0) as fd_operating_subject,
			IFNULL(sum(e.xd_fd_business_unit),0) as fd_business_unit,
			IFNULL(sum(e.xd_fd_electric_power_enterprises),0) as fd_electric_power_enterprises,
			IFNULL(sum(e.xd_fd_communication_enterprises),0) as fd_communication_enterprises,
			IFNULL(sum(e.xd_fd_drainage_enterprise),0) as fd_drainage_enterprise,
			IFNULL(sum(e.xd_fd_heating_enterprises),0) as fd_heating_enterprises,
			IFNULL(sum(e.xd_fd_gas_enterprises),0) as fd_gas_enterprises,
			IFNULL(sum(e.xd_fd_property_unit),0) as fd_property_unit,
			IFNULL(sum(e.xd_fd_other_social),0) as fd_other_social,
			IFNULL(sum(e.xd_fd_financial_institution),0) as fd_financial_institution,
			IFNULL(sum(e.xd_fd_resident),0) as fd_resident,
			IFNULL(sum(e.xd_fd_other),0) as fd_other
from (
select 
	aa.*,d.plan_house_count,d.plan_cons_area,d.plan_build_count,max(e.evolve_stage) as evolveStage,f.community_id,
	e.evolve_house_count,e.evolve_cons_area,e.evolve_build_count
from (select a.*,d.fd_total as zcTotalAmount,d.fd_country as fdcountry2,d.fd_central_finance as fd_central_finance2,
	c.no_complete_house as no_complete_house,
	c.unit_number as unit_number,
	c.no_elevator_unit_number as no_elevator_unit_number
	from gdszzj.base_project a 
	left join gdszzj.base_annual_plan c on c.project_id = a.id
	left join gdszzj.bus_project_capital d on a.id = d.project_id and d.capital_type=2 and d.capital_year = ?	where 1=1 
	and a.county_code like concat(?,'%')
	and a.period = ? 
	and c.plan_year = ? 
group by a.county_code,a.id
) aa 
INNER join gdszzj.base_annual_plan d on aa.id = d.project_id AND  (d.community_id IS NULL OR d.community_id ='')
INNER join gdszzj.base_progress_situation e on d.id = e.plan_id
LEFT JOIN gdszzj.project_community f on aa.id = f.project_id
WHERE d.plan_year = ? 
and (e.fill_month = ? || (e.evolve_stage = 3 && e.fill_month < ?)) 
and aa.id NOT IN(
SELECT
	a.id
FROM
	gdszzj.base_project a
	INNER JOIN gdszzj.base_annual_plan d ON a.id = d.project_id
	INNER JOIN gdszzj.base_progress_situation e ON d.id = e.plan_id 
WHERE
	a.county_code LIKE concat( ?, '%' ) 
	AND a.period = ? 
	AND (d.plan_year < ? && e.evolve_stage = 3)
GROUP BY d.id)
GROUP BY aa.id,d.community_id
) e
) aa
left join (
SELECT
	'4' as type,
	count( DISTINCT a.community_id ) as communityNumber,
	count(DISTINCT case when a.evolve_stage = 1 then a.community_id else null end) as communityNumber1,
	count(DISTINCT case when a.evolve_stage = 2 then a.community_id else null end) as communityNumber2,
	count(DISTINCT case when a.evolve_stage = 3 then a.community_id else null end) as communityNumber3
FROM
	(
SELECT
	d.community_id,
	max(c.evolve_stage) AS evolve_stage 
FROM
	gdszzj.base_project a
	INNER JOIN gdszzj.base_annual_plan b ON a.id = b.project_id
	INNER JOIN gdszzj.base_progress_situation c ON b.id = c.plan_id
	LEFT JOIN gdszzj.project_community d ON a.id = d.project_id
WHERE
	a.county_code like concat(?,'%')
	and a.period = ? 
	AND b.plan_year = ? 
	AND ( c.fill_month = ? || ( c.evolve_stage = 3 && c.fill_month < ? ) ) 
AND a.id NOT IN(
SELECT
	a.id
FROM
	gdszzj.base_project a
	INNER JOIN gdszzj.base_annual_plan d ON a.id = d.project_id
	INNER JOIN gdszzj.base_progress_situation e ON d.id = e.plan_id 
WHERE
	a.county_code LIKE concat( ?, '%' ) 
	AND a.period = ? 
	AND (d.plan_year < ? && e.evolve_stage = 3)
GROUP BY a.id )
	GROUP BY d.community_id) a
) bb on aa.type = bb.type
left join(
	SELECT
'4' as type,
sum(a.no_complete_house) as repeatNoCompleteHouseNumber,
sum(a.unit_number) as repeatUnitNumber,
sum(a.no_elevator_unit_number) as repeatNoElevatorUnitNumber,
sum(a.community_cons_area) as repeatConsArea,
sum(a.community_house_count) as repeatHouseCount,
sum(a.community_build_count) as repeatBuildCount,
sum(a.community_cons_area1) as repeatConsArea1,
sum(a.community_house_count1) as repeatHouseCount1,
sum(a.community_build_count1) as repeatBuildCount1,
sum(a.community_cons_area2) as repeatConsArea2,
sum(a.community_house_count2) as repeatHouseCount2,
sum(a.community_build_count2) as repeatBuildCount2,
sum(a.community_cons_area3) as repeatConsArea3,
sum(a.community_house_count3) as repeatHouseCount3,
sum(a.community_build_count3) as repeatBuildCount3
FROM
(
SELECT 
	*	
FROM
(
SELECT
	a.county_code,
	a.city_code,
	c.community_id,
	e.community_cons_area,
	e.community_house_count,
	e.community_build_count,
	e.no_complete_house,
	e.unit_number,
	e.no_elevator_unit_number,
	case when max(c.evolve_stage) = 1 then e.community_cons_area else 0 end as 'community_cons_area1',
	case when max(c.evolve_stage) = 1 then e.community_house_count else 0 end as 'community_house_count1',
	case when max(c.evolve_stage) = 1 then e.community_build_count else 0 end as 'community_build_count1',
	case when max(c.evolve_stage) = 2 then e.community_cons_area else 0 end as 'community_cons_area2',
	case when max(c.evolve_stage) = 2 then e.community_house_count else 0 end as 'community_house_count2',
	case when max(c.evolve_stage) = 2 then e.community_build_count else 0 end as 'community_build_count2',
	case when max(c.evolve_stage) = 3 then e.community_cons_area else 0 end as 'community_cons_area3',
	case when max(c.evolve_stage) = 3 then e.community_house_count else 0 end as 'community_house_count3',
	case when max(c.evolve_stage) = 3 then e.community_build_count else 0 end as 'community_build_count3'
FROM
	gdszzj.base_project a
	INNER JOIN gdszzj.base_annual_plan b ON a.id = b.project_id
	INNER JOIN gdszzj.base_progress_situation c ON b.id = c.plan_id 
	LEFT JOIN gdszzj.base_community e on c.community_id = e.id
WHERE
	a.county_code LIKE concat( ?, '%' ) 
	and a.period = ? 
	AND a.plan_means = 1
	AND b.plan_year = ? 
	AND ( c.fill_month = ? || ( c.evolve_stage = 3 && c.fill_month < ? ) )
AND a.id NOT IN(
SELECT
	a.id
FROM
	gdszzj.base_project a
	INNER JOIN gdszzj.base_annual_plan d ON a.id = d.project_id
	INNER JOIN gdszzj.base_progress_situation e ON d.id = e.plan_id 
WHERE
	a.county_code LIKE concat( ?, '%' ) 
	AND a.period = ? 
	AND (d.plan_year < ? && e.evolve_stage = 3)
	GROUP BY a.id) GROUP BY a.id,c.community_id
	union all
	SELECT
	a.county_code,
	a.city_code,
	d.community_id,
	e.community_cons_area,
	e.community_house_count,
	e.community_build_count,
	e.no_complete_house,
	e.unit_number,
	e.no_elevator_unit_number,
	case when max(c.evolve_stage) = 1 then e.community_cons_area else 0 end as 'community_cons_area1',
	case when max(c.evolve_stage) = 1 then e.community_house_count else 0 end as 'community_house_count1',
	case when max(c.evolve_stage) = 1 then e.community_build_count else 0 end as 'community_build_count1',
	case when max(c.evolve_stage) = 2 then e.community_cons_area else 0 end as 'community_cons_area2',
	case when max(c.evolve_stage) = 2 then e.community_house_count else 0 end as 'community_house_count2',
	case when max(c.evolve_stage) = 2 then e.community_build_count else 0 end as 'community_build_count2',
	case when max(c.evolve_stage) = 3 then e.community_cons_area else 0 end as 'community_cons_area3',
	case when max(c.evolve_stage) = 3 then e.community_house_count else 0 end as 'community_house_count3',
	case when max(c.evolve_stage) = 3 then e.community_build_count else 0 end as 'community_build_count3'
FROM
	gdszzj.base_project a
	INNER JOIN gdszzj.base_annual_plan b ON a.id = b.project_id
	INNER JOIN gdszzj.base_progress_situation c ON b.id = c.plan_id 
	INNER JOIN gdszzj.project_community d ON a.id = d.project_id 
	LEFT JOIN gdszzj.base_community e on d.community_id = e.id
WHERE
	a.county_code LIKE concat( ?, '%' ) 
	and a.period = ? 
	AND a.plan_means = 2
	AND b.plan_year = ? 
	AND ( c.fill_month = ? || ( c.evolve_stage = 3 && c.fill_month < ? ) )
AND a.id NOT IN(
SELECT
	a.id
FROM
	gdszzj.base_project a
	INNER JOIN gdszzj.base_annual_plan d ON a.id = d.project_id
	INNER JOIN gdszzj.base_progress_situation e ON d.id = e.plan_id 
WHERE
	a.county_code LIKE concat( ?, '%' ) 
	AND a.period = ? 
	AND (d.plan_year < ? && e.evolve_stage = 3)
	GROUP BY a.id) GROUP BY a.id,d.community_id
) a
GROUP BY a.community_id HAVING count(*) > 1
)a 
) cc on aa.type = cc.type """

params = [441225000000, 2024, 2024, 11, 11, 2024, 441225000000, 2024, 2024, 11, 11, 2024, 441225000000, 2024, 2024, 11, 11, 2024, 441225000000, 2024, 2024, 11, 11, 2024, 2024, 441225000000, 2024, 2024, 2024, 11, 11, 441225000000, 2024, 2024, 441225000000, 2024, 2024, 11, 11, 441225000000, 2024, 2024, 441225000000, 2024, 2024, 11, 11, 441225000000, 2024, 2024, 441225000000, 2024, 2024, 11, 11, 441225000000, 2024, 2024]

real_sql = replace_question_marks(sql_string, params)

print(f"Real SQL: {real_sql}")  # 打印最终替换后的 SQL 语句