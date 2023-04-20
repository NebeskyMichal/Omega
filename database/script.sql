create database GameRatings;

use GameRatings;

CREATE TABLE Users (
    id INT PRIMARY KEY IDENTITY(1,1),
    username NVARCHAR(50) NOT NULL,
    email NVARCHAR(100) NOT NULL,
    password NVARCHAR(100) NOT NULL
);

CREATE TABLE Publishers (
    id INT PRIMARY KEY IDENTITY(1,1),
    name NVARCHAR(100) NOT NULL
);

CREATE TABLE Games (
    id INT PRIMARY KEY IDENTITY(1,1),
	publisher_id INT FOREIGN KEY REFERENCES Publishers(id),
    title NVARCHAR(100) NOT NULL,
    release_date DATE NOT NULL,
    global_rating FLOAT
);

CREATE TABLE Ratings (
    id INT PRIMARY KEY IDENTITY(1,1),
    users_id INT FOREIGN KEY REFERENCES Users(id),
    game_id INT FOREIGN KEY REFERENCES Games(id),
    rating float NOT NULL,
    review NVARCHAR(500),
    CONSTRAINT chk_rating CHECK (rating BETWEEN 1 AND 10)
);

CREATE TABLE Admins (
    id INT PRIMARY KEY IDENTITY(1,1),
    username NVARCHAR(50) NOT NULL,
    email NVARCHAR(100) NOT NULL,
    password NVARCHAR(100) NOT NULL
);

create table Bans (
	id INT PRIMARY KEY IDENTITY(1,1),
    users_id INT FOREIGN KEY REFERENCES Users(id),
    admins_id INT FOREIGN KEY REFERENCES Admins(id),
    release_date DATE NOT NULL,
	reason NVARCHAR(500)
);

create table Reports(
	id int PRIMARY KEY IDENTITY(1,1),
	reporter_id int foreign key references Users(id),
	reported_id int foreign key references Users(id),
	checked char(1) not null, check(checked in (0,1)),
	reason NVARCHAR(500)
);

CREATE TRIGGER update_game_rating
ON Ratings
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
    DECLARE @game_id INT;
    DECLARE @global_rating FLOAT;

    IF EXISTS (SELECT * FROM inserted)
    BEGIN
        SELECT @game_id = game_id FROM inserted;
    END
    ELSE IF EXISTS (SELECT * FROM deleted)
    BEGIN
        SELECT @game_id = game_id FROM deleted;
    END
    
    SELECT @global_rating = AVG(rating) FROM Ratings WHERE game_id = @game_id;
    
    UPDATE Games SET global_rating = @global_rating WHERE id = @game_id;
END;

INSERT INTO Publishers (name) VALUES ('Electronic Arts');
INSERT INTO Publishers (name) VALUES ('Activision Blizzard');
INSERT INTO Publishers (name) VALUES ('Ubisoft');
INSERT INTO Publishers (name) VALUES ('Nintendo');
INSERT INTO Publishers (name) VALUES ('Sony Interactive Entertainment');
INSERT INTO Publishers (name) VALUES ('Microsoft Studios');
INSERT INTO Publishers (name) VALUES ('Take-Two Interactive');
INSERT INTO Publishers (name) VALUES ('Square Enix');
INSERT INTO Publishers (name) VALUES ('Capcom');
INSERT INTO Publishers (name) VALUES ('Bethesda Softworks');

INSERT INTO Games (publisher_id, title, release_date, global_rating) VALUES (1, 'FIFA 22', '2021-10-01', 0);
INSERT INTO Games (publisher_id, title, release_date, global_rating) VALUES (1, 'Madden NFL 22', '2021-08-20', 0);
INSERT INTO Games (publisher_id, title, release_date, global_rating) VALUES (2, 'Call of Duty: Vanguard', '2021-11-05', 0);
INSERT INTO Games (publisher_id, title, release_date, global_rating) VALUES (2, 'Overwatch 2', '2022-10-04', 0);
INSERT INTO Games (publisher_id, title, release_date, global_rating) VALUES (3, 'Assassins Creed Valhalla', '2020-11-10', 0);
INSERT INTO Games (publisher_id, title, release_date, global_rating) VALUES (3, 'Far Cry 6', '2021-10-07', 0);
INSERT INTO Games (publisher_id, title, release_date, global_rating) VALUES (4, 'Zelda: Breath of the Wild', '2017-03-03', 0);
INSERT INTO Games (publisher_id, title, release_date, global_rating) VALUES (4, 'Super Mario Odyssey', '2017-10-27', 0);
INSERT INTO Games (publisher_id, title, release_date, global_rating) VALUES (5, 'The Last of Us Part II', '2020-06-19', 0);
INSERT INTO Games (publisher_id, title, release_date, global_rating) VALUES (5, 'Ghost of Tsushima', '2020-07-17', 0);
INSERT INTO Games (publisher_id, title, release_date, global_rating) VALUES (6, 'Halo Infinite', '2021-12-08', 0);
INSERT INTO Games (publisher_id, title, release_date, global_rating) VALUES (6, 'Forza Horizon 5', '2021-11-09', 0);
INSERT INTO Games (publisher_id, title, release_date, global_rating) VALUES (7, 'Grand Theft Auto V', '2013-09-17', 0);
INSERT INTO Games (publisher_id, title, release_date, global_rating) VALUES (7, 'Red Dead Redemption 2', '2018-10-26', 0);
INSERT INTO Games (publisher_id, title, release_date, global_rating) VALUES (8, 'Final Fantasy VII Remake', '2020-04-10', 0);
INSERT INTO Games (publisher_id, title, release_date, global_rating) VALUES (8, 'Kingdom Hearts III', '2019-01-29', 0);
INSERT INTO Games (publisher_id, title, release_date, global_rating) VALUES (9, 'Resident Evil Village', '2021-05-07', 0);
INSERT INTO Games (publisher_id, title, release_date, global_rating) VALUES (9, 'Monster Hunter: Rise', '2021-03-26', 0);
INSERT INTO Games (publisher_id, title, release_date, global_rating) VALUES (10, 'Fallout 4', '2015-11-10', 0);
INSERT INTO Games (publisher_id, title, release_date, global_rating) VALUES (10, 'The Elder Scrolls V: Skyrim', '2011-11-11', 0);

INSERT INTO Users (username, email, password) VALUES ('john_doe', 'johndoe@example.com', '$2b$12$lXDC2LJco.LY4Z4z4/DCbeNp3qcc3f8OyNzplgJfXklo5e5ooUGZK');
INSERT INTO Users (username, email, password) VALUES ('jane_smith', 'janesmith@example.com', '$2b$12$jP5WXskWWtLx7tEZ/MKNIOyIRnhyQkJnnMdx9R2/a78Mg.Lnm4RuK');
INSERT INTO Users (username, email, password) VALUES ('alex_turner', 'alexturner@example.com', '$2b$12$Uzt0vUENx6UwPS6T8Wlmr.yh6HL/mV7EPmZxsY8V7a2jDmSY.7/Yu');
INSERT INTO Users (username, email, password) VALUES ('sara_cohen', 'saracohen@example.com', '$2b$12$p6owwWjAr8r6oL9XzJCBLeDrmV7Y8jvQ2h7qlGnPFdHyPtLz8HvKu');
INSERT INTO Users (username, email, password) VALUES ('mike_smith', 'mikesmith@example.com', '$2b$12$DYI9gQR1ax2eiHFXZ.LN4.y4.JpKj3cbOqOtxyNJ.ZFylnKNI/zIG');
INSERT INTO Users (username, email, password) VALUES ('anna_watson', 'annawatson@example.com', '$2b$12$fD5fOVzmmZwLNS8E2kiG.OxbIYbFvkLxomD8ZWXq9Mg1jZnUelw6i');
INSERT INTO Users (username, email, password) VALUES ('david_brown', 'davidbrown@example.com', '$2b$12$kW0hzl2vOYjKlSNBShmI3.x3qZmCjOlrz.Om0D8/6Ibgg6YpYklUO');
INSERT INTO Users (username, email, password) VALUES ('amy_johnson', 'amyjohnson@example.com', '$2b$12$bjQkV1xOIivjDeuF7SjBcugssjFw3nxq5ql5L5Ht.y66pxfZgjXZ2');
INSERT INTO Users (username, email, password) VALUES ('peter_miller', 'petermiller@example.com', '$2b$12$n2zOhDkHfh90jh7EWGwCROJjj7V4yf81N2EUnbOjJhDee.KS61cOu');
INSERT INTO Users (username, email, password) VALUES ('sophie_taylor', 'sophietaylor@example.com', '$2b$12$8CwRgRYvQYwwKjwhRWoCxujnAq9ZvB1KquDWPLH6zj2AKGtHVKuKK');

INSERT INTO Ratings (users_id, game_id, rating, review)
VALUES (1, 1, 8.5, 'Great graphics and gameplay');

INSERT INTO Ratings (users_id, game_id, rating, review)
VALUES (1, 10, 10, 'Great graphics and gameplay');

INSERT INTO Ratings (users_id, game_id, rating, review)
VALUES (2, 3, 9.2, 'Loved the campaign, multiplayer needs work');

INSERT INTO Ratings (users_id, game_id, rating, review)
VALUES (2, 5, 10, 'Loved the campaign, multiplayer needs work');

INSERT INTO Ratings (users_id, game_id, rating, review)
VALUES (3, 5, 7.8, 'Fun open world, combat gets repetitive');

INSERT INTO Ratings (users_id, game_id, rating, review)
VALUES (4, 8, 9.5, 'One of the best Zelda games ever made');

INSERT INTO Ratings (users_id, game_id, rating, review)
VALUES (5, 9, 6.5, 'Disappointed with the story and character development');

INSERT INTO Ratings (users_id, game_id, rating, review)
VALUES (6, 11, 8.7, 'Gorgeous graphics and fun gameplay, but not enough variety');

INSERT INTO Ratings (users_id, game_id, rating, review)
VALUES (7, 13, 8.9, 'Amazing story and characters, but the online mode is buggy');

INSERT INTO Ratings (users_id, game_id, rating, review)
VALUES (8, 15, 7.3, 'Enjoyable but too many cutscenes');

INSERT INTO Ratings (users_id, game_id, rating, review)
VALUES (9, 17, 8.0, 'Great atmosphere and enemy design, but some of the bosses are too difficult');

INSERT INTO Ratings (users_id, game_id, rating, review)
VALUES (10, 19, 9.8, 'One of the best RPGs ever made, worth playing even if you already played Fallout 3');

INSERT INTO Ratings (users_id, game_id, rating, review)
VALUES (1, 2, 6.0, 'Disappointed with the graphics and controls');

INSERT INTO Ratings (users_id, game_id, rating, review)
VALUES (2, 4, 8.3, 'Great story and voice acting, but the gameplay gets repetitive');

INSERT INTO Ratings (users_id, game_id, rating, review)
VALUES (3, 6, 7.5, 'Good game, but overhyped');

INSERT INTO Ratings (users_id, game_id, rating, review)
VALUES (4, 7, 8.0, 'Fun multiplayer but the matchmaking needs improvement');

INSERT INTO Ratings (users_id, game_id, rating, review)
VALUES (5, 10, 9.5, 'Amazing game, highly recommend it');

INSERT INTO Ratings (users_id, game_id, rating, review)
VALUES (6, 12, 7.0, 'Decent graphics, but the story is lacking');

INSERT INTO Ratings (users_id, game_id, rating, review)
VALUES (7, 14, 9.8, 'One of the best racing games ever made');

INSERT INTO Ratings (users_id, game_id, rating, review)
VALUES (8, 16, 8.5, 'Great gameplay but the story is predictable');

INSERT INTO Ratings (users_id, game_id, rating, review)
VALUES (9, 18, 6.7, 'Too much grinding required to progress');

INSERT INTO Ratings (users_id, game_id, rating, review)
VALUES (10, 20, 9.0, 'Great graphics and fun gameplay, but too short');

INSERT INTO Reports(reporter_id, reported_id, checked, reason)
VALUES
(1, 2, '1', 'Inappropriate content'),
(1, 3, '1', 'Harassment'),
(2, 3, '0', 'Spam'),
(3, 1, '1', 'Hate speech'),
(2, 1, '0', 'Fake news');

INSERT [Admins] ([username], [email], [password]) VALUES (N'admin', N'admin@example.com', N'$2a$12$vbClpZYWUbUOFHYzSqnHX.nXUptVuzNy39GOXPf5OW43gWxOirz3S')