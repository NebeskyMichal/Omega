-- Project: GBLD
-- Author: Michal Nebesky
-- Contact: michalnebesky1@gmail.com

BEGIN TRANSACTION
USE [master]
GO
/****** Object:  Database [GameRatings]    Script Date: 4/18/2023 9:59:04 PM ******/
CREATE DATABASE [GameRatings]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'GameRatings', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.SQLEXPRESS03\MSSQL\DATA\GameRatings.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'GameRatings_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.SQLEXPRESS03\MSSQL\DATA\GameRatings_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT, LEDGER = OFF
GO
ALTER DATABASE [GameRatings] SET COMPATIBILITY_LEVEL = 160
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [GameRatings].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [GameRatings] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [GameRatings] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [GameRatings] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [GameRatings] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [GameRatings] SET ARITHABORT OFF 
GO
ALTER DATABASE [GameRatings] SET AUTO_CLOSE ON 
GO
ALTER DATABASE [GameRatings] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [GameRatings] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [GameRatings] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [GameRatings] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [GameRatings] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [GameRatings] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [GameRatings] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [GameRatings] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [GameRatings] SET  ENABLE_BROKER 
GO
ALTER DATABASE [GameRatings] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [GameRatings] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [GameRatings] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [GameRatings] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [GameRatings] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [GameRatings] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [GameRatings] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [GameRatings] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [GameRatings] SET  MULTI_USER 
GO
ALTER DATABASE [GameRatings] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [GameRatings] SET DB_CHAINING OFF 
GO
ALTER DATABASE [GameRatings] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [GameRatings] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [GameRatings] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [GameRatings] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
ALTER DATABASE [GameRatings] SET QUERY_STORE = ON
GO
ALTER DATABASE [GameRatings] SET QUERY_STORE (OPERATION_MODE = READ_WRITE, CLEANUP_POLICY = (STALE_QUERY_THRESHOLD_DAYS = 30), DATA_FLUSH_INTERVAL_SECONDS = 900, INTERVAL_LENGTH_MINUTES = 60, MAX_STORAGE_SIZE_MB = 1000, QUERY_CAPTURE_MODE = AUTO, SIZE_BASED_CLEANUP_MODE = AUTO, MAX_PLANS_PER_QUERY = 200, WAIT_STATS_CAPTURE_MODE = ON)
GO
USE [GameRatings]
GO
/****** Object:  User [admin]    Script Date: 4/18/2023 9:59:04 PM ******/
CREATE USER [admin] FOR LOGIN [admin] WITH DEFAULT_SCHEMA=[dbo]
GO
ALTER ROLE [db_owner] ADD MEMBER [admin]
GO
/****** Object:  Table [dbo].[Admins]    Script Date: 4/18/2023 9:59:04 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Admins](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[username] [nvarchar](50) NOT NULL,
	[email] [nvarchar](100) NOT NULL,
	[password] [nvarchar](100) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Bans]    Script Date: 4/18/2023 9:59:04 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Bans](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[users_id] [int] NULL,
	[admins_id] [int] NULL,
	[release_date] [date] NOT NULL,
	[reason] [nvarchar](500) NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Games]    Script Date: 4/18/2023 9:59:04 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Games](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[publisher_id] [int] NULL,
	[title] [nvarchar](100) NOT NULL,
	[release_date] [date] NOT NULL,
	[global_rating] [float] NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Publishers]    Script Date: 4/18/2023 9:59:04 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Publishers](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[name] [nvarchar](100) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Ratings]    Script Date: 4/18/2023 9:59:04 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Ratings](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[users_id] [int] NULL,
	[game_id] [int] NULL,
	[rating] [float] NOT NULL,
	[review] [nvarchar](500) NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Reports]    Script Date: 4/18/2023 9:59:04 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Reports](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[reporter_id] [int] NULL,
	[reported_id] [int] NULL,
	[checked] [char](1) NOT NULL,
	[reason] [nvarchar](500) NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Users]    Script Date: 4/18/2023 9:59:04 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Users](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[username] [nvarchar](50) NOT NULL,
	[email] [nvarchar](100) NOT NULL,
	[password] [nvarchar](100) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
SET IDENTITY_INSERT [dbo].[Admins] ON 
GO
INSERT [dbo].[Admins] ([id], [username], [email], [password]) VALUES (1, N'admin', N'admin@example.com', N'$2a$12$vbClpZYWUbUOFHYzSqnHX.nXUptVuzNy39GOXPf5OW43gWxOirz3S')
GO
INSERT [dbo].[Admins] ([id], [username], [email], [password]) VALUES (2, N'test_admin2', N'test_admin2@example.com', N'new_password')
GO
SET IDENTITY_INSERT [dbo].[Admins] OFF
GO
SET IDENTITY_INSERT [dbo].[Games] ON 
GO
INSERT [dbo].[Games] ([id], [publisher_id], [title], [release_date], [global_rating]) VALUES (1, 1, N'FIFA 22', CAST(N'2021-10-01' AS Date), 8.5)
GO
INSERT [dbo].[Games] ([id], [publisher_id], [title], [release_date], [global_rating]) VALUES (2, 1, N'Madden NFL 22', CAST(N'2021-08-20' AS Date), 6)
GO
INSERT [dbo].[Games] ([id], [publisher_id], [title], [release_date], [global_rating]) VALUES (3, 2, N'Call of Duty: Vanguard', CAST(N'2021-11-05' AS Date), 9.2)
GO
INSERT [dbo].[Games] ([id], [publisher_id], [title], [release_date], [global_rating]) VALUES (4, 2, N'Overwatch 2', CAST(N'2022-10-04' AS Date), 8.3)
GO
INSERT [dbo].[Games] ([id], [publisher_id], [title], [release_date], [global_rating]) VALUES (5, 3, N'Assassins Creed Valhalla', CAST(N'2020-11-10' AS Date), 8.9)
GO
INSERT [dbo].[Games] ([id], [publisher_id], [title], [release_date], [global_rating]) VALUES (6, 3, N'Far Cry 6', CAST(N'2021-10-07' AS Date), 7.5)
GO
INSERT [dbo].[Games] ([id], [publisher_id], [title], [release_date], [global_rating]) VALUES (7, 4, N'Zelda: Breath of the Wild', CAST(N'2017-03-03' AS Date), 8)
GO
INSERT [dbo].[Games] ([id], [publisher_id], [title], [release_date], [global_rating]) VALUES (8, 4, N'Super Mario Odyssey', CAST(N'2017-10-27' AS Date), 9.5)
GO
INSERT [dbo].[Games] ([id], [publisher_id], [title], [release_date], [global_rating]) VALUES (9, 5, N'The Last of Us Part II', CAST(N'2020-06-19' AS Date), 6.5)
GO
INSERT [dbo].[Games] ([id], [publisher_id], [title], [release_date], [global_rating]) VALUES (10, 5, N'Ghost of Tsushima', CAST(N'2020-07-17' AS Date), 9.75)
GO
INSERT [dbo].[Games] ([id], [publisher_id], [title], [release_date], [global_rating]) VALUES (11, 6, N'Halo Infinite', CAST(N'2021-12-08' AS Date), 8.7)
GO
INSERT [dbo].[Games] ([id], [publisher_id], [title], [release_date], [global_rating]) VALUES (12, 6, N'Forza Horizon 5', CAST(N'2021-11-09' AS Date), 7)
GO
INSERT [dbo].[Games] ([id], [publisher_id], [title], [release_date], [global_rating]) VALUES (13, 7, N'Grand Theft Auto V', CAST(N'2013-09-17' AS Date), 8.9)
GO
INSERT [dbo].[Games] ([id], [publisher_id], [title], [release_date], [global_rating]) VALUES (14, 7, N'Red Dead Redemption 2', CAST(N'2018-10-26' AS Date), 9.8)
GO
INSERT [dbo].[Games] ([id], [publisher_id], [title], [release_date], [global_rating]) VALUES (15, 8, N'Final Fantasy VII Remake', CAST(N'2020-04-10' AS Date), 7.3)
GO
INSERT [dbo].[Games] ([id], [publisher_id], [title], [release_date], [global_rating]) VALUES (16, 8, N'Kingdom Hearts III', CAST(N'2019-01-29' AS Date), 8.5)
GO
INSERT [dbo].[Games] ([id], [publisher_id], [title], [release_date], [global_rating]) VALUES (17, 9, N'Resident Evil Village', CAST(N'2021-05-07' AS Date), 8)
GO
INSERT [dbo].[Games] ([id], [publisher_id], [title], [release_date], [global_rating]) VALUES (18, 9, N'Monster Hunter: Rise', CAST(N'2021-03-26' AS Date), 6.7)
GO
INSERT [dbo].[Games] ([id], [publisher_id], [title], [release_date], [global_rating]) VALUES (19, 10, N'Fallout 4', CAST(N'2015-11-10' AS Date), 9.8)
GO
INSERT [dbo].[Games] ([id], [publisher_id], [title], [release_date], [global_rating]) VALUES (20, 10, N'The Elder Scrolls V: Skyrim', CAST(N'2011-11-11' AS Date), 9)
GO
SET IDENTITY_INSERT [dbo].[Games] OFF
GO
SET IDENTITY_INSERT [dbo].[Publishers] ON 
GO
INSERT [dbo].[Publishers] ([id], [name]) VALUES (1, N'Electronic Arts')
GO
INSERT [dbo].[Publishers] ([id], [name]) VALUES (2, N'Activision Blizzard')
GO
INSERT [dbo].[Publishers] ([id], [name]) VALUES (3, N'Ubisoft')
GO
INSERT [dbo].[Publishers] ([id], [name]) VALUES (4, N'Nintendo')
GO
INSERT [dbo].[Publishers] ([id], [name]) VALUES (5, N'Sony Interactive Entertainment')
GO
INSERT [dbo].[Publishers] ([id], [name]) VALUES (6, N'Microsoft Studios')
GO
INSERT [dbo].[Publishers] ([id], [name]) VALUES (7, N'Take-Two Interactive')
GO
INSERT [dbo].[Publishers] ([id], [name]) VALUES (8, N'Square Enix')
GO
INSERT [dbo].[Publishers] ([id], [name]) VALUES (9, N'Capcom')
GO
INSERT [dbo].[Publishers] ([id], [name]) VALUES (10, N'Bethesda Softworks')
GO
INSERT [dbo].[Publishers] ([id], [name]) VALUES (11, N'Test Publisher')
GO
SET IDENTITY_INSERT [dbo].[Publishers] OFF
GO
SET IDENTITY_INSERT [dbo].[Ratings] ON 
GO
INSERT [dbo].[Ratings] ([id], [users_id], [game_id], [rating], [review]) VALUES (1, 1, 1, 8.5, N'Great graphics and gameplay')
GO
INSERT [dbo].[Ratings] ([id], [users_id], [game_id], [rating], [review]) VALUES (2, 1, 10, 10, N'Great graphics and gameplay')
GO
INSERT [dbo].[Ratings] ([id], [users_id], [game_id], [rating], [review]) VALUES (3, 2, 3, 9.2, N'Loved the campaign, multiplayer needs work')
GO
INSERT [dbo].[Ratings] ([id], [users_id], [game_id], [rating], [review]) VALUES (4, 2, 5, 10, N'Loved the campaign, multiplayer needs work')
GO
INSERT [dbo].[Ratings] ([id], [users_id], [game_id], [rating], [review]) VALUES (5, 3, 5, 7.8, N'Fun open world, combat gets repetitive')
GO
INSERT [dbo].[Ratings] ([id], [users_id], [game_id], [rating], [review]) VALUES (6, 4, 8, 9.5, N'One of the best Zelda games ever made')
GO
INSERT [dbo].[Ratings] ([id], [users_id], [game_id], [rating], [review]) VALUES (7, 5, 9, 6.5, N'Disappointed with the story and character development')
GO
INSERT [dbo].[Ratings] ([id], [users_id], [game_id], [rating], [review]) VALUES (8, 6, 11, 8.7, N'Gorgeous graphics and fun gameplay, but not enough variety')
GO
INSERT [dbo].[Ratings] ([id], [users_id], [game_id], [rating], [review]) VALUES (9, 7, 13, 8.9, N'Amazing story and characters, but the online mode is buggy')
GO
INSERT [dbo].[Ratings] ([id], [users_id], [game_id], [rating], [review]) VALUES (10, 8, 15, 7.3, N'Enjoyable but too many cutscenes')
GO
INSERT [dbo].[Ratings] ([id], [users_id], [game_id], [rating], [review]) VALUES (11, 9, 17, 8, N'Great atmosphere and enemy design, but some of the bosses are too difficult')
GO
INSERT [dbo].[Ratings] ([id], [users_id], [game_id], [rating], [review]) VALUES (12, 10, 19, 9.8, N'One of the best RPGs ever made, worth playing even if you already played Fallout 3')
GO
INSERT [dbo].[Ratings] ([id], [users_id], [game_id], [rating], [review]) VALUES (13, 1, 2, 6, N'Disappointed with the graphics and controls')
GO
INSERT [dbo].[Ratings] ([id], [users_id], [game_id], [rating], [review]) VALUES (14, 2, 4, 8.3, N'Great story and voice acting, but the gameplay gets repetitive')
GO
INSERT [dbo].[Ratings] ([id], [users_id], [game_id], [rating], [review]) VALUES (15, 3, 6, 7.5, N'Good game, but overhyped')
GO
INSERT [dbo].[Ratings] ([id], [users_id], [game_id], [rating], [review]) VALUES (16, 4, 7, 8, N'Fun multiplayer but the matchmaking needs improvement')
GO
INSERT [dbo].[Ratings] ([id], [users_id], [game_id], [rating], [review]) VALUES (17, 5, 10, 9.5, N'Amazing game, highly recommend it')
GO
INSERT [dbo].[Ratings] ([id], [users_id], [game_id], [rating], [review]) VALUES (18, 6, 12, 7, N'Decent graphics, but the story is lacking')
GO
INSERT [dbo].[Ratings] ([id], [users_id], [game_id], [rating], [review]) VALUES (19, 7, 14, 9.8, N'One of the best racing games ever made')
GO
INSERT [dbo].[Ratings] ([id], [users_id], [game_id], [rating], [review]) VALUES (20, 8, 16, 8.5, N'Great gameplay but the story is predictable')
GO
INSERT [dbo].[Ratings] ([id], [users_id], [game_id], [rating], [review]) VALUES (21, 9, 18, 6.7, N'Too much grinding required to progress')
GO
INSERT [dbo].[Ratings] ([id], [users_id], [game_id], [rating], [review]) VALUES (22, 10, 20, 9, N'Great graphics and fun gameplay, but too short')
GO
SET IDENTITY_INSERT [dbo].[Ratings] OFF
GO
SET IDENTITY_INSERT [dbo].[Reports] ON 
GO
INSERT [dbo].[Reports] ([id], [reporter_id], [reported_id], [checked], [reason]) VALUES (1, 1, 2, N'1', N'Inappropriate content')
GO
INSERT [dbo].[Reports] ([id], [reporter_id], [reported_id], [checked], [reason]) VALUES (2, 1, 3, N'1', N'Harassment')
GO
INSERT [dbo].[Reports] ([id], [reporter_id], [reported_id], [checked], [reason]) VALUES (3, 2, 3, N'0', N'Spam')
GO
INSERT [dbo].[Reports] ([id], [reporter_id], [reported_id], [checked], [reason]) VALUES (4, 3, 1, N'1', N'Hate speech')
GO
INSERT [dbo].[Reports] ([id], [reporter_id], [reported_id], [checked], [reason]) VALUES (5, 2, 1, N'0', N'Fake news')
GO
SET IDENTITY_INSERT [dbo].[Reports] OFF
GO
SET IDENTITY_INSERT [dbo].[Users] ON 
GO
INSERT [dbo].[Users] ([id], [username], [email], [password]) VALUES (1, N'john_doe', N'johndoe@example.com', N'$2b$12$lXDC2LJco.LY4Z4z4/DCbeNp3qcc3f8OyNzplgJfXklo5e5ooUGZK')
GO
INSERT [dbo].[Users] ([id], [username], [email], [password]) VALUES (2, N'jane_smith', N'janesmith@example.com', N'$2b$12$jP5WXskWWtLx7tEZ/MKNIOyIRnhyQkJnnMdx9R2/a78Mg.Lnm4RuK')
GO
INSERT [dbo].[Users] ([id], [username], [email], [password]) VALUES (3, N'alex_turner', N'alexturner@example.com', N'$2b$12$Uzt0vUENx6UwPS6T8Wlmr.yh6HL/mV7EPmZxsY8V7a2jDmSY.7/Yu')
GO
INSERT [dbo].[Users] ([id], [username], [email], [password]) VALUES (4, N'sara_cohen', N'saracohen@example.com', N'$2b$12$p6owwWjAr8r6oL9XzJCBLeDrmV7Y8jvQ2h7qlGnPFdHyPtLz8HvKu')
GO
INSERT [dbo].[Users] ([id], [username], [email], [password]) VALUES (5, N'mike_smith', N'mikesmith@example.com', N'$2b$12$DYI9gQR1ax2eiHFXZ.LN4.y4.JpKj3cbOqOtxyNJ.ZFylnKNI/zIG')
GO
INSERT [dbo].[Users] ([id], [username], [email], [password]) VALUES (6, N'anna_watson', N'annawatson@example.com', N'$2b$12$fD5fOVzmmZwLNS8E2kiG.OxbIYbFvkLxomD8ZWXq9Mg1jZnUelw6i')
GO
INSERT [dbo].[Users] ([id], [username], [email], [password]) VALUES (7, N'david_brown', N'davidbrown@example.com', N'$2b$12$kW0hzl2vOYjKlSNBShmI3.x3qZmCjOlrz.Om0D8/6Ibgg6YpYklUO')
GO
INSERT [dbo].[Users] ([id], [username], [email], [password]) VALUES (8, N'amy_johnson', N'amyjohnson@example.com', N'$2b$12$bjQkV1xOIivjDeuF7SjBcugssjFw3nxq5ql5L5Ht.y66pxfZgjXZ2')
GO
INSERT [dbo].[Users] ([id], [username], [email], [password]) VALUES (9, N'peter_miller', N'petermiller@example.com', N'$2b$12$n2zOhDkHfh90jh7EWGwCROJjj7V4yf81N2EUnbOjJhDee.KS61cOu')
GO
INSERT [dbo].[Users] ([id], [username], [email], [password]) VALUES (10, N'sophie_taylor', N'sophietaylor@example.com', N'$2b$12$8CwRgRYvQYwwKjwhRWoCxujnAq9ZvB1KquDWPLH6zj2AKGtHVKuKK')
GO
INSERT [dbo].[Users] ([id], [username], [email], [password]) VALUES (11, N'TestUser', N'test@example.com', N'$2b$12$1ttuR.4CS0pFY7UjpLUyCOYlTGQVKUeM8gh9vxmGZMr2MY2jSlvBy')
GO
SET IDENTITY_INSERT [dbo].[Users] OFF
GO
ALTER TABLE [dbo].[Bans]  WITH CHECK ADD FOREIGN KEY([admins_id])
REFERENCES [dbo].[Admins] ([id])
GO
ALTER TABLE [dbo].[Bans]  WITH CHECK ADD FOREIGN KEY([users_id])
REFERENCES [dbo].[Users] ([id])
GO
ALTER TABLE [dbo].[Games]  WITH CHECK ADD FOREIGN KEY([publisher_id])
REFERENCES [dbo].[Publishers] ([id])
GO
ALTER TABLE [dbo].[Ratings]  WITH CHECK ADD FOREIGN KEY([game_id])
REFERENCES [dbo].[Games] ([id])
GO
ALTER TABLE [dbo].[Ratings]  WITH CHECK ADD FOREIGN KEY([users_id])
REFERENCES [dbo].[Users] ([id])
GO
ALTER TABLE [dbo].[Reports]  WITH CHECK ADD FOREIGN KEY([reporter_id])
REFERENCES [dbo].[Users] ([id])
GO
ALTER TABLE [dbo].[Reports]  WITH CHECK ADD FOREIGN KEY([reported_id])
REFERENCES [dbo].[Users] ([id])
GO
ALTER TABLE [dbo].[Ratings]  WITH CHECK ADD  CONSTRAINT [chk_rating] CHECK  (([rating]>=(1) AND [rating]<=(10)))
GO
ALTER TABLE [dbo].[Ratings] CHECK CONSTRAINT [chk_rating]
GO
ALTER TABLE [dbo].[Reports]  WITH CHECK ADD CHECK  (([checked]=(1) OR [checked]=(0)))
GO
/****** Object:  Trigger [dbo].[update_game_rating]    Script Date: 4/18/2023 9:59:04 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TRIGGER [dbo].[update_game_rating]
ON [dbo].[Ratings]
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
GO
ALTER TABLE [dbo].[Ratings] ENABLE TRIGGER [update_game_rating]
GO
USE [master]
GO
ALTER DATABASE [GameRatings] SET  READ_WRITE 
GO
COMMIT TRANSACTION