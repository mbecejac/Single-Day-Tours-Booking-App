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
-- Table structure for table `tours`
--

DROP TABLE IF EXISTS `tours`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tours` (
  `id` varchar(50) NOT NULL,
  `tour_name` varchar(50) NOT NULL,
  `tour_date` date NOT NULL,
  `location` varchar(50) NOT NULL,
  `description` varchar(300) DEFAULT NULL,
  `price` float NOT NULL,
  `is_walking_tour` tinyint(1) DEFAULT NULL,
  `tour_language` varchar(50) DEFAULT NULL,
  `tour_guide_id` varchar(50) NOT NULL,
  `bus_carrier_id` varchar(50) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tour_language` (`tour_language`),
  KEY `tour_guide_id` (`tour_guide_id`),
  KEY `bus_carrier_id` (`bus_carrier_id`),
  CONSTRAINT `tours_ibfk_1` FOREIGN KEY (`tour_language`) REFERENCES `languages` (`id`),
  CONSTRAINT `tours_ibfk_2` FOREIGN KEY (`tour_guide_id`) REFERENCES `tour_guides` (`id`),
  CONSTRAINT `tours_ibfk_3` FOREIGN KEY (`bus_carrier_id`) REFERENCES `bus_carriers` (`id`),
  CONSTRAINT `check_date` CHECK ((`tour_date` >= _utf8mb4'2023-02-20 20:55:52.862521'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tours`
--

LOCK TABLES `tours` WRITE;
/*!40000 ALTER TABLE `tours` DISABLE KEYS */;
INSERT INTO `tours` VALUES ('86e01903-041b-452b-a7b4-75e59fcc892b','Disney Paris','2023-06-01','Paris','SPend one day in Disney World in Paris .....',120,0,'8df3bf20-58ba-49ac-861a-45a43645a73f','47310db6-e57c-4d36-8b57-a27be6cae4c5','b6d98ed0-f3f8-4ec0-8794-fb6cd96b6e8e',1),('a7fe0421-bae5-472a-a4e7-417c359258ce','Petrovaradin Fortress Walking Tour','2023-08-01','Novi Sad','Petrovaradin Fortress – the vistas, the history, the bastions, gates and underground corridors… this masterpiece of 18th century fortification has something for everyone.',20,1,'80404d1b-5778-41a5-ad0b-ab1b03a7b35c','241f9add-b980-4254-9dc3-d7bd0150585d','b3919fc4-8820-4f3f-b9e6-96dbed2b2783',1);
/*!40000 ALTER TABLE `tours` ENABLE KEYS */;
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
