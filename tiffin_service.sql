-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 25, 2021 at 03:16 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tiffin_service`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `email` varchar(100) NOT NULL,
  `password` varchar(50) NOT NULL,
  `role` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`email`, `password`, `role`) VALUES
('admin@gmail.com', '321321', 'Admin'),
('limiteduser@gmail.com', '112233', 'Limited user'),
('superadmin@gmail.com', '123123', 'Super Admin');

-- --------------------------------------------------------

--
-- Table structure for table `booking_details`
--

CREATE TABLE `booking_details` (
  `booking_id` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `order_no` int(11) NOT NULL,
  `invoice_date` date NOT NULL,
  `meal_type` varchar(20) NOT NULL,
  `meal_duration` varchar(15) NOT NULL,
  `start_date` date NOT NULL,
  `total_price` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `booking_details`
--

INSERT INTO `booking_details` (`booking_id`, `email`, `order_no`, `invoice_date`, `meal_type`, `meal_duration`, `start_date`, `total_price`) VALUES
(10, 'tanya29sehgal@gmail.com', 11, '2021-06-22', 'dinner', 'one-week', '2021-06-23', 868),
(11, 'tanya29sehgal@gmail.com', 12, '2021-06-22', 'lunch', 'four-weeks', '2021-06-23', 3335),
(12, 'pallav.marwah@gmail.com', 13, '2021-06-22', 'lunch', 'one-week', '2021-06-23', 868),
(13, 'tanya29sehgal@gmail.com', 14, '2021-06-23', 'dinner', 'one-week', '2021-06-24', 868),
(14, 'tanya29sehgal@gmail.com', 15, '2021-06-23', 'lunch', 'four-weeks', '2021-06-28', 3335),
(15, 'rajesh@gmail.com', 16, '2021-06-27', 'Dinner', 'One-Week', '2021-06-28', 868);

-- --------------------------------------------------------

--
-- Table structure for table `customer_order`
--

CREATE TABLE `customer_order` (
  `order_no` int(11) NOT NULL,
  `invoice_date` date NOT NULL,
  `email` varchar(100) NOT NULL,
  `house_no` varchar(150) NOT NULL,
  `area` varchar(50) NOT NULL,
  `start_date` date NOT NULL,
  `total_price` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer_order`
--

INSERT INTO `customer_order` (`order_no`, `invoice_date`, `email`, `house_no`, `area`, `start_date`, `total_price`) VALUES
(8, '2021-06-22', 'tanya29sehgal@gmail.com', '132-A', 'Rani Ka Bagh', '2021-06-23', 868),
(9, '2021-06-22', 'tanya29sehgal@gmail.com', '132-A', 'Rani Ka Bagh', '2021-06-23', 868),
(10, '2021-06-22', 'tanya29sehgal@gmail.com', '132-A', 'Rani Ka Bagh', '2021-06-23', 868),
(11, '2021-06-22', 'tanya29sehgal@gmail.com', '132-A', 'Rani Ka Bagh', '2021-06-23', 868),
(12, '2021-06-22', 'tanya29sehgal@gmail.com', '132-A', 'Rani Ka Bagh', '2021-06-23', 3335),
(13, '2021-06-22', 'pallav.marwah@gmail.com', '55 Aman Avenue', 'Majitha Road', '2021-06-23', 868),
(14, '2021-06-23', 'tanya29sehgal@gmail.com', '132-A', 'Rani Ka Bagh', '2021-06-24', 868),
(15, '2021-06-23', 'tanya29sehgal@gmail.com', '132-A', 'Rani Ka Bagh', '2021-06-28', 3335),
(16, '2021-06-27', 'rajesh@gmail.com', '132-A', 'New Golden Avenue', '2021-06-28', 868);

-- --------------------------------------------------------

--
-- Table structure for table `location`
--

CREATE TABLE `location` (
  `area_id` int(15) NOT NULL,
  `area_name` varchar(100) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `location`
--

INSERT INTO `location` (`area_id`, `area_name`, `city`, `state`) VALUES
(1001, 'Rani Ka Bagh', 'Amritsar', 'Punjab'),
(1002, 'Majitha Road', 'Amritsar', 'Punjab'),
(1003, 'Batala Road', 'Amritsar', 'Punjab'),
(1004, 'Ranjit Avenue', 'Amritsar', 'Punjab');

-- --------------------------------------------------------

--
-- Table structure for table `menu`
--

CREATE TABLE `menu` (
  `meal_id` int(15) NOT NULL,
  `meal_type` varchar(20) NOT NULL,
  `date` date NOT NULL,
  `day` varchar(10) NOT NULL,
  `description` varchar(500) NOT NULL,
  `price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `menu`
--

INSERT INTO `menu` (`meal_id`, `meal_type`, `date`, `day`, `description`, `price`) VALUES
(101, 'Lunch', '2021-06-28', 'Monday', 'Manchurian, Garlic fried rice, Whole wheat chapati', 110),
(102, 'Lunch', '2021-06-29', 'Tuesday', 'Sabzi hari bhari, Vermicelli pulao, Curd, Whole wheat chapati, Chana chat', 110),
(103, 'Lunch', '2021-06-30', 'Wednesday', 'Jeera aloo, Dal banjara, Rice, Buttermilk, Ajwain chapati', 110),
(104, 'Lunch', '2021-07-01', 'Thursday', 'Paneer lababdaar, Hyderabadi khatti dal, Rice, Whole wheat chapati, Beetroot raita', 110),
(105, 'Lunch', '2021-07-02', 'Friday', 'Lemon coriander soup, Pav bhaji, Tawa pulao, Curd, Pav', 110),
(106, 'Lunch', '2021-07-03', 'Saturday', 'Tossed salad with flaxseeds, Methi kofta curry, Raw mango rice, Curd, Whole wheat chapati', 110),
(1001, 'Dinner', '2021-06-28', 'Monday', 'Lemongrass ginger carrot soup, Aloo mutter, Dal panchmel, Rice, Whole wheat chapati', 110),
(1002, 'Dinner', '2021-06-29', 'Tuesday', 'Pea mint soup, Spring onion moong dal sabzi, Dal khichdi, Curd, Whole wheat chapati', 110),
(1003, 'Dinner', '2021-06-30', 'Wednesday', 'Mix veg kheema, Tur dal, Rice, Payasam, Methi chapati', 110),
(1004, 'Dinner', '2021-07-01', 'Thursday', 'Grated salad, Chhole, Rice, Curd, Whole wheat chapati', 110),
(1005, 'Dinner', '2021-07-02', 'Friday', 'Potato coriander raita, Spinach corn sazi, Sindhi kadhi, Rice, Whole wheat chapati', 110),
(1006, 'Dinner', '2021-07-03', 'Saturday', 'Grated salad, Sambhar, Tamarind rice, Curd, Uttapam', 110);

-- --------------------------------------------------------

--
-- Table structure for table `sign_up`
--

CREATE TABLE `sign_up` (
  `email` varchar(100) NOT NULL,
  `password` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `mobile` varchar(10) NOT NULL,
  `house_no` varchar(150) NOT NULL,
  `area` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sign_up`
--

INSERT INTO `sign_up` (`email`, `password`, `name`, `mobile`, `house_no`, `area`, `city`, `state`) VALUES
('pallav.marwah@gmail.com', '2222', 'Pallav Marwaha', '7009368873', '55 Aman Avenue', 'Majitha Road', 'Amritsar', 'Punjab'),
('rajesh@gmail.com', '123456789', 'Rajesh Sehgal', '9417277244', '132-A', 'New Golden Avenue', 'Amritsar', 'Punjab'),
('sanamarora@gmail.com', '123', 'Sanam', '9888157466', 'kljaihd', 'Ranjit Avenue', 'Amritsar', 'Punjab'),
('shivanigudwani@gmail.com', 'maanit79', 'shivani', '9888157466', '22 Friends colony', 'Majitha Road', 'Amritsar', 'Punjab'),
('tanya29sehgal@gmail.com', '1111', 'Tanya Sehgal', '6284747437', '132-A', 'Rani Ka Bagh', 'Amritsar', 'Punjab');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `booking_details`
--
ALTER TABLE `booking_details`
  ADD PRIMARY KEY (`booking_id`),
  ADD KEY `email` (`email`),
  ADD KEY `order_no` (`order_no`);

--
-- Indexes for table `customer_order`
--
ALTER TABLE `customer_order`
  ADD PRIMARY KEY (`order_no`),
  ADD KEY `email` (`email`);

--
-- Indexes for table `location`
--
ALTER TABLE `location`
  ADD PRIMARY KEY (`area_id`);

--
-- Indexes for table `menu`
--
ALTER TABLE `menu`
  ADD PRIMARY KEY (`meal_id`);

--
-- Indexes for table `sign_up`
--
ALTER TABLE `sign_up`
  ADD PRIMARY KEY (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `booking_details`
--
ALTER TABLE `booking_details`
  MODIFY `booking_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `customer_order`
--
ALTER TABLE `customer_order`
  MODIFY `order_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `booking_details`
--
ALTER TABLE `booking_details`
  ADD CONSTRAINT `booking_details_ibfk_1` FOREIGN KEY (`email`) REFERENCES `sign_up` (`email`),
  ADD CONSTRAINT `booking_details_ibfk_2` FOREIGN KEY (`order_no`) REFERENCES `customer_order` (`order_no`);

--
-- Constraints for table `customer_order`
--
ALTER TABLE `customer_order`
  ADD CONSTRAINT `customer_order_ibfk_1` FOREIGN KEY (`email`) REFERENCES `sign_up` (`email`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
