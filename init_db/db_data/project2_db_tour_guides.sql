-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: project2_db
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `tour_guides`
--

DROP TABLE IF EXISTS `tour_guides`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tour_guides` (
  `id` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `phone_number` varchar(30) NOT NULL,
  `user_id` varchar(50) NOT NULL,
  `language_id` varchar(50) DEFAULT NULL,
  `is_employee` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_lastname_phone_language_uc` (`name`,`last_name`,`phone_number`,`language_id`),
  KEY `user_id` (`user_id`),
  KEY `language_id` (`language_id`),
  CONSTRAINT `tour_guides_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `tour_guides_ibfk_2` FOREIGN KEY (`language_id`) REFERENCES `languages` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tour_guides`
--

LOCK TABLES `tour_guides` WRITE;
/*!40000 ALTER TABLE `tour_guides` DISABLE KEYS */;
INSERT INTO `tour_guides` VALUES ('241f9add-b980-4254-9dc3-d7bd0150585d','Darth','Vader','+2256889956652','fb0fb678-e3f9-4cfa-9b95-56cc36ea6565','80404d1b-5778-41a5-ad0b-ab1b03a7b35c',0),('47310db6-e57c-4d36-8b57-a27be6cae4c5','John','Smith','+12565585788','fb0fb678-e3f9-4cfa-9b95-56cc36ea6565','8df3bf20-58ba-49ac-861a-45a43645a73f',1),('c67dddc2-ed8f-4f29-9806-ce7ff3247efc','Marko','Markovic','+38160555777','3a170287-74f0-4eca-af36-54005038a412','06f73046-2db3-499e-b7f0-ed9145f8937c',1);
/*!40000 ALTER TABLE `tour_guides` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-22 17:54:28
