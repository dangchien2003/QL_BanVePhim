-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: ticket-ticket-manager.f.aivencloud.com    Database: ticket_manager
-- ------------------------------------------------------
-- Server version	8.0.30

DROP TABLE IF EXISTS `calendar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `calendar` (
  `id` varchar(25) NOT NULL,
  `time` double NOT NULL,
  `idMovie` varchar(25) NOT NULL,
  `cancleAt` bigint DEFAULT NULL,
  `room` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idMovie` (`idMovie`),
  CONSTRAINT `calendar_ibfk_1` FOREIGN KEY (`idMovie`) REFERENCES `movie` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `calendar`
--

LOCK TABLES `calendar` WRITE;
/*!40000 ALTER TABLE `calendar` DISABLE KEYS */;
INSERT INTO `calendar` VALUES ('1',1718271689.351237,'1',NULL,1),('2',1718277689.351237,'MOVIE_1717866136_46521',NULL,2);
/*!40000 ALTER TABLE `calendar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie`
--

DROP TABLE IF EXISTS `movie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movie` (
  `id` varchar(25) NOT NULL,
  `name` varchar(255) NOT NULL,
  `age` int NOT NULL,
  `minPrice` int NOT NULL,
  `hideAt` bigint DEFAULT NULL,
  `createAt` bigint NOT NULL,
  `time` int NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_movie_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie`
--

LOCK TABLES `movie` WRITE;
/*!40000 ALTER TABLE `movie` DISABLE KEYS */;
INSERT INTO `movie` VALUES ('1','cô dâu 8 tuổi',18,31000,NULL,20,90,NULL),('MOVIE_1717866136_46521','chiến tranh 1',1,45000,NULL,1717866136,120,NULL),('MOVIE_1717866136_55853','tình yêu 1',16,50000,1718043440,1717866136,130,NULL),('MOVIE_1717866136_60078','tình yêu 2',16,100000,1718103412,1717866136,150,NULL),('MOVIE_1718110145_27760','Ngày mai nắng lên',16,45000,1718110186,1718110146,120,NULL),('MOVIE_1718110284_28395','Ngày mai nắng lên 2',16,50000,NULL,1718110285,120,NULL);
/*!40000 ALTER TABLE `movie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `seat`
--

DROP TABLE IF EXISTS `seat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `seat` (
  `id` bigint NOT NULL,
  `idTicket` varchar(25) NOT NULL,
  `location` varchar(3) NOT NULL,
  `idCalendar` varchar(25) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idTicket_idx` (`idTicket`),
  KEY `idCalendar_idx` (`idCalendar`),
  CONSTRAINT `idCalendar` FOREIGN KEY (`idCalendar`) REFERENCES `calendar` (`id`),
  CONSTRAINT `idTicket` FOREIGN KEY (`idTicket`) REFERENCES `ticket` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seat`
--

LOCK TABLES `seat` WRITE;
/*!40000 ALTER TABLE `seat` DISABLE KEYS */;
/*!40000 ALTER TABLE `seat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff`
--

DROP TABLE IF EXISTS `staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff` (
  `idnv` varchar(25) NOT NULL,
  `name` varchar(40) NOT NULL,
  `sdt` varchar(10) DEFAULT NULL,
  `email` varchar(50) NOT NULL,
  `sex` int NOT NULL,
  `rank` enum('admin','staff') NOT NULL DEFAULT 'staff',
  `blockAt` double DEFAULT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`idnv`),
  UNIQUE KEY `email_UNIQUE` (`email`),
  KEY `idx_staff_email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
INSERT INTO `staff` VALUES ('123admin','admin',NULL,'chienboy03@gmail.com',1,'admin',NULL,'xAqQiyJAjBg6vDs4EZ3Nb8QxcpJC/Sg1PLuFmoCIPkTehXlydt+haJgdkrZ2hxgM'),('123staff','staff',NULL,'staff@gmail.com',0,'staff',1717695749.3917224,'QB1LmTi7Gq60TAaRy0qu/e+WYSfvAth1fPBbvhpidfCMRsfMNx8ANEitj2y0sIng'),('STAFF_1717668565_587','chien','0333757429','abc@gmail.com',1,'staff',NULL,'VE+Se067WVdJoCv+nQC1IOSz/fmc6FWUMyqtHdh1ddzLTMDXc2eQASHoIITiyngn'),('STAFF_1717751387_626','chiến điên','123','phuongthanh18032003@gmail.com',0,'staff',NULL,'VE+Se067WVdJoCv+nQC1IOSz/fmc6FWUMyqtHdh1ddzLTMDXc2eQASHoIITiyngn');
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket`
--

DROP TABLE IF EXISTS `ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ticket` (
  `id` varchar(25) NOT NULL,
  `idCalendar` varchar(25) NOT NULL,
  `name` varchar(40) NOT NULL,
  `numPerson` int NOT NULL,
  `numPopcorn` int NOT NULL,
  `numWater` int NOT NULL,
  `priceTicket` int NOT NULL,
  `pricePopcorn` int NOT NULL,
  `priceWater` int NOT NULL,
  `email` varchar(50) NOT NULL,
  `createBy` varchar(25) NOT NULL,
  `createAt` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idCalendar` (`idCalendar`),
  KEY `createBy` (`createBy`),
  CONSTRAINT `ticket_ibfk_1` FOREIGN KEY (`idCalendar`) REFERENCES `calendar` (`id`),
  CONSTRAINT `ticket_ibfk_2` FOREIGN KEY (`createBy`) REFERENCES `staff` (`idnv`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket`
--

LOCK TABLES `ticket` WRITE;
/*!40000 ALTER TABLE `ticket` DISABLE KEYS */;
/*!40000 ALTER TABLE `ticket` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-13 21:24:43
