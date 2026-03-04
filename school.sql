CREATE DATABASE IF NOT EXISTS school;
USE school;

CREATE TABLE Student (
    StudentID   INT PRIMARY KEY,
    StudentName VARCHAR(100) NOT NULL,
    Email       VARCHAR(150) NOT NULL
);

CREATE TABLE Club (
    ClubID      VARCHAR(10) PRIMARY KEY,
    ClubName    VARCHAR(100) NOT NULL,
    ClubRoom    VARCHAR(20),
    ClubMentor  VARCHAR(100)
);

CREATE TABLE Membership (
    MembershipID INT PRIMARY KEY,
    StudentID    INT NOT NULL,
    ClubID       VARCHAR(10) NOT NULL,
    JoinDate     DATE NOT NULL,
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (ClubID)    REFERENCES Club(ClubID)
);

INSERT INTO Student (StudentID, StudentName, Email)
VALUES (8, 'Priya', 'priya@email.com');

INSERT INTO Club (ClubID, ClubName, ClubRoom, ClubMentor)
VALUES ('C5', 'Photography Club', 'R404', 'Ms. Lata');

SELECT
    s.StudentName,
    c.ClubName,
    m.JoinDate
FROM Membership m
INNER JOIN Student s ON m.StudentID = s.StudentID
INNER JOIN Club c ON m.ClubID = c.ClubID
ORDER BY m.JoinDate ASC;