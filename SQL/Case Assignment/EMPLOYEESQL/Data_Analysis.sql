--Data Analysis
--List the following details of each employee: employee number, last name, first name, sex, and salary.
select e.emp_no as "employee number"
	,e.last_name as "last name"
	,e.first_name as "first name"
	,e.sex as "Gender"
	,cast(s.salaries as money) as Salary
from employees e
	inner join salaries s on
	s.emp_no = e.emp_no;

--List first name, last name, and hire date for employees who were hired in 1986.
select e.first_name as "First Name"
	,e.last_name as "Last Name"
	,e.hire_date as "Hire Date"
from employees e
where
	EXTRACT(YEAR FROM hire_date) = '1986'

--List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name.
select dm.dept_no as "Department Number"
	,d.dept_name as "Department Name"
	,e.emp_no as Manager's' employee Number"
	,e.first_name as "Manager First Name"
	,e.last_name as "Manager Last Name"
from dept_manager dm
	inner join departments d on
		d.dept_no = dm.dept_no
	inner join employees e on
		e.emp_no = dm.emp_no;

--List the department of each employee with the following information: employee number, last name, first name, and department name.
select e.empy_no as "Employee Number"
	,e.last_name as "Employee Last Name"
	,e.first_name as "Employee First Name"
	,d.dept_name as "Department Name"
from employees e
	inner join dept_emp de on
		de.emp_no = e.emp_no
	inner join departments d on
		d.dept_no = de.dept_no;

--List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."
select first_name as "Employee First Name"
	,last_name as "Employee Last Name"
	,sex as "Gender"
from employees
where first_name = 'Hercules'
	and upper(last_name) like 'B%';
	
--List all employees in the Sales department, including their employee number, last name, first name, and department name.
select e.emp_no as "Employee Number"
	,e.last_name as "Employee Last Name"
	,e.first_name as "Employee First Name"
	,d.dept_name as "Department Name"
from employees e
	inner join dept_emp de on
		de.emp_no = e.emp_no
	inner join departments d on
	d.dept_no = de.dept_no
	and d.dept_name = 'Sales';


--List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
select e.emp_no as "Employee Number"
	,e.last_name as "Employee Last Name"
	,e.first_name as "Employee First Name"
	,d.dept_name as "Department Name"
from employees e
	inner join dept_emp de on
		de.emp_no = e.emp_no
	inner join departments d on
		d.dept_no = de.dept_no
		and d.dept_name in ('Sales', 'Development');
		
--In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
select last_name as "Last Name"
	,count(last_name) as "Frequency count"
from employees
group by last_name
order by count (last_name) desc;