-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: dop
-- ------------------------------------------------------
-- Server version	8.0.28

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
) ENGINE=InnoDB AUTO_INCREMENT=105 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add activité',7,'add_activité'),(26,'Can change activité',7,'change_activité'),(27,'Can delete activité',7,'delete_activité'),(28,'Can view activité',7,'view_activité'),(29,'Can add famille',8,'add_famille'),(30,'Can change famille',8,'change_famille'),(31,'Can delete famille',8,'delete_famille'),(32,'Can view famille',8,'view_famille'),(33,'Can add perimetre',9,'add_perimetre'),(34,'Can change perimetre',9,'change_perimetre'),(35,'Can delete perimetre',9,'delete_perimetre'),(36,'Can view perimetre',9,'view_perimetre'),(37,'Can add pmt',10,'add_pmt'),(38,'Can change pmt',10,'change_pmt'),(39,'Can delete pmt',10,'delete_pmt'),(40,'Can view pmt',10,'view_pmt'),(41,'Can add project',11,'add_project'),(42,'Can change project',11,'change_project'),(43,'Can delete project',11,'delete_project'),(44,'Can view project',11,'view_project'),(45,'Can add prévision_mensuelle',12,'add_prévision_mensuelle'),(46,'Can change prévision_mensuelle',12,'change_prévision_mensuelle'),(47,'Can delete prévision_mensuelle',12,'delete_prévision_mensuelle'),(48,'Can view prévision_mensuelle',12,'view_prévision_mensuelle'),(49,'Can add recap_famille',13,'add_recap_famille'),(50,'Can change recap_famille',13,'change_recap_famille'),(51,'Can delete recap_famille',13,'delete_recap_famille'),(52,'Can view recap_famille',13,'view_recap_famille'),(53,'Can add recap_region',14,'add_recap_region'),(54,'Can change recap_region',14,'change_recap_region'),(55,'Can delete recap_region',14,'delete_recap_region'),(56,'Can view recap_region',14,'view_recap_region'),(57,'Can add region',15,'add_region'),(58,'Can change region',15,'change_region'),(59,'Can delete region',15,'delete_region'),(60,'Can view region',15,'view_region'),(61,'Can add structure',16,'add_structure'),(62,'Can change structure',16,'change_structure'),(63,'Can delete structure',16,'delete_structure'),(64,'Can view structure',16,'view_structure'),(65,'Can add type',17,'add_type'),(66,'Can change type',17,'change_type'),(67,'Can delete type',17,'delete_type'),(68,'Can view type',17,'view_type'),(69,'Can add realisation_mensuelle',18,'add_realisation_mensuelle'),(70,'Can change realisation_mensuelle',18,'change_realisation_mensuelle'),(71,'Can delete realisation_mensuelle',18,'delete_realisation_mensuelle'),(72,'Can view realisation_mensuelle',18,'view_realisation_mensuelle'),(73,'Can add acces',19,'add_acces'),(74,'Can change acces',19,'change_acces'),(75,'Can delete acces',19,'delete_acces'),(76,'Can view acces',19,'view_acces'),(77,'Can add Computed Fields Model',20,'add_computedfieldsadminmodel'),(78,'Can change Computed Fields Model',20,'change_computedfieldsadminmodel'),(79,'Can delete Computed Fields Model',20,'delete_computedfieldsadminmodel'),(80,'Can view Computed Fields Model',20,'view_computedfieldsadminmodel'),(81,'Can add Model with contributing ForeignKey Fields',21,'add_contributingmodelsmodel'),(82,'Can change Model with contributing ForeignKey Fields',21,'change_contributingmodelsmodel'),(83,'Can delete Model with contributing ForeignKey Fields',21,'delete_contributingmodelsmodel'),(84,'Can view Model with contributing ForeignKey Fields',21,'view_contributingmodelsmodel'),(85,'Can add etat',22,'add_etat'),(86,'Can change etat',22,'change_etat'),(87,'Can delete etat',22,'delete_etat'),(88,'Can view etat',22,'view_etat'),(89,'Can add fiscalite',23,'add_fiscalite'),(90,'Can change fiscalite',23,'change_fiscalite'),(91,'Can delete fiscalite',23,'delete_fiscalite'),(92,'Can view fiscalite',23,'view_fiscalite'),(93,'Can add recap_activite',24,'add_recap_activite'),(94,'Can change recap_activite',24,'change_recap_activite'),(95,'Can delete recap_activite',24,'delete_recap_activite'),(96,'Can view recap_activite',24,'view_recap_activite'),(97,'Can add recap_one_region',25,'add_recap_one_region'),(98,'Can change recap_one_region',25,'change_recap_one_region'),(99,'Can delete recap_one_region',25,'delete_recap_one_region'),(100,'Can view recap_one_region',25,'view_recap_one_region'),(101,'Can add recap',25,'add_recap'),(102,'Can change recap',25,'change_recap'),(103,'Can delete recap',25,'delete_recap'),(104,'Can view recap',25,'view_recap');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$320000$nw1wGz1eWg730d9kh0dysr$pcF4iUvx5M3qFBgRCvxjB5aCm3IuieXNge+0n2ECurI=','2022-03-27 15:23:19.789620',1,'admin','','','',1,1,'2022-03-10 15:34:02.999752');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
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
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=304 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2022-03-10 16:58:08.085476','1','Hassi Messoud',1,'[{\"added\": {}}]',15,1),(2,'2022-03-10 16:58:13.951400','2','Hassi Rmel',1,'[{\"added\": {}}]',15,1),(3,'2022-03-10 16:58:18.462346','3','Stah',1,'[{\"added\": {}}]',15,1),(4,'2022-03-10 16:58:22.589704','4','Houd Berkaoui',1,'[{\"added\": {}}]',15,1),(5,'2022-03-10 16:58:49.535491','1','Gaz',1,'[{\"added\": {}}]',7,1),(6,'2022-03-10 16:58:55.821638','2','Pétrole',1,'[{\"added\": {}}]',7,1),(7,'2022-03-10 16:58:59.327906','3','Gaz et Pétrole',1,'[{\"added\": {}}]',7,1),(8,'2022-03-10 16:59:44.618898','1','Hassi Rmel Nord',1,'[{\"added\": {}}]',9,1),(9,'2022-03-10 16:59:56.528440','2','Hassi Rmel sud',1,'[{\"added\": {}}]',9,1),(10,'2022-03-10 17:00:07.837696','3','Hassi Messoud Centre',1,'[{\"added\": {}}]',9,1),(11,'2022-03-10 17:00:27.084758','4','Houd Berkoui Centre',1,'[{\"added\": {}}]',9,1),(12,'2022-03-10 17:00:40.796357','5','Houd Berkoui Sud',1,'[{\"added\": {}}]',9,1),(13,'2022-03-10 17:01:00.276171','6','Stah Sud',1,'[{\"added\": {}}]',9,1),(14,'2022-03-10 17:03:39.716411','1','Etudes',1,'[{\"added\": {}}]',8,1),(15,'2022-03-10 17:03:44.283293','2','Activité Puits',1,'[{\"added\": {}}]',8,1),(16,'2022-03-10 17:03:47.697005','3','Installations spécifique',1,'[{\"added\": {}}]',8,1),(17,'2022-03-10 17:03:51.792516','4','Infrastructures sociales',1,'[{\"added\": {}}]',8,1),(18,'2022-03-10 17:03:57.060823','5','Installation générales',1,'[{\"added\": {}}]',8,1),(19,'2022-03-10 17:04:01.386581','6','Equipmenet',1,'[{\"added\": {}}]',8,1),(20,'2022-03-10 17:07:52.873838','1','RD',1,'[{\"added\": {}}]',16,1),(21,'2022-03-10 17:07:56.635708','2','RA',1,'[{\"added\": {}}]',16,1),(22,'2022-03-10 17:35:25.811542','1','IT',1,'[{\"added\": {}}]',17,1),(23,'2022-03-10 17:35:30.882025','2','Logistique',1,'[{\"added\": {}}]',17,1),(24,'2022-03-10 17:35:34.393331','3','Projet Boosting',1,'[{\"added\": {}}]',17,1),(25,'2022-03-10 17:35:37.873411','4','Technique',1,'[{\"added\": {}}]',17,1),(26,'2022-03-10 17:43:48.896937','2','Logistique',3,'',17,1),(27,'2022-03-10 17:43:57.597614','5','Logistique',1,'[{\"added\": {}}]',17,1),(28,'2022-03-10 18:17:19.011930','5','project 1',3,'',11,1),(29,'2022-03-10 18:17:19.016931','4','project 1',3,'',11,1),(30,'2022-03-10 18:17:19.022076','3','project 1',3,'',11,1),(31,'2022-03-10 18:17:19.027285','2','project 1',3,'',11,1),(32,'2022-03-10 18:17:19.032096','1','project 1',3,'',11,1),(33,'2022-03-10 19:45:50.730962','1','Hassi Rmel',3,'',14,1),(34,'2022-03-10 19:46:06.393006','1','Etudes',3,'',13,1),(35,'2022-03-14 10:54:15.886000','6','project 1',3,'',11,1),(36,'2022-03-14 11:02:16.796749','2','Hassi Rmel',3,'',14,1),(37,'2022-03-14 11:02:28.211002','2','Etudes',3,'',13,1),(38,'2022-03-14 11:31:45.285173','2','RA',3,'',16,1),(39,'2022-03-14 11:31:45.291988','1','RD',3,'',16,1),(40,'2022-03-14 11:31:49.785901','3','A',1,'[{\"added\": {}}]',16,1),(41,'2022-03-14 11:31:53.561331','4','B',1,'[{\"added\": {}}]',16,1),(42,'2022-03-14 11:31:55.504438','5','C',1,'[{\"added\": {}}]',16,1),(43,'2022-03-14 11:31:57.722756','6','D',1,'[{\"added\": {}}]',16,1),(44,'2022-03-14 11:31:59.712394','7','E',1,'[{\"added\": {}}]',16,1),(45,'2022-03-14 11:32:01.304088','8','F',1,'[{\"added\": {}}]',16,1),(46,'2022-03-14 11:32:37.066292','9','G',1,'[{\"added\": {}}]',16,1),(47,'2022-03-14 11:32:39.173660','10','H',1,'[{\"added\": {}}]',16,1),(48,'2022-03-14 11:32:42.095454','11','I',1,'[{\"added\": {}}]',16,1),(49,'2022-03-14 11:32:44.926398','12','J',1,'[{\"added\": {}}]',16,1),(50,'2022-03-14 11:32:46.973658','13','K',1,'[{\"added\": {}}]',16,1),(51,'2022-03-14 11:32:48.783606','14','L',1,'[{\"added\": {}}]',16,1),(52,'2022-03-14 11:32:50.783866','15','M',1,'[{\"added\": {}}]',16,1),(53,'2022-03-14 11:32:52.655727','16','N',1,'[{\"added\": {}}]',16,1),(54,'2022-03-14 11:32:56.934178','17','O',1,'[{\"added\": {}}]',16,1),(55,'2022-03-14 11:33:09.044869','18','P',1,'[{\"added\": {}}]',16,1),(56,'2022-03-14 11:33:11.833950','19','Q',1,'[{\"added\": {}}]',16,1),(57,'2022-03-14 11:33:14.193990','20','R',1,'[{\"added\": {}}]',16,1),(58,'2022-03-14 11:33:16.023358','21','S',1,'[{\"added\": {}}]',16,1),(59,'2022-03-14 11:33:17.904801','22','T',1,'[{\"added\": {}}]',16,1),(60,'2022-03-14 11:33:19.474703','23','U',1,'[{\"added\": {}}]',16,1),(61,'2022-03-14 11:37:46.974105','1','RD',1,'[{\"added\": {}}]',23,1),(62,'2022-03-14 11:37:52.294698','2','RA',1,'[{\"added\": {}}]',23,1),(63,'2022-03-14 11:51:30.659054','7','Work Over HR Huile',2,'[{\"changed\": {\"fields\": [\"Prevision n2 devise\"]}}]',11,1),(64,'2022-03-14 11:52:23.577051','7','Work Over HR Huile',2,'[{\"changed\": {\"fields\": [\"Cout Globale initial devise\"]}}]',11,1),(65,'2022-03-14 13:06:36.281790','8','Work Over HR Huile',3,'',11,1),(66,'2022-03-14 14:13:28.365370','7','Work Over HR Huile',3,'',11,1),(67,'2022-03-14 14:13:45.721870','3','Etudes',3,'',13,1),(68,'2022-03-14 14:13:52.803715','3','Hassi Rmel',3,'',14,1),(69,'2022-03-14 14:15:38.850055','4','Etudes',3,'',13,1),(70,'2022-03-14 14:15:48.933933','4','Hassi Rmel',3,'',14,1),(71,'2022-03-14 14:16:54.707063','5','Etudes',3,'',13,1),(72,'2022-03-14 14:17:42.960642','11','Work Over HR Huile',3,'',11,1),(73,'2022-03-14 14:17:42.966595','10','Work Over HR Huile',3,'',11,1),(74,'2022-03-14 14:17:42.970584','9','Work Over HR Huile',3,'',11,1),(75,'2022-03-14 14:18:29.841005','5','Hassi Rmel',3,'',14,1),(76,'2022-03-14 14:18:38.991385','6','Etudes',3,'',13,1),(77,'2022-03-14 14:21:46.881715','7','Etudes',3,'',13,1),(78,'2022-03-14 14:21:52.998993','12','Work Over HR Huile',3,'',11,1),(79,'2022-03-14 14:22:07.933204','6','Hassi Rmel',3,'',14,1),(80,'2022-03-14 14:25:01.525771','14','Work Over HR Huile',3,'',11,1),(81,'2022-03-14 14:48:25.174060','13','Work Over HR Huile',3,'',11,1),(82,'2022-03-14 14:49:04.206781','15','Work Over HR Huile',3,'',11,1),(83,'2022-03-14 14:49:34.928912','8','Etudes',3,'',13,1),(84,'2022-03-14 14:49:41.842282','7','Hassi Rmel',3,'',14,1),(85,'2022-03-14 16:52:55.724464','23','project 1',3,'',11,1),(86,'2022-03-14 16:52:55.729207','22','project 1',3,'',11,1),(87,'2022-03-14 16:52:55.732488','21','project 1',3,'',11,1),(88,'2022-03-14 16:52:55.737773','20','project 1',3,'',11,1),(89,'2022-03-14 16:52:55.742157','19','project 1',3,'',11,1),(90,'2022-03-14 16:52:55.746305','18','project 1',3,'',11,1),(91,'2022-03-14 16:52:55.750417','17','project 1',3,'',11,1),(92,'2022-03-14 16:52:55.754358','16','Work Over HR Huile',3,'',11,1),(93,'2022-03-14 16:53:08.294580','9','Stah',3,'',14,1),(94,'2022-03-14 16:53:08.304946','8','Hassi Rmel',3,'',14,1),(95,'2022-03-14 16:53:15.615473','9','Etudes',3,'',13,1),(96,'2022-03-14 17:54:38.897839','31','project 1',3,'',11,1),(97,'2022-03-14 17:54:38.905830','30','project 1',3,'',11,1),(98,'2022-03-14 17:54:38.914007','29','project 1',3,'',11,1),(99,'2022-03-14 17:54:38.921819','28','project 1',3,'',11,1),(100,'2022-03-14 17:54:38.921819','27','project 1',3,'',11,1),(101,'2022-03-14 17:54:38.929813','26','project 1',3,'',11,1),(102,'2022-03-14 17:54:38.929813','25','Work Over HR Huile',3,'',11,1),(103,'2022-03-14 17:54:38.937995','24','project 1',3,'',11,1),(104,'2022-03-14 17:54:47.939228','11','Etudes',3,'',13,1),(105,'2022-03-14 17:54:47.947223','10','Etudes',3,'',13,1),(106,'2022-03-14 17:55:00.362361','11','Hassi Rmel',3,'',14,1),(107,'2022-03-14 17:55:00.370534','10','Stah',3,'',14,1),(108,'2022-03-14 17:56:50.318511','13','Etudes',3,'',13,1),(109,'2022-03-14 17:56:50.326506','12','Etudes',3,'',13,1),(110,'2022-03-14 17:59:03.880601','32','Work Over HR Huile',3,'',11,1),(111,'2022-03-14 17:59:16.953340','12','Hassi Rmel',3,'',14,1),(112,'2022-03-14 18:03:35.157984','15','Etudes',3,'',13,1),(113,'2022-03-14 18:03:35.166159','14','Etudes',3,'',13,1),(114,'2022-03-14 18:03:43.533021','33','project 1',3,'',11,1),(115,'2022-03-14 18:03:50.546884','13','Stah',3,'',14,1),(116,'2022-03-16 09:18:31.804099','5','Rhourde El Baghuel',1,'[{\"added\": {}}]',15,1),(117,'2022-03-16 09:18:39.585434','6','Gassi Touil',1,'[{\"added\": {}}]',15,1),(118,'2022-03-16 09:18:53.847079','7','Rhourde nouss',1,'[{\"added\": {}}]',15,1),(119,'2022-03-16 09:19:18.679909','8','Tin Fouyé Tabankort',1,'[{\"added\": {}}]',15,1),(120,'2022-03-16 09:19:25.611885','9','Ohanet',1,'[{\"added\": {}}]',15,1),(121,'2022-03-16 09:19:41.904873','10','In Aménas',1,'[{\"added\": {}}]',15,1),(122,'2022-03-16 09:19:50.419453','11','Hors Region',1,'[{\"added\": {}}]',15,1),(123,'2022-03-16 09:20:19.309362','12','Structure de siége DPR',1,'[{\"added\": {}}]',15,1),(124,'2022-03-16 10:18:25.554282','46','project 2',3,'',11,1),(125,'2022-03-16 10:18:25.565910','45','project 2',3,'',11,1),(126,'2022-03-16 10:18:25.571176','44','project 2',3,'',11,1),(127,'2022-03-16 10:18:25.576210','43','project 2',3,'',11,1),(128,'2022-03-16 10:18:25.581278','42','project 2',3,'',11,1),(129,'2022-03-16 10:18:25.586792','41','project 2',3,'',11,1),(130,'2022-03-16 10:18:25.591793','40','project 2',3,'',11,1),(131,'2022-03-16 10:18:25.595802','39','project 2',3,'',11,1),(132,'2022-03-16 10:18:25.600761','38','project 2',3,'',11,1),(133,'2022-03-16 10:18:25.605356','37','project 2',3,'',11,1),(134,'2022-03-16 10:18:25.609237','36','project 1',3,'',11,1),(135,'2022-03-16 10:18:25.614770','35','project 1',3,'',11,1),(136,'2022-03-16 10:18:25.619299','34','project 1',3,'',11,1),(137,'2022-03-16 10:18:33.589381','3','Gaz et Pétrole',3,'',24,1),(138,'2022-03-16 10:18:33.596776','2','Gaz',3,'',24,1),(139,'2022-03-16 10:18:33.602120','1','Pétrole',3,'',24,1),(140,'2022-03-16 10:18:43.573310','17','Activité Puits',3,'',13,1),(141,'2022-03-16 10:18:43.580046','16','Etudes',3,'',13,1),(142,'2022-03-16 10:19:07.495680','17','Hassi Messoud',3,'',14,1),(143,'2022-03-16 10:19:07.503198','16','Hassi Rmel',3,'',14,1),(144,'2022-03-16 10:19:07.507869','15','Houd Berkaoui',3,'',14,1),(145,'2022-03-16 10:19:07.511774','14','Stah',3,'',14,1),(146,'2022-03-16 10:19:14.565799','4','Hassi Rmel-Etudes-Pétrole',3,'',25,1),(147,'2022-03-16 10:19:14.571673','3','Hassi Messoud-Activité Puits-Gaz et Pétrole',3,'',25,1),(148,'2022-03-16 10:19:14.575952','2','Hassi Rmel-Activité Puits-Gaz',3,'',25,1),(149,'2022-03-16 10:19:14.580977','1','Hassi Rmel-Etudes-Gaz',3,'',25,1),(150,'2022-03-16 10:19:41.968552','3','Gaz et Pétrole',3,'',7,1),(151,'2022-03-16 10:34:04.282629','6','/',1,'[{\"added\": {}}]',17,1),(152,'2022-03-16 12:47:59.487984','47','project 2',3,'',11,1),(153,'2022-03-16 12:51:57.262220','5','Hassi Rmel-Etudes-Pétrole',3,'',25,1),(154,'2022-03-16 12:52:05.718614','18','Hassi Rmel',3,'',14,1),(155,'2022-03-16 12:52:12.062535','18','Etudes',3,'',13,1),(156,'2022-03-16 12:52:19.924823','4','Pétrole',3,'',24,1),(157,'2022-03-16 13:09:29.015244','7','new famille',1,'[{\"added\": {}}]',8,1),(158,'2022-03-16 13:09:41.447868','7','new famille',3,'',8,1),(159,'2022-03-16 13:35:43.963700','6','Stah Sud',3,'',9,1),(160,'2022-03-16 13:35:43.969584','5','Houd Berkoui Sud',3,'',9,1),(161,'2022-03-16 13:35:43.973801','4','Houd Berkoui Centre',3,'',9,1),(162,'2022-03-16 13:35:43.977793','2','Hassi Rmel sud',3,'',9,1),(163,'2022-03-16 13:35:43.982200','1','Hassi Rmel Nord',3,'',9,1),(164,'2022-03-16 13:37:32.958547','7','Haoud Berkoui',1,'[{\"added\": {}}]',9,1),(165,'2022-03-16 13:38:19.892067','8','Haoud Berkoui sud',1,'[{\"added\": {}}]',9,1),(166,'2022-03-21 13:33:40.956130','2','Work Over HBK-fevrier',3,'',18,1),(167,'2022-03-21 13:33:40.971081','1','Work Over HBK-janvier',3,'',18,1),(168,'2022-03-21 14:23:48.274222','52','Work Over HBK',3,'',11,1),(169,'2022-03-21 14:23:48.282200','51','Work Over HBK',3,'',11,1),(170,'2022-03-21 14:23:48.288187','49','Work Over HBK',3,'',11,1),(171,'2022-03-21 14:33:25.195791','9','Work Over HBK-fevrier',3,'',18,1),(172,'2022-03-21 14:33:25.206758','8','Work Over HBK-janvier',3,'',18,1),(173,'2022-03-21 14:33:25.213736','7','Work Over HBK-janvier',3,'',18,1),(174,'2022-03-21 14:33:25.220723','6','Work Over HBK-janvier',3,'',18,1),(175,'2022-03-21 14:33:25.227697','5','Work Over HBK-janvier',3,'',18,1),(176,'2022-03-21 14:33:25.234745','4','Work Over HBK-janvier',3,'',18,1),(177,'2022-03-21 14:33:25.241795','3','Work Over HBK-janvier',3,'',18,1),(178,'2022-03-22 13:37:48.837286','25','Work Over HBK-janvier',1,'[{\"added\": {}}]',12,1),(179,'2022-03-22 13:38:17.736011','26','Work Over HBK-mars',1,'[{\"added\": {}}]',12,1),(180,'2022-03-22 15:00:30.149720','15','Work Over HBK-janvier',3,'',18,1),(181,'2022-03-22 15:00:30.160917','14','Work Over HBK2-fevrier',3,'',18,1),(182,'2022-03-22 15:00:30.166489','13','Work Over HBK-fevrier',3,'',18,1),(183,'2022-03-22 15:00:30.171467','12','Work Over HBK-fevrier',3,'',18,1),(184,'2022-03-22 15:00:30.176787','11','Work Over HBK-fevrier',3,'',18,1),(185,'2022-03-22 15:00:30.182456','10','Work Over HBK-janvier',3,'',18,1),(186,'2022-03-22 17:37:54.748920','53','Work Over HBK',3,'',11,1),(187,'2022-03-22 18:10:24.812775','28','test-fevrier',2,'[{\"changed\": {\"fields\": [\"Montant Prevu Total\", \"Montant Prevu Devise\"]}}]',12,1),(188,'2022-03-22 18:13:13.651522','28','test-fevrier',2,'[{\"changed\": {\"fields\": [\"Montant Prevu Total\", \"Montant Prevu Devise\"]}}]',12,1),(189,'2022-03-23 10:04:10.242235','17','Work Over HBK2-fevrier',3,'',18,1),(190,'2022-03-23 10:04:10.251631','16','Work Over HBK2-janvier',3,'',18,1),(191,'2022-03-23 10:55:07.775459','19','test-fevrier',3,'',18,1),(192,'2022-03-23 10:55:41.853791','18','test-janvier',3,'',18,1),(193,'2022-03-23 10:57:24.786390','20','test-janvier',3,'',18,1),(194,'2022-03-23 16:40:07.920918','28','Work Over HBK2-fevrier',3,'',18,1),(195,'2022-03-23 16:40:07.928878','27','Work Over HBK2-janvier',3,'',18,1),(196,'2022-03-23 16:40:07.936888','26','test-juin',3,'',18,1),(197,'2022-03-23 16:40:07.936888','25','test-mai',3,'',18,1),(198,'2022-03-23 16:40:07.944868','24','test-avril',3,'',18,1),(199,'2022-03-23 16:40:07.944868','23','test-mars',3,'',18,1),(200,'2022-03-23 16:40:07.961163','22','test-fevrier',3,'',18,1),(201,'2022-03-23 16:40:07.961163','21','test-janvier',3,'',18,1),(202,'2022-03-23 17:02:36.251505','38','test-decembre',3,'',12,1),(203,'2022-03-23 17:02:36.259475','37','test-novombre',3,'',12,1),(204,'2022-03-23 17:02:36.283487','36','test-octobre',3,'',12,1),(205,'2022-03-23 17:02:36.291631','35','test-septembre',3,'',12,1),(206,'2022-03-23 17:02:36.291631','34','test-aout',3,'',12,1),(207,'2022-03-23 17:02:36.299454','33','test-juillet',3,'',12,1),(208,'2022-03-23 17:02:36.299454','32','test-juin',3,'',12,1),(209,'2022-03-23 17:02:36.307460','31','test-mai',3,'',12,1),(210,'2022-03-23 17:02:36.307460','30','test-avril',3,'',12,1),(211,'2022-03-23 17:02:36.315438','29','test-mars',3,'',12,1),(212,'2022-03-23 17:02:36.315438','28','test-fevrier',3,'',12,1),(213,'2022-03-23 17:02:36.323432','27','test-janvier',3,'',12,1),(214,'2022-03-23 17:02:36.331432','24','Work Over HBK2-decembre',3,'',12,1),(215,'2022-03-23 17:02:36.347417','23','Work Over HBK2-novombre',3,'',12,1),(216,'2022-03-23 17:02:36.355417','22','Work Over HBK2-octobre',3,'',12,1),(217,'2022-03-23 17:02:36.363406','21','Work Over HBK2-septembre',3,'',12,1),(218,'2022-03-23 17:02:36.363406','20','Work Over HBK2-aout',3,'',12,1),(219,'2022-03-23 17:02:36.371401','19','Work Over HBK2-juillet',3,'',12,1),(220,'2022-03-23 17:02:36.379395','18','Work Over HBK2-juin',3,'',12,1),(221,'2022-03-23 17:02:36.379395','17','Work Over HBK2-mai',3,'',12,1),(222,'2022-03-23 17:02:36.387391','16','Work Over HBK2-avril',3,'',12,1),(223,'2022-03-23 17:02:36.395389','15','Work Over HBK2-mars',3,'',12,1),(224,'2022-03-23 17:02:36.403561','14','Work Over HBK2-fevrier',3,'',12,1),(225,'2022-03-23 17:02:36.403561','13','Work Over HBK2-janvier',3,'',12,1),(226,'2022-03-23 17:03:41.988494','55','test',3,'',11,1),(227,'2022-03-23 17:03:41.996644','54','Work Over HBK2',3,'',11,1),(228,'2022-03-23 17:31:21.401668','69','Work Over HBK-octobre',3,'',12,1),(229,'2022-03-23 17:31:21.417659','68','Work Over HBK-septembre',3,'',12,1),(230,'2022-03-23 17:31:21.417659','67','Work Over HBK-aout',3,'',12,1),(231,'2022-03-23 17:31:21.425652','66','Work Over HBK-juillet',3,'',12,1),(232,'2022-03-23 17:31:21.425652','65','Work Over HBK-juin',3,'',12,1),(233,'2022-03-23 17:31:21.433614','64','Work Over HBK-mai',3,'',12,1),(234,'2022-03-23 17:31:21.433614','63','Work Over HBK-avril',3,'',12,1),(235,'2022-03-23 17:31:21.441641','62','Work Over HBK-mars',3,'',12,1),(236,'2022-03-23 17:31:21.449637','61','Work Over HBK-fevrier',3,'',12,1),(237,'2022-03-23 17:31:21.449637','60','Work Over HBK-janvier',3,'',12,1),(238,'2022-03-23 17:31:21.457596','59','Work Over HBK-septembre',3,'',12,1),(239,'2022-03-23 17:31:21.465623','58','Work Over HBK-aout',3,'',12,1),(240,'2022-03-23 17:31:21.473767','57','Work Over HBK-juillet',3,'',12,1),(241,'2022-03-23 17:31:21.481580','56','Work Over HBK-juin',3,'',12,1),(242,'2022-03-23 17:31:21.489655','55','Work Over HBK-mai',3,'',12,1),(243,'2022-03-23 17:31:21.497570','54','Work Over HBK-avril',3,'',12,1),(244,'2022-03-23 17:31:21.497570','53','Work Over HBK-mars',3,'',12,1),(245,'2022-03-23 17:31:21.505564','52','Work Over HBK-fevrier',3,'',12,1),(246,'2022-03-23 17:31:21.505564','51','Work Over HBK-janvier',3,'',12,1),(247,'2022-03-23 17:31:21.513559','50','Work Over HBK-decembre',3,'',12,1),(248,'2022-03-23 17:31:21.513559','49','Work Over HBK-novombre',3,'',12,1),(249,'2022-03-23 17:31:21.521570','48','Work Over HBK-octobre',3,'',12,1),(250,'2022-03-23 17:31:21.521570','47','Work Over HBK-septembre',3,'',12,1),(251,'2022-03-23 17:31:21.529549','46','Work Over HBK-aout',3,'',12,1),(252,'2022-03-23 17:31:21.529549','45','Work Over HBK-juillet',3,'',12,1),(253,'2022-03-23 17:31:21.537543','44','Work Over HBK-juin',3,'',12,1),(254,'2022-03-23 17:31:21.545538','43','Work Over HBK-mai',3,'',12,1),(255,'2022-03-23 17:31:21.545538','42','Work Over HBK-avril',3,'',12,1),(256,'2022-03-23 17:31:21.553541','41','Work Over HBK-mars',3,'',12,1),(257,'2022-03-23 17:31:21.553541','40','Work Over HBK-fevrier',3,'',12,1),(258,'2022-03-23 17:31:21.561527','39','Work Over HBK-janvier',3,'',12,1),(259,'2022-03-23 17:33:17.300475','56','Work Over HBK',3,'',11,1),(260,'2022-03-23 22:41:03.227035','13','Hassi Rmel',1,'[{\"added\": {}}]',15,1),(261,'2022-03-23 22:41:12.182982','13','Hassi Rmel',3,'',15,1),(262,'2022-03-23 22:41:34.832387','9','Hassi Rmel',1,'[{\"added\": {}}]',9,1),(263,'2022-03-24 10:23:26.030724','58','Work Over HBK2',3,'',11,1),(264,'2022-03-24 10:23:26.037887','57','Work Over HBK',3,'',11,1),(265,'2022-03-24 10:27:50.101774','59','Work Over HBK',2,'[{\"changed\": {\"fields\": [\"Prevision n total\", \"Prevision n devise\"]}}]',11,1),(266,'2022-03-24 10:28:11.593905','33','Work Over HBK-janvier',3,'',18,1),(267,'2022-03-24 13:52:19.092839','10','Hassi Rmel centre',1,'[{\"added\": {}}]',9,1),(268,'2022-03-24 13:54:09.514474','11','Hassi Rmel pétrole',1,'[{\"added\": {}}]',9,1),(269,'2022-03-24 13:55:23.062088','12','Hassi Rmel Gaz',1,'[{\"added\": {}}]',9,1),(270,'2022-03-24 13:56:32.814027','13','Haoud Berkoui centre',1,'[{\"added\": {}}]',9,1),(271,'2022-03-24 14:14:32.386594','5','Logistique',3,'',17,1),(272,'2022-03-24 14:14:32.393983','4','Technique',3,'',17,1),(273,'2022-03-24 14:14:32.399159','3','Projet Boosting',3,'',17,1),(274,'2022-03-24 14:14:37.180490','7','HSE',1,'[{\"added\": {}}]',17,1),(275,'2022-03-24 14:34:36.761468','60','new project',3,'',11,1),(276,'2022-03-24 14:34:36.770411','59','Work Over HBK',3,'',11,1),(277,'2022-03-24 14:34:50.435880','6','Gaz',3,'',24,1),(278,'2022-03-24 14:34:50.441861','5','Pétrole',3,'',24,1),(279,'2022-03-24 14:34:59.864272','20','Etudes',3,'',13,1),(280,'2022-03-24 14:34:59.871425','19','Activité Puits',3,'',13,1),(281,'2022-03-24 14:35:09.037043','20','Hassi Rmel',3,'',14,1),(282,'2022-03-24 14:35:09.043834','19','Houd Berkaoui',3,'',14,1),(283,'2022-03-24 14:35:17.846938','8','Hassi Rmel-Activité Puits-Gaz',3,'',25,1),(284,'2022-03-24 14:35:17.852922','7','Houd Berkaoui-Etudes-Pétrole',3,'',25,1),(285,'2022-03-24 14:35:17.856912','6','Houd Berkaoui-Activité Puits-Pétrole',3,'',25,1),(286,'2022-03-24 14:36:01.635917','13','Haoud Berkoui centre',3,'',9,1),(287,'2022-03-24 14:36:01.641876','12','Hassi Rmel Gaz',3,'',9,1),(288,'2022-03-24 14:36:01.649852','11','Hassi Rmel pétrole',3,'',9,1),(289,'2022-03-24 14:36:01.653841','10','Hassi Rmel centre',3,'',9,1),(290,'2022-03-24 14:36:01.658873','9','Hassi Rmel',3,'',9,1),(291,'2022-03-24 14:36:01.664002','8','Haoud Berkoui sud',3,'',9,1),(292,'2022-03-24 14:36:01.668337','7','Haoud Berkoui',3,'',9,1),(293,'2022-03-27 15:40:52.071973','14','Hassi Rmel',1,'[{\"added\": {}}]',9,1),(294,'2022-03-27 15:41:04.613872','15','Hassi Rmel centre',1,'[{\"added\": {}}]',9,1),(295,'2022-03-27 15:41:14.633043','16','Haoud Berkoui',1,'[{\"added\": {}}]',9,1),(296,'2022-03-27 15:41:30.806817','17','Haoud Berkoui sud',1,'[{\"added\": {}}]',9,1),(297,'2022-03-27 15:41:47.773636','18','Hassi Messoud',1,'[{\"added\": {}}]',9,1),(298,'2022-03-27 15:57:25.213832','19','Stah',1,'[{\"added\": {}}]',9,1),(299,'2022-03-27 16:05:56.819056','61','Work Over HBK',2,'[{\"changed\": {\"fields\": [\"Point situation\"]}}]',11,1),(300,'2022-03-27 16:35:38.134780','20','Gassi touil',1,'[{\"added\": {}}]',9,1),(301,'2022-03-27 16:35:57.982102','21','ohanet',1,'[{\"added\": {}}]',9,1),(302,'2022-03-27 16:36:53.629302','63','Projet Boosting',2,'[{\"changed\": {\"fields\": [\"Famille\"]}}]',11,1),(303,'2022-03-27 16:37:02.759735','64','Projet Boosting 2',2,'[{\"changed\": {\"fields\": [\"Famille\"]}}]',11,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(20,'computedfields','computedfieldsadminmodel'),(21,'computedfields','contributingmodelsmodel'),(5,'contenttypes','contenttype'),(19,'home','acces'),(7,'home','activité'),(22,'home','etat'),(8,'home','famille'),(23,'home','fiscalite'),(9,'home','perimetre'),(10,'home','pmt'),(12,'home','prévision_mensuelle'),(11,'home','project'),(18,'home','realisation_mensuelle'),(25,'home','recap'),(24,'home','recap_activite'),(13,'home','recap_famille'),(14,'home','recap_region'),(15,'home','region'),(16,'home','structure'),(17,'home','type'),(6,'sessions','session');
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
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-03-10 15:32:34.170113'),(2,'auth','0001_initial','2022-03-10 15:32:35.011243'),(3,'admin','0001_initial','2022-03-10 15:32:35.217507'),(4,'admin','0002_logentry_remove_auto_add','2022-03-10 15:32:35.240810'),(5,'admin','0003_logentry_add_action_flag_choices','2022-03-10 15:32:35.252895'),(6,'contenttypes','0002_remove_content_type_name','2022-03-10 15:32:35.410064'),(7,'auth','0002_alter_permission_name_max_length','2022-03-10 15:32:35.503885'),(8,'auth','0003_alter_user_email_max_length','2022-03-10 15:32:35.533238'),(9,'auth','0004_alter_user_username_opts','2022-03-10 15:32:35.545144'),(10,'auth','0005_alter_user_last_login_null','2022-03-10 15:32:35.619888'),(11,'auth','0006_require_contenttypes_0002','2022-03-10 15:32:35.625664'),(12,'auth','0007_alter_validators_add_error_messages','2022-03-10 15:32:35.636667'),(13,'auth','0008_alter_user_username_max_length','2022-03-10 15:32:35.731373'),(14,'auth','0009_alter_user_last_name_max_length','2022-03-10 15:32:35.818286'),(15,'auth','0010_alter_group_name_max_length','2022-03-10 15:32:35.843343'),(16,'auth','0011_update_proxy_permissions','2022-03-10 15:32:35.854039'),(17,'auth','0012_alter_user_first_name_max_length','2022-03-10 15:32:35.939384'),(18,'computedfields','0001_initial','2022-03-10 15:32:35.948682'),(19,'computedfields','0002_contributingmodelsmodel','2022-03-10 15:32:35.956314'),(20,'computedfields','0003_auto_20200713_2212','2022-03-10 15:32:35.964293'),(21,'home','0001_initial','2022-03-10 15:32:37.311171'),(22,'sessions','0001_initial','2022-03-10 15:32:37.404881'),(23,'home','0002_etat_delete_pmt_remove_project_etat','2022-03-10 17:40:09.771384'),(24,'home','0003_project_etat','2022-03-10 18:09:39.143321'),(25,'home','0004_alter_project_realisation_s1_total','2022-03-14 10:57:47.426815'),(26,'home','0005_project_realisation_cum_devise_and_more','2022-03-14 11:03:54.741411'),(27,'home','0006_fiscalite_alter_project_fiscalite','2022-03-14 11:36:43.791066'),(28,'home','0007_recap_famille_prevision_s2_devise_and_more','2022-03-14 14:52:46.041287'),(29,'home','0008_alter_recap_famille_realisation_cum_devise_and_more','2022-03-14 16:41:55.057756'),(30,'home','0009_alter_project_realisation_cum_devise_and_more','2022-03-14 16:42:45.670689'),(31,'home','0010_alter_project_prevision_s2_total_and_more','2022-03-14 16:48:25.366441'),(32,'home','0011_alter_project_realisation_s1_devise_and_more','2022-03-14 16:49:27.325836'),(33,'home','0012_alter_project_point_situation_and_more','2022-03-14 16:54:12.625940'),(34,'home','0013_alter_project_point_situation','2022-03-14 16:56:20.893872'),(35,'home','0014_recap_activite','2022-03-14 17:17:14.271050'),(36,'home','0015_recap_one_region','2022-03-15 14:54:59.211683'),(37,'home','0016_rename_recap_one_region_recap','2022-03-15 18:48:06.390153'),(38,'home','0017_alter_project_unique_together','2022-03-16 10:19:51.601669'),(39,'home','0018_alter_project_type','2022-03-16 10:33:05.533960'),(40,'home','0019_remove_project_etat_alter_project_type','2022-03-16 10:34:51.852496'),(41,'home','0020_rename_prévision_mensuelle_id_prévision_mensuelle_prevision_mensuelle_id_and_more','2022-03-17 17:50:37.030409'),(42,'home','0021_rename_mois_prév_prévision_mensuelle_mois_prev_and_more','2022-03-17 17:54:27.999117'),(43,'home','0022_realisation_mensuelle_pmt','2022-03-21 13:52:51.091786'),(44,'home','0023_remove_realisation_mensuelle_pmt','2022-03-21 14:19:55.272241'),(45,'home','0024_realisation_mensuelle_pmt','2022-03-21 14:32:53.446978'),(46,'home','0025_realisation_mensuelle_real_cum','2022-03-23 10:04:27.840494'),(47,'home','0026_alter_realisation_mensuelle_montant_real_devise_and_more','2022-03-23 10:56:01.164469'),(48,'home','0027_rename_taux_real_cum_realisation_mensuelle_taux_real_cum_devise_and_more','2022-03-23 16:40:28.801056'),(49,'home','0028_rename_real_cum_realisation_mensuelle_real_cum_devise_and_more','2022-03-23 16:50:52.088892'),(50,'home','0029_prévision_mensuelle_prev_cum_devise_and_more','2022-03-23 17:05:45.548521');
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
INSERT INTO `django_session` VALUES ('7f6y2nnv1cwdz5fi77zs4soaplo6nrru','.eJxVjkEOwiAQRe_C2hAoVAaX7j0DmWGmUjVtUtqV8e6WpAvd_vfy8t8q4baWtFVZ0sjqoqw6_W6E-SlTA_zA6T7rPE_rMpJuij5o1beZ5XU93L9AwVpalgL1gw2YnZMu9jGiZOMMIZM9s3UAguSH3tMAJguDDR58x7sREMwebfd8-HwBvsA6Mw:1nUQl8:aatrrWBEtTwwpTrKd0xbOaWMPfXs0QCBoYIIDNWxWj4','2022-03-30 10:20:02.006502'),('c48azz3a1j91ro0139gvg7qry4xj3wl9','.eJxVjkEOwiAQRe_C2hAotIBL9z1DM8MMUjU0Ke3KeHdL0oVu_3t5-W8xwb7laa-8TjOJq9Di8rshxCeXBugB5b7IuJRtnVE2RZ60ynEhft1O9y-QoeaWRYd90g6iMdyFPgTgqIxCINQDaeM9A9rUW0xeRSavnfW2o8Nw4NURbfeG8PkCvso6Nw:1nYVvK:Sjn_JPV6A1IPvq55qXDNtgvBkBFZ1ldVrej5khZGQBE','2022-04-10 16:39:26.988153'),('s2ld19tedjb1k24prsfbwg7klcidp5v4','.eJxVjkEOwiAQRe_C2hAoVMCle8_QzDCDVA0kpV0Z725JutDtfy8v_y0m2NY8bY2XaSZxEVqcfjeE-OTSAT2g3KuMtazLjLIr8qBN3irx63q4f4EMLfcsOhyTdhCN4SGMIQBHZRQCoT6TNt4zoE2jxeRVZPLaWW8H2g0HXu3Rfs-Gzxe-xDo1:1nUTzf:otDlPf8ZJfonyJriRm6sKmGYiYMgoYgS2uyBverZt0E','2022-03-30 13:47:15.752706'),('t0sd9rv7bce1ylwrcvocrf5l8m53xgyv','.eJxVjksOAiEQBe_C2hAYQMCle88w6aYbGTWQzGdlvLtDMgvdvqpU3luMsK1l3Baex4nERWhx-t0Q0pNrB_SAem8ytbrOE8quyIMu8taIX9fD_QsUWErPokeXtYdkDA_RxQiclFEIhPpM2oTAgDY7izmoxBS0t8EOtBsegtqj_Z6Lny--xzo2:1nXKdk:BbK4W0D0dFxFa-8nrMM-MO6e5ZKXICuoLHVKSZLt0wE','2022-04-07 10:24:24.083999');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_acces`
--

DROP TABLE IF EXISTS `home_acces`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_acces` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `region_id` bigint NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `region_id` (`region_id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `home_acces_region_id_f8ab467a_fk_home_region_region_id` FOREIGN KEY (`region_id`) REFERENCES `home_region` (`region_id`),
  CONSTRAINT `home_acces_user_id_fddbb6e9_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_acces`
--

LOCK TABLES `home_acces` WRITE;
/*!40000 ALTER TABLE `home_acces` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_acces` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_activité`
--

DROP TABLE IF EXISTS `home_activité`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_activité` (
  `activité_id` bigint NOT NULL AUTO_INCREMENT,
  `activité` varchar(100) NOT NULL,
  PRIMARY KEY (`activité_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_activité`
--

LOCK TABLES `home_activité` WRITE;
/*!40000 ALTER TABLE `home_activité` DISABLE KEYS */;
INSERT INTO `home_activité` VALUES (1,'Gaz'),(2,'Pétrole');
/*!40000 ALTER TABLE `home_activité` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_etat`
--

DROP TABLE IF EXISTS `home_etat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_etat` (
  `etat_id` bigint NOT NULL AUTO_INCREMENT,
  `etat` varchar(100) NOT NULL,
  PRIMARY KEY (`etat_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_etat`
--

LOCK TABLES `home_etat` WRITE;
/*!40000 ALTER TABLE `home_etat` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_etat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_famille`
--

DROP TABLE IF EXISTS `home_famille`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_famille` (
  `famille_id` bigint NOT NULL AUTO_INCREMENT,
  `famille` varchar(100) NOT NULL,
  PRIMARY KEY (`famille_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_famille`
--

LOCK TABLES `home_famille` WRITE;
/*!40000 ALTER TABLE `home_famille` DISABLE KEYS */;
INSERT INTO `home_famille` VALUES (1,'Etudes'),(2,'Activité Puits'),(3,'Installations spécifique'),(4,'Infrastructures sociales'),(5,'Installation générales'),(6,'Equipmenet');
/*!40000 ALTER TABLE `home_famille` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_fiscalite`
--

DROP TABLE IF EXISTS `home_fiscalite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_fiscalite` (
  `fiscalite_id` bigint NOT NULL AUTO_INCREMENT,
  `fiscalite` varchar(100) NOT NULL,
  PRIMARY KEY (`fiscalite_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_fiscalite`
--

LOCK TABLES `home_fiscalite` WRITE;
/*!40000 ALTER TABLE `home_fiscalite` DISABLE KEYS */;
INSERT INTO `home_fiscalite` VALUES (1,'RD'),(2,'RA');
/*!40000 ALTER TABLE `home_fiscalite` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_perimetre`
--

DROP TABLE IF EXISTS `home_perimetre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_perimetre` (
  `perimetre_id` bigint NOT NULL AUTO_INCREMENT,
  `Code_perimetre` varchar(30) NOT NULL,
  `perimetre` varchar(100) NOT NULL,
  `activite_id` bigint DEFAULT NULL,
  `region_id` bigint NOT NULL,
  PRIMARY KEY (`perimetre_id`),
  KEY `home_perimetre_region_id_aca15067_fk_home_region_region_id` (`region_id`),
  KEY `home_perimetre_activite_id_81711318_fk_home_activité_activité_id` (`activite_id`),
  CONSTRAINT `home_perimetre_activite_id_81711318_fk_home_activité_activité_id` FOREIGN KEY (`activite_id`) REFERENCES `home_activité` (`activité_id`),
  CONSTRAINT `home_perimetre_region_id_aca15067_fk_home_region_region_id` FOREIGN KEY (`region_id`) REFERENCES `home_region` (`region_id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_perimetre`
--

LOCK TABLES `home_perimetre` WRITE;
/*!40000 ALTER TABLE `home_perimetre` DISABLE KEYS */;
INSERT INTO `home_perimetre` VALUES (14,'BB','Hassi Rmel',1,2),(15,'BB','Hassi Rmel centre',2,2),(16,'CC','Haoud Berkoui',1,4),(17,'HH','Haoud Berkoui sud',2,4),(18,'BB','Hassi Messoud',2,1),(19,'HH','Stah',2,3),(20,'BB','Gassi touil',2,6),(21,'HH','ohanet',1,9);
/*!40000 ALTER TABLE `home_perimetre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_project`
--

DROP TABLE IF EXISTS `home_project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_project` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `PMT` int DEFAULT NULL,
  `Compte_Analytique` varchar(30) NOT NULL,
  `Libelles` varchar(500) NOT NULL,
  `Fiscalite_id` bigint NOT NULL,
  `Cout_Globale_initial_total` double NOT NULL,
  `Cout_Globale_initial_devise` double NOT NULL,
  `Realisation_S1_total` double NOT NULL,
  `Realisation_S1_devise` double NOT NULL,
  `Prevision_S2_total` double NOT NULL,
  `Prevision_S2_devise` double NOT NULL,
  `Previson_de_cloture_total` double NOT NULL,
  `Previson_de_cloture_devise` double NOT NULL,
  `Reste_a_realiser_total` double NOT NULL,
  `Reste_a_realiser_devise` double NOT NULL,
  `Prevision_n_total` double NOT NULL,
  `Prevision_n_devise` double NOT NULL,
  `Prevision_n1_total` double NOT NULL,
  `Prevision_n1_devise` double NOT NULL,
  `Prevision_n2_total` double NOT NULL,
  `Prevision_n2_devise` double NOT NULL,
  `Prevision_n3_total` double NOT NULL,
  `Prevision_n3_devise` double NOT NULL,
  `Prevision_n4_total` double NOT NULL,
  `Prevision_n4_devise` double NOT NULL,
  `Point_situation` varchar(1000) NOT NULL,
  `Famille_id` bigint NOT NULL,
  `Perimetre_id` bigint NOT NULL,
  `Structure_gerante_id` bigint NOT NULL,
  `Type_id` bigint NOT NULL,
  `Realisation_cum_devise` double NOT NULL,
  `Realisation_cum_total` double NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `home_project_PMT_Compte_Analytique_f13bf50e_uniq` (`PMT`,`Compte_Analytique`),
  KEY `home_project_Structure_gerante_id_2889fe8b_fk_home_stru` (`Structure_gerante_id`),
  KEY `home_project_Type_id_0c35e844_fk_home_type_type_id` (`Type_id`),
  KEY `home_project_Famille_id_2a07efea_fk_home_famille_famille_id` (`Famille_id`),
  KEY `home_project_Perimetre_id_44bc2034_fk_home_peri` (`Perimetre_id`),
  KEY `home_project_Fiscalite_id_14df1a55` (`Fiscalite_id`),
  CONSTRAINT `home_project_Famille_id_2a07efea_fk_home_famille_famille_id` FOREIGN KEY (`Famille_id`) REFERENCES `home_famille` (`famille_id`),
  CONSTRAINT `home_project_Fiscalite_id_14df1a55_fk_home_fisc` FOREIGN KEY (`Fiscalite_id`) REFERENCES `home_fiscalite` (`fiscalite_id`),
  CONSTRAINT `home_project_Perimetre_id_44bc2034_fk_home_peri` FOREIGN KEY (`Perimetre_id`) REFERENCES `home_perimetre` (`perimetre_id`),
  CONSTRAINT `home_project_Structure_gerante_id_2889fe8b_fk_home_stru` FOREIGN KEY (`Structure_gerante_id`) REFERENCES `home_structure` (`structure_id`),
  CONSTRAINT `home_project_Type_id_0c35e844_fk_home_type_type_id` FOREIGN KEY (`Type_id`) REFERENCES `home_type` (`type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=70 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_project`
--

LOCK TABLES `home_project` WRITE;
/*!40000 ALTER TABLE `home_project` DISABLE KEYS */;
INSERT INTO `home_project` VALUES (61,2022,'517105','Work Over HBK',1,5929561,1625438,881522,48843,130296,76021,1011818,124864,2869034,896247,1558572,602957,707782,217198,710538,225973,723548,225973,727166,227103,'05 operations programées',2,14,9,1,1370,490137),(62,2022,'517103','Work Over HBK2',2,5929561,1625438,881522,48843,130296,76021,1011818,124864,2869034,896247,1558572,602957,707782,217198,710538,225973,723548,225973,727166,227103,'Projet en cours de réalisation',5,17,5,7,1370,490137),(63,2022,'111111','Projet Boosting',1,5929561,1625438,881522,48843,130296,76021,1011818,124864,2869034,896247,1558572,602957,707782,217198,710538,225973,723548,225973,727166,227103,'Projet en cours de réalisation',1,18,4,7,1370,490137),(64,2022,'517102','Projet Boosting 2',2,5929561,861403,881522,48843,130296,76021,1011818,124864,2869034,132212,1558572,602957,707782,50000,710538,60000,723548,2212,727166,20000,'Projet en cours de réalisation',3,19,5,6,1370,490137),(65,2022,'00000','Work Over Ohanet',1,5929561,1416965,881522,48843,130296,76021,1011818,124864,2869034,689144,1558572,602957,707782,217198,710538,225973,723548,225973,727166,20000,'Projet en cours de réalisation',4,21,5,6,0,490137),(67,2022,'00001','Work Over Gassi Touil',1,5929561,1416965,881522,48843,130296,76021,1011818,124864,2869034,689144,1558572,602957,707782,217198,710538,225973,723548,225973,727166,20000,'Projet en cours de réalisation',1,20,5,6,0,490137),(69,2022,'00002','Work Over Gassi Touil',1,5929561,1416965,881522,48843,130296,76021,1011818,124864,2869034,689144,1558572,602957,707782,217198,710538,225973,723548,225973,727166,20000,'Projet en cours de réalisation',6,16,5,6,0,490137);
/*!40000 ALTER TABLE `home_project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_prévision_mensuelle`
--

DROP TABLE IF EXISTS `home_prévision_mensuelle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_prévision_mensuelle` (
  `prevision_mensuelle_id` bigint NOT NULL AUTO_INCREMENT,
  `Mois_prev` varchar(50) DEFAULT NULL,
  `Montant_Prevu_Total` varchar(30) NOT NULL,
  `Montant_Prevu_Devise` varchar(30) NOT NULL,
  `Project_id` bigint NOT NULL,
  `Prev_cum_devise` varchar(30) NOT NULL,
  `Prev_cum_total` varchar(30) NOT NULL,
  PRIMARY KEY (`prevision_mensuelle_id`),
  KEY `home_prévision_mensuelle_Project_id_c4fa75dd_fk_home_project_id` (`Project_id`),
  CONSTRAINT `home_prévision_mensuelle_Project_id_c4fa75dd_fk_home_project_id` FOREIGN KEY (`Project_id`) REFERENCES `home_project` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=166 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_prévision_mensuelle`
--

LOCK TABLES `home_prévision_mensuelle` WRITE;
/*!40000 ALTER TABLE `home_prévision_mensuelle` DISABLE KEYS */;
INSERT INTO `home_prévision_mensuelle` VALUES (118,'janvier','88813','500',61,'500','88813'),(119,'fevrier','94543','18408',61,'18908','183356'),(120,'mars','253843','109323',61,'128231','437199'),(121,'avril','171896','33469',61,'161700','609095'),(122,'mai','177626','34585',61,'196285','786721'),(123,'juin','278490','174022',61,'370307','1065211'),(124,'juillet','88813','17292',61,'387599','1154024'),(125,'aout','71289','92031',61,'479630','1225313'),(126,'septembre','178223','27745',61,'507375','1403536'),(127,'octobre','153570','89800',61,'597175','1557106'),(128,'novombre','178223','27745',61,'624920','1735329'),(129,'decembre','106936','16646',61,'641566','1842265'),(130,'janvier','88813','500',62,'500','88813'),(131,'fevrier','1000','500',62,'1000','89813'),(132,'mars','17292','500',62,'1500','107105'),(133,'avril','171896','33469',62,'34969','279001'),(134,'mai','1000','0',62,'34969','280001'),(135,'juin','278490','17292',62,'52261','558491'),(136,'juillet','1000','500',62,'52761','559491'),(137,'aout','71289','500',62,'53261','630780'),(138,'septembre','178223','17292',62,'70553','809003'),(139,'octobre','153570','89800',62,'160353','962573'),(140,'novombre','178223','500',62,'160853','1140796'),(141,'decembre','106936','0',62,'160853','1247732'),(142,'janvier','88813','500',63,'500','88813'),(143,'fevrier','1000','500',63,'1000','89813'),(144,'mars','253843','109323',63,'110323','343656'),(145,'avril','171896','33469',63,'143792','515552'),(146,'mai','1000','500',63,'144292','516552'),(147,'juin','278490','500',63,'144792','795042'),(148,'juillet','1000','500',63,'145292','796042'),(149,'aout','165029','92031',63,'237323','961071'),(150,'septembre','178223','27745',63,'265068','1139294'),(151,'octobre','153570','89800',63,'354868','1292864'),(152,'novombre','1000','27745',63,'382613','1293864'),(153,'decembre','106936','16646',63,'399259','1400800'),(154,'janvier','88813','17292',64,'17292','88813'),(155,'fevrier','94543','18408',64,'35700','183356'),(156,'mars','253843','500',64,'36200','437199'),(157,'avril','171896','33469',64,'69669','609095'),(158,'mai','177626','34585',64,'104254','786721'),(159,'juin','278490','174022',64,'278276','1065211'),(160,'juillet','100000','500',64,'278776','1165211'),(161,'aout','165029','92031',64,'370807','1330240'),(162,'septembre','85949','27745',64,'398552','1416189'),(163,'octobre','153570','89800',64,'488352','1569759'),(164,'novombre','178223','500',64,'488852','1747982'),(165,'decembre','106936','16646',64,'505498','1854918');
/*!40000 ALTER TABLE `home_prévision_mensuelle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_realisation_mensuelle`
--

DROP TABLE IF EXISTS `home_realisation_mensuelle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_realisation_mensuelle` (
  `Realisation_mensuelle_id` bigint NOT NULL AUTO_INCREMENT,
  `Mois_real` varchar(50) DEFAULT NULL,
  `Montant_real_Total` double NOT NULL,
  `Montant_real_Devise` double NOT NULL,
  `Point_situation` varchar(1000) NOT NULL,
  `taux_real_mois` double NOT NULL,
  `real_cum_total` double NOT NULL,
  `taux_real_ann` double NOT NULL,
  `Project_id` bigint NOT NULL,
  `prevision_mensuelle_id_id` bigint DEFAULT NULL,
  `PMT` int DEFAULT NULL,
  `real_cum_devise` double NOT NULL,
  `taux_real_cum` double NOT NULL,
  PRIMARY KEY (`Realisation_mensuelle_id`),
  KEY `home_realisation_men_Project_id_9139f166_fk_home_proj` (`Project_id`),
  KEY `home_realisation_men_prevision_mensuelle__659bd6fc_fk_home_prév` (`prevision_mensuelle_id_id`),
  CONSTRAINT `home_realisation_men_prevision_mensuelle__659bd6fc_fk_home_prév` FOREIGN KEY (`prevision_mensuelle_id_id`) REFERENCES `home_prévision_mensuelle` (`prevision_mensuelle_id`),
  CONSTRAINT `home_realisation_men_Project_id_9139f166_fk_home_proj` FOREIGN KEY (`Project_id`) REFERENCES `home_project` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_realisation_mensuelle`
--

LOCK TABLES `home_realisation_mensuelle` WRITE;
/*!40000 ALTER TABLE `home_realisation_mensuelle` DISABLE KEYS */;
INSERT INTO `home_realisation_mensuelle` VALUES (36,'janvier',50000,20000,'/',56.29806447254344,50000,3.208064818308041,63,142,2022,20000,56.29806447254344),(37,'janvier',48000,8000,'/',54.046141893641696,48000,3.0797422255757194,61,118,2022,8000,54.046141893641696),(38,'janvier',900000,9000,'/',1013.3651605057818,900000,57.745166729544735,62,130,2022,9000,1013.3651605057818);
/*!40000 ALTER TABLE `home_realisation_mensuelle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_recap`
--

DROP TABLE IF EXISTS `home_recap`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_recap` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `PMT` int DEFAULT NULL,
  `region` varchar(1000) NOT NULL,
  `famille` varchar(1000) NOT NULL,
  `activite` varchar(1000) NOT NULL,
  `CGI_total` double DEFAULT NULL,
  `CGI_devise` double DEFAULT NULL,
  `Realisation_cum_total` double NOT NULL,
  `Realisation_cum_devise` double NOT NULL,
  `Realisation_S1_devise` double NOT NULL,
  `Realisation_S1_total` double NOT NULL,
  `Prevision_S2_total` double NOT NULL,
  `Previson_de_cloture_total` double NOT NULL,
  `Prevision_S2_devise` double NOT NULL,
  `Previson_de_cloture_devise` double NOT NULL,
  `Reste_a_realiser_total` double NOT NULL,
  `Reste_a_realiser_devise` double NOT NULL,
  `Prevision_n_total` double NOT NULL,
  `Prevision_n_devise` double NOT NULL,
  `Prevision_n1_total` double NOT NULL,
  `Prevision_n1_devise` double NOT NULL,
  `Prevision_n2_total` double NOT NULL,
  `Prevision_n2_devise` double NOT NULL,
  `Prevision_n3_total` double NOT NULL,
  `Prevision_n3_devise` double NOT NULL,
  `Prevision_n4_total` double NOT NULL,
  `Prevision_n4_devise` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_recap`
--

LOCK TABLES `home_recap` WRITE;
/*!40000 ALTER TABLE `home_recap` DISABLE KEYS */;
INSERT INTO `home_recap` VALUES (9,2022,'Hassi Rmel','Activité Puits','Gaz',5929561,1625438,490137,1370,48843,881522,130296,1011818,76021,124864,2869034,896247,1558572,602957,707782,217198,710538,225973,723548,225973,727166,227103),(10,2022,'Houd Berkaoui','Installation générales','Pétrole',5929561,1625438,490137,1370,48843,881522,130296,1011818,76021,124864,2869034,896247,1558572,602957,707782,217198,710538,225973,723548,225973,727166,227103),(11,2022,'Hassi Messoud','Activité Puits','Pétrole',5929561,1625438,490137,1370,48843,881522,130296,1011818,76021,124864,2869034,896247,1558572,602957,707782,217198,710538,225973,723548,225973,727166,227103),(12,2022,'Stah','Installation générales','Pétrole',5929561,861403,490137,1370,48843,881522,130296,1011818,76021,124864,2869034,132212,1558572,602957,707782,50000,710538,60000,723548,2212,727166,20000),(13,2022,'Ohanet','Infrastructures sociales','Gaz',5929561,1416965,490137,0,48843,881522,130296,1011818,76021,124864,2869034,689144,1558572,602957,707782,217198,710538,225973,723548,225973,727166,20000),(14,2022,'Gassi Touil','Etudes','Pétrole',5929561,1416965,490137,0,48843,881522,130296,1011818,76021,124864,2869034,689144,1558572,602957,707782,217198,710538,225973,723548,225973,727166,20000),(15,2022,'Houd Berkaoui','Equipmenet','Gaz',5929561,1416965,490137,0,48843,881522,130296,1011818,76021,124864,2869034,689144,1558572,602957,707782,217198,710538,225973,723548,225973,727166,20000);
/*!40000 ALTER TABLE `home_recap` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_recap_activite`
--

DROP TABLE IF EXISTS `home_recap_activite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_recap_activite` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `PMT` int DEFAULT NULL,
  `activite` varchar(1000) NOT NULL,
  `CGI_total` double DEFAULT NULL,
  `CGI_devise` double DEFAULT NULL,
  `Realisation_cum_total` double NOT NULL,
  `Realisation_cum_devise` double NOT NULL,
  `Realisation_S1_devise` double NOT NULL,
  `Realisation_S1_total` double NOT NULL,
  `Prevision_S2_total` double NOT NULL,
  `Previson_de_cloture_total` double NOT NULL,
  `Prevision_S2_devise` double NOT NULL,
  `Previson_de_cloture_devise` double NOT NULL,
  `Reste_a_realiser_total` double NOT NULL,
  `Reste_a_realiser_devise` double NOT NULL,
  `Prevision_n_total` double NOT NULL,
  `Prevision_n_devise` double NOT NULL,
  `Prevision_n1_total` double NOT NULL,
  `Prevision_n1_devise` double NOT NULL,
  `Prevision_n2_total` double NOT NULL,
  `Prevision_n2_devise` double NOT NULL,
  `Prevision_n3_total` double NOT NULL,
  `Prevision_n3_devise` double NOT NULL,
  `Prevision_n4_total` double NOT NULL,
  `Prevision_n4_devise` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_recap_activite`
--

LOCK TABLES `home_recap_activite` WRITE;
/*!40000 ALTER TABLE `home_recap_activite` DISABLE KEYS */;
INSERT INTO `home_recap_activite` VALUES (7,2022,'Gaz',17788683,4459368,1470411,1370,146529,2644566,390888,3035454,228063,374592,8607102,2274535,4675716,1808871,2123346,651594,2131614,677919,2170644,677919,2181498,267103),(8,2022,'Pétrole',23718244,5529244,1960548,4110,195372,3526088,521184,4047272,304084,499456,11476136,2613850,6234288,2411828,2831128,701594,2842152,737919,2894192,680131,2908664,494206);
/*!40000 ALTER TABLE `home_recap_activite` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_recap_famille`
--

DROP TABLE IF EXISTS `home_recap_famille`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_recap_famille` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `PMT` int DEFAULT NULL,
  `famille` varchar(1000) NOT NULL,
  `CGI_total` double DEFAULT NULL,
  `CGI_devise` double DEFAULT NULL,
  `Prevision_S2_devise` double NOT NULL,
  `Prevision_S2_total` double NOT NULL,
  `Prevision_n1_devise` double NOT NULL,
  `Prevision_n1_total` double NOT NULL,
  `Prevision_n2_devise` double NOT NULL,
  `Prevision_n2_total` double NOT NULL,
  `Prevision_n3_devise` double NOT NULL,
  `Prevision_n3_total` double NOT NULL,
  `Prevision_n4_devise` double NOT NULL,
  `Prevision_n4_total` double NOT NULL,
  `Prevision_n_devise` double NOT NULL,
  `Prevision_n_total` double NOT NULL,
  `Previson_de_cloture_devise` double NOT NULL,
  `Previson_de_cloture_total` double NOT NULL,
  `Realisation_S1_devise` double NOT NULL,
  `Realisation_S1_total` double NOT NULL,
  `Realisation_cum_devise` double NOT NULL,
  `Realisation_cum_total` double NOT NULL,
  `Reste_a_realiser_devise` double NOT NULL,
  `Reste_a_realiser_total` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_recap_famille`
--

LOCK TABLES `home_recap_famille` WRITE;
/*!40000 ALTER TABLE `home_recap_famille` DISABLE KEYS */;
INSERT INTO `home_recap_famille` VALUES (21,2022,'Activité Puits',11859122,3250876,152042,260592,434396,1415564,451946,1421076,451946,1447096,454206,1454332,1205914,3117144,249728,2023636,97686,1763044,2740,980274,1792494,5738068),(22,2022,'Installation générales',11859122,2486841,152042,260592,267198,1415564,285973,1421076,228185,1447096,247103,1454332,1205914,3117144,249728,2023636,97686,1763044,2740,980274,1028459,5738068),(23,2022,'Infrastructures sociales',5929561,1416965,76021,130296,217198,707782,225973,710538,225973,723548,20000,727166,602957,1558572,124864,1011818,48843,881522,0,490137,689144,2869034),(24,2022,'Etudes',5929561,1416965,76021,130296,217198,707782,225973,710538,225973,723548,20000,727166,602957,1558572,124864,1011818,48843,881522,0,490137,689144,2869034),(25,2022,'Equipmenet',5929561,1416965,76021,130296,217198,707782,225973,710538,225973,723548,20000,727166,602957,1558572,124864,1011818,48843,881522,0,490137,689144,2869034);
/*!40000 ALTER TABLE `home_recap_famille` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_recap_region`
--

DROP TABLE IF EXISTS `home_recap_region`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_recap_region` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `PMT` int DEFAULT NULL,
  `region` varchar(1000) NOT NULL,
  `CGI_total` double DEFAULT NULL,
  `CGI_devise` double DEFAULT NULL,
  `Prevision_S2_devise` double NOT NULL,
  `Prevision_S2_total` double NOT NULL,
  `Prevision_n1_devise` double NOT NULL,
  `Prevision_n1_total` double NOT NULL,
  `Prevision_n2_devise` double NOT NULL,
  `Prevision_n2_total` double NOT NULL,
  `Prevision_n3_devise` double NOT NULL,
  `Prevision_n3_total` double NOT NULL,
  `Prevision_n4_devise` double NOT NULL,
  `Prevision_n4_total` double NOT NULL,
  `Prevision_n_devise` double NOT NULL,
  `Prevision_n_total` double NOT NULL,
  `Previson_de_cloture_devise` double NOT NULL,
  `Previson_de_cloture_total` double NOT NULL,
  `Realisation_S1_devise` double NOT NULL,
  `Realisation_S1_total` double NOT NULL,
  `Realisation_cum_devise` double NOT NULL,
  `Realisation_cum_total` double NOT NULL,
  `Reste_a_realiser_devise` double NOT NULL,
  `Reste_a_realiser_total` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_recap_region`
--

LOCK TABLES `home_recap_region` WRITE;
/*!40000 ALTER TABLE `home_recap_region` DISABLE KEYS */;
INSERT INTO `home_recap_region` VALUES (21,2022,'Hassi Rmel',5929561,1625438,76021,130296,217198,707782,225973,710538,225973,723548,227103,727166,602957,1558572,124864,1011818,48843,881522,1370,490137,896247,2869034),(22,2022,'Houd Berkaoui',11859122,3042403,152042,260592,434396,1415564,451946,1421076,451946,1447096,247103,1454332,1205914,3117144,249728,2023636,97686,1763044,1370,980274,1585391,5738068),(23,2022,'Hassi Messoud',5929561,1625438,76021,130296,217198,707782,225973,710538,225973,723548,227103,727166,602957,1558572,124864,1011818,48843,881522,1370,490137,896247,2869034),(24,2022,'Stah',5929561,861403,76021,130296,50000,707782,60000,710538,2212,723548,20000,727166,602957,1558572,124864,1011818,48843,881522,1370,490137,132212,2869034),(25,2022,'Ohanet',5929561,1416965,76021,130296,217198,707782,225973,710538,225973,723548,20000,727166,602957,1558572,124864,1011818,48843,881522,0,490137,689144,2869034),(26,2022,'Gassi Touil',5929561,1416965,76021,130296,217198,707782,225973,710538,225973,723548,20000,727166,602957,1558572,124864,1011818,48843,881522,0,490137,689144,2869034);
/*!40000 ALTER TABLE `home_recap_region` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_region`
--

DROP TABLE IF EXISTS `home_region`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_region` (
  `region_id` bigint NOT NULL AUTO_INCREMENT,
  `region` varchar(100) NOT NULL,
  PRIMARY KEY (`region_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_region`
--

LOCK TABLES `home_region` WRITE;
/*!40000 ALTER TABLE `home_region` DISABLE KEYS */;
INSERT INTO `home_region` VALUES (1,'Hassi Messoud'),(2,'Hassi Rmel'),(3,'Stah'),(4,'Houd Berkaoui'),(5,'Rhourde El Baghuel'),(6,'Gassi Touil'),(7,'Rhourde nouss'),(8,'Tin Fouyé Tabankort'),(9,'Ohanet'),(10,'In Aménas'),(11,'Hors Region'),(12,'Structure de siége DPR');
/*!40000 ALTER TABLE `home_region` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_structure`
--

DROP TABLE IF EXISTS `home_structure`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_structure` (
  `structure_id` bigint NOT NULL AUTO_INCREMENT,
  `structure` varchar(50) NOT NULL,
  PRIMARY KEY (`structure_id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_structure`
--

LOCK TABLES `home_structure` WRITE;
/*!40000 ALTER TABLE `home_structure` DISABLE KEYS */;
INSERT INTO `home_structure` VALUES (3,'A'),(4,'B'),(5,'C'),(6,'D'),(7,'E'),(8,'F'),(9,'G'),(10,'H'),(11,'I'),(12,'J'),(13,'K'),(14,'L'),(15,'M'),(16,'N'),(17,'O'),(18,'P'),(19,'Q'),(20,'R'),(21,'S'),(22,'T'),(23,'U');
/*!40000 ALTER TABLE `home_structure` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_type`
--

DROP TABLE IF EXISTS `home_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_type` (
  `type_id` bigint NOT NULL AUTO_INCREMENT,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_type`
--

LOCK TABLES `home_type` WRITE;
/*!40000 ALTER TABLE `home_type` DISABLE KEYS */;
INSERT INTO `home_type` VALUES (1,'IT'),(6,'/'),(7,'HSE');
/*!40000 ALTER TABLE `home_type` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-28 13:35:05
