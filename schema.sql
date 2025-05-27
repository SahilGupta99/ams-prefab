CREATE DATABASE  IF NOT EXISTS `product_management` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `product_management`;
-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: product_management
-- ------------------------------------------------------
-- Server version	8.0.39

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
-- Table structure for table `admin_user`
--

DROP TABLE IF EXISTS `admin_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(80) NOT NULL,
  `password` varchar(128) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_user`
--

LOCK TABLES `admin_user` WRITE;
/*!40000 ALTER TABLE `admin_user` DISABLE KEYS */;
INSERT INTO `admin_user` VALUES (1,'Lucifer','Lucifer');
/*!40000 ALTER TABLE `admin_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` text,
  `image_url` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (24,'A frame','AMS Enterprises extensive range of Wooden House is manufactured using superior quality panels and other raw materials that ensure its robustness and long life. Farm houses are prepared with high grade steel, CFB, EPS, and PUF panels that are procured from our trusted and consistent merchant due to the assiduous efforts of our brilliant professionals.','/static/uploads/category-images/category_1747199685_1.jpg.jpg'),(25,'wooden house','AMS Enterprises extensive range of Wooden House is manufactured using superior quality panels and other raw materials that ensure its robustness and long life. Farm houses are prepared with high grade steel, CFB, EPS, and PUF panels that are procured from our trusted and consistent merchant due to the assiduous efforts of our brilliant professionals.','/static/uploads/category-images/category_1747199705_2.jpg.jpg'),(26,'double storey','AMS Enterprises extensive range of Wooden House is manufactured using superior quality panels and other raw materials that ensure its robustness and long life. Farm houses are prepared with high grade steel, CFB, EPS, and PUF panels that are procured from our trusted and consistent merchant due to the assiduous efforts of our brilliant professionals.','/static/uploads/category-images/category_1747199788_3.jpg.jpg'),(27,'Prefabricated Luxury House','AMS Enterprises extensive range of Wooden House is manufactured using superior quality panels and other raw materials that ensure its robustness and long life. Farm houses are prepared with high grade steel, CFB, EPS, and PUF panels that are procured from our trusted and consistent merchant due to the assiduous efforts of our brilliant professionals.','/static/uploads/category-images/category_1747199828_4.jpg.jpg');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contact_messages`
--

DROP TABLE IF EXISTS `contact_messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contact_messages` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `requirement` varchar(100) NOT NULL,
  `message` text NOT NULL,
  `ip_address` varchar(45) NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact_messages`
--

LOCK TABLES `contact_messages` WRITE;
/*!40000 ALTER TABLE `contact_messages` DISABLE KEYS */;
INSERT INTO `contact_messages` VALUES (12,'sahil','sahil.sg9971@gmail.com','+1 234 567 8900','a','a','Personal Use Requirement','d','127.0.0.1','2025-05-08 10:03:51'),(13,'sahil','sahil.sg9971@gmail.com','+1 234 567 8900','a','s','Personal Use Requirement','d','127.0.0.1','2025-05-08 10:04:14'),(14,'sahil','sahil.sg9971@gmail.com','+1 234 567 8900','a','a','Hotel Resort Project','s','127.0.0.1','2025-05-08 10:05:13'),(15,'sahil','sahil.sg9971@gmail.com','+1 234 567 8900','a','a','Hotel Resort Project','d','127.0.0.1','2025-05-08 10:05:37'),(16,'sahil','sahil.sg9971@gmail.com','+1 234 567 8900','s','a','Farm house Project','s','127.0.0.1','2025-05-08 10:06:38');
/*!40000 ALTER TABLE `contact_messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `id` int NOT NULL AUTO_INCREMENT,
  `category_id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` text,
  `price` decimal(10,2) DEFAULT NULL,
  `specs` json DEFAULT NULL,
  `image_urls` json DEFAULT NULL,
  `video_url` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `product_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (17,24,'wooden A frame','AMS Enterprises extensive range of Wooden House is manufactured using superior quality panels and other raw materials that ensure its robustness and long life. Farm houses are prepared with high grade steel, CFB, EPS, and PUF panels that are procured from our trusted and consistent merchant due to the assiduous efforts of our brilliant professionals. ',4444.00,'\"{\\\"Color\\\": \\\"brown\\\", \\\"Material\\\": \\\"wooden\\\", \\\"Warranty\\\": \\\"10\\\"}\"','\"/static/uploads/products/product_1747201841_3.jpg.jpg,/static/uploads/products/product_1747201841_4.jpg.jpg,/static/uploads/products/product_1747201841_5.jpg.jpg\"','/static/uploads/videos/video_1747201841_istockphoto-1967534184-640_adpp_is.mp4'),(18,25,'wooden house prefab','AMS Enterprises extensive range of Wooden House is manufactured using superior quality panels and other raw materials that ensure its robustness and long life. Farm houses are prepared with high grade steel, CFB, EPS, and PUF panels that are procured from our trusted and consistent merchant due to the assiduous efforts of our brilliant professionals. ',4444.00,'{\"Color\": \"brown\", \"Material\": \"wooden\", \"Warranty\": \"10\"}','\"/static/uploads/products/product_1747201858_1.jpg.jpg,/static/uploads/products/product_1747201858_2.jpg.jpg,/static/uploads/products/product_1747201858_3.jpg.jpg,/static/uploads/products/product_1747201858_4.jpg.jpg,/static/uploads/products/product_1747201858_5.jpg.jpg\"','/static/uploads/videos/video_1747201858_istockphoto-1967534184-640_adpp_is.mp4'),(19,26,'premium house ','AMS Enterprises extensive range of Wooden House is manufactured using superior quality panels and other raw materials that ensure its robustness and long life. Farm houses are prepared with high grade steel, CFB, EPS, and PUF panels that are procured from our trusted and consistent merchant due to the assiduous efforts of our brilliant professionals. ',4444.00,'{\"Color\": \"brown\", \"Material\": \"wooden\", \"Warranty\": \"10\"}','\"/static/uploads/products/product_1747201872_1.jpg.jpg,/static/uploads/products/product_1747201872_2.jpg.jpg,/static/uploads/products/product_1747201872_3.jpg.jpg,/static/uploads/products/product_1747201872_4.jpg.jpg,/static/uploads/products/product_1747201872_5.jpg.jpg\"','/static/uploads/videos/video_1747201872_istockphoto-1967534184-640_adpp_is.mp4'),(20,27,'prefab house','AMS Enterprises extensive range of Wooden House is manufactured using superior quality panels and other raw materials that ensure its robustness and long life. Farm houses are prepared with high grade steel, CFB, EPS, and PUF panels that are procured from our trusted and consistent merchant due to the assiduous efforts of our brilliant professionals. ',4444.00,'{\"Color\": \"brown\", \"Material\": \"wooden\", \"Warranty\": \"10\"}','\"/static/uploads/products/product_1747201888_1.jpg.jpg,/static/uploads/products/product_1747201888_2.jpg.jpg,/static/uploads/products/product_1747201888_3.jpg.jpg,/static/uploads/products/product_1747201888_4.jpg.jpg,/static/uploads/products/product_1747201888_5.jpg.jpg\"','/static/uploads/videos/video_1747201888_istockphoto-1967534184-640_adpp_is.mp4'),(21,24,'house2','AMS Enterprises extensive range of Wooden House is manufactured using superior quality panels and other raw materials that ensure its robustness and long life. Farm houses are prepared with high grade steel, CFB, EPS, and PUF panels that are procured from our trusted and consistent merchant due to the assiduous efforts of our brilliant professionals. ',4444.00,'{\"Color\": \"brown\", \"Material\": \"wooden\", \"Warranty\": \"10\"}','\"/static/uploads/products/product_1747201902_1.jpg.jpg,/static/uploads/products/product_1747201902_2.jpg.jpg,/static/uploads/products/product_1747201902_3.jpg.jpg,/static/uploads/products/product_1747201902_4.jpg.jpg,/static/uploads/products/product_1747201902_5.jpg.jpg\"','/static/uploads/videos/video_1747201902_istockphoto-1967534184-640_adpp_is.mp4'),(22,24,'house3','AMS Enterprises extensive range of Wooden House is manufactured using superior quality panels and other raw materials that ensure its robustness and long life. Farm houses are prepared with high grade steel, CFB, EPS, and PUF panels that are procured from our trusted and consistent merchant due to the assiduous efforts of our brilliant professionals. ',4444.00,'{\"Color\": \"brown\", \"Material\": \"wooden\", \"Warranty\": \"10\"}','\"/static/uploads/products/product_1747201907_1.jpg.jpg,/static/uploads/products/product_1747201907_2.jpg.jpg,/static/uploads/products/product_1747201907_3.jpg.jpg,/static/uploads/products/product_1747201907_4.jpg.jpg,/static/uploads/products/product_1747201907_5.jpg.jpg\"','/static/uploads/videos/video_1747201907_istockphoto-1967534184-640_adpp_is.mp4'),(23,24,'house4','AMS Enterprises extensive range of Wooden House is manufactured using superior quality panels and other raw materials that ensure its robustness and long life. Farm houses are prepared with high grade steel, CFB, EPS, and PUF panels that are procured from our trusted and consistent merchant due to the assiduous efforts of our brilliant professionals. ',4444.00,'{\"Color\": \"brown\", \"Material\": \"wooden\", \"Warranty\": \"10\"}','\"/static/uploads/products/product_1747201912_1.jpg.jpg,/static/uploads/products/product_1747201912_2.jpg.jpg,/static/uploads/products/product_1747201912_3.jpg.jpg,/static/uploads/products/product_1747201912_4.jpg.jpg,/static/uploads/products/product_1747201912_5.jpg.jpg\"','/static/uploads/videos/video_1747201912_istockphoto-1967534184-640_adpp_is.mp4'),(24,24,'house5','AMS Enterprises extensive range of Wooden House is manufactured using superior quality panels and other raw materials that ensure its robustness and long life. Farm houses are prepared with high grade steel, CFB, EPS, and PUF panels that are procured from our trusted and consistent merchant due to the assiduous efforts of our brilliant professionals. ',4444.00,'{\"Color\": \"brown\", \"Material\": \"wooden\", \"Warranty\": \"10\"}','\"/static/uploads/products/product_1747201918_1.jpg.jpg,/static/uploads/products/product_1747201918_2.jpg.jpg,/static/uploads/products/product_1747201918_3.jpg.jpg,/static/uploads/products/product_1747201918_4.jpg.jpg,/static/uploads/products/product_1747201918_5.jpg.jpg\"','/static/uploads/videos/video_1747201918_istockphoto-1967534184-640_adpp_is.mp4');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-27 22:56:35
