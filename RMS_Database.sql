-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: rms
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
  PRIMARY KEY (`employeeIDNumber`),
  UNIQUE KEY `employeeName` (`employeeName`)
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
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory` (
  `itemID` int NOT NULL AUTO_INCREMENT,
  `itemName` varchar(45) NOT NULL,
  `itemQuantity` int NOT NULL,
  `ranOut` tinyint NOT NULL,
  PRIMARY KEY (`itemID`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES (1,'Forks',200,0),(2,'Knives',200,0),(3,'Napkins',300,0),(4,'Small Plates',300,0),(5,'Large Plates',300,0),(6,'Take Out Bags',400,0),(7,'Chicken',200,0),(8,'Potatoes',5,0),(9,'Duck',0,1),(10,'Lettuce',40,0),(11,'Tomatoes',70,0),(12,'Crutons',0,1),(13,'Steak',89,0),(14,'Scallops',0,1),(15,'Onions',94,0),(16,'Corn',64,0),(17,'Canolis',34,0),(18,'Mostacoli',9,0),(19,'Pennie',0,1),(20,'Salmon',2,0);
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
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
  `menuItemID` int NOT NULL AUTO_INCREMENT,
  `foodOrDrink` varchar(45) NOT NULL,
  `itemName` varchar(45) NOT NULL,
  `itemType` varchar(45) NOT NULL,
  `itemDescription` varchar(1000) NOT NULL,
  `itemAllergies` varchar(45) NOT NULL,
  `itemSpecialsFlag` tinyint NOT NULL,
  `itemPicture` blob,
  PRIMARY KEY (`menuItemID`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu`
--

LOCK TABLES `menu` WRITE;
/*!40000 ALTER TABLE `menu` DISABLE KEYS */;
INSERT INTO `menu` VALUES (1,'Food','Eggs Benedict','Breakfast','Really fancy eggs','Eggs',1,_binary 'C:/Users/angel/OneDrive/Desktop/RMS_Database_MENU_PICTURES/Eggs Benedict.jpg'),(2,'Food','Royal Toast','Breakfast','Even fancier toast','Gluten',1,_binary '\'C:/Users/angel/OneDrive/Desktop/RMS_Database_MENU_PICTURES/Royal Toast.jpg'),(3,'Food','Meditteran Delight','Breakfast','A taste of the meditteranean sea','Gluten, Dairy',1,_binary '\'C:/Users/angel/OneDrive/Desktop/RMS_Database_MENU_PICTURES/Meditteran Delight.jpg\''),(4,'Food','Cevapi','Lunch','An Albanian staple food','Meat',0,_binary '\'C:/Users/angel/OneDrive/Desktop/RMS_Database_MENU_PICTURES/Cevapi.jpg\''),(5,'Food','All American Burger','Lunch','Meat, Bun, Lettuce, Tomatoe, Onion, Pickle, & All American','Meat, Gluten',0,_binary '\'C:/Users/angel/OneDrive/Desktop/RMS_Database_MENU_PICTURES/All American Burger.jpg\''),(6,'Food','Coney\'s Chicken Fingers','Lunch','Chicken, French fries. and ketchup','Pultry',1,_binary '\"C:\\Users\\angel\\OneDrive\\Desktop\\RMS_Database_MENU_PICTURES\\Coney\'s Chicken Fingers.jpg\"'),(7,'Food','100% Toally Steak','Dinner','Steak, mashed potatoes, and choice of vegetable','Meat, Gluten',0,_binary '\'C:/Users/angel/OneDrive/Desktop/RMS_Database_MENU_PICTURES/100% Totally Steak.jpg\''),(8,'Food','Ceaser Salad','Dinner','Lettuce, Crutons, Ceaser Dressing','Gluten',1,_binary '\"C:\\Users\\angel\\OneDrive\\Desktop\\RMS_Database_MENU_PICTURES\\Ceaser Salad.jpg\"'),(9,'Food','Just Caught Salmon','Dinner','Salmon, Brocolini, Potatoes, Rice','Seafood, Gluten',0,_binary '\"C:\\Users\\angel\\OneDrive\\Desktop\\RMS_Database_MENU_PICTURES\\Just Caught Salmon.jpg\"'),(10,'Drink','Water','Fountain Drink','PH 8 Water (H2O)','N/A',0,_binary '\"C:\\Users\\angel\\OneDrive\\Desktop\\RMS_Database_MENU_PICTURES\\Water.jpg\"'),(11,'Drink','Lemonade','Fountain Drink','Lemon & Sugar','N/A',0,_binary '\"C:\\Users\\angel\\OneDrive\\Desktop\\RMS_Database_MENU_PICTURES\\Lavendar Lemonade.jpg\"'),(12,'Drink','Coca Cola','Fountain Drink','Coca-Cola Products','N/A',0,_binary '\"C:\\Users\\angel\\OneDrive\\Desktop\\RMS_Database_MENU_PICTURES\\Coca Cola.jpg\"'),(13,'Drink','Lavendar Lemonade','Mocktail','Lavender, Lemonade, Lime, Lemo','N/A',1,_binary '\"C:\\Users\\angel\\OneDrive\\Desktop\\RMS_Database_MENU_PICTURES\\Lavendar Lemonade.jpg\"'),(14,'Drink','Sunset Rise','Mocktail','Orange Juice, Lemons, Oranges, Lime, Mocktail Concentrate','N/A',1,_binary '\"C:\\Users\\angel\\OneDrive\\Desktop\\RMS_Database_MENU_PICTURES\\Sunrise Mocktail.jpg\"'),(15,'Drink','Peppermint Mocha Latte','Coffee','Peppermint, Coffe Beans, Choice of Milk','Dairy',0,_binary '\"C:\\Users\\angel\\OneDrive\\Desktop\\RMS_Database_MENU_PICTURES\\Peppermint Mocha.jpg\"');
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
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `orderNumber` int NOT NULL,
  `employeeIDNumber` int NOT NULL,
  `orderType` varchar(50) NOT NULL,
  `orderDrink` varchar(45) NOT NULL,
  `orderFood` varchar(45) NOT NULL,
  `orderDesert` varchar(45) NOT NULL,
  `orderTotalPrice` int NOT NULL,
  `totalBill` int NOT NULL,
  PRIMARY KEY (`orderNumber`),
  KEY `employeeID_idx` (`employeeIDNumber`),
  CONSTRAINT `employeeID` FOREIGN KEY (`employeeIDNumber`) REFERENCES `employee` (`employeeIDNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,1,'Dine-In','Water','Pasta','Cake',19,21),(2,1,'Take-Out','Coke','Chicken','Cookie',14,16),(3,1,'Dine-In','Sprite','Salad','Canoli',15,17);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
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

--
-- Table structure for table `scheduele`
--

DROP TABLE IF EXISTS `scheduele`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `scheduele` (
  `employeeIDNumber` int NOT NULL,
  `employeeName` varchar(45) NOT NULL,
  `shiftDay` varchar(45) NOT NULL,
  `shiftTime` time NOT NULL,
  PRIMARY KEY (`employeeIDNumber`),
  KEY `employeeName_idx` (`employeeName`),
  CONSTRAINT `employeeName` FOREIGN KEY (`employeeName`) REFERENCES `employee` (`employeeName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scheduele`
--

LOCK TABLES `scheduele` WRITE;
/*!40000 ALTER TABLE `scheduele` DISABLE KEYS */;
INSERT INTO `scheduele` VALUES (1,'AngelinaBojaj','Monday','12:30:30'),(2,'MichaelJackson','Monday','11:30:45'),(3,'RitaMansoor','Monday','12:00:15'),(4,'EmmaFarrell','Monday','11:45:20');
/*!40000 ALTER TABLE `scheduele` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shift_duties`
--

DROP TABLE IF EXISTS `shift_duties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shift_duties` (
  `shiftDuties_ID` int NOT NULL,
  `shift` varchar(45) NOT NULL,
  `shiftDescription` varchar(400) NOT NULL,
  PRIMARY KEY (`shiftDuties_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shift_duties`
--

LOCK TABLES `shift_duties` WRITE;
/*!40000 ALTER TABLE `shift_duties` DISABLE KEYS */;
INSERT INTO `shift_duties` VALUES (1,'Host','Greet'),(2,'Waiter','Serve'),(3,'Buser','Clean'),(4,'Washer','Dishes'),(5,'Cook','Cooking'),(6,'Manager','Everything');
/*!40000 ALTER TABLE `shift_duties` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tables`
--

DROP TABLE IF EXISTS `tables`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tables` (
  `tableNumber` int NOT NULL AUTO_INCREMENT,
  `employeeIDNumber` int NOT NULL,
  `capacity` int NOT NULL,
  `currentNumberOfGuests` int NOT NULL,
  PRIMARY KEY (`tableNumber`),
  KEY `employeeIDNumber_idx` (`employeeIDNumber`),
  CONSTRAINT `employeeIDNumber` FOREIGN KEY (`employeeIDNumber`) REFERENCES `employee` (`employeeIDNumber`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tables`
--

LOCK TABLES `tables` WRITE;
/*!40000 ALTER TABLE `tables` DISABLE KEYS */;
INSERT INTO `tables` VALUES (1,1,2,1),(2,1,3,2),(3,1,4,4),(4,1,5,3),(5,1,7,7),(6,2,2,2),(7,2,4,3),(8,2,3,2),(9,2,10,9),(10,2,20,17),(11,2,8,6),(12,3,2,1),(13,3,10,8),(14,3,13,11),(15,3,6,4),(16,4,4,3),(17,4,8,7),(18,4,19,16),(19,4,12,10),(20,4,10,8);
/*!40000 ALTER TABLE `tables` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'rms'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-17 20:50:40
