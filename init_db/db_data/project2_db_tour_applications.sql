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
-- Table structure for table `tour_applications`
--

DROP TABLE IF EXISTS `tour_applications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tour_applications` (
  `id` varchar(50) NOT NULL,
  `customer_id` varchar(50) NOT NULL,
  `tour_id` varchar(50) NOT NULL,
  `is_payed` tinyint(1) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `customer_tour_uc` (`customer_id`,`tour_id`),
  KEY `tour_id` (`tour_id`),
  CONSTRAINT `tour_applications_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`),
  CONSTRAINT `tour_applications_ibfk_2` FOREIGN KEY (`tour_id`) REFERENCES `tours` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tour_applications`
--

LOCK TABLES `tour_applications` WRITE;
/*!40000 ALTER TABLE `tour_applications` DISABLE KEYS */;
INSERT INTO `tour_applications` VALUES ('486a7cc9-97e8-4250-a11e-05e9439daad7','9aaceb65-a97d-4c46-bc74-be29b123e555','86e01903-041b-452b-a7b4-75e59fcc892b',1,1),('6aebc15f-c21f-4ff8-a790-d641fc3f0208','e874bb5d-0835-4418-8cef-a36f2e16d5ee','a7fe0421-bae5-472a-a4e7-417c359258ce',0,1),('824ea04d-4d7c-4568-bf9c-8157789c4d2b','191547dc-a593-4f1c-bc3c-3a4e82ed957f','a7fe0421-bae5-472a-a4e7-417c359258ce',0,1),('84f89bce-2234-4571-8ea3-317b8a6e4220','191547dc-a593-4f1c-bc3c-3a4e82ed957f','86e01903-041b-452b-a7b4-75e59fcc892b',0,1),('87551ad8-471c-47b2-9ff9-aa78b6a2cc76','4567b06a-e6e6-4af3-9c6d-e0c369d84a4b','a7fe0421-bae5-472a-a4e7-417c359258ce',0,1),('dca64206-2946-47b7-b65a-b6953c1bb511','baf84d11-b988-4a3a-9f9c-776e0a77994d','a7fe0421-bae5-472a-a4e7-417c359258ce',0,1);
/*!40000 ALTER TABLE `tour_applications` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-22 17:54:29
