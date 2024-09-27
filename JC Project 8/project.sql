-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `found`
--

DROP TABLE IF EXISTS `found`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `found` (
  `item_id` int DEFAULT NULL,
  `category` varchar(40) DEFAULT NULL,
  `item` varchar(40) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `found_location` varchar(40) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `pic` longblob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `found`
--

LOCK TABLES `found` WRITE;
/*!40000 ALTER TABLE `found` DISABLE KEYS */;
INSERT INTO `found` VALUES (144398,'Stationary','sdghateh','fgtheth','adfhadfh','keeru0000@gmail.com',_binary 'C:/Users/keeru/Documents/JC Project 8/CCPAPP.png'),(159217,'Valueables','jhftyehn','nf76r6uyh','nfytr87iyuk','keeru0000@gmail.com',_binary 'C:/Users/keeru/Pictures/Saved Pictures/twilight.jpg'),(154104,'Stationary','eryty','rtyur6','rtyu6','ghyru',_binary 'C:/Users/keeru/Pictures/Screenshots/Screenshot 2024-06-17 231654.png');
/*!40000 ALTER TABLE `found` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lost`
--

DROP TABLE IF EXISTS `lost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lost` (
  `item_id` int DEFAULT NULL,
  `category` varchar(40) DEFAULT NULL,
  `item` varchar(40) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `last_known_location` varchar(40) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lost`
--

LOCK TABLES `lost` WRITE;
/*!40000 ALTER TABLE `lost` DISABLE KEYS */;
INSERT INTO `lost` VALUES (142862,'Stationary','ftuttu','ryusrtu','sryius 647r46 ','keeru0000@gmail.com'),(137163,'Valueables','gold chain','gold','ghe5r6yjuh','keeru0000@gmail.com');
/*!40000 ALTER TABLE `lost` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `std`
--

DROP TABLE IF EXISTS `std`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `std` (
  `idno` varchar(10) NOT NULL,
  `fname` varchar(30) NOT NULL,
  `lname` varchar(30) NOT NULL,
  `uname` varchar(30) NOT NULL,
  `pass` varchar(40) DEFAULT NULL,
  `ccp` int DEFAULT NULL,
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `std`
--

LOCK TABLES `std` WRITE;
/*!40000 ALTER TABLE `std` DISABLE KEYS */;
INSERT INTO `std` VALUES ('163925','keerthana','a r','keer','keer',1100,'keeru0000@gmail.com'),('155433','k','e','k','k',0,'keeru0000@gmail.com'),('144185','k','k','k','k',0,'keeru0000@gmail.com');
/*!40000 ALTER TABLE `std` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-28  0:03:15
