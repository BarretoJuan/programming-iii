-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 18, 2023 at 01:11 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `escuela_urbe`
--

-- --------------------------------------------------------


-- --------------------------------------------------------

--
-- Table structure for table `estudiante`
--

CREATE TABLE `estudiante` (
  `nombre` varchar(45) NOT NULL,
  `cedula` varchar(12) NOT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `direccion` text DEFAULT NULL,
  `email` varchar(45) NOT NULL,
  `carrera` varchar(100) NOT NULL,
  `telefono` varchar(11) NOT NULL,
  `id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `estudiante`
--

INSERT INTO `estudiante` (`nombre`, `cedula`, `fecha_nacimiento`, `direccion`, `email`, `carrera`, `telefono`, `id`) VALUES
('juan', '31106376', '1500-04-04', 'juan', 'juaaaan', 'juan', '04684658947', 1),
('Juan Barreto', '55555555', '2004-07-09', 'juan', 'juan@gmail.com', 'ingenieria', '04145555555', 2),
('Pedro Gonzalez', '10408853', '1990-04-04', 'la victoria', 'pedro@gmail.com', 'ingenieriaaa', '04246395009', 3),
('juan', '9747693', '1980-04-04', 'hyab', 'juan10@gmail.com', 'ingenieria', '04146668888', 4),
('juan', '31106847', '1800-04-04', 'juan', 'juan', 'juan', '04265555987', 5),
('pepe', '34567567', '0000-00-00', 'juan', 'juaigrnio', 'juan', '04125555555', 6);

-- --------------------------------------------------------

--
ALTER TABLE `estudiante`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `cedula` (`cedula`),
  ADD UNIQUE KEY `cedula_2` (`cedula`),
  ADD UNIQUE KEY `telefono` (`telefono`),
  ADD UNIQUE KEY `telefono_2` (`telefono`),
  ADD UNIQUE KEY `telefono_3` (`telefono`),
  ADD UNIQUE KEY `cedula_3` (`cedula`);

--
ALTER TABLE `estudiante`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
