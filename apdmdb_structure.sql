-- phpMyAdmin SQL Dump
-- version 4.5.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Jun 04, 2017 at 05:45 PM
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

-- --------------------------------------------------------

--
-- Table structure for table `alert`
--

CREATE TABLE `alert` (
  `alert_id` int(11) NOT NULL,
  `alert_date` datetime NOT NULL,
  `crop_production_id` int(11) NOT NULL,
  `disease_id` int(11) NOT NULL,
  `risk_rate` float NOT NULL,
  `feedback_date` datetime DEFAULT NULL,
  `feedback_type` varchar(50) COLLATE utf8_bin DEFAULT NULL,
  `client_id` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Stand-in structure for view `alert_client`
--
CREATE TABLE `alert_client` (
`client_id` int(11)
,`alert_id` int(11)
);

-- --------------------------------------------------------

--
-- Table structure for table `anomaly`
--

CREATE TABLE `anomaly` (
  `anomaly_id` int(11) NOT NULL,
  `occurence_date` datetime NOT NULL,
  `reporting_date` datetime NOT NULL,
  `client_id` int(11) NOT NULL,
  `crop_production_id` int(11) NOT NULL,
  `disease_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `apdm_client`
--

CREATE TABLE `apdm_client` (
  `client_id` int(11) NOT NULL,
  `username` varchar(150) COLLATE utf8_bin NOT NULL,
  `first_name` varchar(30) COLLATE utf8_bin DEFAULT NULL,
  `last_name` varchar(30) COLLATE utf8_bin DEFAULT NULL,
  `email` varchar(254) COLLATE utf8_bin NOT NULL,
  `gender` enum('homme','femme') COLLATE utf8_bin DEFAULT NULL,
  `phone_contact` varchar(50) COLLATE utf8_bin DEFAULT NULL,
  `phone_sms` varchar(50) COLLATE utf8_bin DEFAULT NULL,
  `language` enum('','arabic','english','french','spanish','german') COLLATE utf8_bin DEFAULT NULL,
  `comments` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `notification_sms` tinyint(1) DEFAULT NULL,
  `notification_email` tinyint(1) DEFAULT NULL,
  `password` varchar(128) COLLATE utf8_bin NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `apdm_client_groups`
--

CREATE TABLE `apdm_client_groups` (
  `id` int(11) NOT NULL,
  `client_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `apdm_client_user_permissions`
--

CREATE TABLE `apdm_client_user_permissions` (
  `id` int(11) NOT NULL,
  `client_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `apdm_cropproductiondisease`
--

CREATE TABLE `apdm_cropproductiondisease` (
  `id` int(11) NOT NULL,
  `crop_production_id` int(11) NOT NULL,
  `disease_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `apdm_cropproductionsensor`
--

CREATE TABLE `apdm_cropproductionsensor` (
  `id` int(11) NOT NULL,
  `crop_production_id` int(11) NOT NULL,
  `sensor_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `apdm_ownfarm`
--

CREATE TABLE `apdm_ownfarm` (
  `id` int(11) NOT NULL,
  `client_id` int(11) NOT NULL,
  `farm_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `apdm_sensorplot`
--

CREATE TABLE `apdm_sensorplot` (
  `id` int(11) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date DEFAULT NULL,
  `plot_id` int(11) NOT NULL,
  `sensor_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) COLLATE utf8_bin NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_bin NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_bin NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `celery_taskmeta`
--

CREATE TABLE `celery_taskmeta` (
  `id` int(11) NOT NULL,
  `task_id` varchar(255) NOT NULL,
  `status` varchar(50) NOT NULL,
  `result` longtext,
  `date_done` datetime NOT NULL,
  `traceback` longtext,
  `hidden` tinyint(1) NOT NULL,
  `meta` longtext
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `celery_tasksetmeta`
--

CREATE TABLE `celery_tasksetmeta` (
  `id` int(11) NOT NULL,
  `taskset_id` varchar(255) NOT NULL,
  `result` longtext NOT NULL,
  `date_done` datetime NOT NULL,
  `hidden` tinyint(1) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `city`
--

CREATE TABLE `city` (
  `city_id` int(11) NOT NULL,
  `city_name` varchar(50) COLLATE utf8_bin NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `crop`
--

CREATE TABLE `crop` (
  `crop_id` int(11) NOT NULL,
  `crop_name` varchar(50) COLLATE utf8_bin NOT NULL,
  `crop_description` text COLLATE utf8_bin
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Stand-in structure for view `crop_client`
--
CREATE TABLE `crop_client` (
`client_id` int(11)
,`crop_production_id` int(11)
);

-- --------------------------------------------------------

--
-- Table structure for table `crop_production`
--

CREATE TABLE `crop_production` (
  `crop_production_id` int(11) NOT NULL,
  `name` varchar(50) COLLATE utf8_bin NOT NULL,
  `crop_id` int(11) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date DEFAULT NULL,
  `yield` double DEFAULT NULL,
  `plot_id` int(11) NOT NULL,
  `comments` varchar(100) COLLATE utf8_bin DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `disease`
--

CREATE TABLE `disease` (
  `disease_id` int(11) NOT NULL,
  `disease_name` varchar(50) COLLATE utf8_bin NOT NULL,
  `disease_description` text COLLATE utf8_bin,
  `crop_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime NOT NULL,
  `object_id` longtext COLLATE utf8_bin,
  `object_repr` varchar(200) COLLATE utf8_bin NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext COLLATE utf8_bin NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) COLLATE utf8_bin NOT NULL,
  `model` varchar(100) COLLATE utf8_bin NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) COLLATE utf8_bin NOT NULL,
  `name` varchar(255) COLLATE utf8_bin NOT NULL,
  `applied` datetime NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_bin NOT NULL,
  `session_data` longtext COLLATE utf8_bin NOT NULL,
  `expire_date` datetime NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `djcelery_crontabschedule`
--

CREATE TABLE `djcelery_crontabschedule` (
  `id` int(11) NOT NULL,
  `minute` varchar(64) NOT NULL,
  `hour` varchar(64) NOT NULL,
  `day_of_week` varchar(64) NOT NULL,
  `day_of_month` varchar(64) NOT NULL,
  `month_of_year` varchar(64) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `djcelery_intervalschedule`
--

CREATE TABLE `djcelery_intervalschedule` (
  `id` int(11) NOT NULL,
  `every` int(11) NOT NULL,
  `period` varchar(24) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `djcelery_periodictask`
--

CREATE TABLE `djcelery_periodictask` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `task` varchar(200) NOT NULL,
  `args` longtext NOT NULL,
  `kwargs` longtext NOT NULL,
  `queue` varchar(200) DEFAULT NULL,
  `exchange` varchar(200) DEFAULT NULL,
  `routing_key` varchar(200) DEFAULT NULL,
  `expires` datetime DEFAULT NULL,
  `enabled` tinyint(1) NOT NULL,
  `last_run_at` datetime DEFAULT NULL,
  `total_run_count` int(10) UNSIGNED NOT NULL,
  `date_changed` datetime NOT NULL,
  `description` longtext NOT NULL,
  `crontab_id` int(11) DEFAULT NULL,
  `interval_id` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `djcelery_periodictasks`
--

CREATE TABLE `djcelery_periodictasks` (
  `ident` smallint(6) NOT NULL,
  `last_update` datetime NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `djcelery_taskstate`
--

CREATE TABLE `djcelery_taskstate` (
  `id` int(11) NOT NULL,
  `state` varchar(64) NOT NULL,
  `task_id` varchar(36) NOT NULL,
  `name` varchar(200) DEFAULT NULL,
  `tstamp` datetime NOT NULL,
  `args` longtext,
  `kwargs` longtext,
  `eta` datetime DEFAULT NULL,
  `expires` datetime DEFAULT NULL,
  `result` longtext,
  `traceback` longtext,
  `runtime` double DEFAULT NULL,
  `retries` int(11) NOT NULL,
  `hidden` tinyint(1) NOT NULL,
  `worker_id` int(11)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `djcelery_workerstate`
--

CREATE TABLE `djcelery_workerstate` (
  `id` int(11) NOT NULL,
  `hostname` varchar(255) NOT NULL,
  `last_heartbeat` datetime DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `farm`
--

CREATE TABLE `farm` (
  `farm_id` int(11) NOT NULL,
  `farm_name` varchar(50) COLLATE utf8_bin NOT NULL,
  `city_id` varchar(50) COLLATE utf8_bin NOT NULL,
  `comments` varchar(100) COLLATE utf8_bin DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `measure`
--

CREATE TABLE `measure` (
  `measure_id` int(11) NOT NULL,
  `measure_value` double NOT NULL,
  `measure_timestamp` timestamp NOT NULL,
  `sensor_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `oauth2_provider_accesstoken`
--

CREATE TABLE `oauth2_provider_accesstoken` (
  `id` int(11) NOT NULL,
  `token` varchar(255) COLLATE utf8_bin NOT NULL,
  `expires` datetime NOT NULL,
  `scope` longtext COLLATE utf8_bin NOT NULL,
  `application_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `oauth2_provider_application`
--

CREATE TABLE `oauth2_provider_application` (
  `id` int(11) NOT NULL,
  `client_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `redirect_uris` longtext COLLATE utf8_bin NOT NULL,
  `client_type` varchar(32) COLLATE utf8_bin NOT NULL,
  `authorization_grant_type` varchar(32) COLLATE utf8_bin NOT NULL,
  `client_secret` varchar(255) COLLATE utf8_bin NOT NULL,
  `name` varchar(255) COLLATE utf8_bin NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `skip_authorization` tinyint(1) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `oauth2_provider_grant`
--

CREATE TABLE `oauth2_provider_grant` (
  `id` int(11) NOT NULL,
  `code` varchar(255) COLLATE utf8_bin NOT NULL,
  `expires` datetime NOT NULL,
  `redirect_uri` varchar(255) COLLATE utf8_bin NOT NULL,
  `scope` longtext COLLATE utf8_bin NOT NULL,
  `application_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `oauth2_provider_refreshtoken`
--

CREATE TABLE `oauth2_provider_refreshtoken` (
  `id` int(11) NOT NULL,
  `token` varchar(255) COLLATE utf8_bin NOT NULL,
  `access_token_id` int(11) NOT NULL,
  `application_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `plot`
--

CREATE TABLE `plot` (
  `plot_id` int(11) NOT NULL,
  `plot_name` varchar(50) COLLATE utf8_bin NOT NULL,
  `latitude` double NOT NULL DEFAULT '0',
  `longitude` double NOT NULL DEFAULT '0',
  `soil_type` enum('aride','semi-aride') COLLATE utf8_bin DEFAULT NULL,
  `farm_id` int(11) NOT NULL,
  `comments` varchar(50) COLLATE utf8_bin DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `sensor`
--

CREATE TABLE `sensor` (
  `sensor_id` int(11) NOT NULL,
  `sensor_type` varchar(20) COLLATE utf8_bin NOT NULL,
  `sensor_unit` varchar(20) COLLATE utf8_bin NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Structure for view `alert_client`
--
DROP TABLE IF EXISTS `alert_client`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `alert_client`  AS  select `apdm_client`.`client_id` AS `client_id`,`alert`.`alert_id` AS `alert_id` from (((((`apdm_ownfarm` join `apdm_client`) join `crop_production`) join `plot`) join `farm`) join `alert`) where ((`apdm_ownfarm`.`farm_id` = `farm`.`farm_id`) and (`apdm_client`.`client_id` = `apdm_ownfarm`.`client_id`) and (`plot`.`farm_id` = `farm`.`farm_id`) and (`crop_production`.`plot_id` = `plot`.`plot_id`) and (`alert`.`crop_production_id` = `crop_production`.`crop_production_id`)) ;

-- --------------------------------------------------------

--
-- Structure for view `crop_client`
--
DROP TABLE IF EXISTS `crop_client`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `crop_client`  AS  select `apdm_client`.`client_id` AS `client_id`,`crop_production`.`crop_production_id` AS `crop_production_id` from ((((`apdm_ownfarm` join `apdm_client`) join `crop_production`) join `plot`) join `farm`) where ((`apdm_ownfarm`.`farm_id` = `farm`.`farm_id`) and (`apdm_client`.`client_id` = `apdm_ownfarm`.`client_id`) and (`plot`.`farm_id` = `farm`.`farm_id`) and (`crop_production`.`plot_id` = `plot`.`plot_id`)) ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alert`
--
ALTER TABLE `alert`
  ADD PRIMARY KEY (`alert_id`),
  ADD KEY `client_id` (`client_id`),
  ADD KEY `crop_production_id` (`crop_production_id`),
  ADD KEY `disease_id` (`disease_id`);

--
-- Indexes for table `anomaly`
--
ALTER TABLE `anomaly`
  ADD PRIMARY KEY (`anomaly_id`),
  ADD KEY `client_id` (`client_id`),
  ADD KEY `crop_production_id` (`crop_production_id`),
  ADD KEY `disease_id` (`disease_id`);

--
-- Indexes for table `apdm_client`
--
ALTER TABLE `apdm_client`
  ADD PRIMARY KEY (`client_id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `apdm_client_groups`
--
ALTER TABLE `apdm_client_groups`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `apdm_client_user_permissions`
--
ALTER TABLE `apdm_client_user_permissions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `apdm_cropproductiondisease`
--
ALTER TABLE `apdm_cropproductiondisease`
  ADD PRIMARY KEY (`id`),
  ADD KEY `apdm_cropproductiondisease_32ebadbc` (`crop_production_id`),
  ADD KEY `apdm_cropproductiondisease_daa24ab7` (`disease_id`);

--
-- Indexes for table `apdm_cropproductionsensor`
--
ALTER TABLE `apdm_cropproductionsensor`
  ADD PRIMARY KEY (`id`),
  ADD KEY `apdm_cropproductionsensor_32ebadbc` (`crop_production_id`),
  ADD KEY `apdm_cropproductionsensor_d96d866a` (`sensor_id`);

--
-- Indexes for table `apdm_ownfarm`
--
ALTER TABLE `apdm_ownfarm`
  ADD PRIMARY KEY (`id`),
  ADD KEY `apdm_ownfarm_2bfe9d72` (`client_id`),
  ADD KEY `apdm_ownfarm_55fc7f5a` (`farm_id`);

--
-- Indexes for table `apdm_sensorplot`
--
ALTER TABLE `apdm_sensorplot`
  ADD PRIMARY KEY (`id`),
  ADD KEY `apdm_sensorplot_b9e8bb91` (`plot_id`),
  ADD KEY `apdm_sensorplot_d96d866a` (`sensor_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissions_0e939a4f` (`group_id`),
  ADD KEY `auth_group_permissions_8373b171` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  ADD KEY `auth_permission_417f1b1c` (`content_type_id`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_e8701ad4` (`user_id`),
  ADD KEY `auth_user_groups_0e939a4f` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  ADD KEY `auth_user_user_permissions_8373b171` (`permission_id`);

--
-- Indexes for table `celery_taskmeta`
--
ALTER TABLE `celery_taskmeta`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `task_id` (`task_id`),
  ADD KEY `celery_taskmeta_662f707d` (`hidden`);

--
-- Indexes for table `celery_tasksetmeta`
--
ALTER TABLE `celery_tasksetmeta`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `taskset_id` (`taskset_id`),
  ADD KEY `celery_tasksetmeta_662f707d` (`hidden`);

--
-- Indexes for table `city`
--
ALTER TABLE `city`
  ADD PRIMARY KEY (`city_id`);

--
-- Indexes for table `crop`
--
ALTER TABLE `crop`
  ADD PRIMARY KEY (`crop_id`);

--
-- Indexes for table `crop_production`
--
ALTER TABLE `crop_production`
  ADD PRIMARY KEY (`crop_production_id`),
  ADD KEY `plot_id` (`plot_id`),
  ADD KEY `crop_id` (`crop_id`);

--
-- Indexes for table `disease`
--
ALTER TABLE `disease`
  ADD PRIMARY KEY (`disease_id`),
  ADD KEY `crop_id` (`crop_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_417f1b1c` (`content_type_id`),
  ADD KEY `django_admin_log_e8701ad4` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_de54fa62` (`expire_date`);

--
-- Indexes for table `djcelery_crontabschedule`
--
ALTER TABLE `djcelery_crontabschedule`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `djcelery_intervalschedule`
--
ALTER TABLE `djcelery_intervalschedule`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `djcelery_periodictask`
--
ALTER TABLE `djcelery_periodictask`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`),
  ADD KEY `djcelery_periodictask_f3f0d72a` (`crontab_id`),
  ADD KEY `djcelery_periodictask_1dcd7040` (`interval_id`);

--
-- Indexes for table `djcelery_periodictasks`
--
ALTER TABLE `djcelery_periodictasks`
  ADD PRIMARY KEY (`ident`);

--
-- Indexes for table `djcelery_taskstate`
--
ALTER TABLE `djcelery_taskstate`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `task_id` (`task_id`),
  ADD KEY `djcelery_taskstate_9ed39e2e` (`state`),
  ADD KEY `djcelery_taskstate_b068931c` (`name`),
  ADD KEY `djcelery_taskstate_863bb2ee` (`tstamp`),
  ADD KEY `djcelery_taskstate_662f707d` (`hidden`),
  ADD KEY `djcelery_taskstate_ce77e6ef` (`worker_id`);

--
-- Indexes for table `djcelery_workerstate`
--
ALTER TABLE `djcelery_workerstate`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `hostname` (`hostname`),
  ADD KEY `djcelery_workerstate_f129901a` (`last_heartbeat`);

--
-- Indexes for table `farm`
--
ALTER TABLE `farm`
  ADD PRIMARY KEY (`farm_id`),
  ADD KEY `city_id` (`city_id`);

--
-- Indexes for table `measure`
--
ALTER TABLE `measure`
  ADD PRIMARY KEY (`measure_id`),
  ADD KEY `sensor_id` (`sensor_id`);

--
-- Indexes for table `oauth2_provider_accesstoken`
--
ALTER TABLE `oauth2_provider_accesstoken`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `oauth2_provider_accesstoken_token_8af090f8_uniq` (`token`),
  ADD KEY `oauth2_provider_accesstoken_6bc0a4eb` (`application_id`),
  ADD KEY `oauth2_provider_accesstoken_e8701ad4` (`user_id`);

--
-- Indexes for table `oauth2_provider_application`
--
ALTER TABLE `oauth2_provider_application`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `client_id` (`client_id`),
  ADD KEY `oauth2_provider_application_9d667c2b` (`client_secret`),
  ADD KEY `oauth2_provider_application_e8701ad4` (`user_id`);

--
-- Indexes for table `oauth2_provider_grant`
--
ALTER TABLE `oauth2_provider_grant`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `oauth2_provider_grant_code_49ab4ddf_uniq` (`code`),
  ADD KEY `oauth2_provider_grant_6bc0a4eb` (`application_id`),
  ADD KEY `oauth2_provider_grant_e8701ad4` (`user_id`);

--
-- Indexes for table `oauth2_provider_refreshtoken`
--
ALTER TABLE `oauth2_provider_refreshtoken`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `access_token_id` (`access_token_id`),
  ADD UNIQUE KEY `oauth2_provider_refreshtoken_token_d090daa4_uniq` (`token`),
  ADD KEY `oauth2_provider_refreshtoken_6bc0a4eb` (`application_id`),
  ADD KEY `oauth2_provider_refreshtoken_e8701ad4` (`user_id`);

--
-- Indexes for table `plot`
--
ALTER TABLE `plot`
  ADD PRIMARY KEY (`plot_id`),
  ADD KEY `farm_id` (`farm_id`);

--
-- Indexes for table `sensor`
--
ALTER TABLE `sensor`
  ADD PRIMARY KEY (`sensor_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `alert`
--
ALTER TABLE `alert`
  MODIFY `alert_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=122;
--
-- AUTO_INCREMENT for table `anomaly`
--
ALTER TABLE `anomaly`
  MODIFY `anomaly_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=106;
--
-- AUTO_INCREMENT for table `apdm_client`
--
ALTER TABLE `apdm_client`
  MODIFY `client_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;
--
-- AUTO_INCREMENT for table `apdm_client_groups`
--
ALTER TABLE `apdm_client_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `apdm_client_user_permissions`
--
ALTER TABLE `apdm_client_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `apdm_cropproductiondisease`
--
ALTER TABLE `apdm_cropproductiondisease`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;
--
-- AUTO_INCREMENT for table `apdm_cropproductionsensor`
--
ALTER TABLE `apdm_cropproductionsensor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;
--
-- AUTO_INCREMENT for table `apdm_ownfarm`
--
ALTER TABLE `apdm_ownfarm`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;
--
-- AUTO_INCREMENT for table `apdm_sensorplot`
--
ALTER TABLE `apdm_sensorplot`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=58;
--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=242;
--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `celery_taskmeta`
--
ALTER TABLE `celery_taskmeta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `celery_tasksetmeta`
--
ALTER TABLE `celery_tasksetmeta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `city`
--
ALTER TABLE `city`
  MODIFY `city_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;
--
-- AUTO_INCREMENT for table `crop`
--
ALTER TABLE `crop`
  MODIFY `crop_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `crop_production`
--
ALTER TABLE `crop_production`
  MODIFY `crop_production_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
--
-- AUTO_INCREMENT for table `disease`
--
ALTER TABLE `disease`
  MODIFY `disease_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=464;
--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=82;
--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=60;
--
-- AUTO_INCREMENT for table `djcelery_crontabschedule`
--
ALTER TABLE `djcelery_crontabschedule`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `djcelery_intervalschedule`
--
ALTER TABLE `djcelery_intervalschedule`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `djcelery_periodictask`
--
ALTER TABLE `djcelery_periodictask`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- AUTO_INCREMENT for table `djcelery_taskstate`
--
ALTER TABLE `djcelery_taskstate`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=93;
--
-- AUTO_INCREMENT for table `djcelery_workerstate`
--
ALTER TABLE `djcelery_workerstate`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `farm`
--
ALTER TABLE `farm`
  MODIFY `farm_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;
--
-- AUTO_INCREMENT for table `measure`
--
ALTER TABLE `measure`
  MODIFY `measure_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=349;
--
-- AUTO_INCREMENT for table `oauth2_provider_accesstoken`
--
ALTER TABLE `oauth2_provider_accesstoken`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=516;
--
-- AUTO_INCREMENT for table `oauth2_provider_application`
--
ALTER TABLE `oauth2_provider_application`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `oauth2_provider_grant`
--
ALTER TABLE `oauth2_provider_grant`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `oauth2_provider_refreshtoken`
--
ALTER TABLE `oauth2_provider_refreshtoken`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=516;
--
-- AUTO_INCREMENT for table `plot`
--
ALTER TABLE `plot`
  MODIFY `plot_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
--
-- AUTO_INCREMENT for table `sensor`
--
ALTER TABLE `sensor`
  MODIFY `sensor_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
