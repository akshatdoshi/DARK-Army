-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 03, 2018 at 04:00 AM
-- Server version: 10.1.29-MariaDB
-- PHP Version: 7.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hackathon`
--

-- --------------------------------------------------------

--
-- Table structure for table `ingrident`
--

CREATE TABLE `ingrident` (
  `ingri_Id` int(11) NOT NULL,
  `ingri_name` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `ingrident`
--

INSERT INTO `ingrident` (`ingri_Id`, `ingri_name`) VALUES
(1, 'egg'),
(2, 'milk'),
(3, 'peanut'),
(4, 'chilly flakes');

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `product_id` int(11) NOT NULL,
  `product_name` varchar(45) NOT NULL,
  `total_qty` int(11) NOT NULL,
  `product_sold` int(11) NOT NULL,
  `brand` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`product_id`, `product_name`, `total_qty`, `product_sold`, `brand`) VALUES
(1, 'bread_1', 10, 8, 'abc'),
(2, 'break', 14, 7, 'bcd');

-- --------------------------------------------------------

--
-- Table structure for table `prod_ingri`
--

CREATE TABLE `prod_ingri` (
  `product_id` int(11) NOT NULL,
  `ingri_Id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `prod_ingri`
--

INSERT INTO `prod_ingri` (`product_id`, `ingri_Id`) VALUES
(1, 1),
(2, 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `ingrident`
--
ALTER TABLE `ingrident`
  ADD PRIMARY KEY (`ingri_Id`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `prod_ingri`
--
ALTER TABLE `prod_ingri`
  ADD PRIMARY KEY (`product_id`,`ingri_Id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `ingrident`
--
ALTER TABLE `ingrident`
  MODIFY `ingri_Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
