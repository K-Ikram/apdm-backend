-- phpMyAdmin SQL Dump
-- version 4.5.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Jun 04, 2017 at 05:31 PM
-- Server version: 5.7.11
-- PHP Version: 5.6.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `apdmdb`
--

--
-- Dumping data for table `alert`
--

INSERT INTO `alert` (`alert_id`, `alert_date`, `crop_production_id`, `disease_id`, `risk_rate`, `feedback_date`, `feedback_type`, `client_id`) VALUES
(38, '2017-05-05 12:34:04', 22, 1, 0.57, NULL, NULL, NULL),
(39, '2017-05-05 12:34:04', 21, 1, 0.6, '2017-06-04 14:51:52', 'denied', 23),
(40, '2017-05-05 12:34:04', 20, 1, 0.87, '2017-05-08 22:19:31', 'denied', 23),
(41, '2017-05-05 12:34:04', 17, 1, 0.98, '2017-05-06 15:05:41', 'denied', 23),
(42, '2017-06-04 13:42:58', 16, 1, 0.51, '2017-06-04 13:44:15', 'confirmed', 23),
(43, '2017-05-11 16:31:25', 21, 1, 0.58, '2017-05-11 19:28:41', 'confirmed', 23),
(44, '2017-05-11 16:33:25', 18, 1, 0.6, '2017-06-04 13:44:18', 'confirmed', 23),
(45, '2017-05-05 12:34:04', 22, 1, 0.57, '2017-05-06 15:04:59', 'confirmed', 23),
(46, '2017-05-31 15:55:45', 18, 1, 0.87, '2017-05-31 15:59:47', 'confirmed', 23),
(47, '2017-06-02 14:30:40', 18, 2, 0.87, '2017-06-02 17:06:02', 'confirmed', 23),
(48, '2017-06-02 14:31:04', 18, 2, 0.9, '2017-06-02 18:38:46', 'confirmed', 23),
(49, '2017-06-02 18:45:18', 17, 2, 0.87, '2017-06-02 18:46:30', 'denied', 23),
(50, '2017-06-02 18:45:54', 17, 2, 0.87, '2017-06-02 20:05:59', 'denied', 23),
(51, '2017-06-02 18:45:54', 18, 2, 0.87, '2017-06-02 20:10:19', 'confirmed', 23),
(92, '2017-06-02 23:26:56', 16, 1, 1, '2017-06-04 14:52:53', 'confirmed', 23),
(53, '2017-06-02 18:45:54', 16, 1, 0.87, '2017-06-02 19:19:07', 'confirmed', 23),
(54, '2017-06-02 18:45:54', 17, 1, 0.87, '2017-06-02 20:06:40', 'denied', 23),
(55, '2017-06-02 18:45:54', 17, 2, 0.87, '2017-06-02 20:07:24', 'confirmed', 23),
(56, '2017-06-02 18:45:54', 18, 2, 0.87, '2017-06-02 20:06:51', 'confirmed', 23),
(93, '2017-06-02 23:26:56', 16, 1, 1, '2017-06-03 22:56:38', 'confirmed', 23),
(58, '2017-06-02 18:45:54', 16, 1, 0.87, '2017-06-02 18:46:12', 'confirmed', 23),
(59, '2017-06-02 18:45:54', 17, 1, 0.87, '2017-06-02 20:09:04', 'confirmed', 23),
(60, '2017-06-07 10:12:00', 19, 2, 0.9, '2017-06-04 14:52:17', 'confirmed', 23),
(61, '2017-06-07 10:12:00', 19, 2, 0.9, '2017-06-04 14:53:40', 'confirmed', 23),
(62, '2017-06-07 10:12:00', 19, 2, 0.9, '2017-06-02 21:30:35', 'confirmed', 23),
(63, '2017-06-07 10:12:00', 19, 2, 0.9, '2017-06-02 21:47:58', 'confirmed', 23),
(88, '2017-06-02 23:26:56', 16, 1, 1, '2017-06-03 22:56:45', 'denied', 23),
(66, '2017-06-02 22:08:45', 18, 2, 1, '2017-06-02 22:51:52', 'confirmed', 23),
(67, '2017-06-02 22:29:16', 18, 2, 1, '2017-06-02 22:52:41', 'confirmed', 23),
(68, '2017-06-04 00:00:00', 17, 2, 0.6, '2017-06-02 22:54:13', 'confirmed', 23),
(69, '2017-06-04 00:00:00', 17, 2, 0.6, '2017-06-02 23:23:38', 'confirmed', 23),
(70, '2017-06-04 00:00:00', 17, 2, 0.6, '2017-06-02 22:57:31', 'confirmed', 23),
(71, '2017-06-04 00:00:00', 17, 2, 0.6, '2017-06-02 22:57:39', 'denied', 23),
(72, '2017-06-04 00:00:00', 17, 2, 0.6, '2017-06-02 22:57:44', 'denied', 23),
(73, '2017-06-04 00:00:00', 17, 2, 0.6, '2017-06-02 23:06:59', 'confirmed', 23),
(74, '2017-06-04 00:00:00', 17, 2, 0.6, '2017-06-02 23:08:05', 'denied', 23),
(75, '2017-06-02 23:26:43', 16, 1, 1, '2017-06-03 21:30:30', 'confirmed', 23),
(76, '2017-06-02 23:26:56', 16, 1, 1, '2017-06-04 16:29:42', 'confirmed', 23),
(77, '2017-06-02 23:26:56', 16, 1, 1, '2017-06-04 16:36:57', 'confirmed', 23),
(78, '2017-06-02 23:26:56', 16, 1, 1, '2017-06-04 16:37:06', 'denied', 23),
(79, '2017-06-02 23:26:56', 16, 1, 1, '2017-06-04 16:41:51', 'confirmed', 23),
(80, '2017-06-02 23:26:56', 16, 1, 1, '2017-06-02 23:42:32', 'denied', 23),
(81, '2017-05-03 01:55:31', 18, 2, 0.51, '2017-06-03 02:38:49', 'confirmed', 23),
(82, '2017-06-03 03:31:50', 16, 2, 0.8, '2017-06-04 00:43:27', 'denied', 23),
(83, '2017-06-03 03:32:58', 16, 2, 0.8, '2017-06-03 03:51:11', 'denied', 23),
(91, '2017-06-02 23:26:56', 16, 1, 1, '2017-06-03 22:56:48', 'confirmed', 23),
(90, '2017-06-02 23:26:56', 16, 1, 1, '2017-06-03 23:11:51', 'denied', 23),
(89, '2017-06-02 23:26:56', 16, 1, 1, '2017-06-04 16:33:02', 'confirmed', 23),
(87, '2017-06-03 03:32:58', 16, 2, 0.8, '2017-06-03 21:33:57', 'confirmed', 23),
(94, '2017-06-02 23:26:56', 16, 1, 1, '2017-06-03 23:13:00', 'confirmed', 23),
(95, '2017-06-02 23:26:56', 16, 1, 1, '2017-06-03 23:16:48', 'confirmed', 23),
(96, '2017-06-02 23:26:56', 16, 1, 1, '2017-06-03 23:15:51', 'denied', 23),
(97, '2017-06-02 23:26:56', 16, 1, 1, '2017-06-03 22:57:31', 'denied', 23),
(98, '2017-06-02 23:26:56', 16, 1, 1, '2017-06-03 23:02:40', 'denied', 23),
(99, '2017-06-02 23:26:56', 16, 2, 1, '2017-06-03 23:15:02', 'confirmed', 23),
(100, '2017-06-02 18:45:54', 16, 1, 0.87, '2017-06-04 13:44:21', 'denied', 23),
(101, '2017-06-04 14:57:06', 16, 2, 1, '2017-06-04 15:00:06', 'confirmed', 23),
(102, '2017-06-04 15:06:19', 16, 2, 1, '2017-06-04 15:06:46', 'confirmed', 23),
(103, '2017-06-04 15:09:18', 16, 2, 1, '2017-06-04 15:09:31', 'confirmed', 23),
(104, '2017-06-04 15:09:18', 16, 2, 1, '2017-06-04 15:09:47', 'confirmed', 23),
(105, '2017-06-04 15:09:18', 16, 2, 1, '2017-06-04 15:11:42', 'confirmed', 23),
(106, '2017-06-04 15:10:54', 16, 2, 1, '2017-06-04 15:23:31', 'confirmed', 23),
(107, '2017-06-04 15:24:15', 16, 2, 1, '2017-06-04 15:25:57', 'confirmed', 23),
(108, '2017-06-04 15:36:32', 16, 2, 1, '2017-06-04 15:36:45', 'confirmed', 23),
(109, '2017-06-04 15:39:35', 16, 2, 1, '2017-06-04 15:39:59', 'confirmed', 23),
(110, '2017-06-04 15:39:35', 16, 2, 1, '2017-06-04 15:42:30', 'confirmed', 23),
(111, '2017-06-04 15:39:35', 16, 2, 1, '2017-06-04 15:44:49', 'confirmed', 23),
(112, '2017-06-04 15:39:35', 16, 2, 1, '2017-06-04 15:46:38', 'confirmed', 23),
(113, '2017-06-04 15:39:35', 16, 2, 1, '2017-06-04 15:48:06', 'confirmed', 23),
(114, '2017-06-04 15:39:35', 16, 2, 1, '2017-06-04 15:48:29', 'confirmed', 23),
(115, '2017-06-04 15:39:35', 16, 2, 1, '2017-06-04 15:49:57', 'confirmed', 23),
(116, '2017-06-04 15:39:35', 16, 2, 1, '2017-06-04 16:59:21', 'confirmed', 23),
(117, '2017-06-04 15:39:35', 16, 2, 1, '2017-06-04 17:12:58', 'confirmed', 23),
(118, '2017-06-04 15:39:35', 16, 2, 1, '2017-06-04 17:01:14', 'confirmed', 23),
(119, '2017-06-04 15:39:35', 16, 2, 1, '2017-06-04 17:17:31', 'confirmed', 23),
(120, '2017-06-04 15:39:35', 16, 2, 1, '2017-06-04 17:18:19', 'confirmed', 23),
(121, '2017-06-04 15:39:35', 16, 2, 1, '2017-06-04 17:26:38', 'confirmed', 23);

--
-- Dumping data for table `anomaly`
--

INSERT INTO `anomaly` (`anomaly_id`, `occurence_date`, `reporting_date`, `client_id`, `crop_production_id`, `disease_id`) VALUES
(76, '2017-05-04 20:24:00', '2017-05-04 21:25:21', 23, 22, 1),
(77, '2017-05-06 14:07:00', '2017-05-06 15:07:55', 23, 15, 1),
(78, '2017-05-06 14:13:00', '2017-05-06 15:13:44', 23, 17, 1),
(79, '2017-05-06 14:13:00', '2017-05-06 15:14:12', 23, 17, 1),
(80, '2017-05-06 14:13:00', '2017-05-06 15:15:00', 23, 17, 1),
(81, '2017-05-06 14:13:00', '2017-05-06 15:15:54', 23, 19, 1),
(82, '2017-05-10 00:28:00', '2017-05-31 01:29:27', 23, 17, 1),
(83, '2017-05-31 00:32:00', '2017-05-31 01:32:55', 23, 17, 1),
(84, '2017-05-31 00:32:00', '2017-05-31 01:33:00', 23, 17, 1),
(85, '2017-05-31 00:48:00', '2017-05-31 01:49:27', 23, 17, 1),
(86, '2017-05-31 00:48:00', '2017-05-31 01:49:30', 23, 17, 1),
(87, '2017-05-31 00:48:00', '2017-05-31 01:49:36', 23, 17, 1),
(88, '2017-05-31 15:02:00', '2017-05-31 16:02:21', 23, 17, 1),
(89, '2017-05-31 21:40:00', '2017-05-31 22:41:13', 23, 17, 1),
(90, '2017-06-01 16:06:00', '2017-06-01 17:06:31', 23, 23, 2),
(91, '2017-06-01 16:43:00', '2017-06-01 17:43:54', 23, 17, 1),
(92, '2017-06-01 16:48:00', '2017-06-01 17:48:21', 23, 19, 1),
(93, '2017-06-01 17:27:00', '2017-06-01 18:28:37', 23, 16, 1),
(94, '2017-06-01 17:30:00', '2017-06-01 18:30:24', 23, 19, 1),
(95, '2017-06-01 20:29:00', '2017-06-01 21:29:30', 23, 17, 1),
(96, '2017-06-01 22:01:00', '2017-06-01 23:05:26', 23, 19, 1),
(97, '2017-06-01 22:27:00', '2017-06-01 23:28:38', 23, 15, 1),
(98, '2017-06-01 22:35:00', '2017-06-01 23:36:41', 23, 16, 1),
(99, '2017-06-02 15:23:00', '2017-06-02 16:26:03', 23, 17, 1),
(100, '2017-06-02 19:08:00', '2017-06-02 20:09:40', 23, 16, 1),
(101, '2017-04-04 02:51:00', '2017-06-03 03:51:54', 23, 16, 1),
(102, '2017-06-03 16:39:00', '2017-06-03 18:04:02', 23, 16, 1),
(103, '2017-06-03 17:43:00', '2017-06-03 18:43:39', 23, 17, 1),
(104, '2017-06-03 20:24:00', '2017-06-03 21:25:24', 23, 18, 1);

--
-- Dumping data for table `apdm_client`
--

INSERT INTO `apdm_client` (`client_id`, `username`, `first_name`, `last_name`, `email`, `gender`, `phone_contact`, `phone_sms`, `language`, `comments`, `is_active`, `is_staff`, `is_superuser`, `date_joined`, `last_login`, `notification_sms`, `notification_email`, `password`) VALUES
(23, 'admin', 'sorrita', 'Bouhenni', 'cs_bouhenni@esi.dz', 'femme', '+213797820473', '+213797820473', 'arabic', NULL, 1, 1, 1, '2017-05-03 19:11:36', '2017-06-04 13:38:33', 0, 1, 'pbkdf2_sha256$30000$vsDmn1YlFd4I$61lAnxrotySpFPXmEf400OPD5WRuezHNRln9labklfg='),
(24, 'sarra', '', '', 'sarra93bouhenni@gmail.com', NULL, '', '', NULL, NULL, 1, 1, 1, '2017-05-06 13:13:44', NULL, 1, 1, 'pbkdf2_sha256$30000$Ygf3fTLPxIGg$tvG/MYy18nReaMHWou0Sv0burI0Az/zxepsAphoO9P0='),
(34, 'farmer', '', '', 'sarra93bouhenni@gmail.com', NULL, '', '', NULL, NULL, 1, 0, 0, '2017-05-06 19:02:39', NULL, 1, 1, 'pbkdf2_sha256$30000$RXpo0hInzRrT$bgoK7EhiEoGnK9rdvikncsun1UDu1cmesVc+4tPiKfc='),
(35, 'client', '', '', 'sarra93bouhenni@gmail.com', NULL, '', '', NULL, NULL, 1, 0, 0, '2017-05-06 19:03:33', NULL, 1, 1, 'pbkdf2_sha256$30000$JdF7YzKBLNKi$2dKAsA48g97EHaX4DgIRnKAQ5SQK340M2zSZKXmomlQ='),
(36, 'utilisateur', '', '', 'utilisateur@aitech.dz', NULL, '', '', NULL, NULL, 1, 1, 1, '2017-05-30 14:18:48', '2017-05-31 20:36:26', 1, 1, 'pbkdf2_sha256$30000$9131fkDfFNv5$ByZIoJDub5u27Vvyxgs9yNRipGRGdArQQOcnn6Y8BEY='),
(37, 'sarrabouhenni', '', '', 'cs_bouhenni@esi.dz', NULL, '', '', NULL, NULL, 1, 1, 1, '2017-06-03 14:55:13', NULL, 1, 1, 'pbkdf2_sha256$30000$Gd3ReqjZXx5b$N1XOmPNi3uFtivW/bHPlGUyGiU6B4UAqtkstSRSzXco='),
(38, 'sarra_bouhenni', '', '', 'cs_bouhenni@esi.dz', NULL, '', '', NULL, NULL, 1, 1, 1, '2017-06-03 14:55:42', NULL, 1, 1, 'pbkdf2_sha256$30000$hnfxuwv8lJEv$kip0g2V6QaRT8ZCrG0MOlvTl/lWzS0VYGA8AhCcPPh8='),
(39, 'sar', '', '', 'cs_bouhenni@esi.dz', NULL, '', '', NULL, NULL, 1, 0, 0, '2017-06-03 15:14:30', NULL, 1, 1, 'pbkdf2_sha256$30000$cwAtMoTpnoO7$AQnQCpk5zN3S/KtNnaOGOSJKCBPcwkuys3muY3nbKsU='),
(40, 'ikram', '', '', 'cs_bouhenni@esi.dz', NULL, '', '', NULL, NULL, 1, 0, 0, '2017-06-03 15:14:59', NULL, 1, 1, 'pbkdf2_sha256$30000$uYfJdv9WR8e0$ucXE1tV3EmcqhC4eEPVkkmhrM5qNpwJgTt9jLPOETMg=');

--
-- Dumping data for table `apdm_cropproductiondisease`
--

INSERT INTO `apdm_cropproductiondisease` (`id`, `crop_production_id`, `disease_id`) VALUES
(20, 22, 1),
(21, 15, 1),
(22, 16, 1),
(23, 17, 1),
(24, 18, 1),
(25, 19, 1),
(26, 20, 1),
(27, 21, 1),
(29, 23, 2),
(30, 24, 2),
(31, 25, 1);

--
-- Dumping data for table `apdm_cropproductionsensor`
--

INSERT INTO `apdm_cropproductionsensor` (`id`, `crop_production_id`, `sensor_id`) VALUES
(19, 22, 1),
(20, 22, 5),
(21, 22, 10),
(22, 23, 1),
(23, 23, 5),
(24, 23, 10),
(25, 24, 1),
(26, 24, 5),
(27, 24, 10);

--
-- Dumping data for table `apdm_ownfarm`
--

INSERT INTO `apdm_ownfarm` (`id`, `client_id`, `farm_id`) VALUES
(26, 23, 37),
(27, 23, 31),
(28, 23, 1),
(29, 24, 2),
(30, 24, 1),
(31, 24, 37),
(32, 34, 37);

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(130, 'Can add log entry', 47, 'add_logentry'),
(131, 'Can change log entry', 47, 'change_logentry'),
(132, 'Can delete log entry', 47, 'delete_logentry'),
(133, 'Can add group', 48, 'add_group'),
(134, 'Can change group', 48, 'change_group'),
(135, 'Can delete group', 48, 'delete_group'),
(136, 'Can add permission', 49, 'add_permission'),
(137, 'Can change permission', 49, 'change_permission'),
(138, 'Can delete permission', 49, 'delete_permission'),
(139, 'Can add content type', 50, 'add_contenttype'),
(140, 'Can change content type', 50, 'change_contenttype'),
(141, 'Can delete content type', 50, 'delete_contenttype'),
(142, 'Can add session', 51, 'add_session'),
(143, 'Can change session', 51, 'change_session'),
(144, 'Can delete session', 51, 'delete_session'),
(145, 'Can add Alerte', 52, 'add_alert'),
(146, 'Can change Alerte', 52, 'change_alert'),
(147, 'Can delete Alerte', 52, 'delete_alert'),
(148, 'Can add Parcelle', 53, 'add_plot'),
(149, 'Can change Parcelle', 53, 'change_plot'),
(150, 'Can delete Parcelle', 53, 'delete_plot'),
(151, 'Can add Propriétaire', 54, 'add_ownfarm'),
(152, 'Can change Propriétaire', 54, 'change_ownfarm'),
(153, 'Can delete Propriétaire', 54, 'delete_ownfarm'),
(154, 'Can add alert client', 55, 'add_alertclient'),
(155, 'Can change alert client', 55, 'change_alertclient'),
(156, 'Can delete alert client', 55, 'delete_alertclient'),
(157, 'Can add Type de culture', 56, 'add_crop'),
(158, 'Can change Type de culture', 56, 'change_crop'),
(159, 'Can delete Type de culture', 56, 'delete_crop'),
(160, 'Can add Ferme', 57, 'add_farm'),
(161, 'Can change Ferme', 57, 'change_farm'),
(162, 'Can delete Ferme', 57, 'delete_farm'),
(163, 'Can add Capteur', 58, 'add_sensor'),
(164, 'Can change Capteur', 58, 'change_sensor'),
(165, 'Can delete Capteur', 58, 'delete_sensor'),
(166, 'Can add Culture', 59, 'add_cropproduction'),
(167, 'Can change Culture', 59, 'change_cropproduction'),
(168, 'Can delete Culture', 59, 'delete_cropproduction'),
(169, 'Can add Parcelle', 60, 'add_sensorplot'),
(170, 'Can change Parcelle', 60, 'change_sensorplot'),
(171, 'Can delete Parcelle', 60, 'delete_sensorplot'),
(172, 'Can add Ville', 61, 'add_city'),
(173, 'Can change Ville', 61, 'change_city'),
(174, 'Can delete Ville', 61, 'delete_city'),
(175, 'Can add django migrations', 62, 'add_djangomigrations'),
(176, 'Can change django migrations', 62, 'change_djangomigrations'),
(177, 'Can delete django migrations', 62, 'delete_djangomigrations'),
(178, 'Can add Maladie', 46, 'add_disease'),
(179, 'Can change Maladie', 46, 'change_disease'),
(180, 'Can delete Maladie', 46, 'delete_disease'),
(181, 'Can add Anomalie', 63, 'add_anomaly'),
(182, 'Can change Anomalie', 63, 'change_anomaly'),
(183, 'Can delete Anomalie', 63, 'delete_anomaly'),
(184, 'Can add Maladie', 64, 'add_cropproductiondisease'),
(185, 'Can change Maladie', 64, 'change_cropproductiondisease'),
(186, 'Can delete Maladie', 64, 'delete_cropproductiondisease'),
(187, 'Can add Culture', 65, 'add_cropproductionsensor'),
(188, 'Can change Culture', 65, 'change_cropproductionsensor'),
(189, 'Can delete Culture', 65, 'delete_cropproductionsensor'),
(190, 'Can add Utilisateur', 66, 'add_client'),
(191, 'Can change Utilisateur', 66, 'change_client'),
(192, 'Can delete Utilisateur', 66, 'delete_client'),
(193, 'Can add crop client', 67, 'add_cropclient'),
(194, 'Can change crop client', 67, 'change_cropclient'),
(195, 'Can delete crop client', 67, 'delete_cropclient'),
(196, 'Can add grant', 68, 'add_grant'),
(197, 'Can change grant', 68, 'change_grant'),
(198, 'Can delete grant', 68, 'delete_grant'),
(199, 'Can add access token', 69, 'add_accesstoken'),
(200, 'Can change access token', 69, 'change_accesstoken'),
(201, 'Can delete access token', 69, 'delete_accesstoken'),
(202, 'Can add application', 45, 'add_application'),
(203, 'Can change application', 45, 'change_application'),
(204, 'Can delete application', 45, 'delete_application'),
(205, 'Can add refresh token', 70, 'add_refreshtoken'),
(206, 'Can change refresh token', 70, 'change_refreshtoken'),
(207, 'Can delete refresh token', 70, 'delete_refreshtoken'),
(208, 'Can add cors model', 71, 'add_corsmodel'),
(209, 'Can change cors model', 71, 'change_corsmodel'),
(210, 'Can delete cors model', 71, 'delete_corsmodel'),
(211, 'Can add periodic task', 72, 'add_periodictask'),
(212, 'Can change periodic task', 72, 'change_periodictask'),
(213, 'Can delete periodic task', 72, 'delete_periodictask'),
(214, 'Can add crontab', 73, 'add_crontabschedule'),
(215, 'Can change crontab', 73, 'change_crontabschedule'),
(216, 'Can delete crontab', 73, 'delete_crontabschedule'),
(217, 'Can add interval', 74, 'add_intervalschedule'),
(218, 'Can change interval', 74, 'change_intervalschedule'),
(219, 'Can delete interval', 74, 'delete_intervalschedule'),
(220, 'Can add periodic tasks', 75, 'add_periodictasks'),
(221, 'Can change periodic tasks', 75, 'change_periodictasks'),
(222, 'Can delete periodic tasks', 75, 'delete_periodictasks'),
(223, 'Can add task state', 76, 'add_taskmeta'),
(224, 'Can change task state', 76, 'change_taskmeta'),
(225, 'Can delete task state', 76, 'delete_taskmeta'),
(226, 'Can add saved group result', 77, 'add_tasksetmeta'),
(227, 'Can change saved group result', 77, 'change_tasksetmeta'),
(228, 'Can delete saved group result', 77, 'delete_tasksetmeta'),
(229, 'Can add worker', 78, 'add_workerstate'),
(230, 'Can change worker', 78, 'change_workerstate'),
(231, 'Can delete worker', 78, 'delete_workerstate'),
(232, 'Can add task', 79, 'add_taskstate'),
(233, 'Can change task', 79, 'change_taskstate'),
(234, 'Can delete task', 79, 'delete_taskstate'),
(235, 'Can add Admin-translation_backup-singular', 80, 'add_translationbackup'),
(236, 'Can change Admin-translation_backup-singular', 80, 'change_translationbackup'),
(237, 'Can delete Admin-translation_backup-singular', 80, 'delete_translationbackup'),
(238, 'Can add Admin-translation_entry-singular', 81, 'add_translationentry'),
(239, 'Can change Admin-translation_entry-singular', 81, 'change_translationentry'),
(240, 'Can delete Admin-translation_entry-singular', 81, 'delete_translationentry'),
(241, 'admin-translation_entry-load-from-po', 81, 'load');

--
-- Dumping data for table `city`
--

INSERT INTO `city` (`city_id`, `city_name`) VALUES
(1, 'Adrar'),
(2, 'Chlef'),
(3, 'Laghouat'),
(4, 'Oum El Bouaghi'),
(5, 'Batna'),
(6, 'Bejaia'),
(7, 'Biskra'),
(8, 'Bechar'),
(9, 'Blida'),
(10, 'Bouira'),
(11, 'Tamanrasset'),
(12, 'Tebessa'),
(13, 'Tlemcen'),
(14, 'Tiaret'),
(15, 'Tizi Ouzou'),
(16, 'Alger'),
(17, 'Djelfa'),
(18, 'Jijel'),
(19, 'Setif'),
(20, 'Saida'),
(21, 'Skikda'),
(22, 'Sidi Bel Abbes'),
(23, 'Annaba'),
(24, 'Guelma'),
(25, 'Constantine'),
(26, 'Medea'),
(27, 'Mostaganem'),
(28, 'MSila'),
(29, 'Mascara'),
(30, 'Ouargla'),
(31, 'Oran'),
(32, 'El Bayadh'),
(33, 'Illizi'),
(34, 'Bordj Bou Arreridj'),
(35, 'Boumerdes'),
(36, 'Tarf'),
(37, 'Tindouf'),
(38, 'Tissemsilt'),
(39, 'El Oued'),
(40, 'Khenchela'),
(41, 'Souk Ahras'),
(42, 'Tipaza'),
(43, 'Mila'),
(44, 'Ain Defla');

--
-- Dumping data for table `crop`
--

INSERT INTO `crop` (`crop_id`, `crop_name`, `crop_description`) VALUES
(1, 'Blé', 'la culture de blé est très consommée dans notre pays, pour la protéger il faut appliquer deux à 3 fois un fongicide pendant la saison de printemps. Le blé devient très sensible à plusieurs maladies pendant la phase de floraison, notamment la fusariose qui est provoquée par des périodes prolongées avec un humidité élevée.'),
(2, 'Pomme de terre', 'la pomme de terre est connue par sa résistance à la plupart des maladies fongiques contrairement à d\'autres plantes mais vous devez appliquer des produits chimiques contre le mildiou une fois nous détectons un risque élevé. ');

--
-- Dumping data for table `crop_production`
--

INSERT INTO `crop_production` (`crop_production_id`, `name`, `crop_id`, `start_date`, `end_date`, `yield`, `plot_id`, `comments`) VALUES
(15, 'crop one', 1, '2017-02-01', '2017-04-20', NULL, 1, NULL),
(16, 'crop two', 1, '2017-02-01', '2017-04-20', NULL, 1, NULL),
(17, 'crop three', 1, '2017-02-01', '2017-04-20', NULL, 1, NULL),
(18, 'crop four', 1, '2017-02-01', '2017-04-20', NULL, 1, NULL),
(19, 'crop five', 1, '2017-02-01', '2017-04-20', NULL, 12, NULL),
(20, 'crop six', 1, '2017-02-01', '2017-05-20', NULL, 12, NULL),
(21, 'crop seven', 1, '2017-02-01', '2017-05-20', NULL, 12, NULL),
(22, 'crop diff', 1, '2017-04-03', '2017-08-03', NULL, 7, ''),
(23, 'crop eight', 2, '2017-05-06', '2017-08-08', NULL, 1, ''),
(24, 'crop nine', 2, '2017-05-06', '2017-08-08', NULL, 1, ''),
(25, 'crop ten', 1, '2017-05-06', NULL, NULL, 12, '');

--
-- Dumping data for table `disease`
--

INSERT INTO `disease` (`disease_id`, `disease_name`, `disease_description`, `crop_id`) VALUES
(1, 'Fusariose de ble', 'La fusariose du blé est une maladie fongique qui peut apparaître pendant la phase de floraison, au début du printemps. Pour protéger votre culture, il faut appliquer plusieurs types de fongicides recommandés par un expert qui analyse les plantes de votre culture. \r\nVous pouvez observer ses symptômes sur les différentes parties de l\'épi du blé, sa tige, ses feuilles ainsi que la partie basale. Cette maladie fongique peut détruire toute une récolte, causant ainsi des pertes économiques énormes. ', 1),
(2, 'Mildiou de la pomme de terre', 'Le mildiou de la pomme de terre est une maladie fongique qui peut apparaître dans n\'importe qu\'elle phase du cycle de développement de cette plante. Elle est se propage à travers l\'air et peut détruire toute la récolte dans moins de 48 heures. Afin de protéger votre culture contre cette maladie, il faut appliquer les produits phytosanitaires appropriés une fois vous recevez une alerte indiquant un risque élevé. ', 2);
--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(45, 'oauth2_provider', 'application'),
(46, 'APDM', 'disease'),
(47, 'admin', 'logentry'),
(48, 'auth', 'group'),
(49, 'auth', 'permission'),
(50, 'contenttypes', 'contenttype'),
(51, 'sessions', 'session'),
(52, 'APDM', 'alert'),
(53, 'APDM', 'plot'),
(54, 'APDM', 'ownfarm'),
(55, 'APDM', 'alertclient'),
(56, 'APDM', 'crop'),
(57, 'APDM', 'farm'),
(58, 'APDM', 'sensor'),
(59, 'APDM', 'cropproduction'),
(60, 'APDM', 'sensorplot'),
(61, 'APDM', 'city'),
(62, 'APDM', 'djangomigrations'),
(63, 'APDM', 'anomaly'),
(64, 'APDM', 'cropproductiondisease'),
(65, 'APDM', 'cropproductionsensor'),
(66, 'APDM', 'client'),
(67, 'APDM', 'cropclient'),
(68, 'oauth2_provider', 'grant'),
(69, 'oauth2_provider', 'accesstoken'),
(70, 'oauth2_provider', 'refreshtoken'),
(71, 'corsheaders', 'corsmodel'),
(72, 'djcelery', 'periodictask'),
(73, 'djcelery', 'crontabschedule'),
(74, 'djcelery', 'intervalschedule'),
(75, 'djcelery', 'periodictasks'),
(76, 'djcelery', 'taskmeta'),
(77, 'djcelery', 'tasksetmeta'),
(78, 'djcelery', 'workerstate'),
(79, 'djcelery', 'taskstate'),
(80, 'translation_manager', 'translationbackup'),
(81, 'translation_manager', 'translationentry');

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(33, 'APDM', '0001_initial', '2017-05-03 19:07:25'),
(34, 'APDM', '0002_auto_20170503_2003', '2017-05-03 19:07:25'),
(35, 'APDM', '0003_auto_20170503_2007', '2017-05-03 19:07:25'),
(36, 'contenttypes', '0001_initial', '2017-05-03 19:07:25'),
(37, 'admin', '0001_initial', '2017-05-03 19:07:25'),
(38, 'admin', '0002_logentry_remove_auto_add', '2017-05-03 19:07:25'),
(39, 'contenttypes', '0002_remove_content_type_name', '2017-05-03 19:07:25'),
(40, 'auth', '0001_initial', '2017-05-03 19:07:25'),
(41, 'auth', '0002_alter_permission_name_max_length', '2017-05-03 19:07:25'),
(42, 'auth', '0003_alter_user_email_max_length', '2017-05-03 19:07:25'),
(43, 'auth', '0004_alter_user_username_opts', '2017-05-03 19:07:25'),
(44, 'auth', '0005_alter_user_last_login_null', '2017-05-03 19:07:25'),
(45, 'auth', '0006_require_contenttypes_0002', '2017-05-03 19:07:25'),
(46, 'auth', '0007_alter_validators_add_error_messages', '2017-05-03 19:07:25'),
(47, 'auth', '0008_alter_user_username_max_length', '2017-05-03 19:07:25'),
(48, 'oauth2_provider', '0001_initial', '2017-05-03 19:07:25'),
(49, 'oauth2_provider', '0002_08_updates', '2017-05-03 19:07:25'),
(50, 'oauth2_provider', '0003_auto_20160316_1503', '2017-05-03 19:07:25'),
(51, 'oauth2_provider', '0004_auto_20160525_1623', '2017-05-03 19:07:25'),
(52, 'sessions', '0001_initial', '2017-05-03 19:07:25'),
(53, 'djcelery', '0001_initial', '2017-05-03 20:52:13'),
(54, 'APDM', '0004_auto_20170503_2332', '2017-05-03 22:32:38'),


--
-- Dumping data for table `djcelery_crontabschedule`
--

INSERT INTO `djcelery_crontabschedule` (`id`, `minute`, `hour`, `day_of_week`, `day_of_month`, `month_of_year`) VALUES
(1, '0', '4', '*', '*', '*'),
(2, '*', '*/1', '*', '*', '*');

--
-- Dumping data for table `djcelery_intervalschedule`
--

INSERT INTO `djcelery_intervalschedule` (`id`, `every`, `period`) VALUES
(1, 12, 'hours'),
(2, 10, 'minutes'),
(3, 1, 'minutes'),
(4, 2, 'minutes'),
(5, 24, 'hours');

--
-- Dumping data for table `djcelery_periodictask`
--

INSERT INTO `djcelery_periodictask` (`id`, `name`, `task`, `args`, `kwargs`, `queue`, `exchange`, `routing_key`, `expires`, `enabled`, `last_run_at`, `total_run_count`, `date_changed`, `description`, `crontab_id`, `interval_id`) VALUES
(7, 'forecastPLB', 'project.celery.forecastDisease', '[2]', '{}', NULL, NULL, NULL, NULL, 0, NULL, 4, '2017-05-03 22:21:50', '', NULL, 1),
(2, 'celery.backend_cleanup', 'celery.backend_cleanup', '[]', '{}', NULL, NULL, NULL, NULL, 1, NULL, 0, '2017-05-04 18:33:19', '', 1, NULL),
(8, 'NewTask', 'project.celery.forecastDisease', '[1]', '{}', NULL, NULL, NULL, NULL, 0, NULL, 0, '2017-06-02 21:26:21', '', NULL, 5),
(6, 'forecastFHB', 'project.celery.forecastDisease', '[1]', '{}', NULL, NULL, NULL, NULL, 1, '2017-05-04 20:23:27', 132, '2017-05-04 20:24:22', '', NULL, 3),
(9, 'forecastMildew', 'project.celery.forecastDisease', '[1]', '{}', NULL, NULL, NULL, NULL, 1, NULL, 0, '2017-06-02 21:26:05', '', NULL, 4);

--
-- Dumping data for table `djcelery_periodictasks`
--

INSERT INTO `djcelery_periodictasks` (`ident`, `last_update`) VALUES
(1, '2017-06-02 21:26:21');

--
-- Dumping data for table `djcelery_workerstate`
--

INSERT INTO `djcelery_workerstate` (`id`, `hostname`, `last_heartbeat`) VALUES
(1, 'celery@DESKTOP-JB38MKB', '2017-05-04 20:26:29');

--
-- Dumping data for table `farm`
--

INSERT INTO `farm` (`farm_id`, `farm_name`, `city_id`, `comments`) VALUES
(1, 'farma', '19', ''),
(31, 'farmb', '9', ''),
(32, 'farmc', '1', NULL),
(33, 'new farm', '2', NULL),
(34, 'farmyy', '22', NULL),
(35, 'farm', '48', NULL),
(3, 'farm abc', '26', NULL),
(37, 'smartfarm', '16', '');

--
-- Dumping data for table `measure`
--

INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES
(291, 15, '2017-05-03 19:19:35', 5),
(292, 15, '2017-05-03 19:19:35', 5),
(293, 15, '2017-05-03 19:19:35', 5),
(294, 15, '2017-05-03 19:19:35', 5),
(295, 15, '2017-05-03 19:19:35', 5),
(296, 15, '2017-05-03 19:19:35', 5),
(297, 15, '2017-05-03 19:19:35', 5),
(298, 15, '2017-05-03 19:19:35', 5),
(299, 15, '2017-05-03 19:19:35', 5),
(300, 15, '2017-05-03 19:19:35', 5),
(301, 15, '2017-05-03 19:19:35', 5),
(302, 15, '2017-05-03 19:19:35', 5),
(303, 15, '2017-05-03 19:19:35', 5),
(304, 15, '2017-05-03 19:19:35', 5),
(305, 15, '2017-05-03 19:19:35', 5),
(306, 15, '2017-05-03 19:19:35', 5),
(307, 15, '2017-05-03 19:19:35', 5),
(308, 15, '2017-05-03 19:19:35', 5),
(309, 15, '2017-05-03 19:19:35', 5),
(310, 15, '2017-05-03 19:19:35', 5),
(311, 15, '2017-05-03 19:19:35', 5),
(312, 15, '2017-05-03 19:19:35', 5),
(313, 15, '2017-05-03 19:19:35', 5),
(314, 95, '2017-05-03 19:19:35', 1),
(315, 95, '2017-05-03 19:19:35', 1),
(316, 95, '2017-05-03 19:19:35', 1),
(317, 95, '2017-05-03 19:19:35', 1),
(318, 95, '2017-05-03 19:19:35', 1),
(319, 95, '2017-05-03 19:19:35', 1),
(320, 95, '2017-05-03 19:19:35', 1),
(321, 95, '2017-05-03 19:19:35', 1),
(322, 95, '2017-05-03 19:19:35', 1),
(323, 95, '2017-05-03 19:19:35', 1),
(324, 95, '2017-05-03 19:19:35', 1),
(325, 95, '2017-05-03 19:19:35', 1),
(326, 95, '2017-05-03 19:19:35', 1),
(327, 95, '2017-05-03 19:19:35', 1),
(328, 95, '2017-05-03 19:19:35', 1),
(329, 95, '2017-05-03 19:19:35', 1),
(330, 95, '2017-05-03 19:19:35', 1),
(331, 95, '2017-05-03 19:19:35', 1),
(332, 95, '2017-05-03 19:19:35', 1),
(333, 0.8, '2017-05-03 19:19:35', 10),
(334, 0.8, '2017-05-03 19:19:35', 10),
(335, 0.8, '2017-05-03 19:19:35', 10),
(336, 0.8, '2017-05-03 19:19:35', 10),
(337, 0.8, '2017-05-03 19:19:35', 10),
(338, 0.8, '2017-05-03 19:19:35', 10),
(339, 0.8, '2017-05-03 19:19:35', 10),
(340, 0.8, '2017-05-03 19:19:35', 10),
(341, 0.8, '2017-05-03 19:19:35', 10),
(342, 0.8, '2017-05-03 19:19:35', 10),
(343, 0.8, '2017-05-03 19:19:35', 10),
(344, 0.8, '2017-05-03 19:19:35', 10),
(345, 0.8, '2017-05-03 19:19:35', 10),
(346, 0.8, '2017-05-03 19:19:35', 10),
(347, 0.8, '2017-05-03 19:19:35', 10),
(348, 0.8, '2017-05-03 19:19:35', 10);


--
-- Dumping data for table `oauth2_provider_application`
--

INSERT INTO `oauth2_provider_application` (`id`, `client_id`, `redirect_uris`, `client_type`, `authorization_grant_type`, `client_secret`, `name`, `user_id`, `skip_authorization`) VALUES
(2, '7lUesSIoMIvN3r4FCBakVWp4IwQAu6tMlmRjQD8o', '', 'public', 'password', '4BGxi0aTdnLc3sQPU0SNxoyadPkltXpxG7a6YIns5jaM1tmHTR0M0d5qY3F2FN0upiZusSG1TKo0wYNIyRhgkjIiFPllSFPACB0B9ud479iTpEBBoUcvD4z85WxcmESX', 'Angular frontend', 23, 0);


--
-- Dumping data for table `plot`
--

INSERT INTO `plot` (`plot_id`, `plot_name`, `latitude`, `longitude`, `soil_type`, `farm_id`, `comments`) VALUES
(7, 'plot in metidja', 0, 0, 'aride', 2, NULL),
(8, 'plot in farm_ida', 0, 0, 'aride', 3, NULL),
(9, 'plot in farm_ida', 0, 0, 'aride', 3, NULL),
(10, 'plot in metidja', 0, 0, 'aride', 2, NULL),
(1, 'plot in metidja', 35, 1, 'aride', 1, ''),
(12, 'plot one', 36, 1, 'aride', 1, ''),
(13, 'parcelle', 1, 1, 'aride', 37, ''),
(14, 'plot n', 2, 2, 'aride', 37, ''),
(15, 'plot ten', 0, 0, 'aride', 1, 'no comment');

--
-- Dumping data for table `sensor`
--

INSERT INTO `sensor` (`sensor_id`, `sensor_type`, `sensor_unit`) VALUES
(1, 'humidity', '%'),
(16, 'humidity', '%'),
(17, 'humidity', '%'),
(18, 'humidity', '%'),
(5, 'temperature', '°C'),
(20, 'temperature', '°C'),
(21, 'temperature', '°C'),
(22, 'temperature', '°C'),
(23, 'temperature', '°C'),
(24, 'rainfall', 'mm'),
(25, 'rainfall', 'mm'),
(26, 'rainfall', 'mm'),
(10, 'rainfall', 'mm'),
(28, 'rainfall', 'mm');

-- --------------------------------------------------------

--
-- Structure for view `alert_client`
--
DROP TABLE IF EXISTS `alert_client`;

CREATE ALGORITHM=UNDEFINED DEFINER=`esi`@`localhost` SQL SECURITY DEFINER VIEW `alert_client`  AS  select `apdm_client`.`client_id` AS `client_id`,`alert`.`alert_id` AS `alert_id` from (((((`apdm_ownfarm` join `apdm_client`) join `crop_production`) join `plot`) join `farm`) join `alert`) where ((`apdm_ownfarm`.`farm_id` = `farm`.`farm_id`) and (`apdm_client`.`client_id` = `apdm_ownfarm`.`client_id`) and (`plot`.`farm_id` = `farm`.`farm_id`) and (`crop_production`.`plot_id` = `plot`.`plot_id`) and (`alert`.`crop_production_id` = `crop_production`.`crop_production_id`)) ;

-- --------------------------------------------------------

--
-- Structure for view `crop_client`
--
DROP TABLE IF EXISTS `crop_client`;

CREATE ALGORITHM=UNDEFINED DEFINER=`esi`@`localhost` SQL SECURITY DEFINER VIEW `crop_client`  AS  select `apdm_client`.`client_id` AS `client_id`,`crop_production`.`crop_production_id` AS `crop_production_id` from ((((`apdm_ownfarm` join `apdm_client`) join `crop_production`) join `plot`) join `farm`) where ((`apdm_ownfarm`.`farm_id` = `farm`.`farm_id`) and (`apdm_client`.`client_id` = `apdm_ownfarm`.`client_id`) and (`plot`.`farm_id` = `farm`.`farm_id`) and (`crop_production`.`plot_id` = `plot`.`plot_id`)) ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
