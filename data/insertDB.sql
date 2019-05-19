insert into LesSpectacles(noSpec, nomSpec) values (1, 'How to be a Parisian?');
insert into LesSpectacles(noSpec, nomSpec) values (2, 'Je parle toute seule');
insert into LesSpectacles(noSpec, nomSpec) values (3, 'La bédédé de dédé!');

insert into LesZones(noZone, catZone, prixZone) values (1, 'orchestre', 5);
insert into LesZones(noZone, catZone, prixZone) values (2, 'balcon', 3.5);
insert into LesZones(noZone, catZone, prixZone) values (3, 'scène', 100);

insert into LesPlaces(noPlace, noRang, noZone) values (1, 1, 1);
insert into LesPlaces(noPlace, noRang, noZone) values (2, 1, 1);
insert into LesPlaces(noPlace, noRang, noZone) values (3, 1, 1);
insert into LesPlaces(noPlace, noRang, noZone) values (4, 1, 1);
insert into LesPlaces(noPlace, noRang, noZone) values (5, 1, 1);

insert into LesPlaces(noPlace, noRang, noZone) values (1, 2, 1);
insert into LesPlaces(noPlace, noRang, noZone) values (2, 2, 1);
insert into LesPlaces(noPlace, noRang, noZone) values (3, 2, 1);
insert into LesPlaces(noPlace, noRang, noZone) values (4, 2, 1);
insert into LesPlaces(noPlace, noRang, noZone) values (5, 2, 1);

insert into LesPlaces(noPlace, noRang, noZone) values (1, 3, 2);
insert into LesPlaces(noPlace, noRang, noZone) values (2, 3, 2);
insert into LesPlaces(noPlace, noRang, noZone) values (3, 3, 2);
insert into LesPlaces(noPlace, noRang, noZone) values (4, 3, 2);
insert into LesPlaces(noPlace, noRang, noZone) values (5, 3, 2);

insert into LesPlaces(noPlace, noRang, noZone) values (1, 666, 3);

insert into LesDossiers_base(noDos) values (1);
insert into LesDossiers_base(noDos) values (2);
insert into LesDossiers_base(noDos) values (3);
insert into LesDossiers_base(noDos) values (4);

insert into LesRepresentations_base(noSpec, dateRep) values (1, '24/01/2018 17:00');
insert into LesRepresentations_base(noSpec, dateRep) values (1, '25/01/2018 20:00');
insert into LesRepresentations_base(noSpec, dateRep) values (1, '26/01/2018 21:00');
insert into LesRepresentations_base(noSpec, dateRep) values (2, '24/01/2018 21:00');
insert into LesRepresentations_base(noSpec, dateRep) values (2, '25/01/2018 23:00');
insert into LesRepresentations_base(noSpec, dateRep) values (3, '25/12/2018 4:00');
insert into LesRepresentations_base(noSpec, dateRep) values (3, '31/12/2018 16:00');


insert into LesTickets(noSpec, dateRep, noPlace, noRang, dateEmTick, noDos) values (1, '24/01/2018 17:00', 1, 1, '23/01/2018 21:30:20',1);
insert into LesTickets(noSpec, dateRep, noPlace, noRang, dateEmTick, noDos) values (1, '24/01/2018 17:00', 2, 1, '23/01/2018 21:30:20',1);
insert into LesTickets(noSpec, dateRep, noPlace, noRang, dateEmTick, noDos) values (1, '24/01/2018 17:00', 3, 1, '23/01/2018 21:30:20',1);
insert into LesTickets(noSpec, dateRep, noPlace, noRang, dateEmTick, noDos) values (1, '24/01/2018 17:00', 4, 1, '23/01/2018 21:30:20',1);
insert into LesTickets(noSpec, dateRep, noPlace, noRang, dateEmTick, noDos) values (1, '24/01/2018 17:00', 5, 1, '23/01/2018 21:30:20',1);

insert into LesTickets(noSpec, dateRep, noPlace, noRang, dateEmTick, noDos) values (2, '25/01/2018 23:00', 1, 2, '20/01/2018 22:31:00',2);
insert into LesTickets(noSpec, dateRep, noPlace, noRang, dateEmTick, noDos) values (2, '25/01/2018 23:00', 2, 2, '20/01/2018 22:31:00',2);

insert into LesTickets(noSpec, dateRep, noPlace, noRang, dateEmTick, noDos) values (2, '25/01/2018 23:00', 1, 3, '20/01/2018 14:22:00',3);
insert into LesTickets(noSpec, dateRep, noPlace, noRang, dateEmTick, noDos) values (2, '25/01/2018 23:00', 2, 3, '20/01/2018 14:22:00',3);

insert into LesTickets(noSpec, dateRep, noPlace, noRang, dateEmTick, noDos) values (3, '25/12/2018 4:00', 1, 2, '20/11/2018 0:22:12',4);
insert into LesTickets(noSpec, dateRep, noPlace, noRang, dateEmTick, noDos) values (3, '25/01/2018 23:00', 1, 3, '20/11/2018 0:22:12',4);
insert into LesTickets(noSpec, dateRep, noPlace, noRang, dateEmTick, noDos) values (3, '31/12/2018 16:00', 4, 4, '20/11/2018 0:22:12',4);
