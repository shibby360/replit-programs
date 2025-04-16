--The Transfroming Birds!!!!!!
Create table transbirds (id integer primary key, name text, power text, kids text, position text);

insert into transbirds values (1, 'Captain', 'Opposify', 'Tiny', 'Leader');
insert into transbirds values (2, 'Disguiser', 'Disguise', 'Junior', 'Second-in-command');
insert into transbirds values (3, 'Blow up', 'Speed', 'BU', 'Lead Attacker');
insert into transbirds values (4, 'Cool Change', NULL, 'Tiny', NULL);
insert into transbirds values (5, 'Flippy', NULL, 'Junior', NULL);
insert into transbirds values (6, 'Blew', NULL, 'BU', NULL);
insert into transbirds values (7, 'Ace of Spades/A', 'Aces Everything', NULL, 'Card Planes/Army');
insert into transbirds values (8, 'E', 'Knows when anything happens', NULL, 'Army');
insert into transbirds values (9, 'F', 'Block Shield', NULL, 'Army');
insert into transbirds values (10, 'G', 'Bubble Shield', NULL, 'Army');
insert into transbirds values (11, 'H', 'Fly high, Enhance weapons', NULL, 'Hi Squad/Army');
insert into transbirds values (12, 'I', 'Fly high, Enhance weapons', NULL, 'Hi Squad/Army');


--The Elemntal Masters!!!!!!!!!!!
Create table elemasterstb (id integer primary key, name text, move1 text, move2 text, move3 text, kid_name text, kid_move text);

insert into elemasterstb values (1, 'Earth', 'Earthquake', 'Mountain raise', 'Rocker', 'Earthy', 'Mountain trap');
insert into elemasterstb values (2, 'Water', 'Tsunami', 'Riverrang', 'Lake Shield', 'Watry', 'Riverang');
insert into elemasterstb values (3, 'Air', 'Tornado', 'Mega Gust', 'Airshield', 'Airry', 'Smallnado');
insert into elemasterstb values (4, 'Fire', 'Blaze', 'Fire Beam', 'Fire Shield', 'Firy', 'Fire Dome');
insert into elemasterstb values (5, 'Space', 'Asteroid', 'Air Star', 'Blaze Star', 'Spacer', 'Ice Star');

--The rollers!
Create table rollers (id integer primary key, name text, type text, element text, power_name text, move text, move_damage integer, installed_move text, installed_move_damage text, special_abilites text);

insert into rollers values (1, 'Expo', 'ninja', 'Dark', 'Dark Ninja', 'Dark Clot', 600, 'Capture', 'FULL', 'Can defeat anybody');

insert into rollers values (2, 'Blaze', 'ninja', 'Fire', 'Fire Ninja', 'Wave of flames', 400, 'Capture', 'FULL', null);

insert into rollers values (3, 'Weed', 'ninja', 'Plants', 'Plant Ninja', 'Spinning Weeds', 200, 'Capture', 'FULL', null);

insert into rollers values (4, 'River', 'ninja', 'Water', 'Water Ninja', 'Water spray', 50, 'Capture', 'FULL', null);

insert into rollers values (5, 'Shadow bird', 'plane', 'Dark', 'Dark Plane', 'Dark Blast', 500, 'Fly', '250', 'Can defeat anybody');

insert into rollers values (6, 'Fire Bird', 'plane', 'Fire', 'Fire Plane', 'Inferno launch', 300, 'Fly', '250', null);

insert into rollers values (7, 'Weed Bird', 'plane', 'Plants', 'Plant Plane', 'Grow', 100, 'Fly', '250', null);

insert into rollers values (8, 'Wet Bird', 'plane', 'Water', 'Water Plane', 'Water Splash', 25, 'Fly', '250', null);

select * from transbirds;