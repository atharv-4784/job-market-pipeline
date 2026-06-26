
-- ==========================================================
-- SECTION 1 : DATA EXPLORATION
-- ==========================================================

-- View the first 10 records
SELECT *
FROM jobs
LIMIT 10;


-- Count total number of job listings
SELECT COUNT(*) AS total_jobs
FROM jobs;


-- Count the number of unique job roles
SELECT COUNT(DISTINCT title) AS available_job_roles
FROM jobs;


-- Count the number of unique job locations
SELECT COUNT(DISTINCT location) AS total_locations
FROM jobs;

-- Count the number of unique job locations
SELECT COUNT(DISTINCT company) AS total_companies
FROM jobs;

SELECT MIN(avg_salary) AS lowest_salary
FROM jobs;

SELECT MAX(avg_salary) AS highest_salary
FROM jobs;
-- ==========================================================
-- SECTION 2 : LOCATION ANALYSIS
-- ==========================================================

-- Top 10 locations with the highest number of job postings
SELECT
    location,
    COUNT(*) AS total_jobs
FROM jobs
GROUP BY location
ORDER BY total_jobs DESC
LIMIT 10;

SELECT
    company,
    COUNT(*) AS total_jobs
FROM jobs
GROUP BY company
ORDER BY total_jobs DESC
LIMIT 10;

-- ==========================================================
-- SECTION 3 : CATEGORY ANALYSIS
-- ==========================================================

-- Top 10 job categories by number of job postings
SELECT
    category,
    COUNT(*) AS total_jobs
FROM jobs
GROUP BY category
ORDER BY total_jobs DESC
LIMIT 10;



-- ==========================================================
-- SECTION 4 : JOB TITLE ANALYSIS
-- ==========================================================

-- Top 10 most common job titles
SELECT
    title,
    COUNT(*) AS total_jobs
FROM jobs
GROUP BY title
ORDER BY total_jobs DESC
LIMIT 10;



-- ==========================================================
-- SECTION 5 : SALARY ANALYSIS
-- ==========================================================

-- Top 10 highest paying job titles (Average Salary)
SELECT
    title,
    ROUND(AVG(avg_salary), 2) AS average_salary
FROM jobs
GROUP BY title
ORDER BY average_salary DESC
LIMIT 10;


-- Top 10 lowest paying jobs
SELECT
    title,
    company,
    avg_salary
FROM jobs
ORDER BY avg_salary ASC
LIMIT 10;


-- Top 10 highest paying jobs
SELECT
    title,
    company,
    avg_salary
FROM jobs
ORDER BY avg_salary DESC
LIMIT 10;

--Highest Paying Job in Each Category
SELECT *
FROM
(
    SELECT *,
           RANK() OVER
           (
               PARTITION BY category
               ORDER BY avg_salary DESC
           ) rnk
    FROM jobs
) t
WHERE rnk = 1;
-- ==========================================================
-- END OF SQL ANALYSIS
-- ==========================================================
```
