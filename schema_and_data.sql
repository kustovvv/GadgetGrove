-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: gadgetgrove
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `account_personalinformation`
--

DROP TABLE IF EXISTS `account_personalinformation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `account_personalinformation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `avatar_url` varchar(100) DEFAULT NULL,
  `gender` varchar(255) DEFAULT NULL,
  `married` tinyint(1) NOT NULL,
  `have_children` tinyint(1) DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `phone_number` varchar(10) DEFAULT NULL,
  `facebook_url` varchar(255) DEFAULT NULL,
  `instagram_url` varchar(255) DEFAULT NULL,
  `twitter_url` varchar(255) DEFAULT NULL,
  `google_url` varchar(255) DEFAULT NULL,
  `pinterest_url` varchar(255) DEFAULT NULL,
  `about` longtext,
  `hobby` longtext,
  `interests` longtext,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `account_personalinfo_user_id_8940db9b_fk_authentic` (`user_id`),
  CONSTRAINT `account_personalinfo_user_id_8940db9b_fk_authentic` FOREIGN KEY (`user_id`) REFERENCES `authentication_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_personalinformation`
--

LOCK TABLES `account_personalinformation` WRITE;
/*!40000 ALTER TABLE `account_personalinformation` DISABLE KEYS */;
INSERT INTO `account_personalinformation` VALUES (4,'http://example.com/avatar1.jpg','Male',1,0,'1990-05-15','1234567890','http://facebook.com/user1','http://instagram.com/user1','http://twitter.com/user1','http://google.com/user1','http://pinterest.com/user1','I love hiking and photography.','Reading books, playing guitar','Traveling, photography, technology',1),(5,'http://example.com/avatar2.jpg','Female',1,1,'1985-08-22','9876543210','http://facebook.com/user2','http://instagram.com/user2','http://twitter.com/user2','http://google.com/user2','http://pinterest.com/user2','Passionate about art and design.','Painting, drawing','Art, design, music',2),(6,'http://example.com/avatar3.jpg','Non-Binary',0,0,'1995-02-10','5554443333','http://facebook.com/user3','http://instagram.com/user3','http://twitter.com/user3','http://google.com/user3','http://pinterest.com/user3','Tech enthusiast and software developer.','Coding, gaming','Technology, programming, gaming',3),(7,'http://example.com/avatar4.jpg','Male',0,1,'1980-11-30','9998887777','http://facebook.com/user4','http://instagram.com/user4','http://twitter.com/user4','http://google.com/user4','http://pinterest.com/user4','Outdoor activities and fitness freak.','Running, cycling','Fitness, outdoor activities',4),(8,'http://example.com/avatar5.jpg','Female',1,0,'1992-07-05','6667778888','http://facebook.com/user5','http://instagram.com/user5','http://twitter.com/user5','http://google.com/user5','http://pinterest.com/user5','Bookworm and coffee lover.','Reading, coffee brewing','Books, coffee, literature',5),(11,'personal_information_avatar/cat_2LErAJP.jpg','male',0,0,'1997-07-14','0123456789','http://facebook.com/alexalen','http://instagram.com/alexalen','http://twitter.com/alexalen',NULL,NULL,'I love hiking and photography.','Reading books, playing guitar','Traveling, photography, technology',74),(12,'personal_information_avatar/dog.jpg','female',1,1,'1987-06-23','0732739297','http://facebook.com/emily_johnson','http://instagram.com/emily_johnson','http://twitter.com/emily_johnson',NULL,'http://pinterest.com/emily_johnson','Passionate about art and design.','Painting, drawing','Art, design, music',73);
/*!40000 ALTER TABLE `account_personalinformation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=121 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add user',6,'add_user'),(22,'Can change user',6,'change_user'),(23,'Can delete user',6,'delete_user'),(24,'Can view user',6,'view_user'),(25,'Can add brand',7,'add_brand'),(26,'Can change brand',7,'change_brand'),(27,'Can delete brand',7,'delete_brand'),(28,'Can view brand',7,'view_brand'),(29,'Can add category',8,'add_category'),(30,'Can change category',8,'change_category'),(31,'Can delete category',8,'delete_category'),(32,'Can view category',8,'view_category'),(33,'Can add contact info',9,'add_contactinfo'),(34,'Can change contact info',9,'change_contactinfo'),(35,'Can delete contact info',9,'delete_contactinfo'),(36,'Can view contact info',9,'view_contactinfo'),(37,'Can add shipping address',10,'add_shippingaddress'),(38,'Can change shipping address',10,'change_shippingaddress'),(39,'Can delete shipping address',10,'delete_shippingaddress'),(40,'Can view shipping address',10,'view_shippingaddress'),(41,'Can add personal information',11,'add_personalinformation'),(42,'Can change personal information',11,'change_personalinformation'),(43,'Can delete personal information',11,'delete_personalinformation'),(44,'Can view personal information',11,'view_personalinformation'),(45,'Can add order',12,'add_order'),(46,'Can change order',12,'change_order'),(47,'Can delete order',12,'delete_order'),(48,'Can view order',12,'view_order'),(49,'Can add item',13,'add_item'),(50,'Can change item',13,'change_item'),(51,'Can delete item',13,'delete_item'),(52,'Can view item',13,'view_item'),(53,'Can add order item',14,'add_orderitem'),(54,'Can change order item',14,'change_orderitem'),(55,'Can delete order item',14,'delete_orderitem'),(56,'Can view order item',14,'view_orderitem'),(57,'Can add shopping cart item',15,'add_shoppingcartitem'),(58,'Can change shopping cart item',15,'change_shoppingcartitem'),(59,'Can delete shopping cart item',15,'delete_shoppingcartitem'),(60,'Can view shopping cart item',15,'view_shoppingcartitem'),(61,'Can add item rewiew',16,'add_itemrewiew'),(62,'Can change item rewiew',16,'change_itemrewiew'),(63,'Can delete item rewiew',16,'delete_itemrewiew'),(64,'Can view item rewiew',16,'view_itemrewiew'),(65,'Can add item review',16,'add_itemreview'),(66,'Can change item review',16,'change_itemreview'),(67,'Can delete item review',16,'delete_itemreview'),(68,'Can view item review',16,'view_itemreview'),(69,'Can add review',16,'add_review'),(70,'Can change review',16,'change_review'),(71,'Can delete review',16,'delete_review'),(72,'Can view review',16,'view_review'),(73,'Can add comments',16,'add_comments'),(74,'Can change comments',16,'change_comments'),(75,'Can delete comments',16,'delete_comments'),(76,'Can view comments',16,'view_comments'),(77,'Can add category brand',17,'add_categorybrand'),(78,'Can change category brand',17,'change_categorybrand'),(79,'Can delete category brand',17,'delete_categorybrand'),(80,'Can view category brand',17,'view_categorybrand'),(81,'Can add favorite',18,'add_favorite'),(82,'Can change favorite',18,'change_favorite'),(83,'Can delete favorite',18,'delete_favorite'),(84,'Can view favorite',18,'view_favorite'),(85,'Can add favorite',19,'add_favorite'),(86,'Can change favorite',19,'change_favorite'),(87,'Can delete favorite',19,'delete_favorite'),(88,'Can view favorite',19,'view_favorite'),(89,'Can add favorite compare',20,'add_favoritecompare'),(90,'Can change favorite compare',20,'change_favoritecompare'),(91,'Can delete favorite compare',20,'delete_favoritecompare'),(92,'Can view favorite compare',20,'view_favoritecompare'),(93,'Can add order status',21,'add_orderstatus'),(94,'Can change order status',21,'change_orderstatus'),(95,'Can delete order status',21,'delete_orderstatus'),(96,'Can view order status',21,'view_orderstatus'),(97,'Can add payment method',22,'add_paymentmethod'),(98,'Can change payment method',22,'change_paymentmethod'),(99,'Can delete payment method',22,'delete_paymentmethod'),(100,'Can view payment method',22,'view_paymentmethod'),(101,'Can add conversation',23,'add_conversation'),(102,'Can change conversation',23,'change_conversation'),(103,'Can delete conversation',23,'delete_conversation'),(104,'Can view conversation',23,'view_conversation'),(105,'Can add conversation message',24,'add_conversationmessage'),(106,'Can change conversation message',24,'change_conversationmessage'),(107,'Can delete conversation message',24,'delete_conversationmessage'),(108,'Can view conversation message',24,'view_conversationmessage'),(109,'Can add seller review',25,'add_sellerreview'),(110,'Can change seller review',25,'change_sellerreview'),(111,'Can delete seller review',25,'delete_sellerreview'),(112,'Can view seller review',25,'view_sellerreview'),(113,'Can add order review',26,'add_orderreview'),(114,'Can change order review',26,'change_orderreview'),(115,'Can delete order review',26,'delete_orderreview'),(116,'Can view order review',26,'view_orderreview'),(117,'Can add order review',27,'add_orderreview'),(118,'Can change order review',27,'change_orderreview'),(119,'Can delete order review',27,'delete_orderreview'),(120,'Can view order review',27,'view_orderreview');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authentication_user`
--

DROP TABLE IF EXISTS `authentication_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `authentication_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `is_email_verified` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `authentication_user_email_2220eff5_uniq` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authentication_user`
--

LOCK TABLES `authentication_user` WRITE;
/*!40000 ALTER TABLE `authentication_user` DISABLE KEYS */;
INSERT INTO `authentication_user` VALUES (1,'pbkdf2_sha256$600000$u2wThgBQQwgTBAEJa0Sw4f$Xnw5mtYq2A2U8rQh4QfZBWOlIbzZnXFgUTtx9AjKlnM=','2024-01-04 18:54:17.043250',1,'admin','','','',1,1,'2023-10-17 22:58:44.692722',0),(73,'pbkdf2_sha256$600000$uCTTWLcpt8UfA5DFw9Ixkp$v0M0/UqruWtlijwcLOIxI9V0BgIzIC4bTTLa8CdFF/g=','2024-01-04 18:31:53.984636',0,'Emilyss','Emily','Johnson','emily_johnson@gmail.com',0,1,'2024-01-04 17:56:02.235779',1),(74,'pbkdf2_sha256$600000$btfnd1EClRS2wPrgEiZ5zk$kx6bsFTXedyHLSdZKDkit3lTz5K9OPPNMcjuMFJyWyU=','2024-01-04 18:43:26.178258',0,'alexalen','Alex','Smith','alex@gmail.com',0,1,'2024-01-04 18:10:19.273713',1);
/*!40000 ALTER TABLE `authentication_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authentication_user_groups`
--

DROP TABLE IF EXISTS `authentication_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `authentication_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `authentication_user_groups_user_id_group_id_8af031ac_uniq` (`user_id`,`group_id`),
  KEY `authentication_user_groups_group_id_6b5c44b7_fk_auth_group_id` (`group_id`),
  CONSTRAINT `authentication_user__user_id_30868577_fk_authentic` FOREIGN KEY (`user_id`) REFERENCES `authentication_user` (`id`),
  CONSTRAINT `authentication_user_groups_group_id_6b5c44b7_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authentication_user_groups`
--

LOCK TABLES `authentication_user_groups` WRITE;
/*!40000 ALTER TABLE `authentication_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `authentication_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authentication_user_user_permissions`
--

DROP TABLE IF EXISTS `authentication_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `authentication_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `authentication_user_user_user_id_permission_id_ec51b09f_uniq` (`user_id`,`permission_id`),
  KEY `authentication_user__permission_id_ea6be19a_fk_auth_perm` (`permission_id`),
  CONSTRAINT `authentication_user__permission_id_ea6be19a_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `authentication_user__user_id_736ebf7e_fk_authentic` FOREIGN KEY (`user_id`) REFERENCES `authentication_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authentication_user_user_permissions`
--

LOCK TABLES `authentication_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `authentication_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `authentication_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `conversation_conversation`
--

DROP TABLE IF EXISTS `conversation_conversation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `conversation_conversation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `modified_at` datetime(6) NOT NULL,
  `created_by_id` bigint NOT NULL,
  `item_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `conversation_convers_created_by_id_519b8b4a_fk_authentic` (`created_by_id`),
  KEY `conversation_conversation_item_id_228c4088_fk_item_item_id` (`item_id`),
  CONSTRAINT `conversation_convers_created_by_id_519b8b4a_fk_authentic` FOREIGN KEY (`created_by_id`) REFERENCES `authentication_user` (`id`),
  CONSTRAINT `conversation_conversation_item_id_228c4088_fk_item_item_id` FOREIGN KEY (`item_id`) REFERENCES `item_item` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `conversation_conversation`
--

LOCK TABLES `conversation_conversation` WRITE;
/*!40000 ALTER TABLE `conversation_conversation` DISABLE KEYS */;
/*!40000 ALTER TABLE `conversation_conversation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `conversation_conversation_members`
--

DROP TABLE IF EXISTS `conversation_conversation_members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `conversation_conversation_members` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `conversation_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `conversation_conversatio_conversation_id_user_id_8676b40f_uniq` (`conversation_id`,`user_id`),
  KEY `conversation_convers_user_id_226f9afc_fk_authentic` (`user_id`),
  CONSTRAINT `conversation_convers_conversation_id_c146fce9_fk_conversat` FOREIGN KEY (`conversation_id`) REFERENCES `conversation_conversation` (`id`),
  CONSTRAINT `conversation_convers_user_id_226f9afc_fk_authentic` FOREIGN KEY (`user_id`) REFERENCES `authentication_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `conversation_conversation_members`
--

LOCK TABLES `conversation_conversation_members` WRITE;
/*!40000 ALTER TABLE `conversation_conversation_members` DISABLE KEYS */;
/*!40000 ALTER TABLE `conversation_conversation_members` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `conversation_conversationmessage`
--

DROP TABLE IF EXISTS `conversation_conversationmessage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `conversation_conversationmessage` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `content` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `conversation_id` bigint NOT NULL,
  `created_by_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `conversation_convers_conversation_id_fdd084d4_fk_conversat` (`conversation_id`),
  KEY `conversation_convers_created_by_id_aa6cea66_fk_authentic` (`created_by_id`),
  CONSTRAINT `conversation_convers_conversation_id_fdd084d4_fk_conversat` FOREIGN KEY (`conversation_id`) REFERENCES `conversation_conversation` (`id`),
  CONSTRAINT `conversation_convers_created_by_id_aa6cea66_fk_authentic` FOREIGN KEY (`created_by_id`) REFERENCES `authentication_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `conversation_conversationmessage`
--

LOCK TABLES `conversation_conversationmessage` WRITE;
/*!40000 ALTER TABLE `conversation_conversationmessage` DISABLE KEYS */;
/*!40000 ALTER TABLE `conversation_conversationmessage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_authentication_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_authentication_user_id` FOREIGN KEY (`user_id`) REFERENCES `authentication_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=522 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2024-01-04 18:08:52.021872','67','alexalen',2,'[{\"changed\": {\"fields\": [\"Username\", \"First name\", \"Last name\"]}}]',6,1),(2,'2024-01-04 18:09:56.003225','67','alexalen',3,'',6,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (26,'account','orderreview'),(11,'account','personalinformation'),(25,'account','sellerreview'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(6,'authentication','user'),(4,'contenttypes','contenttype'),(23,'conversation','conversation'),(24,'conversation','conversationmessage'),(7,'item','brand'),(8,'item','category'),(17,'item','categorybrand'),(16,'item','comments'),(19,'item','favorite'),(20,'item','favoritecompare'),(13,'item','item'),(9,'order','contactinfo'),(18,'order','favorite'),(12,'order','order'),(14,'order','orderitem'),(27,'order','orderreview'),(21,'order','orderstatus'),(22,'order','paymentmethod'),(10,'order','shippingaddress'),(15,'order','shoppingcartitem'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=201 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-10-17 22:47:54.451348'),(2,'contenttypes','0002_remove_content_type_name','2023-10-17 22:47:54.481347'),(3,'auth','0001_initial','2023-10-17 22:47:54.619503'),(4,'auth','0002_alter_permission_name_max_length','2023-10-17 22:47:54.647507'),(5,'auth','0003_alter_user_email_max_length','2023-10-17 22:47:54.652508'),(6,'auth','0004_alter_user_username_opts','2023-10-17 22:47:54.658507'),(7,'auth','0005_alter_user_last_login_null','2023-10-17 22:47:54.664508'),(8,'auth','0006_require_contenttypes_0002','2023-10-17 22:47:54.668525'),(9,'auth','0007_alter_validators_add_error_messages','2023-10-17 22:47:54.674509'),(10,'auth','0008_alter_user_username_max_length','2023-10-17 22:47:54.680507'),(11,'auth','0009_alter_user_last_name_max_length','2023-10-17 22:47:54.685508'),(12,'auth','0010_alter_group_name_max_length','2023-10-17 22:47:54.696509'),(13,'auth','0011_update_proxy_permissions','2023-10-17 22:47:54.703510'),(14,'auth','0012_alter_user_first_name_max_length','2023-10-17 22:47:54.708504'),(15,'authentication','0001_initial','2023-10-17 22:47:54.839934'),(16,'admin','0001_initial','2023-10-17 22:47:54.904532'),(17,'admin','0002_logentry_remove_auto_add','2023-10-17 22:47:54.910553'),(18,'admin','0003_logentry_add_action_flag_choices','2023-10-17 22:47:54.916908'),(19,'sessions','0001_initial','2023-10-17 22:47:54.937269'),(20,'account','0001_initial','2023-10-17 22:53:17.679639'),(21,'item','0001_initial','2023-10-17 22:53:17.703640'),(22,'order','0001_initial','2023-10-17 22:53:17.788636'),(23,'order','0002_order','2023-10-17 22:53:41.763388'),(24,'item','0002_item','2023-10-17 22:54:26.018236'),(25,'order','0003_shoppingcartitem_orderitem','2023-10-17 22:55:04.156605'),(26,'authentication','0002_alter_user_email','2023-10-20 12:57:51.911180'),(27,'item','0003_itemrewiew','2023-10-23 18:35:48.913911'),(28,'item','0004_rename_itemrewiew_itemreview','2023-10-23 18:36:44.274842'),(29,'item','0005_rename_itemreview_review','2023-10-23 19:07:38.620935'),(30,'item','0006_rename_review_comments','2023-10-23 22:27:54.679177'),(31,'item','0007_delete_comments','2023-10-25 06:25:40.272638'),(32,'item','0008_comments','2023-10-25 06:28:37.210932'),(33,'item','0009_delete_comments','2023-10-25 06:28:37.225932'),(34,'item','0010_comments','2023-10-25 06:28:57.351233'),(35,'item','0011_alter_comments_advantages_alter_comments_comment_and_more','2023-10-25 06:37:16.317951'),(36,'item','0012_alter_comments_rating','2023-10-25 06:43:48.724762'),(37,'item','0013_alter_comments_options_and_more','2023-10-25 06:50:29.605492'),(38,'item','0014_alter_comments_comment_alter_comments_rating','2023-10-25 10:49:28.503888'),(39,'item','0015_alter_comments_options','2023-10-25 19:38:24.142619'),(40,'order','0004_remove_shoppingcartitem_item_and_more','2023-10-25 20:56:49.845677'),(41,'item','0016_remove_comments_item_remove_item_brand_and_more','2023-10-25 20:56:49.849677'),(42,'item','0017_brand','2023-10-25 20:57:55.769503'),(43,'item','0018_delete_brand','2023-10-25 20:57:55.783502'),(44,'item','0019_brand','2023-10-25 21:02:10.658294'),(45,'item','0020_item','2023-10-25 21:02:24.582166'),(46,'item','0021_comments','2023-10-25 21:02:35.699578'),(47,'order','0005_shoppingcartitem_orderitem','2023-10-25 21:03:26.145112'),(48,'item','0022_remove_brand_category_brand_categories','2023-10-26 08:38:53.131157'),(49,'order','0006_remove_shoppingcartitem_item_and_more','2023-10-26 09:00:17.777562'),(50,'item','0023_remove_item_brand_remove_brand_categories_and_more','2023-10-26 09:00:17.791628'),(51,'item','0024_categorybrand','2023-10-26 09:00:58.572486'),(52,'item','0025_item','2023-10-26 09:03:50.514154'),(53,'item','0026_comments','2023-10-26 09:04:14.814746'),(54,'order','0007_shoppingcartitem_orderitem','2023-10-26 09:06:07.972801'),(55,'item','0027_alter_brand_name_alter_category_name','2023-10-26 09:11:47.834523'),(56,'order','0008_alter_order_options','2023-10-27 11:18:22.698187'),(57,'order','0009_favorite','2023-10-27 11:18:38.832118'),(58,'order','0010_rename_item_favorite_items','2023-10-27 14:58:24.121891'),(59,'item','0028_favorite','2023-10-29 10:26:25.858912'),(60,'order','0011_auto_20231029_1320','2023-10-29 10:26:25.972911'),(61,'item','0029_delete_favorite','2023-10-29 13:45:36.887689'),(62,'item','0030_favoritecompare','2023-10-29 13:48:53.786793'),(63,'item','0031_favoritecompare_compare_items_and_more','2023-10-29 13:48:53.921016'),(64,'order','0012_orderstatus','2023-10-31 10:16:31.777958'),(65,'order','0013_paymentmethod_alter_orderstatus_options_and_more','2023-10-31 10:33:59.181931'),(66,'order','0014_remove_orderitem_item_remove_orderitem_order_and_more','2023-10-31 10:49:56.730550'),(67,'order','0015_order','2023-10-31 10:51:58.622997'),(68,'order','0016_orderitem','2023-10-31 10:52:12.946458'),(69,'order','0017_remove_orderitem_item_remove_orderitem_order_and_more','2023-10-31 11:16:02.989532'),(70,'order','0018_order','2023-10-31 11:16:44.290412'),(71,'order','0019_orderitem','2023-10-31 11:16:55.687845'),(72,'order','0020_remove_shoppingcartitem_item_and_more','2023-11-08 20:11:24.944307'),(73,'item','0032_remove_favoritecompare_compare_items_and_more','2023-11-08 20:11:24.947306'),(74,'item','0033_item','2023-11-08 20:16:22.007543'),(75,'item','0034_favoritecompare_comments','2023-11-08 20:20:41.191332'),(76,'order','0021_shoppingcartitem_orderitem','2023-11-08 20:21:05.874795'),(77,'order','0022_remove_shoppingcartitem_item_and_more','2023-11-08 20:54:37.452157'),(78,'item','0035_remove_favoritecompare_compare_items_and_more','2023-11-08 20:54:37.466376'),(79,'item','0036_item','2023-11-08 20:56:53.629804'),(80,'item','0037_favoritecompare_comments','2023-11-08 20:57:36.406215'),(81,'order','0023_shoppingcartitem_orderitem','2023-11-08 20:58:07.757321'),(82,'conversation','0001_initial','2023-11-08 21:25:31.051587'),(83,'conversation','0002_conversationmessage','2023-11-08 21:42:04.847661'),(84,'conversation','0003_remove_conversationmessage_conversation_and_more','2023-11-09 17:37:17.883208'),(85,'order','0024_remove_shoppingcartitem_item_and_more','2023-11-09 17:37:17.886902'),(86,'item','0038_remove_favoritecompare_compare_items_and_more','2023-11-09 17:37:17.888906'),(87,'item','0039_item','2023-11-09 17:37:38.029647'),(88,'item','0040_favoritecompare_comments','2023-11-09 17:38:27.284505'),(89,'item','0041_remove_favoritecompare_compare_items_and_more','2023-11-09 17:40:09.290234'),(90,'order','0025_shoppingcartitem_orderitem','2023-11-09 17:42:24.560822'),(91,'order','0026_remove_shoppingcartitem_item_and_more','2023-11-09 17:42:24.565819'),(92,'item','0042_delete_item','2023-11-09 17:42:24.568457'),(93,'item','0043_item','2023-11-09 17:42:38.507823'),(94,'item','0044_favoritecompare_comments','2023-11-09 17:43:32.439000'),(95,'order','0027_shoppingcartitem_orderitem','2023-11-09 17:45:37.862838'),(96,'order','0028_delete_shoppingcartitem','2023-11-09 17:45:37.869001'),(97,'order','0029_remove_orderitem_item_remove_orderitem_order_and_more','2023-11-09 17:45:37.875181'),(98,'order','0030_order','2023-11-09 17:47:35.318909'),(99,'order','0031_remove_shippingaddress_user_delete_order_and_more','2023-11-09 17:47:35.332014'),(100,'order','0032_shippingaddress','2023-11-09 17:47:54.793136'),(101,'order','0033_order','2023-11-09 17:48:24.402546'),(102,'order','0034_shoppingcartitem_orderitem','2023-11-09 17:49:41.871292'),(103,'conversation','0004_initial','2023-11-09 17:50:11.007975'),(104,'conversation','0005_conversationmessage','2023-11-09 17:50:21.182631'),(105,'item','0045_alter_item_availability','2023-11-09 20:34:49.237952'),(106,'conversation','0006_remove_conversationmessage_conversation_and_more','2023-11-13 23:33:32.740405'),(107,'conversation','0007_initial','2023-11-13 23:35:32.657980'),(108,'conversation','0008_conversationmessage','2023-11-13 23:35:42.313554'),(109,'account','0002_alter_personalinformation_user','2023-11-15 16:44:04.601644'),(110,'conversation','0009_alter_conversationmessage_options_and_more','2023-11-15 16:44:04.624478'),(111,'conversation','0010_alter_conversationmessage_created_at','2023-11-15 16:47:10.775089'),(112,'order','0035_remove_orderitem_item_remove_orderitem_order_and_more','2023-11-17 15:34:08.613213'),(113,'order','0036_order','2023-11-17 15:34:57.819291'),(114,'order','0037_orderitem','2023-11-17 15:35:30.381854'),(115,'order','0038_shoppingcartitem','2023-11-17 15:35:39.487068'),(116,'account','0003_sellerreview','2023-11-17 17:18:50.755693'),(117,'account','0004_delete_sellerreview','2023-11-17 17:23:42.735889'),(118,'account','0005_sellerreview','2023-11-17 17:23:56.496109'),(119,'account','0006_delete_sellerreview','2023-11-17 21:51:19.690954'),(120,'account','0007_orderreview','2023-11-17 21:51:32.021773'),(121,'account','0008_alter_orderreview_comment','2023-11-17 22:01:02.100378'),(122,'account','0009_delete_orderreview','2023-11-18 13:23:02.000762'),(123,'order','0039_orderreview','2023-11-18 13:23:02.093971'),(124,'account','0010_alter_personalinformation_married','2023-11-26 16:51:10.751795'),(125,'account','0011_delete_personalinformation','2023-11-26 16:51:10.759721'),(126,'account','0012_initial','2023-11-26 16:51:44.728966'),(127,'account','0002_initial','2023-12-20 13:02:50.493116'),(128,'account','0003_delete_personalinformation','2023-12-20 13:02:50.511215'),(129,'account','0004_initial','2023-12-20 13:03:04.583823'),(130,'item','0002_delete_brand_delete_category','2023-12-20 13:03:54.479147'),(131,'item','0003_initial','2023-12-20 13:04:08.958224'),(132,'item','0004_categorybrand','2023-12-20 13:04:43.643870'),(133,'item','0005_item','2023-12-20 13:04:56.323793'),(134,'item','0006_comments','2023-12-20 13:05:16.692239'),(135,'item','0007_favoritecompare','2023-12-20 13:05:32.763588'),(136,'order','0002_contactinfo','2023-12-20 13:18:30.611165'),(137,'order','0003_orderstatus_paymentmethod','2023-12-20 13:18:47.931449'),(138,'order','0004_order','2023-12-20 13:20:15.368723'),(139,'order','0005_remove_shippingaddress_user_delete_order_and_more','2023-12-20 13:20:15.382724'),(140,'order','0006_shippingaddress','2023-12-20 13:20:27.896530'),(141,'order','0007_order','2023-12-20 13:21:14.996111'),(142,'order','0008_orderitem','2023-12-20 13:21:32.774778'),(143,'order','0009_shoppingcartitem_orderreview','2023-12-20 13:21:49.003556'),(144,'conversation','0009_remove_conversationmessage_conversation_and_more','2023-12-20 13:23:09.741136'),(145,'conversation','0010_initial','2023-12-20 13:23:28.742072'),(146,'conversation','0011_delete_conversationmessage','2023-12-20 13:23:50.835692'),(147,'conversation','0012_conversationmessage','2023-12-20 13:24:31.145387'),(148,'order','0010_alter_orderstatus_status_alter_paymentmethod_method','2023-12-21 17:44:25.025301'),(149,'account','0005_alter_personalinformation_have_children','2023-12-22 14:37:12.166395'),(150,'account','0006_rename_avatar_personalinformation_avatar_url','2023-12-23 12:12:07.183394'),(151,'account','0007_rename_facebook_personalinformation_facebook_url_and_more','2023-12-23 12:39:21.333465'),(152,'conversation','0013_remove_conversationmessage_conversation_and_more','2023-12-23 13:00:50.992277'),(153,'order','0011_remove_orderitem_item_remove_orderitem_order_and_more','2023-12-23 13:00:51.463581'),(154,'item','0008_alter_item_created_at','2023-12-23 13:01:02.043995'),(155,'item','0009_remove_favoritecompare_compare_items_and_more','2023-12-23 13:01:02.043995'),(156,'item','0010_item','2023-12-23 13:09:19.914627'),(157,'item','0011_delete_item','2023-12-23 13:09:19.931002'),(158,'item','0012_item','2023-12-23 16:17:35.450274'),(159,'item','0013_alter_item_created_at','2023-12-23 16:19:51.609370'),(160,'item','0014_alter_item_created_at','2023-12-23 16:19:51.615369'),(161,'item','0015_delete_item','2023-12-23 16:19:51.617369'),(162,'item','0016_item','2023-12-23 16:20:03.654548'),(163,'item','0017_delete_item','2023-12-23 16:20:44.373433'),(164,'item','0018_item','2023-12-23 17:03:40.726047'),(165,'item','0019_delete_item','2023-12-23 17:03:40.740071'),(166,'item','0022_remove_item_category_brand_remove_item_created_by_and_more','2023-12-23 17:11:16.346633'),(167,'item','0023_item_comments','2023-12-23 17:11:16.359715'),(168,'item','0024_delete_comments','2023-12-23 17:11:16.362700'),(169,'item','0025_comments','2023-12-23 17:11:16.364702'),(170,'item','0026_delete_comments','2023-12-23 17:11:16.367700'),(171,'item','0027_delete_item','2023-12-23 17:11:16.370701'),(172,'item','0028_item','2023-12-23 17:11:16.372700'),(173,'item','0029_delete_item','2023-12-23 17:11:16.375701'),(174,'item','0030_item','2023-12-23 17:11:26.076830'),(175,'account','0008_remove_personalinformation_first_name_and_more','2023-12-24 10:56:26.186537'),(176,'order','0012_shoppingcartitem','2023-12-24 10:56:26.509791'),(177,'order','0013_order','2023-12-24 11:03:50.138683'),(178,'conversation','0014_initial','2023-12-24 11:04:55.409677'),(179,'account','0009_alter_personalinformation_have_children','2023-12-24 13:09:36.469005'),(180,'order','0014_orderreview_delete_order','2023-12-24 13:48:51.308615'),(181,'order','0003_delete_order','2023-12-24 13:57:58.361713'),(182,'order','0004_order_orderitem','2023-12-24 14:10:25.749581'),(183,'item','0002_favoritecompare_comments','2023-12-24 14:13:47.807997'),(184,'order','0005_remove_orderitem_item_remove_orderitem_order_and_more','2023-12-25 09:35:54.561115'),(185,'order','0006_order','2023-12-25 09:36:34.859304'),(186,'order','0007_orderreview_orderitem','2023-12-25 09:37:20.073407'),(187,'order','0008_remove_order_contact_info_and_more','2023-12-25 11:05:35.759296'),(188,'order','0009_order','2023-12-25 11:07:17.503921'),(189,'order','0010_contactinfo','2023-12-25 11:08:40.241648'),(190,'order','0011_orderreview_orderitem','2023-12-25 11:09:15.978662'),(191,'order','0012_remove_order_payment_method_remove_order_seller_and_more','2023-12-25 12:01:30.559583'),(192,'order','0013_contactinfo_shippingaddress','2023-12-25 12:03:49.683147'),(193,'order','0014_order','2023-12-25 12:04:05.992222'),(194,'order','0015_orderreview_orderitem','2023-12-25 12:04:22.498308'),(195,'conversation','0003_delete_conversationmessage','2023-12-25 12:56:45.542095'),(196,'conversation','0004_conversationmessage','2023-12-25 12:57:07.296502'),(197,'item','0003_alter_item_availability','2023-12-25 18:08:15.519532'),(198,'item','0004_alter_item_availability','2023-12-25 18:11:06.722434'),(199,'item','0005_alter_item_availability','2023-12-26 12:12:35.205058'),(200,'authentication','0002_alter_user_first_name_alter_user_last_name_and_more','2024-01-01 16:01:47.193172');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('2t4viwdhcn02k7rzqcnibtnhmrk3hycn','.eJxVjEEOwiAQRe_C2hAYKENduvcMZGBAqoYmpV0Z765NutDtf-_9lwi0rTVsPS9hYnEWgxan3zFSeuS2E75Tu80yzW1dpih3RR60y-vM-Xk53L-DSr1-a2UQi0MkGBUah4qyp-JGYsvkvCHW2UNBBoZBs1fakgILORqrY0zi_QHy-zfH:1r3ukB:E2kpyy7e-lnPV7T1lpkwgdksIMRJTb0PkOk1L0oEo1I','2023-12-01 09:02:31.798225'),('7os3pmv7n2f2miickrf0rrfrf0qclaam','.eJxVjMsOwiAQRf-FtSEwKTC4dO83kBkeUjWQlHZl_Hdt0oVu7znnvkSgba1hG3kJcxJnYZQ4_Y5M8ZHbTtKd2q3L2Nu6zCx3RR50yGtP-Xk53L-DSqN-awc6cdFsnQcC6xIiEFvwRUdCA1aBdxnsZExGY8k4BK8yF9LoXZnE-wPsejcy:1r3YZi:AVo7SQfCBuERIIuzQOhGGtoKqhT1bm6ySd3M28a6XdM','2023-11-30 09:22:14.008478'),('e07513brr365s8nyeooon6hlxm6q2czv','.eJxVjEEOwiAQRe_C2hAYKENduvcMZGBAqoYmpV0Z765NutDtf-_9lwi0rTVsPS9hYnEWgxan3zFSeuS2E75Tu80yzW1dpih3RR60y-vM-Xk53L-DSr1-a2UQi0MkGBUah4qyp-JGYsvkvCHW2UNBBoZBs1fakgILORqrY0zi_QHy-zfH:1r3iWD:oOd8cZgyrrbwHKINn_Ql6LQ9jayDwoN-6SG_0S_ZYqk','2023-11-30 19:59:17.746774'),('ejk2nbc6qjwja77k7gzow60d6wh92wsg','.eJxVjEEOwiAQRe_C2hAYKENduvcMZGBAqoYmpV0Z765NutDtf-_9lwi0rTVsPS9hYnEWgxan3zFSeuS2E75Tu80yzW1dpih3RR60y-vM-Xk53L-DSr1-a2UQi0MkGBUah4qyp-JGYsvkvCHW2UNBBoZBs1fakgILORqrY0zi_QHy-zfH:1r4lKf:wZ2efUen79UYJMfLYKrtNTHMSDv2A5qU1Bn_0ah1SQQ','2023-12-03 17:11:41.877657'),('etlfwi66cfytqvzkqs4m01j3p6sizfe1','.eJxVjEEOwiAQRe_C2hDQzpS6dO8ZyMAMUjU0KdSN8e62STfd_vfe_6pCn0Czr42aqKvKI7MUdVKelpb9UmX2I6_AHrdA8SVlA_yk8ph0nEqbx6A3Re-06vvE8r7t7uEgU81rLZKiQ-jApKEP_fmM0VqTolgOmBIOibqLFcBIwmyCs-AcIIjpyQCi-v0B-ShAYg:1qtoU2:AAp3cgO6dEvF3KA61evMLvkt-3gQtlhrY1Gxu5Fe0K4','2023-11-03 12:20:06.818744'),('hrfn488wdz2ztddx8q3kdzj9hpgov0bn','.eJxVjMsOwiAQRf-FtSEwKTC4dO83kBkeUjWQlHZl_Hdt0oVu7znnvkSgba1hG3kJcxJnYZQ4_Y5M8ZHbTtKd2q3L2Nu6zCx3RR50yGtP-Xk53L-DSqN-awc6cdFsnQcC6xIiEFvwRUdCA1aBdxnsZExGY8k4BK8yF9LoXZnE-wPsejcy:1r3O1S:ci5WHcpBh8OHeFYlzq_lymT1MPLYLD34JTxmuzXCKPA','2023-11-29 22:06:10.956917'),('ie9t61x0dkdrpdyaxy78uj8hsvaoiwyk','.eJxVjMsOwiAQRf-FtSEwKTC4dO83kBkeUjWQlHZl_Hdt0oVu7znnvkSgba1hG3kJcxJnYZQ4_Y5M8ZHbTtKd2q3L2Nu6zCx3RR50yGtP-Xk53L-DSqN-awc6cdFsnQcC6xIiEFvwRUdCA1aBdxnsZExGY8k4BK8yF9LoXZnE-wPsejcy:1r3IF2:BuBZ3QJWS-s--0oWTs45BQY-ezQJYDRt_B3HOPDAHcs','2023-11-29 15:55:48.029272'),('l8pynhxhh6q62sc6vgy89vjcvo6f0iiz','.eJxVjEEOwiAQRe_C2hDQzpS6dO8ZyMAMUjU0KdSN8e62STfd_vfe_6pCn0Czr42aqKvKI7MUdVKelpb9UmX2I6_AHrdA8SVlA_yk8ph0nEqbx6A3Re-06vvE8r7t7uEgU81rLZKiQ-jApKEP_fmM0VqTolgOmBIOibqLFcBIwmyCs-AcIIjpyQCi-v0B-ShAYg:1qtoQG:0rBVrl7_tJGZwMMn8qkC8jUnZcRqg5Tpm2g4ug-lUGU','2023-11-03 12:16:12.648792'),('ndbka2yedwppicgfvhppsioj6yqdr5i1','.eJxVjMsOwiAQRf-FtSEwKTC4dO83kBkeUjWQlHZl_Hdt0oVu7znnvkSgba1hG3kJcxJnYZQ4_Y5M8ZHbTtKd2q3L2Nu6zCx3RR50yGtP-Xk53L-DSqN-awc6cdFsnQcC6xIiEFvwRUdCA1aBdxnsZExGY8k4BK8yF9LoXZnE-wPsejcy:1rGpgO:jCBlfAPx98vIQDbSUu13Jyn3ANOa-YpPgld3k6ngSQQ','2024-01-06 00:16:00.739191'),('oojseimfyuiocptlxdffmwp62j8bte27','.eJxVjMsOwiAQRf-FtSEwKTC4dO83kBkeUjWQlHZl_Hdt0oVu7znnvkSgba1hG3kJcxJnYZQ4_Y5M8ZHbTtKd2q3L2Nu6zCx3RR50yGtP-Xk53L-DSqN-awc6cdFsnQcC6xIiEFvwRUdCA1aBdxnsZExGY8k4BK8yF9LoXZnE-wPsejcy:1r4PsG:p3HazWlXD6ypQF_tlrkE50TAAOBTXLOGLVJR2szvY90','2023-12-02 18:16:56.286489'),('pz8q52s7kikor4rb0r85m40rioerk72j','.eJxVjEEOwiAQRe_C2hCmdgbq0n3P0AwwSNVAUtqV8e7apAvd_vfef6mJtzVPW5NlmqO6KFCn381zeEjZQbxzuVUdalmX2etd0QdteqxRntfD_TvI3PK3FknBEfZo0mC97ToKACYFgegpJRoS92cQpMASo_EO0DkkFGPZIJF6fwD4kzgO:1rESKd:03s1njvJ7HLAH1pq31kjt0vy0vlIOdD13M2tYbU-1Ts','2023-12-30 10:55:43.252581'),('sbfww9ikmh0hbm491iwcuygkj1dy2rfl','eyJuYXZiYXJfc3RhdGUiOiJoaWRkZW4ifQ:1qtDBz:G46DENa8P8N_ZpCXD4zhgBV2vlSQgjxHEZr-zAhCAdY','2023-11-01 20:30:59.605252'),('vwwi0lho9gth0echwct5tpzq9ax58fwh','.eJxVjMsOwiAQRf-FtSEwKTC4dO83kBkeUjWQlHZl_Hdt0oVu7znnvkSgba1hG3kJcxJnYZQ4_Y5M8ZHbTtKd2q3L2Nu6zCx3RR50yGtP-Xk53L-DSqN-awc6cdFsnQcC6xIiEFvwRUdCA1aBdxnsZExGY8k4BK8yF9LoXZnE-wPsejcy:1r7IgR:MtEPc9ChQ3cJil3qH0MI_fUNVbbz3x1x2UjwMVQrZu4','2023-12-10 17:12:39.488713'),('vxsiqypgaol960pb3b37gkk0v1c824bp','.eJxVjEEOwiAQRe_C2hCmdgbq0n3P0AwwSNVAUtqV8e7apAvd_vfef6mJtzVPW5NlmqO6KFCn381zeEjZQbxzuVUdalmX2etd0QdteqxRntfD_TvI3PK3FknBEfZo0mC97ToKACYFgegpJRoS92cQpMASo_EO0DkkFGPZIJF6fwD4kzgO:1rLSrB:mUHs6QwiSKvHPunV2oZp8NQGsk-cCreOUm3P1Nr5MKg','2024-01-18 18:54:17.048255');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item_brand`
--

DROP TABLE IF EXISTS `item_brand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item_brand` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item_brand`
--

LOCK TABLES `item_brand` WRITE;
/*!40000 ALTER TABLE `item_brand` DISABLE KEYS */;
INSERT INTO `item_brand` VALUES (1,'Apple'),(4,'Lenovo'),(2,'Samsung'),(3,'Xiaomi');
/*!40000 ALTER TABLE `item_brand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item_category`
--

DROP TABLE IF EXISTS `item_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item_category`
--

LOCK TABLES `item_category` WRITE;
/*!40000 ALTER TABLE `item_category` DISABLE KEYS */;
INSERT INTO `item_category` VALUES (5,'Dish'),(6,'Electronics'),(4,'Kitchen'),(2,'Laptops'),(1,'Phone'),(3,'Play');
/*!40000 ALTER TABLE `item_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item_categorybrand`
--

DROP TABLE IF EXISTS `item_categorybrand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item_categorybrand` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `brand_id` bigint NOT NULL,
  `category_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `item_categorybrand_category_id_brand_id_025a6cc6_uniq` (`category_id`,`brand_id`),
  KEY `item_categorybrand_brand_id_0a28ddb3_fk_item_brand_id` (`brand_id`),
  CONSTRAINT `item_categorybrand_brand_id_0a28ddb3_fk_item_brand_id` FOREIGN KEY (`brand_id`) REFERENCES `item_brand` (`id`),
  CONSTRAINT `item_categorybrand_category_id_9e38ba23_fk_item_category_id` FOREIGN KEY (`category_id`) REFERENCES `item_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item_categorybrand`
--

LOCK TABLES `item_categorybrand` WRITE;
/*!40000 ALTER TABLE `item_categorybrand` DISABLE KEYS */;
INSERT INTO `item_categorybrand` VALUES (1,1,1),(2,2,1),(4,3,1),(3,4,1),(7,1,2),(5,4,2),(8,3,3),(6,4,5);
/*!40000 ALTER TABLE `item_categorybrand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item_comments`
--

DROP TABLE IF EXISTS `item_comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item_comments` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `rating` int DEFAULT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL,
  `comment` longtext NOT NULL,
  `advantages` varchar(255) DEFAULT NULL,
  `disadvantages` varchar(255) DEFAULT NULL,
  `comment_date` datetime(6) NOT NULL,
  `item_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `item_comments_item_id_68af52fd_fk_item_item_id` (`item_id`),
  CONSTRAINT `item_comments_item_id_68af52fd_fk_item_item_id` FOREIGN KEY (`item_id`) REFERENCES `item_item` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item_comments`
--

LOCK TABLES `item_comments` WRITE;
/*!40000 ALTER TABLE `item_comments` DISABLE KEYS */;
INSERT INTO `item_comments` VALUES (5,5,'Alex','Smith','alex@gmail.com','Having used the Lenovo Legion Pro 5 16IRX8 (82WK00KLRA) Onyx Gray laptop for an extended period, I must say it has exceeded my expectations. The performance is still top-notch, handling everything from intensive gaming sessions to demanding work tasks with ease. The sleek Onyx Gray design remains stylish, and the build quality has proven durable. Battery life has held up well, providing long hours of uninterrupted use. Overall, a fantastic investment that continues to impress with its reliability and power. Kudos to Lenovo for crafting such an excellent device!','Performance',NULL,'2024-01-04 18:23:21.437778',17),(6,4,'Alex','Smith','alex@gmail.com','As a long-time user of the Xiaomi 14 Pro, I\'m consistently impressed by its performance and sleek design. This phone has been a reliable companion, seamlessly handling both work and entertainment tasks. The lightweight build makes it incredibly portable, and the stunning display enhances every visual experience.','Display and lightweight build','Life time battery','2024-01-04 18:26:33.424518',16);
/*!40000 ALTER TABLE `item_comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item_favoritecompare`
--

DROP TABLE IF EXISTS `item_favoritecompare`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item_favoritecompare` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `item_favoritecompare_user_id_e003c436_fk_authentication_user_id` (`user_id`),
  CONSTRAINT `item_favoritecompare_user_id_e003c436_fk_authentication_user_id` FOREIGN KEY (`user_id`) REFERENCES `authentication_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item_favoritecompare`
--

LOCK TABLES `item_favoritecompare` WRITE;
/*!40000 ALTER TABLE `item_favoritecompare` DISABLE KEYS */;
INSERT INTO `item_favoritecompare` VALUES (1,1),(4,74);
/*!40000 ALTER TABLE `item_favoritecompare` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item_favoritecompare_compare_items`
--

DROP TABLE IF EXISTS `item_favoritecompare_compare_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item_favoritecompare_compare_items` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `favoritecompare_id` bigint NOT NULL,
  `item_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `item_favoritecompare_com_favoritecompare_id_item__100fcb80_uniq` (`favoritecompare_id`,`item_id`),
  KEY `item_favoritecompare_item_id_29f34e97_fk_item_item` (`item_id`),
  CONSTRAINT `item_favoritecompare_favoritecompare_id_0cda737f_fk_item_favo` FOREIGN KEY (`favoritecompare_id`) REFERENCES `item_favoritecompare` (`id`),
  CONSTRAINT `item_favoritecompare_item_id_29f34e97_fk_item_item` FOREIGN KEY (`item_id`) REFERENCES `item_item` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item_favoritecompare_compare_items`
--

LOCK TABLES `item_favoritecompare_compare_items` WRITE;
/*!40000 ALTER TABLE `item_favoritecompare_compare_items` DISABLE KEYS */;
INSERT INTO `item_favoritecompare_compare_items` VALUES (7,4,14),(8,4,16);
/*!40000 ALTER TABLE `item_favoritecompare_compare_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item_favoritecompare_favorite_items`
--

DROP TABLE IF EXISTS `item_favoritecompare_favorite_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item_favoritecompare_favorite_items` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `favoritecompare_id` bigint NOT NULL,
  `item_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `item_favoritecompare_fav_favoritecompare_id_item__5e4eda88_uniq` (`favoritecompare_id`,`item_id`),
  KEY `item_favoritecompare_item_id_ea86b2a8_fk_item_item` (`item_id`),
  CONSTRAINT `item_favoritecompare_favoritecompare_id_8670cba0_fk_item_favo` FOREIGN KEY (`favoritecompare_id`) REFERENCES `item_favoritecompare` (`id`),
  CONSTRAINT `item_favoritecompare_item_id_ea86b2a8_fk_item_item` FOREIGN KEY (`item_id`) REFERENCES `item_item` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item_favoritecompare_favorite_items`
--

LOCK TABLES `item_favoritecompare_favorite_items` WRITE;
/*!40000 ALTER TABLE `item_favoritecompare_favorite_items` DISABLE KEYS */;
INSERT INTO `item_favoritecompare_favorite_items` VALUES (10,4,15),(11,4,17);
/*!40000 ALTER TABLE `item_favoritecompare_favorite_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item_item`
--

DROP TABLE IF EXISTS `item_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item_item` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `model` varchar(255) NOT NULL,
  `description` longtext,
  `price` double NOT NULL,
  `availability` tinyint(1) NOT NULL,
  `image_url` varchar(100) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `category_brand_id` bigint NOT NULL,
  `created_by_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `item_item_category_brand_id_0b217a5f_fk_item_categorybrand_id` (`category_brand_id`),
  KEY `item_item_created_by_id_abf41b7a_fk_authentication_user_id` (`created_by_id`),
  CONSTRAINT `item_item_category_brand_id_0b217a5f_fk_item_categorybrand_id` FOREIGN KEY (`category_brand_id`) REFERENCES `item_categorybrand` (`id`),
  CONSTRAINT `item_item_created_by_id_abf41b7a_fk_authentication_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `authentication_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item_item`
--

LOCK TABLES `item_item` WRITE;
/*!40000 ALTER TABLE `item_item` DISABLE KEYS */;
INSERT INTO `item_item` VALUES (14,'Samsung Galaxy S23 Ultra 12/256GB Phantom Black (SM-S9180) WARRANTY 3 months.','Samsung Galaxy S23 Ultra\r\nYour photos and videos will be clear from dusk to dawn. Our most innovative Galaxy sensor and fastest processor let you shoot in low light and reduce noise.\r\n\r\nThe most powerful processor in a Galaxy smartphone lets you enjoy your favorite movies or games all day long.\r\n\r\nUsing recycled glass and PET film, this is the greenest smartphone we\'ve ever made. And the packaging made from recycled paper emphasizes this once again.\r\n\r\nUse the Expert RAW app to achieve professional-level detail in your photos. Expand your collection of incredible images with astrophotography, multiple exposures, and more.\r\n',2000,1,'item_images/samsung-galaxy-s23-ultra_3__2_1_1_1_88KzNTC.jpg','2024-01-04 17:59:46.218035',2,73),(15,'Smartphone Xiaomi 13T 8/256Gb Black','Xiaomi 13T is a new generation of smartphones that is designed to make your life easy, high-quality and enjoyable! The crystal AMOLED display displays all colors, the incomparable MediaTek processor will ensure smooth operation of the smartphone, and 67W fast charging ensures that you are always connected.',1400,1,'item_images/Xiaomi_13_Pro_4C2UVvn.jpg','2024-01-04 18:02:18.846589',4,73),(16,'Xiaomi 14 Pro','Brand: Xiaomi Smartphone Screen: 6.73\"; OLED; 3200x1440; 120 Hz Processor: Qualcomm Snapdragon 8 Gen 3 OS: Android 14 Battery: 4880 mAh (non-removable) Camera: 50 (f/1.8, wide-angle) + 50 (f/2.2, ultra-wide-angle, 115 degrees) + 50 (f/2.0, 3.2x telephoto) MpBody: glass/aluminum; 230 g; thickness 8.5 mmNFC: + (contactless payment support, check in stores)\r\n',1600,1,'item_images/Xiaomi_14_Pro_tezzEfw.jpg','2024-01-04 18:03:06.993082',4,73),(17,'Lenovo Legion Pro 5 16IRX8 (82WK00KLRA) Onyx Gray laptop','Lenovo Legion 5 15 is a gaming laptop designed to provide maximum comfort and productivity. The strict design allows it to look great on any desk, which will be appreciated by those users who are simply looking for a powerful work solution. Lenovo Legion 5 15 comes in a fairly wide list of configurations. It uses lines of processors from both Intel and AMD, thanks to which you can choose the most optimal option.',1559,1,'item_images/lenovo_legion_slCsxiT.jpg','2024-01-04 18:06:14.182839',5,73);
/*!40000 ALTER TABLE `item_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_contactinfo`
--

DROP TABLE IF EXISTS `order_contactinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_contactinfo` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `phone_number` varchar(255) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_contactinfo`
--

LOCK TABLES `order_contactinfo` WRITE;
/*!40000 ALTER TABLE `order_contactinfo` DISABLE KEYS */;
INSERT INTO `order_contactinfo` VALUES (1,'0123456789','Alex','Smith','alex@gmail.com'),(2,'0123456789','Alex','Alen','alex@gmail.com'),(3,'0123456789','Alex','Smith','alex@gmail.com');
/*!40000 ALTER TABLE `order_contactinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_order`
--

DROP TABLE IF EXISTS `order_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_order` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `order_date` datetime(6) NOT NULL,
  `total_price` double DEFAULT NULL,
  `comment` longtext NOT NULL,
  `contact_info_id` bigint NOT NULL,
  `payment_method_id` bigint NOT NULL,
  `seller_id` bigint NOT NULL,
  `shipping_address_id` bigint NOT NULL,
  `status_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `order_order_contact_info_id_b9d515dd_fk_order_contactinfo_id` (`contact_info_id`),
  KEY `order_order_payment_method_id_edf8fb89_fk_order_paymentmethod_id` (`payment_method_id`),
  KEY `order_order_seller_id_003495e4_fk_authentication_user_id` (`seller_id`),
  KEY `order_order_shipping_address_id_57e64931_fk_order_shi` (`shipping_address_id`),
  KEY `order_order_status_id_ec745f82_fk_order_orderstatus_id` (`status_id`),
  KEY `order_order_user_id_7cf9bc2b_fk_authentication_user_id` (`user_id`),
  CONSTRAINT `order_order_contact_info_id_b9d515dd_fk_order_contactinfo_id` FOREIGN KEY (`contact_info_id`) REFERENCES `order_contactinfo` (`id`),
  CONSTRAINT `order_order_payment_method_id_edf8fb89_fk_order_paymentmethod_id` FOREIGN KEY (`payment_method_id`) REFERENCES `order_paymentmethod` (`id`),
  CONSTRAINT `order_order_seller_id_003495e4_fk_authentication_user_id` FOREIGN KEY (`seller_id`) REFERENCES `authentication_user` (`id`),
  CONSTRAINT `order_order_shipping_address_id_57e64931_fk_order_shi` FOREIGN KEY (`shipping_address_id`) REFERENCES `order_shippingaddress` (`id`),
  CONSTRAINT `order_order_status_id_ec745f82_fk_order_orderstatus_id` FOREIGN KEY (`status_id`) REFERENCES `order_orderstatus` (`id`),
  CONSTRAINT `order_order_user_id_7cf9bc2b_fk_authentication_user_id` FOREIGN KEY (`user_id`) REFERENCES `authentication_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_order`
--

LOCK TABLES `order_order` WRITE;
/*!40000 ALTER TABLE `order_order` DISABLE KEYS */;
INSERT INTO `order_order` VALUES (7,'2024-01-04 18:16:41.593061',8118,'',2,6,73,2,1,74),(8,'2024-01-04 18:20:24.473513',3000,'Some comment',3,7,73,2,1,74);
/*!40000 ALTER TABLE `order_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_orderitem`
--

DROP TABLE IF EXISTS `order_orderitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_orderitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `amount` int NOT NULL,
  `item_price` double NOT NULL,
  `item_id` bigint NOT NULL,
  `order_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `order_orderitem_item_id_ade63ba0_fk_item_item_id` (`item_id`),
  KEY `order_orderitem_order_id_aba34f44_fk_order_order_id` (`order_id`),
  CONSTRAINT `order_orderitem_item_id_ade63ba0_fk_item_item_id` FOREIGN KEY (`item_id`) REFERENCES `item_item` (`id`),
  CONSTRAINT `order_orderitem_order_id_aba34f44_fk_order_order_id` FOREIGN KEY (`order_id`) REFERENCES `order_order` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_orderitem`
--

LOCK TABLES `order_orderitem` WRITE;
/*!40000 ALTER TABLE `order_orderitem` DISABLE KEYS */;
INSERT INTO `order_orderitem` VALUES (7,1,2000,14,7),(8,1,1400,15,7),(9,1,1600,16,7),(10,2,1559,17,7),(11,1,1600,16,8),(12,1,1400,15,8);
/*!40000 ALTER TABLE `order_orderitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_orderreview`
--

DROP TABLE IF EXISTS `order_orderreview`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_orderreview` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `rating` int DEFAULT NULL,
  `comment` longtext,
  `comment_date` datetime(6) NOT NULL,
  `order_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `order_orderreview_order_id_816b3e35_fk_order_order_id` (`order_id`),
  CONSTRAINT `order_orderreview_order_id_816b3e35_fk_order_order_id` FOREIGN KEY (`order_id`) REFERENCES `order_order` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_orderreview`
--

LOCK TABLES `order_orderreview` WRITE;
/*!40000 ALTER TABLE `order_orderreview` DISABLE KEYS */;
INSERT INTO `order_orderreview` VALUES (4,5,'Smooth and easy ordering process! The website is user-friendly, and I appreciate the wide range of products available.','2024-01-04 18:20:53.271445',8),(5,5,'Excited to receive my order; hoping for a speedy delivery. Kudos to your customer service team for promptly addressing my pre-order inquiries. Looking forward to doing business with you again!','2024-01-04 18:21:44.249997',7);
/*!40000 ALTER TABLE `order_orderreview` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_orderstatus`
--

DROP TABLE IF EXISTS `order_orderstatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_orderstatus` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `order_orderstatus_status_189c9bc3_uniq` (`status`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_orderstatus`
--

LOCK TABLES `order_orderstatus` WRITE;
/*!40000 ALTER TABLE `order_orderstatus` DISABLE KEYS */;
INSERT INTO `order_orderstatus` VALUES (1,'In progress');
/*!40000 ALTER TABLE `order_orderstatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_paymentmethod`
--

DROP TABLE IF EXISTS `order_paymentmethod`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_paymentmethod` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `method` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `order_paymentmethod_method_b18060c6_uniq` (`method`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_paymentmethod`
--

LOCK TABLES `order_paymentmethod` WRITE;
/*!40000 ALTER TABLE `order_paymentmethod` DISABLE KEYS */;
INSERT INTO `order_paymentmethod` VALUES (6,'Card'),(8,'GadgetPay'),(7,'Mail');
/*!40000 ALTER TABLE `order_paymentmethod` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_shippingaddress`
--

DROP TABLE IF EXISTS `order_shippingaddress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_shippingaddress` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `street_address` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `state` varchar(255) NOT NULL,
  `postal_code` varchar(255) NOT NULL,
  `country` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_shippingaddress`
--

LOCK TABLES `order_shippingaddress` WRITE;
/*!40000 ALTER TABLE `order_shippingaddress` DISABLE KEYS */;
INSERT INTO `order_shippingaddress` VALUES (1,'789 Pine Street','Willowville','CA','23456','United States'),(2,'123 Main Street','Springfield','CA','12345','United States');
/*!40000 ALTER TABLE `order_shippingaddress` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_shoppingcartitem`
--

DROP TABLE IF EXISTS `order_shoppingcartitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_shoppingcartitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `amount` int NOT NULL,
  `item_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `order_shoppingcartitem_item_id_563bff38_fk_item_item_id` (`item_id`),
  KEY `order_shoppingcartit_user_id_a1f9ef6c_fk_authentic` (`user_id`),
  CONSTRAINT `order_shoppingcartit_user_id_a1f9ef6c_fk_authentic` FOREIGN KEY (`user_id`) REFERENCES `authentication_user` (`id`),
  CONSTRAINT `order_shoppingcartitem_item_id_563bff38_fk_item_item_id` FOREIGN KEY (`item_id`) REFERENCES `item_item` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_shoppingcartitem`
--

LOCK TABLES `order_shoppingcartitem` WRITE;
/*!40000 ALTER TABLE `order_shoppingcartitem` DISABLE KEYS */;
/*!40000 ALTER TABLE `order_shoppingcartitem` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-04 21:00:29
