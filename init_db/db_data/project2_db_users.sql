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
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  `is_superuser` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('10138f18-6120-4452-9a7a-c960c9a1a47d','user_customer1@example.com','93fedde43203e0a76172135221b8636313635d7afff96a490ae9066330505d47',1,0),('1e1fa8db-8858-4ecf-9628-a57bc0c77648','user_customer2@example.com','93fedde43203e0a76172135221b8636313635d7afff96a490ae9066330505d47',1,0),('3a170287-74f0-4eca-af36-54005038a412','marko@example.com','e3c4a8e68c23890091f9b9531ef3e0f805ce0a9378d6fb4bbcb6eed403c91342',1,0),('4fdc397c-1653-4211-87bd-c5c7df5b6126','test_user@example.com','0362795b2ee7235b3b4d28f0698a85366703eacf0ba4085796ffd980d7653337',0,0),('5c8eb766-3bd1-4f2a-8aa1-b35ee1da362b','admin@itbc.rs','3eb3fe66b31e3b4d10fa70b5cad49c7112294af6ae4e476a1c405155d45aa121',1,1),('634ab987-0a3c-4f4e-9cbd-91e06f18176a','m.becejac@signalizacija.rs','473287f8298dba7163a897908958f7c0eae733e25d2e027992ea2edc9bed2fa8',1,0),('724e0dcf-a1c2-400c-86ea-a558d1591b31','super_user@example.com','4e4c56e4a15f89f05c2f4c72613da2a18c9665d4f0d6acce16415eb06f9be776',1,1),('9088975a-a457-4a02-81b6-6c126859b4b4','user@example.com','473287f8298dba7163a897908958f7c0eae733e25d2e027992ea2edc9bed2fa8',1,0),('cd605bf9-6ca3-4af6-b3f2-935c4fd1fd4e','pera_peric@example.com','eb7754a618bffe7715f2cd0d9ebbaa2b1f1c594f921e5bb66b8aea0c3a75938c',1,0),('d2ad43bf-e267-4502-b021-229b080a14eb','user_customer3@example.com','0362795b2ee7235b3b4d28f0698a85366703eacf0ba4085796ffd980d7653337',1,0),('fb0fb678-e3f9-4cfa-9b95-56cc36ea6565','vodic1@example.com','d303ad72b90589ee90e64c9d2229d7cda1adb362259b073d1069db69579fa2d9',1,0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
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
