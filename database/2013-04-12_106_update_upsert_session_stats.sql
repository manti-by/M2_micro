DROP PROCEDURE IF EXISTS `UPSERT_SESSION_STAT`;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `UPSERT_SESSION_STAT`(IN `_session` varchar(255), IN `_ip` varchar(50), IN `_country` varchar(2), IN `_count` int)
BEGIN
    INSERT INTO `stats_browser` (`session`, `ip`, `country`, `count`, `timestamp`)
    VALUES (_session, _ip, _country, _count, DATE(NOW() - INTERVAL 1 DAY));
END
;;
DELIMITER ;