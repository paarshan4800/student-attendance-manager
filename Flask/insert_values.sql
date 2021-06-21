Students:
Note:- 
1) Let the password be firstname and last four digits of roll_no for now.
2) Email ID is firstname.lastname@gmail.com for now.

INSERT INTO Students VALUES (2018103075,'umar3075','Umar','Ahmed','T','umar.ahmed@gmail.com','30-Oct-2000','M');
INSERT INTO Students VALUES (2018103006,'akash3006','Akash','Kirthik','G','akash.kirthik@gmail.com','26-Jul-2000','M');
INSERT INTO Students VALUES (2018103060,'serjius3060','Serjius','Infanto','S','serjius.infanto@gmail.com','14-Feb-2000','M');
INSERT INTO Students VALUES (2018103054,'ritika3054','Ritika',' ','M','ritika@gmail.com','01-Jan-2000','F');
INSERT INTO Students VALUES (2018103580,'risheek3580','Risheek','Rakshit','SK','risheek.rakshit@gmail.com','10-Sep-2000','M');
INSERT INTO Students VALUES (2018103556,'krithik3556','Krithik','Kumar','D','krithik.kumar@gmail.com','01-Jan-2000','M');
INSERT INTO Students VALUES (2018103045,'naveen3045','Naveen','Muthukumar',' ','naveen.muthukumar@gmail.com','01-Jan-2000','M');
INSERT INTO Students VALUES (2018103057,'sanjay3057','Sanjay','Krishnan',' ','sanjay.krishnan@gmail.com','01-Jan-2000','M');
INSERT INTO Students VALUES (2018103078,'vignesh3078','Vignesh',' ','G','vignesh@gmail.com','01-Jan-2000','M');
INSERT INTO Students VALUES (2018103081,'vishal3081','Vishal','Bharadwaj','V','vishal.bharadwaj@gmail.com','01-Jan-2000','M');




Faculty:
Note:-
1) Same as Students for Password and Email ID
2) For Faculty_id first two digits show the department and last three be their unique id.
3) Took Author names as faculty names. Had no other idea.

INSERT INTO Faculty VALUES (10001,'abraham001','Abraham','Silberschatz',' ','abraham.silberschatz@gmail.com');
INSERT INTO Faculty VALUES (10002,'henry002','Henry','Korth','F','henry.korth@gmail.com');
INSERT INTO Faculty VALUES (10003,'greg003','Greg','Gagne',' ','greg.gagne@gmail.com');
INSERT INTO Faculty VALUES (19001,'stephen001','Stephen','Friedberg','H','stephen.friedberg@gmail.com');
INSERT INTO Faculty VALUES (10004,'john004','John','Hopcroft','E','john.hopcroft@gmail.com');
INSERT INTO Faculty VALUES (17001,'gilbert001','Gilbert','Masters','M','gilbert.masters@gmail.com');
INSERT INTO Faculty VALUES (17002,'benny002','Benny','Joseph',' ','benny.joseph@gmail.com');
INSERT INTO Faculty VALUES (10005,'ellis005','Ellis',' Horowit',' ','ellis.horowit@gmail.com');
INSERT INTO Faculty VALUES (10006,'morris006','Morris','Mano','M','morris.mano@gmail.com');
INSERT INTO Faculty VALUES (19002,'milton002','Milton','J','S','milton.j@gmail.com');




Course:

INSERT INTO Course VALUES ('CS6106','Database Management Systems');
INSERT INTO Course VALUES ('CS6108','Operating Systems');
INSERT INTO Course VALUES ('MA6201','Linear Algebra');
INSERT INTO Course VALUES ('CS6202','Theory of Computation');
INSERT INTO Course VALUES ('CY6391','Environmental Science and Engineering'); 
INSERT INTO Course VALUES ('CS6104','Data Structures and Algorithms '); 
INSERT INTO Course VALUES ('CS6105','Digital Fundamentals and Computer Organization'); 
INSERT INTO Course VALUES ('MA6351','Probability and Statistic'); 
INSERT INTO Course VALUES ('GE6251','Engineering Graphic'); 
INSERT INTO Course VALUES ('CY6251','Engineering Chemistry'); 



Teaches:
Note:-
1) Faculty_id is taken from Faculty and Course_id from Course

INSERT INTO Teaches VALUES (10001,'CS6106');
INSERT INTO Teaches VALUES (10002,'CS6106');
INSERT INTO Teaches VALUES (10001,'CS6108');
INSERT INTO Teaches VALUES (10003,'CS6108');
INSERT INTO Teaches VALUES (19001,'MA6201');
INSERT INTO Teaches VALUES (10004,'CS6202');
INSERT INTO Teaches VALUES (17001,'CY6391');
INSERT INTO Teaches VALUES (17002,'CY6391');
INSERT INTO Teaches VALUES (10005,'CS6104');
INSERT INTO Teaches VALUES (10006,'CS6105');
INSERT INTO Teaches VALUES (19002,'MA6351');



Enrolls:
Note:-
1) Roll_no is taken from Students and Course_id from Course.

INSERT INTO Enrolls VALUES (2018103075,'CS6106',0,0,0);
INSERT INTO Enrolls VALUES (2018103075,'CS6108',0,0,0);
INSERT INTO Enrolls VALUES (2018103075,'MA6201',0,0,0);
INSERT INTO Enrolls VALUES (2018103075,'CY6391',0,0,0);
INSERT INTO Enrolls VALUES (2018103006,'CS6106',0,0,0);
INSERT INTO Enrolls VALUES (2018103006,'CS6108',0,0,0);
INSERT INTO Enrolls VALUES (2018103006,'CS6202',0,0,0);
INSERT INTO Enrolls VALUES (2018103006,'CY6391',0,0,0);
INSERT INTO Enrolls VALUES (2018103060,'CS6106',0,0,0);
INSERT INTO Enrolls VALUES (2018103060,'CS6108',0,0,0);
INSERT INTO Enrolls VALUES (2018103060,'MA6201',0,0,0);
INSERT INTO Enrolls VALUES (2018103060,'CY6391',0,0,0);




Student_Faculty:

INSERT INTO Student_Faculty VALUES (2018103075,10001,'CS6106');
INSERT INTO Student_Faculty VALUES (2018103075,10002,'CS6106');
INSERT INTO Student_Faculty VALUES (2018103075,10003,'CS6108');
INSERT INTO Student_Faculty VALUES (2018103075,19001,'MA6201');
INSERT INTO Student_Faculty VALUES (2018103075,17001,'CY6391');

INSERT INTO Student_Faculty VALUES (2018103060,10001,'CS6106');
INSERT INTO Student_Faculty VALUES (2018103060,10002,'CS6106');
INSERT INTO Student_Faculty VALUES (2018103060,10003,'CS6108');
INSERT INTO Student_Faculty VALUES (2018103060,19001,'MA6201');
INSERT INTO Student_Faculty VALUES (2018103060,17002,'CY6391');

INSERT INTO Student_Faculty VALUES (2018103006,10001,'CS6106');
INSERT INTO Student_Faculty VALUES (2018103006,10002,'CS6106');
INSERT INTO Student_Faculty VALUES (2018103006,10003,'CS6108');
INSERT INTO Student_Faculty VALUES (2018103006,10004,'CS6202');
INSERT INTO Student_Faculty VALUES (2018103006,17002,'CY6391');



Attendace_Log:

INSERT INTO Attendance_Log (roll_no,faculty_id,course_id,hour) VALUES  (2018103075,10001,'CS6106',4);
INSERT INTO Attendance_Log (roll_no,faculty_id,course_id,hour) VALUES  (2018103075,10002,'CS6106',2);
INSERT INTO Attendance_Log (roll_no,faculty_id,course_id,hour) VALUES  (2018103075,10003,'CS6108',2);
INSERT INTO Attendance_Log (roll_no,faculty_id,course_id,hour) VALUES  (2018103075,19001,'MA6201',2);
INSERT INTO Attendance_Log (roll_no,faculty_id,course_id,hour) VALUES  (2018103075,17001,'CY6391',2);

INSERT INTO Attendance_Log (roll_no,faculty_id,course_id,hour) VALUES  (2018103060,10001,'CS6106',4);
INSERT INTO Attendance_Log (roll_no,faculty_id,course_id,hour) VALUES  (2018103060,10002,'CS6106',-2);
INSERT INTO Attendance_Log (roll_no,faculty_id,course_id,hour) VALUES  (2018103060,10003,'CS6108',2);
INSERT INTO Attendance_Log (roll_no,faculty_id,course_id,hour) VALUES  (2018103060,19001,'MA6201',2);
INSERT INTO Attendance_Log (roll_no,faculty_id,course_id,hour) VALUES  (2018103060,17002,'CY6391',2);

INSERT INTO Attendance_Log (roll_no,faculty_id,course_id,hour) VALUES  (2018103006,10001,'CS6106',4);
INSERT INTO Attendance_Log (roll_no,faculty_id,course_id,hour) VALUES  (2018103006,10002,'CS6106',-2);
INSERT INTO Attendance_Log (roll_no,faculty_id,course_id,hour) VALUES  (2018103006,10003,'CS6108',2);
INSERT INTO Attendance_Log (roll_no,faculty_id,course_id,hour) VALUES  (2018103006,10004,'CS6202',-2);
INSERT INTO Attendance_Log (roll_no,faculty_id,course_id,hour) VALUES  (2018103006,17002,'CY6391',2);
