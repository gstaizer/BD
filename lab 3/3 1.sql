-- INSERT Без указания списка полей
INSERT INTO doctor VALUES (5, 27, 738261, 'cur_address', 'cardiologist');
-- INSERT С указанием списка полей
INSERT INTO doctor (age, telephone, address, position)
VALUES (46, 738261, 'next_address', 'cardiologist');
-- INSERT С чтением значения из другой таблицы
INSERT INTO doctor (address)  SELECT (address) FROM hospital;

-- DELETE Всех записей
DELETE FROM doctor;
-- DELETE По условию
DELETE FROM doctor WHERE id_doctor > 5;
-- TRUNCATE Очистить таблицу
TRUNCATE doctor;

-- UPDATE Всех записей
UPDATE doctor
SET telephone = 754862
WHERE true;
-- UPDATE По условию обновляя один атрибут
UPDATE doctor
SET age = age + 1 WHERE age > 26;
-- UPDATE По условию обновляя несколько атрибутов
UPDATE doctor
SET age = age + 1, position = 'cardio' WHERE position = 'cardiologist';

-- SELECT С определенным набором извлекаемых атрибутов

SELECT address, telephone FROM hospital;
-- SELECT Со всеми атрибутами
SELECT * FROM sick;
-- SELECT С условием по атрибуту
SELECT * FROM medicine WHERE name = 'NHT';

-- SELECT ORDER BY + TOP (LIMIT) 

-- С сортировкой по возрастанию ASC + ограничение вывода количества записей
SELECT * FROM sick ORDER BY id_sick ASC LIMIT 1;
-- С сортировкой по убыванию DESC
SELECT * FROM sick ORDER BY id_sick DESC;
-- С сортировкой по двум атрибутам + ограничение вывода количества записей
SELECT * FROM doctor ORDER BY age, id_doctor DESC LIMIT 1;
-- С сортировкой по первому атрибуту, из списка извлекаемых
SELECT * FROM sick ORDER BY 1 DESC;

-- Работа с датами. WHERE по дате
SELECT * FROM sick WHERE date_of_birth = date('1991-07-27');
-- Извлечь из таблицы не всю дату, а только год.
SELECT telephone, EXTRACT(YEAR FROM age) AS date FROM doctor;

-- SELECT GROUP BY с функциями агрегации

-- MIN: вычисляет наименьшее значение
SELECT MIN(date_of_birth), id_sick FROM sick GROUP BY id_sick;
-- MAX: вычисляет наибольшее значение
SELECT MAX(age), id_doctor FROM doctor GROUP BY id_doctor;
-- AVG: вычисляет среднее значение
SELECT AVG(age) FROM doctor GROUP BY id_doctor;
-- SUM: вычисляет сумму значений
SELECT SUM(cost), id_medicine FROM medicine GROUP BY id_medicine;
-- COUNT: вычисляет количество строк в выборке null игнорит
SELECT COUNT(snills), id_sick FROM sick GROUP BY id_sick;



-- SELECT GROUP BY + HAVING Написать 3 разных запроса - having после группировки where до
SELECT id_doctor, COUNT(id_inspection) FROM inspection GROUP BY id_doctor HAVING COUNT(id_inspection) > 10;
SELECT id_medicine, AVG(cost) FROM medicine GROUP BY id_medicine HAVING AVG(cost) > 1000
SELECT id_medicine, MIN(cost) FROM medicine GROUP BY id_medicine HAVING cost > 3000;

-- SELECT JOIN
-- LEFT JOIN двух таблиц и WHERE по одному из атрибутов
SELECT * FROM medicine LEFT JOIN illness_history i on medicine.id_medicine = i.id_medicine WHERE cost > 1000;
-- RIGHT JOIN. Получить такую же выборку, как и в 9.1
SELECT * FROM medicine RIGHT JOIN illness_history i on medicine.id_medicine = i.id_medicine WHERE cost > 1000;
-- LEFT JOIN трех таблиц + WHERE по атрибуту из каждой таблицы
SELECT * FROM inspection LEFT JOIN doctor n on inspection.id_inspection = n.id_doctor
                     LEFT JOIN hospital h on n.id_doctor = h.id_hospital
                     WHERE age > 30 AND n.id_doctor < 1 AND id_hospital < 2;
-- FULL OUTER JOIN двух таблиц
SELECT * FROM doctor FULL OUTER JOIN inspection n on doctor.id_doctor = n.id_doctor;

-- Подзапросы
-- Написать запрос с WHERE IN (подзапрос)
SELECT * FROM doctor WHERE date(age) IN (date('1991-09-24'), date('1993-03-05'));
-- Написать запрос SELECT atr1, atr2, (подзапрос) FROM ...
SELECT * FROM hospital WHERE telephone IN (SELECT telephone FROM doctor);
