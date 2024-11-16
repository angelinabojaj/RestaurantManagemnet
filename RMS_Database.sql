-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: restaurantmangement
-- ------------------------------------------------------
-- Server version	8.0.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `absent_request`
--

DROP TABLE IF EXISTS `absent_request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `absent_request` (
  `employeeIDNumber` int NOT NULL,
  `timeOff` time NOT NULL,
  PRIMARY KEY (`employeeIDNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `absent_request`
--

LOCK TABLES `absent_request` WRITE;
/*!40000 ALTER TABLE `absent_request` DISABLE KEYS */;
/*!40000 ALTER TABLE `absent_request` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `employeeIDNumber` int NOT NULL,
  `employeeName` varchar(45) NOT NULL,
  `shiftType` varchar(45) NOT NULL,
  `clockInTime` time NOT NULL,
  `clockOutTime` time NOT NULL,
  `break` time NOT NULL,
  `averagePerformanceNumber` decimal(3,0) NOT NULL,
  `managerOrNot` tinyint NOT NULL,
  PRIMARY KEY (`employeeIDNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,'AngelinaBojaj','1','12:45:30','13:45:30','12:50:30',5,1),(2,'MichaelJackson','1','12:45:30','13:45:30','12:54:30',8,0),(3,'RitaMansoor','2','12:45:30','13:45:30','12:54:24',6,0),(4,'EmmaFarrell','3','12:45:30','13:45:30','12:50:30',7,0);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manager`
--

DROP TABLE IF EXISTS `manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manager` (
  `employeeIDNumber` int NOT NULL,
  `employeeName` varchar(45) NOT NULL,
  `clockInTime` time NOT NULL,
  `clockOutTime` time NOT NULL,
  `break` time NOT NULL,
  PRIMARY KEY (`employeeIDNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manager`
--

LOCK TABLES `manager` WRITE;
/*!40000 ALTER TABLE `manager` DISABLE KEYS */;
/*!40000 ALTER TABLE `manager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu`
--

DROP TABLE IF EXISTS `menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menu` (
  `menuItemID` int NOT NULL,
  `foodOrDrink` varchar(45) NOT NULL,
  `itemName` varchar(45) NOT NULL,
  `itemType` varchar(45) NOT NULL,
  `itemDescription` varchar(45) NOT NULL,
  `itemAllergies` varchar(45) NOT NULL,
  `itemSpecialsFlag` tinyint NOT NULL,
  `itemPrice` decimal(10,0) NOT NULL,
  `itemPicture` blob NOT NULL,
  PRIMARY KEY (`menuItemID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu`
--

LOCK TABLES `menu` WRITE;
/*!40000 ALTER TABLE `menu` DISABLE KEYS */;
/*!40000 ALTER TABLE `menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notifcations`
--

DROP TABLE IF EXISTS `notifcations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notifcations` (
  `employeeIDNumber` int NOT NULL,
  `employeeName` varchar(45) NOT NULL,
  `chatTitle` varchar(45) NOT NULL,
  `chatMessage` varchar(150) NOT NULL,
  `time` time NOT NULL,
  PRIMARY KEY (`employeeIDNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notifcations`
--

LOCK TABLES `notifcations` WRITE;
/*!40000 ALTER TABLE `notifcations` DISABLE KEYS */;
INSERT INTO `notifcations` VALUES (1,'AngelinaBojaj','Hello','Hello','12:45:30'),(2,'MichaelJackson','Hello','Hello','12:30:40');
/*!40000 ALTER TABLE `notifcations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `restaurant`
--

DROP TABLE IF EXISTS `restaurant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `restaurant` (
  `restaurantIDNumber` int NOT NULL,
  `restaurantName` varchar(45) NOT NULL,
  `location` varchar(45) NOT NULL,
  `hoursOfOperation` varchar(45) NOT NULL,
  PRIMARY KEY (`restaurantIDNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restaurant`
--

LOCK TABLES `restaurant` WRITE;
/*!40000 ALTER TABLE `restaurant` DISABLE KEYS */;
/*!40000 ALTER TABLE `restaurant` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-16 16:56:03
