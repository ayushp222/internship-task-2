
CREATE TABLE Students (
  student_id INT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100)
);

CREATE TABLE Courses (
  course_id INT PRIMARY KEY,
  course_name VARCHAR(100),
  course_description TEXT
);

CREATE TABLE Enrolments (
  enrolment_id INT PRIMARY KEY,
  student_id INT,
  course_id INT,
  enrolment_date DATE,
  FOREIGN KEY (student_id) REFERENCES Students(student_id),
  FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);


INSERT INTO Students VALUES
(1, 'Ayush Patil', 'ayush@example.com'),
(2, 'Anjali Mehta', 'anjali@example.com'),
(3, 'Rahul Verma', 'rahul@example.com');

INSERT INTO Courses VALUES
(101, 'Python Programming', 'Learn Python from basics'),
(102, 'Data Structures', 'DS in C++'),
(103, 'DBMS', 'SQL and relational DBs'),
(104, 'Web Development', 'HTML, CSS, JS');

INSERT INTO Enrolments VALUES
(1, 1, 101, '2025-07-01'),
(2, 1, 102, '2025-07-03'),
(3, 2, 101, '2025-07-02'),
(4, 2, 103, '2025-07-05');


SELECT s.name AS student_name, c.course_name
FROM Students s
INNER JOIN Enrolments e ON s.student_id = e.student_id
INNER JOIN Courses c ON e.course_id = c.course_id;


SELECT c.course_name, COUNT(e.student_id) AS enrolled_students
FROM Courses c
LEFT JOIN Enrolments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name;


SELECT s.name, COUNT(e.course_id) AS course_count
FROM Enrolments e
JOIN Students s ON e.student_id = s.student_id
GROUP BY e.student_id
HAVING COUNT(e.course_id) > 1;


SELECT c.course_name
FROM Courses c
LEFT JOIN Enrolments e ON c.course_id = e.course_id
WHERE e.enrolment_id IS NULL;
